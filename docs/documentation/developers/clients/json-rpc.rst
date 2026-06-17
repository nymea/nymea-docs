.. _doc-developers-clients-json-rpc:

The nymea JSON-RPC API
======================

nymea offers a JSON-RPC based API for client applications. On a nymea:core instance it is exposed
through plain TCP sockets or WebSocket-based communication, each either plaintext or SSL encrypted.
In the default configuration, nymea exposes the API via an SSL-enabled TCP socket on port 2222 and
an SSL-enabled WebSocket on port 4444. A nymea:core instance can be configured with any combination
of these transports. The interfaces are described using URLs.

Transport types
---------------

Plaintext nymea TCP sockets
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Plaintext nymea TCP sockets use the URL scheme ``nymea://``. ``telnet`` or ``ncat`` can be used to
communicate with them. Establishing a standard TCP connection is sufficient. Example:

.. code-block:: text

   nymea://192.168.0.10:2222

SSL encrypted nymea TCP sockets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SSL-encrypted nymea TCP sockets use the URL scheme ``nymeas://``. They behave like ``nymea://``
sockets but require a valid SSL handshake first. ``ncat --ssl`` can be used for testing. Example:

.. code-block:: text

   nymeas://192.168.0.10:2222

Plaintext WebSockets
~~~~~~~~~~~~~~~~~~~~

Plaintext WebSockets use the standard ``ws://`` scheme. A valid WebSocket handshake is required
before communication. Example:

.. code-block:: text

   ws://192.168.0.10:4444

SSL encrypted WebSockets
~~~~~~~~~~~~~~~~~~~~~~~~~

SSL-encrypted WebSockets use the ``wss://`` scheme. Both a valid SSL handshake and a valid
WebSocket handshake must be completed before communicating with the server. Example:

.. code-block:: text

   wss://192.168.0.10:4444

SSL certificates
----------------

Because nymea instances are typically installed on a local network, most will use a self-signed SSL
certificate. A client implementation cannot expect a publicly signed certificate from the server.

It is strongly recommended to use certificate pinning. The first time the user connects to a new
instance, store the certificate fingerprint on the client device and inform the user about accepting
the new connection. On all subsequent connections, compare the certificate provided by the server to
the stored fingerprint. If it has changed, warn the user about a potential man-in-the-middle attack
or a modification of the server (for example after a factory reset).

Discovering nymea instances in the network
------------------------------------------

nymea can be discovered in the local network using **UPnP 1.1** (`Universal Plug and Play
<https://en.wikipedia.org/wiki/Universal_Plug_and_Play>`__) or **Zeroconf** (mDNS/DNS-SD).

UPnP
~~~~

nymea presents itself as a `UPnP Basic 1.0
<http://upnp.org/specs/basic/UPnP-basic-Basic-v1-Device.pdf>`__ device. The full UPnP device
architecture specification is available at
`UPnP-arch-DeviceArchitecture-v1.1.pdf <http://upnp.org/specs/arch/UPnP-arch-DeviceArchitecture-v1.1.pdf>`__.

Once nymea is running, it can be discovered via the `Simple Service Discovery Protocol
<https://en.wikipedia.org/wiki/Simple_Service_Discovery_Protocol>`__ (SSDP). A client discovers
devices by binding to the UDP multicast address ``239.255.255.250`` on port ``1900`` and sending:

.. code-block:: text

   M-SEARCH * HTTP/1.1
   HOST:239.255.255.250:1900
   MAN:"ssdp:discover"
   MX:4
   ST: ssdp:all

.. note::

   Use ``\r\n`` at the end of each line and twice at the end of the message.

Each UPnP device in the network responds with an HTTP/1.1 message. The nymead server response looks
like this:

