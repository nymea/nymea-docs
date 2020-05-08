---
id: faq
title: Frequently asked questions
---

## nymea

### How do I install nymea?

TODO Insert link to install page

### Is there a list of supported devices/services?

TODO insert link to plug-in list

### How do I (re)start nymea?

``` sudo systemctl restart nymead ```

### How do I make nymea start on reboot?*

``` sudo systemctl enable nymead ```

### How do I see the debug output?

nymea:app -> menu -> system settings -> developer tools -> debug interface

### My plug-in hasn't loaded/displayed, even though I've installed it

Possible issues:

* nymea hasn't been restarted after installation
* API incompatibility between plug-in and nymea
* Unreferred symbols of the plug-in
* Missing/wrong entry in the plug-in json file
* Plug-in stored in the wrong folder

nymea prints the reason why a plug-in hasn't loaded during start as warning.

## nymea:app

### nymea:app can't find my nymea instance

Possible issues:

* nymea:app device is not in the same network as the nymea device
* Router is blocking UPnP and mDNS
* Firewall on the nymea:app device is blocking UPnP or mDNS
* nymea hasn't booted yet completely, or nymea is not running
* Weak WiFi signal strenght on eather nymea or nymea:app device

### How can I reset my nymea password?

Deleting the file user-db.sqlite and restarting nymea will reset the user,
and you will be required to setup a new user the first time you connect 
to your nymea.


### Can I install nymea on Windows/macOS/Unix/Comodore64?

Find here a complete list of supported operating systems: TODO

### Can I install nymea on Banana/Orange/Litchie/Raspberry Pi?

nymea offers precompiled packages for ARMHF, ARM64, AMD64, X86 processor architectures-
As long as your operating system is supported, you will have a good change to get 
nymea running on it.

## nymea:cloud

### Does nymea:cloud store personal information?

nymea:cloud does only store information that it needs for operation:
  * A user account
  * Device IDs belonging to a user to match remote connection attempts
  * Optionally, notification endpoints for sending push notifications to devices
  
We take your privacy seriously.

## License 

### Can I build commercial products out of nymea?

Yes! As long as you fullfill all condidionts of one of our licenses. You can go with the GPLv3
license, or you can contact us to optain a commercial reseller license or even obtain a full developer SDK license.

For more details, please visit [nymea's general terms on conditions](https://nymea.io/legal/GTC.pdf).

### Can I use nymea:app or BerryLan for my own app?

Yes! As long as you fullfill all conditions of one of our licenses.

### What does the GPLv3 require me to do?

Using GPLv3 code generally requires you to be a good player in the Free and Open Source ecosystem. That means for a start, that you cannot change the license.
Any change you do to the code is required to be open sourced too. Whenever you release your code to the public (or sell it to someone) you need to also ship the entire source code required for a user to create their own builds from it. In addition to that, devices you create with GPLv3 licensed code must not be locked down in a way that users cannot modify and flash their own builds to it.

### Will obtaining a commercial license get rid of the GPLv3 restrictions

Yes. We will build closed source packages for you which you can distribute without the GPLv3 obligations. Upon request we can add additional features and tune the system according to your use case.

There is also the possibility to obtain a developer/SDK license of nymea. This license will allow you to create your own modifications to nymea and all of its components without the GPLv3 obligations. Note that for such a license, a Qt developer license is required in addition.
