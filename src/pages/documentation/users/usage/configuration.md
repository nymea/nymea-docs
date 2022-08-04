---
id: configuration
title: Configuration
---

Nymea configuration happens in nymea:app. The main menu will hold two sections: "System settings" and "App settings". System settings contains all the settings that affect nymea:core while App Settings contains the configuration for the particular app client being used.

## System Settings


![](/img/configuration/system-settings.png)

### General

The general settings section allows to configure the name which is used for this nymea system and the time and timezone settings.

![](/img/configuration/system-settings-general.png)

#### Name
The name will be used whenever the nymea system announces itself in the network. This is useful if there are more than one nymea systems in a network to be able to identify them.

#### Date and time

Date and time sets the date and time on the nymea:core system. By default this will be set to automatically obtain the current date and time from the internet. If that is not possible, for example because the nymea system is used without any internet connection, the automatic time setting can be disabled and the time can be set manually.

### User settings

In the user section the current password can be changed as well as locking out authenticated clients.

> Note: This section will only be available if nymea:core is configured to require authentication.

![](/img/configuration/system-settings-user.png)

#### User info

Tapping the "Change password" field allows to change the current password.

#### Devices/Apps accessing nymea:core

This list holds all the clients that have successfully authenticated to this nymea system. If a device has been stolen or lost, the authentication token can be removed here and with that this particular device will be locked out of the system and needs to authenticate again before accessing the system. Swipe or longpress an entry to reveal the delete button.

### Network settings

The networking section allows to configure network connectivity of the nymea:core system.

> Warning: Using wrong configuration settings might prevent clients to connect to the nymea:core system

When using hardware with wired and wireless network available, such as a Raspberry Pi 3 or 4, a good choice is to connect nymea to the local network using a cable and at the same time use the wireless interface to host an access point which can be used to directly connect wireless IoT devices to the nymea system without having them part of your private network.

![](/img/configuration/system-settings-networking.png)

#### General

The general section allows to completely disable networking.

#### Wired network

The wired connection setup will list all available wired network interfaces of the nymea:core system.

#### Wireless network

The wireless connection setup allows to control the wireless network interfaces of the nymea:core system. Using this section, the nymea:core system can be connected to a wireless network or host an access point. 

### Cloud

The cloud settings allow connecting a nymea:core system to nymea:cloud. For this, the nymea:core system needs to be registered in nymea:cloud. Once done so, it will connect to the cloud server and wait for incoming requests through the cloud. This is useful in order to access a nymea:core system from anywhere.

Using the cloud connection, a user can connect from anywhere to the nymea:core without having to configure any port forwarding or similar in the router or signing up for a dynamic DNS service.

![](/img/configuration/system-settings-cloud.png)

Note that in order to access a nymea:core system through the cloud, nymea:app needs to be signed into nymea:cloud too and the box needs to be paired with a cloud username. If nymea:core and nymea:app are connected to nymea:cloud the pairing will happen automatically when the two are connected locally in the same network first. Once this happens, the remote connection for this user and core system will be activated.

### Connection interfaces

The connection interfaces section allows to configure on which ports the clients can connect to this nymea:core system.

![](/img/configuration/system-settings-api-interfaces.png)

By default, a nymea:core system can be connected to via a TCP socket on port 2222 and a WebSocket on port 4444. For usage with nymea:app, any of them work equally. Due to the overhead that comes with WebSocket compared to a TCP socket, the TCP socket would perform slightly better. When using different clients than nymea:app, for example a self made script, it might be easier to connect using a WebSocket as that is a well supported technology in web browsers.

This section also allows to configure the usage of SSL encryption per connection interface. It is strongly advised to keep both, SSL encryption and authentication enabled. However, when using clients that do not support SSL encryption it can be disabled here. Each interface can be configured to listen to only localhost connections (useful for e.g. scripts or nymea-cli on the nymea:core system), to any network interface or only to a particular network interface.

Swipe an entry to the left or longpress on it to revleal the remove button and disable it.

> Note that removing the connection interface currently used will disconnect the connection immediately. The currently used connection interface is shown via the highlighted icon.

### MQTT broker

Nymea features an integrated MQTT broker. This section allows to configure it.

![](/img/configuration/system-settings-mqtt.png)

#### MQTT server interfaces

Similar to the Connection interfaces, this section allows to configure all the network interfaces and ports where the MQTT broker should be avaialbe. For each interface/port SSL encryption and authentication can be enabled or disabled. Longpress or swipe to the left in order to remove an interface. In order to use integration plugins that use MQTT, at least one MQTT server interface must be enabled.