.. code-block:: text

   HTTP/1.1 200 OK
   Cache-Control: max-age=1900
   DATE: Mon, 12 Oct 2015 09:39:36 GMT
   EXT:
   CONTENT-LENGTH:0
   Location: http://10.10.10.50:80/server.xml
   Server: nymea/0.9.0 UPnP/1.1
   ST:upnp:rootdevice
   USN:uuid:81d520cd-90cd-422d-9cbb-a0287e467e79::urn:schemas-upnp-org:device:Basic:1

The ``Location`` header points to an XML description document. Fetching it with an HTTP GET
identifies whether the remote system is a nymea:core instance:

.. code-block:: text

   GET http://10.10.10.50:80/server.xml

On a nymea:core instance this returns:

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <root xmlns="urn:schemas-upnp-org:device-1-0">
       <specVersion>
           <major>1</major>
           <minor>1</minor>
       </specVersion>
       <device>
           <presentationURL>http://10.10.10.60:80</presentationURL>
           <deviceType>urn:schemas-upnp-org:device:Basic:1</deviceType>
           <friendlyName>nymea home</friendlyName>
           <manufacturer>nymea GmbH</manufacturer>
           <manufacturerURL>http://nymea.io</manufacturerURL>
           <modelDescription>IoT server</modelDescription>
           <modelName>nymead</modelName>
           <modelNumber>1.16.0+202606081530~trixie1</modelNumber>
           <modelURL>http://nymea.io</modelURL>
           <serialNumber>57ae3295-13f8-42be-9de3-92acf9e8aa48</serialNumber>
           <UDN>uuid:57ae3295-13f8-42be-9de3-92acf9e8aa48</UDN>
           <iconList>
               <icon>
                   <mimetype>image/png</mimetype>
                   <width>32</width>
                   <height>32</height>
                   <depth>8</depth>
                   <url>/icons/nymea-logo-32x32.png</url>
               </icon>
               <icon>
                   <mimetype>image/png</mimetype>
                   <width>48</width>
                   <height>48</height>
                   <depth>8</depth>
                   <url>/icons/nymea-logo-48x48.png</url>
               </icon>
               <icon>
                   <mimetype>image/png</mimetype>
                   <width>64</width>
                   <height>64</height>
                   <depth>8</depth>
                   <url>/icons/nymea-logo-64x64.png</url>
               </icon>
               <icon>
                   <mimetype>image/png</mimetype>
                   <width>128</width>
                   <height>128</height>
                   <depth>8</depth>
                   <url>/icons/nymea-logo-128x128.png</url>
               </icon>
               <icon>
                   <mimetype>image/png</mimetype>
                   <width>256</width>
                   <height>256</height>
                   <depth>8</depth>
                   <url>/icons/nymea-logo-256x256.png</url>
               </icon>
           </iconList>
       </device>
   </root>

Compare ``modelName`` to ``nymead`` to confirm the remote system is a nymea:core instance. The
``uuid`` (from the ``UDN`` field, stripped of the ``uuid:`` prefix) uniquely identifies the
instance across reboots. Use Zeroconf (see below) to discover the actual API connection endpoints.

Zeroconf
~~~~~~~~

nymea advertises its services via `Zeroconf <https://en.wikipedia.org/wiki/Zero-configuration_networking>`__
using mDNS discovery. The service types are:

* ``_jsonrpc._tcp`` — nymea TCP socket interfaces
* ``_ws._tcp`` — WebSocket interfaces

The ``sslEnabled`` field in the ``txt`` record indicates whether the interface uses SSL encryption.
The ``port`` and ``address`` records provide the connection parameters.

Discovery with Avahi
^^^^^^^^^^^^^^^^^^^^

`Avahi <https://www.avahi.org>`__ is an open source Zeroconf implementation. With
``avahi-utils`` installed, search for nymea systems on the local network:

.. code-block:: bash

   avahi-browse -arl | grep -P '^=' -A 4 | grep "IPv4 nymea-" -A 4

Example output:

