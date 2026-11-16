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


Product information
-------------------

An operating system image can provide optional, static product information in
``/usr/share/nymea/product-info``. This is a separate file from ``nymead.conf``.
Use UTF-8 text with one ``key=value`` pair per line, for example::

   vendor=chargebyte GmbH.
   vendorurl=https://chargebyte.com/
   model=Cool nymea based prouct
   hardwareRevision=HW1
   producttype=wallbox

All five keys are optional. ``vendor`` identifies the product vendor, while
``model`` identifies the product model. ``producttype`` can be used by clients
to choose a suitable icon or setup flow (for example, ``gateway``, ``wallbox``,
``router`` or ``node``). The file is read when ``nymead`` starts; restart the
service after changing it.

If any value is set, the ``JSONRPC.Hello`` reply contains a ``productInfo``
object with all five keys. Missing values are empty strings. The zeroconf TXT
records advertise nonempty ``vendor``, ``model`` and ``producttype`` values.
If the file is absent or all values are empty, ``productInfo`` and these TXT
records are omitted.


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
