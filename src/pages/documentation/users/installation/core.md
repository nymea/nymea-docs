---
id: core
title: nymea:core
---

The typical use case is to have nymea:core installed on a low power machine in the network. nymea offers a ready to use
Raspberry Pi image for this but it can also be installed manually on any GNU/Linux based system. nymea provides repositories with
packaged builds for Ubuntu and Debian, as well as a distribution independent snap.

## Raspberry Pi

The recommended way to install nymea on a Raspberry Pi is to use nymea's prebuilt images for the Raspberry Pi. However, if you already have
a Raspberry Pi set up, nymea can be installed on top of that without the need of reflashing the entire SD Card.

![](/img/touch-screen-and-pi-love.png)

Please pick one of the options below:


### Raspberry Pi images

* [nymea:core image](https://downloads.nymea.io/images/raspberrypi/nymea-core-image-raspios-bullseye-latest.zip) for headless Raspberry Pis.
* [nymea:kiosk image](https://downloads.nymea.io/images/raspberrypi/nymea-kiosk-image-raspios-bullseye-latest.zip) containing nymea:core and nymea:app for Raspberry Pis with touchscreen or display.

After downloading, this image needs to be written to an SD card. This step varies between operating systems.

nymea recommends to use [Raspberry Pi imager](https://www.raspberrypi.com/software/) for writing the image to the SD card.

After the image has been written to the SD card, insert the SD card into the Raspberry Pi and connect it to the power supply. nymea:core
will automatically start upon boot. Please proceed with the [usage guide](/documentation/users/usage/first-steps).

### Manual installation on a Raspberry Pi

If the nymea Raspberry Pi image is not used, nymea:core can also be installed on an existing Raspberry Pi running Raspbian.

Create a file named `/etc/apt/sources.list.d/nymea.list` with this content:

```bash
deb http://repository.nymea.io buster rpi
```

Add the repository signing key by running

```bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key A1A19ED6
```

Once done so, nymea:core can be installed using apt-get:

```bash
sudo apt-get update
sudo apt-get install nymea nymea-plugins
```

Once this command completes, nymea:core should be up and running on the Raspberry Pi.

## Debian GNU/Linux and Ubuntu

The recommended way to install nymea on a Debian GNU/Linux or Ubuntu machine is to use nymea's repository. However, nymea also
offers the option to install nymea:core using a snap directly from the snap store.

![](/img/nymea-ubuntu.svg)

Please pick one of the options below:

### Using apt-get

nymea provides a repository for Debian GNU/Linux and Ubuntu.

Currently, these versions are officially supported:

* Debian 10 ("buster")
* Debian 11 ("bullseye")
* Ubuntu 16.04 ("xenial")
* Ubuntu 18.04 ("bionic")
* Ubuntu 20.04 ("focal")
* Ubuntu 22.04 ("jammy")

For each of the repositories four architectures are provided:

* amd64
* armhf
* arm64

To enable the repository, create a file named `/etc/apt/sources.list.d/nymea.list` with the following content:

> Note: Replace `<distro>` with the codename of the distro, e.g. `buster` for Debian 10 or `focal` for Ubuntu 20.04

```bash
deb http://repository.nymea.io <distro> main
```

Add the repository signing key by running:

```bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key A1A19ED6
```

Once done so, nymea:core can be installed using apt-get:

```bash
sudo apt-get update
sudo apt-get install nymea nymea-plugins
```

Once this command completes, nymea:core should be up and running.



### From the Snap store

The nymea:core snap can be found in the [snap app store](https://snapcraft.io/nymea). For the snap, nymea
provides amd64 and armhf packages.

<dl>
<a href="http://snapcraft.io/nymea" target="_blank" rel="noopener" style="display:inline-block;overflow:hidden;background:url(https://snapcraft.io/static/images/badges/en/snap-store-black.svg) no-repeat;width:182px;height:56px;background-size:contain;"></a>
</dl>
<br />


It can be installed using the app store application of the used distribution, or via this command:

```bash
sudo snap install nymea
```



## Other distributions or architectures

To install nymea:core on other distributions or architectures, nymea:core needs to be built manually from the sources.
Please see the [developer section](/documentation/developers/build-nymea) for instructions on how to build nymea:core.