.. code-block:: text

   =  wlan0 IPv4 nymea-tcp-default   _jsonrpc._tcp   local
       hostname = [nymea.local]
       address = [10.10.10.121]
       port = [2222]
       txt = ["uuid={c82f7b33-d283-44f0-85df-6e7992dcf9e6}" "name=nymea" "sslEnabled=false"
              "jsonrpcVersion=1.4" "manufacturer=nymea GmbH" "serverVersion=0.9.0"]

   =  wlan0 IPv4 nymea-ws-default    _ws._tcp        local
       hostname = [nymea.local]
       address = [10.10.10.121]
       port = [4444]
       txt = ["uuid={c82f7b33-d283-44f0-85df-6e7992dcf9e6}" "name=nymea" "sslEnabled=false"
              "jsonrpcVersion=1.4" "manufacturer=nymea GmbH" "serverVersion=0.9.0"]

Message format
--------------

Once connected, the message exchange format is the same across all transports. With the exception of
notifications, all messages follow a request/reply pattern. Every message must be terminated with a
newline (``\n``) character.

Requests
~~~~~~~~

A request sent from the client to nymea:core:

.. code-block:: json

   {
       "id": 1,
       "method": "Namespace.Method",
       "token": "string",
       "params": {}
   }

Every request must include at least ``id`` and ``method``. The ``id`` must be unique per call and is
used to match responses back to their requests. Depending on the method, ``params`` may or may not
be required. If authentication is enabled on the interface, a ``token`` must also be included.

Responses
~~~~~~~~~

nymea:core responds with:

.. code-block:: json

   {
       "id": 1,
       "status": "string",
       "params": {},
       "error": "string"
   }

The ``id`` matches the originating request. The ``status`` field is always one of ``success``,
``error``, or ``unauthorized``. On success, ``params`` contains the response data. On failure,
``error`` contains a diagnostic message intended for developers, not end users.

The initial handshake
---------------------

Every new connection must send a ``JSONRPC.Hello`` message first:

.. code-block:: json

   {
       "id": 0,
       "method": "JSONRPC.Hello",
       "params": {
           "locale": "de_DE"
       }
   }

The ``locale`` parameter is optional. When provided, nymea:core translates all user-facing strings
(thing class display names etc.) into the requested language for the lifetime of the connection.
``JSONRPC.Hello`` can be called multiple times on the same connection — only the locale from the
last call is used. Other fields such as ``initialSetupRequired`` may also change between calls if
the system state has changed in the meantime.

If a token is included in the call, nymea:core verifies it and adds ``authenticated``,
``username``, and ``permissionScopes`` to the reply, so clients can combine the handshake and token
validation into a single round trip.

nymea:core replies with:

.. code-block:: json

   {
       "id": 0,
       "status": "success",
       "params": {
           "authenticationRequired": false,
           "initialSetupRequired": false,
           "language": "de",
           "locale": "de_DE",
           "name": "nymea home",
           "protocol version": "9.0",
           "pushButtonAuthAvailable": false,
           "server": "nymea",
           "uuid": "57ae3295-13f8-42be-9de3-92acf9e8aa48",
           "version": "1.16.0",
           "cacheHashes": [
               {"method": "Integrations.GetThings", "hash": "a1b2c3..."}
           ],
           "experiences": []
       }
   }

Response fields:

