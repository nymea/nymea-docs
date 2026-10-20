.. _doc-users-usage-advanced-configuration:

Advanced configuration
======================


Most configuration should be changed through nymea:app. The options described here are advanced settings
that are normally not needed for regular installations, but can be useful for special deployments or
debugging.

For a standard nymea:core installation, where ``nymead`` runs as root, the configuration file can be
found in ``/var/lib/nymea/nymead.conf``. The ``/etc/nymea`` directory is no longer used since nymea
1.15.0. If ``nymead`` is started as a user, the configuration file can be found in
``~/.config/nymea``.

After changing the configuration file, restart ``nymead``:

::

   sudo systemctl restart nymead


Section [BluetoothServer]
-------------------------


::

   [BluetoothServer]
   enabled=false


This hidden feature exposes the nymea API through a Bluetooth RFCOMM service. It requires Bluetooth
hardware and BlueZ. It is intended for special-purpose setups where the nymea API should be available
without TCP/IP networking.

Section [SSL]
-------------


::

   [SSL]
   certificate=
   certificate-key=


The SSL section allows providing an SSL certificate that will be used for server interfaces, such as API
interfaces, the web server and the MQTT server. If nymea starts without a configured SSL certificate, a
self-signed certificate will be generated.

Section [LoggingRules]
----------------------


This section configures debug output of ``nymead``. It can be used to filter debug output in a more
customized way.

::

   [LoggingRules]
   *.debug=false


This example would disable all debug output and only keep warnings and errors. Individual debug categories can be enabled by adding e.g.

::

   Bluetooth.debug=true


.. _web-server-reverse-proxy:

Section [WebServer] — Reverse proxy settings
----------------------------------------------

When a reverse proxy exposes the web server on a different port or beneath a path
prefix, configure the public endpoint for each web server in ``nymead.conf``::

   [WebServer]
   local\address=127.0.0.1
   local\port=8080
   local\sslEnabled=false
   local\proxyPort=443
   local\proxySslEnabled=true
   local\proxyPathPrefix=/nymea

Here ``local`` is the web server configuration ID. These settings are edited in
the configuration file only, then applied by restarting ``nymead``. They are
exposed read-only to nymea:app; ordinary web server edits in the app preserve them.

``proxyPort``
   Public port, from 1 to 65535. The default, 0, disables the proxy override.
``proxySslEnabled``
   Whether the public endpoint uses HTTPS. Defaults to false. This does not
   enable TLS on the internal listener: the example terminates HTTPS at the proxy
   and forwards HTTP to localhost port 8080.
``proxyPathPrefix``
   Shared public prefix for the debug interface and EvDash. Defaults to empty.
   A nonempty prefix must begin with ``/``; trailing slashes are removed and
   ``/`` means no prefix. Authorities, query strings, fragments and path traversal
   segments are invalid. Invalid proxy settings disable the override and log a warning.

The app chooses an active LAN IPv4 address, preferring wired networking over Wi-Fi.
No hostname or IP address is stored in the proxy settings. For a selected address
of ``192.168.1.10``, the example produces these links:

* ``https://192.168.1.10/nymea/debug/``
* ``https://192.168.1.10/nymea/evdash/``

The reverse proxy must be reachable at that LAN address, strip ``/nymea`` before
forwarding to nymead, and forward WebSocket upgrades, including the connections
under ``/nymea/debug/ws`` and ``/nymea/evdash/ws``. A localhost backend is supported.
The prefix applies to both interfaces; their internal routes remain ``/debug``
and ``/evdash``. Direct backend access continues to work without the prefix.

These settings advertise an endpoint; they do not configure the reverse proxy,
change authentication, enable either interface, or make LAN links remotely
accessible. Without an override (or when connected to an older server), the app
uses the web server's listener protocol and port. Older app versions do not use
this metadata. If several proxy endpoints are advertised, the app chooses the
first by configuration ID. If no active LAN address is available, no link is shown.
