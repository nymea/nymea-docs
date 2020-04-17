---
id: plugin-build-environment
title: Build environment
---

## Set up the build environment

This documentation assumes you are working on a Debian or Ubuntu system. The recommended IDE to use is QtCreator. Other Linux distributions should work too, however at this point, nymea only ships packages for Debian and Ubuntu so libnymea needs to be build from code if you prefer to use a different linux distribution.
Install Qt

In the first step you need to install the Qt libraries:
```
$ sudo apt-get install qtcreator qt5-default qtbase5-dev python dpkg-dev debhelper
```
## Install nymea dependencies

For that we add the nymea repository by first importing the signing key for the repository.
```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key A1A19ED6
```
Now add the repository to the system.
```
sudo apt-add-repositry "deb http://repository.nymea.io `lsb_release -cs` main"
```
More detailed instructions on how to install the nymea repository can be found here:

→ nymea install wiki

Update your package lists:
```
$ sudo apt-get update
```
Now you are ready to install the nymea packages:
```
$ sudo apt-get install nymea nymea-doc libnymea1-dev nymea-dev-tools nymea-qtcreator-wizards
```

This should be enough to start wring a plugin from scratch. However, in order to build existing plugins
additional dependencies might be required. Those vary between plugins. All the required dependencies for
building the main nymea-plugins repository can be installed with

```
$ sudo apt-get build-dep nymea-plugins
```