* ``authenticationRequired`` — if ``true``, all subsequent calls must include a valid ``token``.
* ``initialSetupRequired`` — if ``true``, no user exists yet; call ``Users.CreateUser`` to complete initial setup.
* ``language`` — the BCP 47 language tag derived from the active locale (e.g. ``"de"`` for ``"de_DE"``).
* ``locale`` — the full locale active for this connection (e.g. ``"de_DE"``).
* ``name`` — the user-visible name of this nymea:core instance.
* ``protocol version`` — the JSON-RPC API version of this instance.
* ``pushButtonAuthAvailable`` — whether push button authentication is available on this system.
* ``server`` — always ``"nymea"`` unless the product is rebranded.
* ``uuid`` — the persistent UUID of this nymea:core instance.
* ``version`` — the build version of this instance.
* ``o:authenticated`` — present when a token was supplied in the request; ``true`` if the token is valid.
* ``o:cacheHashes`` — list of ``{method, hash}`` pairs. As long as the MD5 hash for a given method has not changed since the last connection, the client may use a previously cached response for that method instead of fetching it again.
* ``o:experiences`` — list of active product experiences (``{name, version}``) loaded on this instance, used for product-specific overlays or feature sets.
* ``o:permissionScopes`` — present when a valid token was supplied; lists the permission scopes granted to that token.
* ``o:username`` — present when a valid token was supplied; the username associated with that token.

Introspecting the API
---------------------

The JSON-RPC API is self-describing. Call ``JSONRPC.Introspect`` to retrieve the full API schema at
runtime:

.. code-block:: json

   {
       "id": 1,
       "method": "JSONRPC.Introspect"
   }

The reply contains the complete schema:

.. code-block:: json

   {
       "id": 1,
       "status": "success",
       "params": {
           "enums": {},
           "flags": {},
           "objects": {},
           "methods": {},
           "notifications": {}
       }
   }

enums
~~~~~

The enums map lists enumeration types and their allowed values:

.. code-block:: json

   "CreateMethod": [
       "CreateMethodUser",
       "CreateMethodAuto",
       "CreateMethodDiscovery"
   ]

Wherever the schema uses ``$ref:CreateMethod``, an actual call carries one of those values:

.. code-block:: json

   "createMethod": "CreateMethodUser"

flags
~~~~~

The flags map lists flag types, which are enumerations that allow multiple values:

.. code-block:: json

   "CreateMethods": [
       "$ref:CreateMethod"
   ]

Wherever the schema uses ``$ref:CreateMethods``, an actual call carries an array of values:

.. code-block:: json

   "createMethods": ["CreateMethodUser", "CreateMethodDiscovery"]

objects
~~~~~~~

The objects map lists structured types used in the API:

.. code-block:: json

   "Vendor": {
       "id": "Uuid",
       "name": "String",
       "displayName": "String"
   }

Wherever the schema uses ``$ref:Vendor``, an actual call carries the full object:

.. code-block:: json

   "vendor": {
       "id": "8c566f13-d231-420e-b6cf-e3e810d0cc42",
       "name": "nymea",
       "displayName": "nymea GmbH"
   }

methods
~~~~~~~

The methods map lists all callable API methods:

.. code-block:: json

   "JSONRPC.Introspect": {
       "description": "Introspect this API.",
       "params": {},
       "returns": {
           "methods": "Object",
           "notifications": "Object",
           "enums": "Object",
           "flags": "Object",
           "objects": "Object"
       }
   }

notifications
~~~~~~~~~~~~~

The notifications map lists all events nymea:core can push to clients. A client subscribes to a
namespace using ``JSONRPC.SetNotificationsEnabled``. Once enabled, nymea:core pushes matching events
without the client polling. Example notification definition:

.. code-block:: json

   "Things.ThingAdded": {
       "description": "Emitted whenever a Thing was added.",
       "params": {
           "thing": "$ref:Thing"
       }
   }

The notification arrives as:

.. code-block:: json

   {
       "id": 13666,
       "notification": "Things.ThingAdded",
       "params": {}
   }

Property modifiers
------------------

Every property in the API can carry modifiers: ``r:`` (read-only), ``o:`` (optional), ``d:``
(deprecated). They can be combined.

.. code-block:: json

   "SomeObject": {
       "property1": "bool",
       "r:property2": "bool",
       "o:property3": "bool",
       "d:property4": "bool",
       "o:d:property5": "bool"
   }

* **No modifier** — present in both requests and responses.
* **r:** — only returned by nymea:core; must not be included in request params.
* **o:** — may be absent in both requests and responses.
* **d:** — still functional but may be removed in the next major API version. Check ``protocol version`` from the handshake before relying on deprecated properties.

