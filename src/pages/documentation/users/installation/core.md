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

* [nymea:core image](https://downloads.nymea.io/images/raspberrypi/nymea-core-image-raspios-bookworm-latest.zip) for headless Raspberry Pis.
* [nymea:kiosk image](https://downloads.nymea.io/images/raspberrypi/nymea-kiosk-image-raspios-bookworm-latest.zip) containing nymea:core and nymea:app for Raspberry Pis with touchscreen or display.

After downloading, this image needs to be written to an SD card. This step varies between operating systems.

nymea recommends to use [Raspberry Pi imager](https://www.raspberrypi.com/software/) for writing the image to the SD card.

After the image has been written to the SD card, insert the SD card into the Raspberry Pi and connect it to the power supply. nymea:core
will automatically start upon boot. Please proceed with the [usage guide](/documentation/users/usage/first-steps).

### Manual installation on a Raspberry Pi

If the nymea Raspberry Pi image is not used, nymea:core can also be installed on an existing Raspberry Pi running Raspbian.

Currently, the following Raspberry Pi Models are supported:<br>
Raspberry Pi 2, 3, 4, 5 and Zero 2W

To enable the repository, create a file named `/etc/apt/sources.list.d/nymea.list` using the following command:

```bash
echo "deb http://repository.nymea.io $(lsb_release -s -c) main" | sudo tee /etc/apt/sources.list.d/nymea.list
```

The packages in the nymea repository are signed with nymeas GPG key which can be imported by running:

```bash
sudo wget -O /etc/apt/trusted.gpg.d/nymea.gpg https://repository.nymea.io/nymea.gpg
```

Optionally, the keys fingerprint can be verified with:
```bash
gpg --show-keys --with-fingerprint /etc/apt/trusted.gpg.d/nymea.gpg
```

```bash
pub   rsa4096 2016-04-08 [SC]
      B1C8 9C2A E70D 2FC8 27DF  0BFF 457A 6EE4 A1A1 9ED6
uid                      nymea GmbH <developer@nymea.io>
sub   rsa4096 2016-04-08 [E]
sub   rsa4096 2016-04-08 [S]
```

Once done so, nymea:core can be installed using apt-get:

```bash
sudo apt-get update
sudo apt-get install nymea
```

Once this command completes, nymea:core should be up and running on the Raspberry Pi.

#### Important note:

If you are still using an older installation running with the old rpi-repo you need to switch to the main-repo.

In this case you need to change the repository line in `/etc/apt/sources.list.d/nymea.list` <br>from `deb http://repository.nymea.io bullseye rpi` to `deb http://repository.nymea.io bullseye main`.<br>
Without this change, your Raspberry Pi will stop receiveing updates from now on.<br>
In order to simplify this for users, a package named `nymea-rpi-repo-migration` will be provided.<br> 
Installing that package either via `apt-get` or via the app in `system settings -> system updates`<br> will do everything required and the system will continue to work as it did before.<br> 
After installing the migration package, an update for the entire system will be available.



## Debian GNU/Linux and Ubuntu

The recommended way to install nymea on a Debian GNU/Linux or Ubuntu machine is to use nymea's repository. However, nymea also
offers the option to install nymea:core using a snap directly from the snap store.

![](/img/nymea-ubuntu.svg)

Please pick one of the options below:

### Using apt-get

nymea provides a repository for Debian GNU/Linux and Ubuntu.

Currently, these versions are officially supported:

Debian:

* Debian 11 ("bullseye")
* Debian 12 ("bookworm")

Ubuntu:

* Ubuntu 20.04 ("focal")
* Ubuntu 22.04 ("jammy")
* Ubuntu 24.04 ("noble")
* Ubuntu 24.10 ("oracular")

For each of the repositories four architectures are provided:

* amd64
* armhf
* arm64
* riscv64

To enable the repository, create a file named `/etc/apt/sources.list.d/nymea.list` using the following command:

```bash
echo "deb http://repository.nymea.io $(lsb_release -s -c) main" | sudo tee /etc/apt/sources.list.d/nymea.list
```

The packages in the nymea repository are signed with nymeas GPG key which can be imported by running:

```bash
sudo wget -O /etc/apt/trusted.gpg.d/nymea.gpg https://repository.nymea.io/nymea.gpg
```

Optionally, the keys fingerprint can be verified with:
```bash
gpg --show-keys --with-fingerprint /etc/apt/trusted.gpg.d/nymea.gpg
```

```bash
pub   rsa4096 2016-04-08 [SC]
      B1C8 9C2A E70D 2FC8 27DF  0BFF 457A 6EE4 A1A1 9ED6
uid                      nymea GmbH <developer@nymea.io>
sub   rsa4096 2016-04-08 [E]
sub   rsa4096 2016-04-08 [S]
```

Once done so, nymea:core can be installed using apt-get:

```bash
sudo apt-get update
sudo apt-get install nymea
```

Once this command completes, nymea:core should be up and running.

> Note: The nymea RPi image will have SSH enabled with username `nymea` and password `nymea` by default. If setting up a nymea instance in a publicly accessible network, consider changing the credentials.

## Other distributions or architectures

To install nymea:core on other distributions or architectures, nymea:core needs to be built manually from the sources.
Please see the [developer section](/documentation/developers/build-nymea) for instructions on how to build nymea:core.


## Joining the beta tests

> Note: Running experimental or testing builds of nymea is not recommended for users expecting a stable setup.

In order to help with testing pre-releases of nymea or give early feedback on features which are still in development, it is possible to install packages that are still under development and not released to stable yet.

We have 3 different stability channels:

* `stable`: The current stable release which is also referring to the current `master` branch on each repository. This is the default repository described in the [Using apt-get](#using-apt-get) section
* `landing`: The next candidate for the next release. You may also call it beta release. This is where the testing for the new releases happens. 
* `experimental`: The current construction zone. Might be very unstable. Using this may break your setup, only use it if you know what you are doing and be prepared to reset everything related to nymea.

Assuming you already added the stable repository, you can add following lines in the  `/etc/apt/sources.list.d/nymea.list` file, depending on the channel you want to use.

> Note: replace `$(lsb_release -s -c)` with your distribution name, like `bookworm`.

```bash
deb http://repository.nymea.io/landing $(lsb_release -s -c) main
deb http://repository.nymea.io/experimental $(lsb_release -s -c) main
```