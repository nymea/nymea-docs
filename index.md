# nymea developer documentation


## nymea:core SDK

The main nymea:core SDK provides a middleware service interacting with devices/services and managing them. Usually nymead is ran on a edge gateway device (e.g. a bridge) and interacts with devices in that location. However, nymead can also be run on edge devices to add features like cloud connections, Bluetooth-to-WiFi setup capabilities or an API to interact with such a device from client applications.

Adding support for new devices to nymea is done via plugins.

### Setting up nymea:core for development

As nymea is built with Qt, having Qt installed is a prerequisite. The recommended development platform is Debian based Linux distributions as nymea provides packages for all libraries for Debian and Ubuntu. Please refer to the [nymea wiki](http://wiki.nymea.io) for information on supported versions for prebuild packages.

The recommended IDE is QtCreator. nymea provides a QtCreator wizard for creating plugins. However, QtCreator is not a requirement, everything can be built with common unix development tools (make/make install) or any IDE with support for those.

TODO: apt-foo for getting up and running in subpage

#### Building nymea:core from sources

Normally, having a pre-built edition of nymea installed on a development machine is enough to work on nymea plugins or client apps. In order to work on patches for nymea:core itself, or if there are no prebuilt packages available for the target platform, nymea can be compiled from source code manually.

TODO: Build instructions on a subpage

#### Running nymea:core for development

On a target platform, nymead is normally started at system startup as a system service. For development however, it is more efficient to manually run nymead from the command line.

TODO: Run instructions, logging options etc in subpage

### The plugin API

Plugins provide a way to extend nymead features. Most commonly a nymea plugin adds support for a certain device or online service. Plugins can interact with local hardware, remote hardware (e.g. through network or Bluetooth) or with remote services, for instance cloud APIs in the internet. Basically, a plugin is the translator between nymea's internal data structures and another API/Protocol.

[nymea plugins](nymea-plugins/index.html)
[Write plugins](nymea/write-plugins.html)

### The client API

[The nymea client API](nymea/jsonrpc.html) is used to build client applications for nymea. For instance, a mobile application like nymea:app interacts with nymea through this API. This JSON-RPC based API can either be used raw, or through a client lib.

## Client libraries
In order to ease up development for client applications, nymea provides client libraries and apps.

### nymea:app
nymea:app is a fully featured client app for nymea. It can be styled and branded but also used as a Qt/QML nymea client library to build a completely custom application UI for IoT devices running nymea:core.

## Standalone tools

In addition to the main nymea SDK, smaller subsets of nymea features are broken out in standalone libraries or tools. For instance, to just add easy Bluetooth-to-WiFi setup to an IoT device without the need of other APIs, nymea-networkmanager can be used standalone.

### nymea-networkmanager

[nymea-networkmanager](libnymea-networkmanager/index.html) provides easy to use Bluetooth-to-WiFi setup for IoT devices.

### nymea CoAP
[nymea-coap](nymea-coap/index.html) is a C++/Qt5 based coap library by nymea.

### nymea MQTT
[nymea-mqtt](nymea-mqtt/index.html) provides a C++/Qt5 based MQTT library. Both, an MQTT client and an MQTT are supported up to version 3.1.1 via TCP or WebSocket, both plaintext or SSL encrypted. In addition, nymea-mqtt also provides a minimalistic standalone MQTT server.

### nymea GPIO
[nymea-gpio](nymea-gpio/index.html) procides a C++/Qt5 based GPIO library to easily interact with GPIOs on devices.


## Building images for devices

### Raspberry Pi

nymea provides build scripts and pre-built images for the Raspberry Pi based on the upstream Raspbian image. The scripts used to build those images can be found [here](https://github.com/nymea/pi-gen).

### Yocto

nymea provides a [meta-layer](https://gihtub.com/nymea/meta-nymea) for all the libraries and tools of nymea.
