---
id: build-env
title: Build environment
---

>This page assumes you are working on one of the supported Debian or Ubuntu versions. Other Linux distributions should work too, however installation of the build dependencies may vary.

Like with a regular nymea installation, all the required packages can be obtained from the nymea repository. In addition to the
regular repository.


```bash
echo -e "deb http://repository.nymea.io $(lsb_release -s -c) main\ndeb-src http://repository.nymea.io $(lsb_release -s -c) main" | sudo tee /etc/apt/sources.list.d/nymea.list
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

Now the nymea SDK can be installed with this command:

```bash
sudo apt-get update
sudo apt-get install nymea-sdk
```

This will install nymea and all the development packages. It will also install QtCreator as the recommended IDE.

If you whish to use a different IDE, you may install the SDK with the following command instead:

```bash
sudo apt-get install --no-install-recommends nymea-sdk
```

In order to build existing plugins additional dependencies might be required. Those vary
between plugins. All the required dependencies for building the main nymea-plugins repository can
be installed with this command:

```bash
sudo apt-get build-dep nymea-plugins
```
