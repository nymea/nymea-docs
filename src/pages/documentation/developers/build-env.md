---
id: build-env
title: Build environment
---

This page assumes you are working on one of the supported Debian or Ubuntu versions. The recommended IDE to use is QtCreator. 
Other Linux distributions should work too, however installation of the build dependencies may vary.

The first step is to install the compiler and Qt libraries.
```bash
sudo apt install build-essential qt5-default qtbase5-dev qtcreator git ccache dpkg-dev python debhelper \
  rsync dbus-test-runner libssl-dev libavahi-common-dev libavahi-client-dev \
  libqt5dbus5 libqt5sql5-sqlite libqt5bluetooth5 libqt5serialport5-dev libqt5websockets5-dev \
  qtconnectivity5-dev qttools5-dev-tools qtbase5-dev-tools qt5-qmake
```

This would be sufficient to build the entire nymea core software stack. However, in most cases
a developer is interested only in changing a particlar part of the system or creating a new plugin. Because
of that it is recommended to install the entire nymea stack using the binary packages and then only replace
the parts that have been changed with the self built ones.

Like with a regular nymea installation, all the required packages can be obtained from the nymea repository:

```bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key A1A19ED6
sudo apt-add-repositry "deb http://repository.nymea.io `lsb_release -cs` main"
sudo apt-get update
```

Now the nymea packages can be installed with this command:

```bash
sudo apt-get install nymea nymea-doc libnymea1-dev nymea-dev-tools nymea-qtcreator-wizards
```

Now the machine is prepared to start working on nymea:core or creating new plugins from scratch. 
However, in order to build existing plugins additional dependencies might be required. Those vary
between plugins. All the required dependencies for building the main nymea-plugins repository can
be installed with this command:

```bash
sudo apt-get build-dep nymea-plugins
```
