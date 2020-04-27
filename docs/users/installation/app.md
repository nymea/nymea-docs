---
id: app
title: nymea:app
---

The typical use case for nymea:app is to be installed on the mobile device of the users along with additional installations on laptops, desktop PCs and wall mounted or centrally placed touch screens to interact with the system.

### Android

nymea:app can be found in the Google Play store ready to be installed on any Android device supporting Android 5.0 or greater.

### iOS

nymea:app can be found in the iTunes store ready to be installed on any iOS device supporting iOS 11.0 or greater.

### Ubuntu Touch

nymea:app can be found in the Open Store and should work fine on any Ubuntu Phone with at least framework 16.04 in place.

### macOS

nymea:app can be found in the macOS app store and should work fine on any Mac with macOS 10.13 or greater.

### Windows

nymea:app for Windows can be downloaded from [here](https://downloads.nymea.io/nymea-app/). Please note that installing the app from the downloads section will require to manually redownload and update to newer versions. At this point we do not providing a package for the Windows app store.

### Debian GNU/Linux and Ubuntu

nymea:app for Debian GNU/Linux and Ubuntu can be found in the same repository as nymea:core.

Currently, these versions are officially supported:

* Debian 10 ("buster")
* Ubuntu 18.04 ("bionic")
* Ubuntu 19.10 ("eoan")

For each of the repositories four architectures are provided:

* amd64
* armhf

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
sudo apt-get install nymea-app
```

Once this command completes, nymea:app should be installed and ready to use from the applications menu.

### Snap

The nymea:app snap can be found in the [snap app store](https://snapcraft.io/nymea-app). For the snap, nymea
provides amd64 and armhf packages.


It can be installed using the app store application of the used distribution, or via this command:

```
sudo snap install nymea-app
```
