---
id: build-env
title: Build environment
---

>This page assumes you are working on one of the supported Debian or Ubuntu versions. Other Linux distributions should work too, however installation of the build dependencies may vary.

Like with a regular nymea installation, all the required packages can be obtained from the nymea repository. In addition to the
regular repository.

```bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key A1A19ED6
sudo apt-add-repository -s "deb http://repository.nymea.io `lsb_release -cs` main"
sudo apt-get update
```

Now the nymea SDK can be installed with this command:

```bash
sudo apt-get install nymea-sdk
```

This will install nymea and all the development packages. It will also install QtCreator as the recommended IDE.

If you whish to use a different IDE, you may install the SDK with the following command instead:

```bash
sudo apt-get install --no-install-recommends nymea-sdk
```

Now that the compiler and build tools are installed, individual repositories may require additional dependencies. Depending on the repository you want to build, install the build dependencies for that particular repository.

For example, to build nymea core:

```bash
sudo apt-get build-dep nymea
```

To build nymea-zigbee:
```bash
sudo apt-get build-dep nymea-zigbee
```

To build nymea-plugins:
```bash
sudo apt-get build-dep nymea-plugins
```

etc.