#### MQTT permissions

When authentication is enabled on an MQTT server interface, a permission needs to be created in order to allow 3rd party MQTT clients to connect to the MQTT broker. MQTT permissions are defined by a client ID, a username, a password and the topics this client should be allowed to connect to.

> Note that this is not required for integration plugins using MQTT. Integrations can grant permissions to clients automatically by generating a permission specifically for the particular use case.


### ZigBee

The ZigBee section allows to manage ZigBee networks within nymea. In order to use ZigBee with nymea, a ZigBee adapter is required.

#### Supported ZigBee adapters

The following hardware adapters are supported:

* [Texas Instruments](https://www.ti.com/product/CC2652R)
    This adapter can be found in various shops, either without firmware or preflashed. A z-Stack based firmware is required on the adapter to work with nymea. When choosing an option, select the firmware for zigbee2mqtt which will work fine with nymea (zigbee2mqtt is not required) or manually flash the stick with a build of z-Stack
    * CC2652 (P/R/RB) - recommended option
    * CC253x

* [Dresden Elektronik](https://www.dresden-elektronik.de/)
    All phoscon models are supported, however, only ConBee can be auto-detected. Select baut rate 38400 for RaspBee modules during ZigBee network setup.
    * [ConBee](https://phoscon.de/en/conbee)
    * [ConBee II](https://phoscon.de/en/conbee2)
    * [RaspBee](https://phoscon.de/en/raspbee)
    * [RaspBee II](https://phoscon.de/en/raspbee2)

* [NXP ZigBee 3.0 Modules](https://www.nxp.com/pages/jn516x-7x-zigbee-3-0:ZIGBEE-3-0)
    NXP based adapters are supported, provided they are flashed with the nymea firmware.
    * JN5168
    * JN5169 

#### Setting up a ZigBee network

With the ZigBee adapter connected to the nymea system, a new ZigBee network can be created from System Settings -> ZigBee. Multiple ZigBee adapters may be used to create multiple separated ZigBee networks.

![](/img/configuration/system-settings-zigbee-add-network.png)

Since most ZigBee modules are based on UART communication, the hardware cannot always be auto-detected. Some hardware modules (USB based like ConBee II) can be identified and recognized automatically, other modules based on raw UART connections like the JN5168 or RaspBee II need to be added and configured manually.

![](/img/configuration/system-settings-zigbee-adapters.png)

When adding a new ZigBee network in nymea, available UART ports can be listed. If a module can be auto-detected, all the UART information will be pre-filled, else it needs to be provided when configuring the ZigBee network.

If a module does not get recognized due to missing hardware information (like JN5168 or ConBee 1 / RaspBee 1), the user has to select the UART port, the backend type to use and the baud rate for this hardware type.

![](/img/configuration/system-settings-zigbee-custom-uart.png)

#### Adding new ZigBee devices

In order to add a new ZigBee device into a nymea managed network, the network needs to be opend for allowing new nodes to join the network. The default open time window is 120 seconds, but it can be extended if required or closed immediatly if desired.

Once the network is open, the pairing prodecure of the ZigBee device can be started and the node will join the network. Initiating the pairing procedure on the device may vary between different devices and manufacturers. Please refer to the manual of the device to learn how to start the pairing procedure.

![](/img/configuration/system-settings-zigbee-network-overview.png)

![](/img/configuration/system-settings-zigbee-network-open.png)

If nymea recognized the ZigBee node, a new thing will show up automatically in the system and is ready to use. If a ZigBee node appears but is listed as unrecognized device, an appropriate nymea integration plugin may be required.

The list of supported ZigBee integration plugins can be found [here](https://preview.nymea.io/documentation/resources/integrations/?technology=zigbee).

> Installing the meta package `nymea-plugins-zigbee` will install all available ZigBee integrations and is recommended for most users.

#### Removing a ZigBee device

In order to remove a ZigBee node from the network, there are two possible options:

* **Remove related thing**: If the ZigBee node has been recognized and a device has been created for the node, the device can be removed from the network by removing the thing from the system.
* **Restart pairing process**: Some device can also be removed from a network by restarting the pairing process, while the network is closed. Not all backends support this feature.

#### Removing / Resetting a ZigBee network

In order to remove an entire network and all releated things within nymea, there are two possibilies.

* **Removing the network**: By removing the network, the UART will be free again for other software to use and all ZigBee nodes, settings and related things will be removed permanent from the system.
* **Factory reset network**: By factory resetting a network, all nodes and related things will be removed from the network. If the backend supports it, also all configuration on the ZigBee hardware will be wiped. The entire stack performs a restart and will start a new network, perform a new channel scan and pick a new network ID.

![](/img/configuration/system-settings-zigbee-network-settings.png)

### Z-Wave

The Z-Wave section allows to manage Z-Wave networks within nymea. In order to use Z-Wave with nymea, a Z-Wave adapter is required.

#### Supported Z-Wave adapters

Pretty much all Z-Wave adapters should work with nymea, given Z-Wave uses a standardized protocol. However here's a list of well tested and known to work adapters. Please report any known to work adapters to nymea so this list can be updated.

* [Aotec](https://aeotec.com/)
    * [Aeotec Z-Stick Gen5](https://aeotec.com/products/aeotec-z-stick-gen5/): This adapter is also sold as other brands such as the Zooz S2 USB controller.

* [Z-Wave.Me](https://z-wave.me/)    
    * [RaZberry](https://z-wave.me/products/razberry/)


#### Setting up a Z-Wave network

With the Z-Wave adapter connected to the nymea system, a new Z-Wave network can be created from System Settings -> Z-Wave. Multiple Z-Wave adapters may be used to create multiple separated Z-Wave networks.

#### Adding new Z-Wave devices

In order to add a Z-Wave device into a nymea managed network, enter the network settings and press the "Add device" button. Once the network is waiting for the new device to join, the pairing prodecure of the Z-Wave device can be started and the node will join the network. Initiating the pairing procedure on the device may vary between different devices and manufacturers. Please refer to the manual of the device to learn how to start the pairing procedure.

If nymea recognized the Z-Wave node, a new thing will show up automatically in the system and is ready to use. If a Z-Wave node appears but is listed as unrecognized device, an appropriate nymea integration plugin may be required.

The list of supported Z-Wave integration plugins can be found [here](https://preview.nymea.io/documentation/resources/integrations/?technology=z-wave).

> Installing the meta package `nymea-plugins-zwave` will install all available Z-Wave integrations and is recommended for most users.

#### Removing a Z-Wave device

In order to remove a Z-Wave node from the network, enter the Z-Wave settings and press the "Remove device" button. Once the network is waiting for the device to leave, initiate the pairing procedure on the device.

#### Removing / Resetting a Z-Wave network

Z-Wave networks can be removed from nymea. This, however, will not reset the configuration of the Z-Wave controller. A network can be removed from one nymea instance and tranferred to another simply by removing it and creating it again on a different instance.

In order to permanently remove the Z-Wave network from the controller, the "Factory reset controller" button may be used from the Z-Wave network settings. Please note that all devices connected to the Z-Wave network need to be factory reset in order to connect to another Z-Wave network again.

### Web server

Nymea features an integrated web server. The web server is used to host the [nymea debug interface](#debug-interface) but can also be used to host any website.

![](/img/configuration/system-settings-webserver.png)

In order to use the debug interface, at least one web server interface needs to be enabled. Similar to the connection interfaces, SSL encryption and authentication can be enabled for each web server individually. When adding a server interface, the path to a website located on the nymea:core system can be provided.

> At this point nymea does not support server-side code execution like php or similar.

### Plugins

This section lists all the installed integration plugins. Some integration plugins may offer a plugin wide configuration which can be accessed here.

![](/img/configuration/system-settings-plugins.png)

### Deverloper tools

The developer tools section hosts options specific to development and trouble shooting.

![](/img/configuration/system-settings-developer.png)

#### Debug interface

When the debug interface is enabled, it will be served on all the enabled [web server](#web-server) interfaces. The debug interface allows to inspect system logs and create debug information bundles that can be submitted to developers to help with development.

### System update

This section allows to update the nymea:core system as well as installing more plugins.

![](/img/configuration/system-settings-updates.png)

When system updates are available, they will be listed here and can be updated individually or all at once. It is recommended to update all at once for most users.

#### Testing and experimental

For users that want to test prereleases of nymea software, the configuration button on the upper right allows to enable additional repositories.

> Please be aware that using testing or experimental repositories is likely to introduce issues into a nymea system occationally. Please only enable those sections if acknowledging this and being ready to repair things.

### Log viewer

The log viewer shows everything that happens in the nymea system. Every button press, ever sensor state change and such will be logged in here and can be inspected at a later point. This is useful when tracing down unexpected behavior, for instance if smart rules or scripts are not behaving as expected.

![](/img/configuration/system-settings-logs.png)

### About nymea:core

The last section in the system setttings shows version numbers, license information and other useful details that might be of interest when reporting issues.

![](/img/configuration/system-settings-about.png)

