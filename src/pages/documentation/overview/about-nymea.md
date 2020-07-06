---
id: overview
title: About nymea
---

The main purpose of nymea is to provide a collection of tools, libraries and services to build fully connected devices. Nymea provides solutions that scale from highly specific IoT use cases to fully featured smart home platforms, including cloud connectivity.

Given nymea follows a local-first approach, everything can be done without cloud connection and all data is kept in the local network.

## nymea structure

Nymea consists of three parts: nymea:core, nymea:app and nymea:cloud.


![](/img/nymea-overview.svg)

### nymea:core

nymea:core is the core piece of the platform. It refers to the services and libraries used to build the edge or bridge device where the main software is the nymea daemon or nymead. It can run on any Linux powered device:

  * A typical smart home setup for instance would run a nymea:core on a Raspberry Pi in a home network and talk to IoT devices in the home via WiFi, Bluetooth, ZigBee etc.
  * A smart hot tub for instance would run nymea:core in a embedded device in the Hot Tub (e.g. a Beaglebone Black, a Raspberry Pi or any other SoC running Linux) and control the hot tub through GPIOs.

See [nymea:core](/documentation/users/installation/core) for more details.

### nymea:app

nymea:app is the user facing frontend of a nymea system. It is a client app running on a phone, on the IoT edge device (in case it has a display) or a Laptop/PC. Please refer to the [nymea:app](/documentation/users/installation/app) page for more details.

### nymea:cloud

nymea:cloud is optional and extends nymea with cloud centric features such as delivering push notifications to client devices or enabling remote connections from nymea:app to nymea:core in an easy to setup and secure manner.

## Plug-in based and extensible

nymea is made of building blocks. Using plugins for many tasks, a large variety of setup combinations is possible.

![nymea structure](https://raw.githubusercontent.com/guh/nymea-wiki/master/docs/en/images/home-stack.png)

