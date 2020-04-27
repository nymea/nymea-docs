---
id: firststeps
title: First steps
---


At this point, a working installation of nymea:core should be set up on one device and nymea:app 
should be running on one or more devices such as smartphones or dektop PCs. Please refer to the 
previous sections if any of those isn't installed yet.

## Connecting to the network

The next step is to connect nymea:core to the local network. The recommended way to connect 
nymea:core to the network is by plugging in a LAN cable. However, if you installed nymea:core on a
device without LAN port, or just prefer to use WiFi, nymea offers an easy way to get nymea:core
connected to the network.

### Connecting via LAN cable

Connect the LAN cable to the system running nymea:core. It will automatically obtain the network
configuration via DHCP.

### WiFi setup in nymea:app

Depending on the used hardware, there are different ways to connect to WiFi. If nymea:app is running
on the same system as nymea:core, for example on a Raspberry Pi with touch screen, the network can be
set up using nymea:app by entering the *Network settings* in the *System Settings* view.

TODO: Screenies!

### Bluetooth to WiFi setup

If nymea:core is running on a headless system, nymea:app can be used from another device, e.g. a smart phone
or Laptop to configure the WiFi of the nymea:core system by connecting via Bluetooth.

In nymea:app, open the *Wireless setup* menu and wait for the nymea:core system to appear in the list.

TODO: Screenie

Connecto to nymea:core by selecting it from the list. Once connected, nymea:core will start scanning for
WiFi networks and present the result to nymea:app.

TODO: Screenie

Select the preferred WiFi from the list and enter the password.

TODO: Screenie

If everything went well, the nymea:core system is now connected to the WiFi.


## First setup

Now that nymea:core is connected to the network, it is time to create login credentials to keep the nymea
setup protected. When connecting to a nymea:core system for the first time, it will prompt for a username
and a password.

