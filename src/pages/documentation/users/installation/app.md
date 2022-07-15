---
id: app
title: nymea:app
---

The typical use case for nymea:app is to be installed on the mobile device of the users along with additional installations on laptops, desktop PCs and wall mounted or centrally placed touch screens to interact with the system.

## Smartphones and tablets

nymea:app can be found in the Google Play store for Android, on the iTunes store for iOS and on the Open Store for the Ubuntu phone.

![](/img/mobile-app.png)

<div align="center">
<a href="https://itunes.apple.com/us/app/nymea-app/id1400810250?mt=8" target="_blank" rel="noopener" style="display: inline-block;"><img src="/img/badges/appstore.png" height="50px"></a>
<a href="https://open-store.io/app/io.guh.nymeaapp" target="_blank" style="display: inline-block;" rel="noopener"><img src="/img/badges/open-store.svg" height="50px"/></a>
<a href="https://play.google.com/store/apps/details?id=io.guh.nymeaapp" target="_blank" style="display: inline-block;" rel="noopener"><img src="/img/badges/playstore.png" height="50px"></a>
</div>


Minimum system requirements:
* iOS 11 or greater
* Android 5.0 or greater
* Ubuntu Phone framework 16.04 or greater

## Laptops and Desktops

nymea:app can be found in the macOS app store and the Ubuntu Core Snap store. For Windows we offer an offline installer from our downloads section.

![](/img/desktop-app.png)


<div align="center">
<a href="https://apps.apple.com/us/app/nymea-app/id1488785734" target="_blank" style="display: inline-block;" rel="noopener"><img src="/img/badges/macos.svg" height="50px"/></a>
<a href="https://snapcraft.io/nymea-app" target="_blank" style="display: inline-block;" rel="noopener"><img src="/img/badges/snap-store.png" height="50px"/></a>
<a href="https://downloads.nymea.io/nymea-app/windows/latest" target="_blank" style="display: inline-block;" rel="noopener"><img src="/img/badges/windows.svg" height="50px"/></a>
</div>

Minimum system requirements:

* Windows 10 or greater
* macOS 10.13 or greater
* Ubuntu Core 18.04 or greater

> Please note that installing the app from the downloads section will require to manually redownload to update to newer versions. At this point we are not providing a package for the Windows app store.

> Alternatively, on Ubuntu and Debian GNU/Linux, the repository version can be used too. See below for details.

## Embedded devices and manual setups

nymea:app can also be installed from the same package repository as nymea:core.

Currently, these versions are officially supported:

* Debian 10 ("buster")
* Debian 11 ("bullseye")
* Ubuntu 18.04 ("bionic")
* Ubuntu 20.04 ("focal")
* Ubuntu 22.04 ("jammy")

For each of the repositories the following architectures are provided:

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

Once done so, nymea:app can be installed using apt-get:

```bash
sudo apt-get update
sudo apt-get install nymea-app
```

Once this command completes, nymea:app should be installed and ready to use from the applications menu.

