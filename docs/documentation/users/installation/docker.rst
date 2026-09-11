.. _doc-users-installation-docker:

Docker
======

The official `nymea Docker image <https://hub.docker.com/r/nymea/nymea/>`__ runs
``nymead`` on ``debian:trixie-slim``. Its settings and application data are kept
in a folder on the Docker host, so they survive container replacement and image
updates.

Requirements
------------

This deployment requires native Linux Docker Engine with the Docker Compose
plugin and host networking. Docker Desktop and rootless Docker are not supported.
Host networking lets nymea:app discover the instance on the LAN, but means that
only one default-port nymea instance can run on a host.

Quick start
-----------

Create an empty directory, then save the following as ``docker-compose.yml``:

.. code-block:: yaml

   services:
     nymead:
       image: nymea/nymea:latest
       network_mode: host
       uts: host
       restart: unless-stopped
       stop_grace_period: 45s
       environment:
         TZ: ${TZ:-Europe/Vienna}
         NYMEAD_EXTRA_ARGS: ${NYMEAD_EXTRA_ARGS:--n -m}
       volumes:
         - ${NYMEA_DATA_DIR:-./data}/nymea:/var/lib/nymea
         - ${NYMEA_DATA_DIR:-./data}/cache:/var/cache/nymea
         - ${NYMEA_DATA_DIR:-./data}/backups:/var/backups
       tmpfs:
         - /run

Create a ``.env`` file and start the container:

.. code-block:: sh

   printf 'NYMEA_DATA_DIR=./data\nTZ=Europe/Vienna\n' > .env
   docker compose up -d --wait --wait-timeout 120

Open nymea:app on the same LAN, select the discovered instance, and create the
first user. If discovery is unavailable, add the Docker host's LAN IP manually
with the TLS TCP API on port ``2222``. The initial ``-n -m`` arguments disable
history logging, so the container can start without InfluxDB connection warnings;
device control and the API work normally.

Connecting and daily operation
------------------------------

The container runs its own D-Bus and Avahi. Host D-Bus, systemd and Avahi are
not required. Host UTS makes Avahi advertise the host name and its LAN addresses.

.. code-block:: sh

   docker compose ps
   docker compose logs -f --tail 100 nymead
   docker compose stop
   docker compose start
   docker compose down  # removes the container but keeps host data

The image includes `nymea-cli <https://github.com/nymea/nymea-cli>`__ for
terminal-based checks and control:

.. code-block:: sh

   docker compose exec nymead nymea-cli --ssl --host 127.0.0.1 --port 2222

At the first connection, it asks for credentials and acceptance of the TLS
fingerprint. The token and fingerprint are stored in the bind-mounted data
folder, and therefore remain available after the container is recreated.

Configuration and persistence
-----------------------------

Set these values in ``.env``:

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Setting
     - Default
     - Purpose
   * - ``NYMEA_DATA_DIR``
     - ``./data``
     - Host data folder; relative to the Compose project.
   * - ``TZ``
     - ``Europe/Vienna``
     - Container timezone, for example ``Etc/UTC``.
   * - ``NYMEAD_EXTRA_ARGS``
     - empty
     - Extra daemon flags, such as ``-m`` to disable LogEngine.

The data folder has this layout:

.. code-block:: text

   data/
     nymea/     # settings, users, certificates, scripts and databases
     cache/     # cached application state
     backups/   # backups initiated through nymea:app

Settings are normally managed in nymea:app. Advanced configuration is in
``data/nymea/nymead.conf``; stop the container before changing it. nymea 1.15+
stores configuration in ``/var/lib/nymea``, rather than ``/etc/nymea``.

The daemon runs as root inside the container, so bind mounts contain root-owned
files. Use ``sudo`` for maintenance and backups; do not make them world-writable.
An existing ``configs/`` folder from an older setup is neither loaded nor
migrated. InfluxDB history is also optional and not migrated.

Networking and discovery
------------------------

``network_mode: host`` shares the host network namespace: there is no NAT,
``ports:`` configuration or ``-p`` mapping. A port configured in nymea is
directly opened on the host LAN IP. Configure firewalls on the host and verify
that no other host service owns the port.

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - Port
     - Default use
   * - TCP 2222
     - Authenticated TLS nymea API; nymea:app and health check
   * - TCP 4444
     - Authenticated secure WebSocket API
   * - TCP 80/443
     - nymea HTTP / HTTPS listeners
   * - TCP 1883
     - Authenticated MQTT broker
   * - UDP 5353
     - Avahi mDNS discovery

Listeners are configurable in nymea:app or ``nymead.conf``. LAN firewalls,
wireless client isolation, VLANs, and integration-specific multicast or
broadcast requirements can still prevent discovery. If another mDNS responder
exists on the host, it must allow UDP 5353 to be shared.

The image has no separate web frontend, no default USB or Bluetooth access, no
privileged mode, and no host D-Bus mount. The packaged daemon's ``NET_ADMIN``
file capability is dropped because Docker does not provide it by default. If a
specific plugin genuinely needs it, add ``cap_add: [NET_ADMIN]`` to the service.

Serial hardware: Zigbee, Z-Wave and Modbus RTU
-----------------------------------------------

Pass each USB serial adapter through explicitly. First find its stable host
path, avoiding ``/dev/ttyUSB*`` and ``/dev/ttyACM*`` names which may change:

.. code-block:: sh

   ls -l /dev/serial/by-id/

Then add the devices to the ``nymead`` service, using fixed container paths:

