---
id: overview
title: Overview
---

The main purpose of nymea is to provide a collection of tools, libraries and services to connect devices and online services between each other or build connected devices.
Nymea can be used to solve specific small problems for IoT based use cases as well as building a fully featured smart home platform. It is open source and privacy focused. Given nymea follows a local-first approach, everything can be done without cloud connection and all data is kept in the local network.

## nymea structure

nymea consists of three parts: nymea:core, nymea:ux and nymea:cloud.


![](/img/nymea-overview.svg)

### nymea:core

nymea:core is the core piece of the platform. It refers to the services and libraries used to build the edge device where the main software is the nymea daemon or nymead. It can run on Linux powered 
devices like on a Raspberry Pi:

  * A typical smart home setup for instance would run a nymea:core on a Raspberry Pi in a home network and talk to IoT devices in the home via WiFi, Bluetooth, ZigBee etc.
  * A smart hot tub for instance would run nymea:core in a embedded device in the Hot Tub (e.g. a Beaglebone Black, or a Raspberry Pi) and control the hot tup through GPIOs.

### nymea:ux

nymea:ux refers to the user facing frontend of a nymea system. This can be a client app running on a phone, a frontend app running on the IoT edge device too (in case it has a display) or a command line interface. Please refer to the [Clients](https://nymea.io/en/wiki/nymea/master/clients) page for available frontends.

### nymea:cloud

nymea:cloud is optional and extends nymea with cloud centric features such as delivering push notifications to client devices or enabling remote connections from nymea:ux to nymea:core in an easy to setup and secure manner.

## Plug-in based and extensible

nymea is made of building blocks. Using plugins for many tasks, a large variety of setup combinations is possible.

![nymea structure](https://raw.githubusercontent.com/guh/nymea-wiki/master/docs/en/images/home-stack.png)

