---
id: installation
title: Installing nymea
---

A nymea installation requires 2 parts. The first step is to install nymea:core on a machine and the second step is to install
a cliean application, typically nymea:app or nymea-cli on the machines that are used to control nymea:core. This can be all on the
same host or distributed across multiple devices.

A typical nymea setup will have nymea:core running on a low power host, such as a Raspberry Pi which is connected to the local network
and a multitude of client installations on various other devices. For example every member of the network having nymea:app on their mobile
phone, PCs etc.

## nymea:core

As said before, the typical use case is to have nymea:core installed on a low power machine in the network. nymea offers a ready to use
Raspberry Pi image for this but it can also be installed manually on any GNU/Linux based system. For that nymea provides repositories with
packaged builds for Ubuntu and Debian, as well as a distribution independent snap. Please note that the snap package might not support
all the bells and whistles given the security implications with snap packages.

### Raspberry Pi images

The latest Raspberry Pi image can be obtained from [the nymea downloads section](https://downloads.nymea.io/images/raspberrypi/latest).

After downloading, this image needs to be written to an SD card. This step varies between operating systems.

nymea recommends to use [balenaEtcher](https://www.balena.io/etcher/) for writing the image to the SD card.

Alternatively, various other options can be found at the 
[Raspberry Pi installation guide](https://www.raspberrypi.org/documentation/installation/installing-images/windows.md). The nymea image 
is built using the same tools as the Raspberry Pi image and all the provided installation guides should work for the nymea image too.

After the image has been written to the SD card, insert the SD card into the Raspberry Pi and connect it to the power supply. nymea:core
will automatically start upon boot. Please proceed with the [usage guide](TODO-broken).

### Manual installation on a Raspberry Pi

If the nymea Raspberry Pi image is not used, nymea:core can also be installed on an existing Raspberry Pi running Raspbian.

Create a file named `/etc/apt/sources.list.d/nymea.list` with this content:

```
deb http://repository.nymea.io buster rpi
```

Add the repository signing key by running
```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key A1A19ED6
```

Once done so, nymea:core can be installed using apt-get:
```
sudo apt-get update
sudo apt-get install nymea nymea-plugins
```

Once this command completes, nymea:core should be up and running on the Raspberry Pi.

### Debian GNU/Linux and Ubuntu

nymea provides a repository for Debian GNU/Linux and Ubuntu.

Currently, these versions are officially supported:

* Debian 9 ("stretch")
* Debian 10 ("buster")
* Ubuntu 16.04 ("xenial")
* Ubuntu 18.04 ("bionic")
* Ubuntu 19.10 ("eoan")

For each of the repositories four architectures are provided:

* i386
* amd64
* armhf
* arm64

To enable the repository, create a file named `/etc/apt/sources.list.d/nymea.list` with the following content:

> Note: Replace `<distro>` with the codename of the distro, e.g. `buster` for Debian 10 or `bionic` for Ubuntu 18.4

```
deb http://repository.nymea.io <distro> main
```

Add the repository signing key by running:

```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key A1A19ED6
```

Once done so, nymea:core can be installed using apt-get:
```
sudo apt-get update
sudo apt-get install nymea nymea-plugins
```

Once this command completes, nymea:core should be up and running.

### Snap

The nymea:core snap can be found in the [snap app store](https://snapcraft.io/nymea). For the snap, nymea
provides amd64 and armhf packages.


It can be installed using the app store application of the used distribution, or via this command:

```
sudo snap install nymea
```

### Other distributions or architectures

To install nymea:core on other distributions or architectures, nymea:core needs to be built manually from the sources.
Please see the [developer section](TODO-broken) for instructions on how to build nymea:core.