.. code-block:: yaml

   devices:
     - /dev/serial/by-id/usb-Nabu_Casa_ZBT-1_XXXXXXXX-if00-port0:/dev/ttyZigbee
     - /dev/serial/by-id/usb-0658_0200_XXXXXXXX-if00:/dev/ttyZwave
     - /dev/serial/by-id/usb-FTDI_USB-RS485_Cable_XXXXXXXX-if00-port0:/dev/ttyModbus

This grants access only to the selected device nodes; neither ``privileged: true``
nor mounting all of ``/dev`` is required. Add packages and rebuild as needed:

================  ======================================================================
Hardware          Package
================  ======================================================================
Zigbee            ``nymea-plugin-zigbee-generic`` plus vendor packages, or ``nymea-plugins-zigbee``
Z-Wave            ``nymea-zwave-plugin-openzwave`` plus desired plugins, or ``nymea-plugins-zwave``
Modbus RTU        ``nymea-plugin-modbuscommander``
================  ======================================================================

When building a customized image, add packages to ``packages.txt``, rebuild and
recreate it. In nymea:app, configure the appropriate hardware resource with the
container-side serial path and the adapter's serial settings. Adding a stick
later requires recreating the container.

Plugins and image updates
-------------------------

For a reproducible deployment, replace ``latest`` with a versioned image tag,
for example ``nymea/nymea:1.16.0``. To update a Docker Hub image:

.. code-block:: sh

   docker compose pull
   docker compose up -d --wait --wait-timeout 120

Back up data before upgrading: an older daemon may not understand data written
by a newer version. To customize the package set, clone the
`nymea-docker repository <https://github.com/nymea/nymea-docker>`__, edit its
``packages.txt``, then build and recreate the image:

.. code-block:: sh

   docker compose build --pull --no-cache
   docker compose up -d --wait --wait-timeout 120

Zigbee, Z-Wave and Modbus packages also require the serial-device mapping above.
The Daikin Python integration is excluded because the packaged Qt 6 daemon has
no Python plugin support; integrations with both LAN and Bluetooth features can
use only their LAN features in this container.

InfluxDB history support
------------------------

InfluxDB is optional. nymea's LogEngine uses InfluxDB 1.8 for historical states
and nymea:app charts. To enable it, add this service next to ``nymead``:

.. code-block:: yaml

   influxdb:
     image: influxdb:1.8
     network_mode: host
     restart: unless-stopped
     environment:
       TZ: ${TZ:-Europe/Vienna}
       INFLUXDB_HTTP_BIND_ADDRESS: 127.0.0.1:8086
       INFLUXDB_DB: nymea
       INFLUXDB_ADMIN_USER: admin
       INFLUXDB_ADMIN_PASSWORD: ${INFLUXDB_ADMIN_PASSWORD:?set in .env}
       INFLUXDB_USER: nymea
       INFLUXDB_USER_PASSWORD: ${INFLUXDB_USER_PASSWORD:?set in .env}
       INFLUXDB_HTTP_AUTH_ENABLED: "true"
     volumes:
       - ${NYMEA_DATA_DIR:-./data}/influxdb:/var/lib/influxdb

Add strong ``INFLUXDB_ADMIN_PASSWORD`` and ``INFLUXDB_USER_PASSWORD`` values to
``.env`` before its first start. Then configure ``data/nymea/nymead.conf``:

.. code-block:: ini

   [Logs]
   logDBHost=127.0.0.1
   logDBName=nymea
   logDBUser=nymea
   logDBPassword=<INFLUXDB_USER_PASSWORD>

Restart nymead after editing the configuration. InfluxDB initialization values
apply only to an empty data folder, and its API is deliberately bound to
``127.0.0.1``. Include its ``influxdb`` directory in backups.

Backup and restore
------------------

Stop nymea before copying data to keep databases and configuration consistent:

.. code-block:: sh

   docker compose stop
   sudo tar -C ./data -czf nymea-backup.tar.gz nymea cache backups
   docker compose start

Restore only to an empty data folder, preserving ownership:

.. code-block:: sh

   docker compose stop
   sudo mkdir -p /srv/nymea-restored
   sudo tar -C /srv/nymea-restored -xzf nymea-backup.tar.gz
   # Set NYMEA_DATA_DIR=/srv/nymea-restored in .env.
   docker compose up -d --force-recreate --wait --wait-timeout 120

Keep backups outside the project checkout: they include user credentials and
private certificates.

Health and validation
---------------------

Supervisor starts D-Bus, Avahi and nymea in order, and stops the container if a
required service exits. Docker restarts it unless it was explicitly stopped.
Logs rotate at 10 MB with three retained files. The health check verifies the
supervised services and makes a TCP API handshake using the persisted instance
UUID. Keep at least one TCP API listener enabled; Docker marks a failed check
unhealthy but does not restart a container solely for that reason.

For source-image validation, clone the nymea-docker repository and run:

.. code-block:: sh

   docker compose config --quiet
   python3 tests/smoke.py

The smoke test uses temporary data and a temporary TCP port, creates disposable
data, checks persistence, backup/restore and recovery, then removes its
containers. For final LAN acceptance, connect nymea:app from another device,
confirm discovery and add a real LAN device through its integration plugin.

Building and publishing
-----------------------

Maintainers can build the source repository locally with ``docker compose build``.
To publish a multi-platform release to Docker Hub, tag it with the verified
nymea daemon version and ``latest``:

.. code-block:: sh

   docker buildx build \
     --platform linux/amd64,linux/arm64 \
     --tag nymea/nymea:<version> \
     --tag nymea/nymea:latest \
     --push .

Confirm the result with ``docker buildx imagetools inspect
nymea/nymea:<version>``. The full build, release and Docker Hub-description
instructions remain in the `nymea-docker source repository
<https://github.com/nymea/nymea-docker>`__.
