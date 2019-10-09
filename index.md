# nymea developer documentation


## nymea:core

The main nymea SDK provides a middleware service interacting with devices/services and managing them. Usually nymead is ran on a edge gateway device (e.g. a bridge) and interacts with devices in that location. However, nymead can also be run on edge devices to add cloud connections, Bluetooth-to-WiFi setup capabilities or an API to interact with such a device. nymea:core's functionalities are extended with nymea:plugins.

[libnymea](nymea/libnymea-module.html)
[nymea](nymea/index.html)
[nymea server](nymea/nymeaserver.html)
[nymea interfaces](nymea/interfaces.html)


### The plugin API

Plugins provide a way to extend nymead features. Most commonly a nymea plugin adds support for a certain device or online service.

[nymea plugins](nymea-plugins/index.html)
[Write plugins](nymea/write-plugins.html)

### The client API

[The nymea client API](nymea/jsonrpc.html) is used to build client applications for nymea. For instance, a mobile application like nymea:app interacts with nymea through this API. This JSON-RPC based API can either be used raw, or through a client lib.

## Client libraries
In order to ease up development for client applications, nymea provides client libraries and apps.

### nymea:app
nymea:app is a fully featured client app for nymea. It can be styled and branded but also used as a Qt/QML nymea client library to build a completely custom application UI.

## Standalone tools

In addition to the main nymea SDK, smaller subsets of nymea features are broken out in standalone libraries or tools. For instance, to just add the Bluetooth-to-WiFi to an IoT device without the need of other APIs, nymea-networkmanager can be used standalone.

### nymea-networkmanager

[nymea-networkmanager](libnymea-networkmanager/index.html) provides easy to use Bluetooth-to-WiFi setup for IoT devices.

### nymea CoAP
[nymea-coap](nymea-coap/index.html) is a C++/Qt5 based coap library by nymea.

## nymea MQTT
[nymea-mqtt](nymea-mqtt/index.html) provides a C++/Qt5 based MQTT library. Both, an MQTT client and an MQTT are supported up to version 3.1.1 via TCP or WebSocket, both plaintext or SSL encrypted. In addition, nymea-mqtt also provides a minimalistic standalone MQTT server.

## nymea GPIO
[nymea-gpio](nymea-gpio/index.html) procides a C++/Qt5 based GPIO library to easily interact with GPIOs on devices.


## Example

This is an example link for showing the link possibilities

[example](example.html)
