---
id: snap
title: Snap
---

Get the nymea snap from the official Snap Store:

<dl>
<a href="http://snapcraft.io/nymea" style="display:inline-block;overflow:hidden;background:url(https://snapcraft.io/static/images/badges/en/snap-store-black.svg) no-repeat;width:182px;height:56px;background-size:contain;"><span style="clip: rect(1px, 1px, 1px, 1px);clip-path: inset(50%);height: 1px;width: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;">Snap Store</span></a>
</dl>
<br />

The nymea server is also available as a snap package for `amd64` and `armhf`. The snap contains the `nymead` service, the default `nymea-plugins` and `nymea-cli`. You can find the snap build scripts [here](https://github.com/nymea/nymea-snap). If you have a running snapd daemon on your system, you should find the nymea package using following command:

    $ snap find nymea
    Name       Version              Publisher  Notes  Summary
    nymea      0.16.0+201910281459  nymea-gmbh   -    An open source IoT server
    nymea-app  1.0.149              nymea-gmbh   -    Client application for nymea



You can install the snap using following command:

    $ sudo snap install nymea
    nymea 0.16.0+201910281459 from 'nymea-gmbh' installed


You can get information about the snap using following command:

    $ snap info nymea
    
    name:      nymea
    summary:   An open source IoT server
    publisher: nymea GmbH developer (nymea-gmbh)
    contact:   https://nymea.io
    license:   unset
    description: |
      nymea is a plugin based IoT (Internet of Things) system.
      
      It consists of nymea:core, nymea:app and nymea:cloud.
      
      nymea:core works like a translator for devices, things and services
      and allows them to interact. With the powerful rule engine you can connect
      any device available in the system and create individual scenes and
      behaviors for your environment.
      
      nymea:app is a client application available for just about any
      platform/form factor out there. It allows to interact with nymea:core and
      nymea:cloud.
      
      nymea:cloud is the cloud instance, which can connect nymea:app to
      nymea:core even when you're not in your home network and enables other
      features like push notifications being sent from nymea:core to the devices
      running nymea:app.
    commands:
      - nymea.nymea-cli
    services:
      nymea.nymead: simple, enabled, active
    snap-id:      vuamj1HCwJHJ1cxi7FAbMxvPyV4ae5qW
    tracking:     stable
    refresh-date: today at 21:56 CET
    channels:
      stable:    0.16.0+201910281459 2019-10-28 (399) 69MB -
      candidate: 0.16.0+201910281459 2019-10-28 (399) 69MB -
      beta:      0.17.0+201911271725 2019-11-27 (431) 69MB -
      edge:      0.17.0+201911270103 2019-11-27 (427) 69MB -
    installed:   0.16.0+201910281459            (399) 69MB -


## Interact with the snap


### Run the nymea-cli command line interfaces

        $ nymea.nymea-cli

### Get the status of nymea

        $ systemctl status snap.nymea.nymead.service

### Stop nymea

        $ sudo systemctl stop snap.nymea.nymead.service

### Restart nymea

        $ sudo systemctl restart snap.nymea.nymead.service

### Disable autostart of nymea

        $ sudo systemctl disable snap.nymea.nymead.service

### Enable autostart of nymea

        $ sudo systemctl disable snap.nymea.nymead.service

### Get the debug output of nymea

        $ sudo journalctl -f -u snap.nymea.nymead.service


## Connect the needed interfaces
----------------------------------

Since snap is very stric about permissions, you need to connect the slots and plugs needed by the nymea snap.

- nymea:avahi-control
- nymea:avahi-observe
- nymea:bluez
- nymea:network-manager

Once you connected an interface, you need to restart the nymea daemon using `sudo systemctl restart snap.nymea.nymead.service`.

### Enable avahi discovery

        sudo snap connect nymea:avahi-control
        sudo snap connect nymea:avahi-observe

### Enable bluetooth support

        sudo snap connect nymea:bluez

### Enable network-manager support

        sudo snap connect nymea:nymea:network-manager


## Switch channel

If you want to switch the release channel of the nymea snap, you can take a look with `snap info nymea` which channels are available and which version is released in each channel.

Here you can see an example of the channel list. The `tracking` field tells you which channel is currently installed and gets updated.

    channels:
      stable:       0.9.0 (2) 72MB -
      candidate:    0.9.1 (3) 72MB -
      beta:         0.9.2 (4) 73MB -
      edge:         0.9.3 (5) 74MB -
      
### Switching to `stable`

        $ sudo snap refresh nymea --stable

###  Switching to `candidate`

        $ sudo snap refresh nymea --candidate

###  Switching to `beta`

        $ sudo snap refresh nymea --beta

###  Switching to `edge`

        $ sudo snap refresh nymea --edge
