.. _doc-overview-features:

Features
========

nymea is built as a local-first IoT and smart-home platform. It connects devices and services on a
Linux-based edge system, exposes APIs for client applications and automation, and can optionally use
cloud services for remote access and push notifications.

Local-first platform
--------------------

nymea:core runs locally and keeps device control, automation and data inside the local network. Internet
access is optional for local operation. This makes nymea suitable for private smart-home installations,
connected products and gateways that must continue working without cloud connectivity.

Supported platforms
-------------------

nymea:core is available for Debian and Ubuntu based Linux systems, including common single-board
computers and PCs. It can also be built from source for other Linux based systems.

For product development and embedded systems, nymea can be integrated into custom Linux distributions,
including Yocto based systems.

Client applications
-------------------

:doc:`nymea:app <../users/installation/app>` is the user-facing client for configuring and controlling a
nymea system. It is written with Qt and is available for common desktop and mobile platforms, including
Android, iOS, Windows, macOS and Linux desktop systems.

Integrations and device support
-------------------------------

Integration plugins connect nymea to devices, online services and protocols. Plugins expose devices as
things with states, events and actions, so automations and client applications can interact with different
products through a consistent model.

Supported device and service categories include:

* lights, sockets, switches and buttons
* sensors for temperature, humidity, light, presence, pressure and similar values
* blinds, awnings, shutters, doors and gates
* smart meters, energy devices and electric vehicle chargers
* heating, ventilation and climate devices
* media devices and online services
* notifications and system services

Devices that do not fit an existing category can still be integrated using generic states, events and
actions.

Zigbee and Z-Wave
-----------------

nymea can manage Zigbee and Z-Wave networks through supported adapters. Zigbee support includes common
device classes from the Zigbee cluster library, such as lighting, measurement and sensing, HVAC, closures,
security and smart energy devices.

More information about managing Zigbee and Z-Wave networks can be found in
:doc:`the configuration documentation <../users/usage/configuration>`.

Automation rules and scenes
---------------------------

Rules add automation behavior to a nymea system. They can react to state changes, events, time conditions
and system context, then execute actions on one or more devices.

Rules can be used for tasks such as:

* turning lights on when presence is detected
* sending notifications when a door lock changes state
* controlling blinds based on sunrise, sunset or time schedules
* changing heating or charging behavior based on device state
* creating scenes that can be triggered from a client application

Tags can be assigned to things and rules to group devices by room, building, function or favorites.

Script engine
-------------

nymea also includes a script engine for custom system behavior that goes beyond regular automation rules.
Scripts can react to events, inspect system state and execute actions using a QML-like syntax. See
:doc:`the scripting documentation <../users/usage/scripting>` for examples and API details.

Connectivity and APIs
---------------------

nymea exposes its API through JSON-RPC over TCP and WebSocket connections. Authentication and encrypted
connections can be configured depending on the deployment and client requirements.

The local API is the foundation for nymea:app, custom client applications and integrations with other
systems. See :doc:`the client development documentation <../developers/clients/index>` for more details.

Network and device services
---------------------------

nymea includes services that are useful for IoT gateways and connected products:

* integrated web server for local interfaces and debugging tools
* MQTT broker and MQTT client functionality
* network discovery using technologies such as Zeroconf and UPnP
* Ethernet and Wi-Fi connectivity support

Remote access
-------------

nymea does not require an online account or cloud infrastructure to run. Local device control,
automation, logging and APIs work inside the local network.

For remote access, nymea can use an optional remote proxy server. The proxy allows a client to connect to
a nymea system behind a firewall without manual port forwarding in the user's network.

Logging and troubleshooting
---------------------------

nymea records state changes, events and actions in a local log database. The logs can be filtered by
device, type and time range, making it easier to understand system behavior and diagnose issues.

An optional debug web interface provides access to configuration, logs and diagnostics for troubleshooting
and support.

Developer support
-----------------

nymea provides APIs and C++ libraries for building integrations and clients. Integration developers can
use existing abstractions for common protocols and hardware layers such as Zigbee, Z-Wave, Bluetooth,
NFC, CoAP, MQTT, Modbus, GPIO and HTTP based devices or services.

Development of nymea:core and integration plugins is supported on Linux. Development workflows can use
standard C++ tools for building, debugging and profiling. See :doc:`the developer documentation
<../developers/index>` for build instructions and plugin development guides.