Authentication
--------------

nymea can require authentication on the API (enabled by default). The ``authenticationRequired``
field in the handshake response indicates this. When required, every call except
``JSONRPC.Hello``, ``JSONRPC.Introspect``, ``Users.Authenticate``, and
``Users.RequestPushButtonAuth`` must include a valid token:

.. code-block:: json

   {
       "id": 1,
       "method": "Namespace.Method",
       "token": "NGE4ZTRjOWQtMjdiNi00ZDk0LTljOTYtOWRmNjkwYzY1MDNlCg==",
       "params": {}
   }

If the token is missing or invalid, the response is:

.. code-block:: json

   {
       "id": 1,
       "status": "unauthorized"
   }

Creating a user
~~~~~~~~~~~~~~~

On a fresh nymea system the handshake will return ``initialSetupRequired: true``. Call
``Users.CreateUser`` to create the first user. The username must be a valid email address; the
password must be at least 8 characters and contain uppercase, lowercase, and numeric characters:

.. code-block:: json

   {
       "id": 1,
       "method": "Users.CreateUser",
       "params": {
           "username": "a.valid@email.org",
           "password": "Upper,lower and a 1"
       }
   }

After a successful call, ``initialSetupRequired`` becomes ``false``.

Obtaining a token
~~~~~~~~~~~~~~~~~

Username and password
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: json

   {
       "id": 1,
       "method": "Users.Authenticate",
       "params": {
           "username": "a.valid@email.org",
           "password": "...",
           "deviceName": "nymea:app on Steve's iPhone"
       }
   }

Use a descriptive ``deviceName`` — it is shown to the user in the connected clients list.

On success:

.. code-block:: json

   {
       "id": 1,
       "status": "success",
       "params": {
           "success": true,
           "token": "NGE4ZTRjOWQtMjdiNi00ZDk0LTljOTYtOWRmNjkwYzY1MDNlCg=="
       }
   }

On failure:

.. code-block:: json

   {
       "id": 1,
       "status": "success",
       "params": {
           "success": false
       }
   }

The outer ``status`` is ``success`` because the server processed the request correctly. The inner
``success`` flag indicates authentication failure. No further detail is returned intentionally — a
potential attacker should learn as little as possible about the failure reason.

Push button
^^^^^^^^^^^

If push button authentication is available (indicated by ``pushButtonAuthAvailable`` in the
handshake), call ``Users.RequestPushButtonAuth``:

.. code-block:: json

   {
       "id": 1,
       "method": "Users.RequestPushButtonAuth",
       "params": {
           "deviceName": "nymea:app on Steve's iPhone"
       }
   }

nymea:core replies immediately with a transaction ID:

.. code-block:: json

   {
       "id": 1,
       "status": "success",
       "params": {
           "transactionId": "627f091d-06f0-4d17-b316-def225ddae25"
       }
   }

nymea then waits for a physical button press (30-second timeout). If the button is pressed in time,
a ``Users.PushButtonAuthFinished`` notification is sent to the requesting client:

.. code-block:: json

   {
       "id": 2,
       "notification": "Users.PushButtonAuthFinished",
       "params": {
           "success": true,
           "transactionId": "627f091d-06f0-4d17-b316-def225ddae25",
           "token": "NGE4ZTRjOWQtMjdiNi00ZDk0LTljOTYtOWRmNjkwYzY1MDNlCg=="
       }
   }

.. note::

   If a new push button request is started while another is already in progress (from the same or a
   different client), the previous attempt is cancelled with a ``PushButtonAuthFinished``
   notification with ``success: false``. The same happens when the timeout expires.

.. note::

   For development purposes, a fake push button module is available in the nymea source repository
   at ``tests/tools/simplepushbuttonhandler/``. Starting it simulates a push button and lets you
   trigger it with the space bar.
