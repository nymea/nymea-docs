---
id: build-nymea
title: Building nymea
---

This section assumes that the build environment has already been set up. Please refer to the previous 
section if the build environment has not been set up yet.

Depending on the need, nymea can be built using a graphical IDE or via command line. If the purpose of 
building nymea from source is to install nymea on a new system, or do only small modifications like 
applying patches, building via the command line might be the better choice. A developer changing the 
code will most likely want to use QtCreator as it offers code completion, inline documentation and all 
the other features that are expected from an IDE. 

## Building natively

The nymea source code can be obtained from [GitHub](https://github.com/nymea/) and consists of multiple modules, distributed across multiple code repositories. The modules have dependencies between each other. This means, that some repositories will be required to be built before others can be built. However, if the objective is to just develop with a single repository or apply a single patch to a particular module, the dependencies may also be installed from the binary pacakge repository instead.

The build options may vary a bit between modues. In order to activate particular options, append the given option to the `qmake` line. For
example: `qmake .. PREFIX=/usr CONFIG+=release`.

### nymea-zigbee

```bash
git clone https://github.com/nymea/nymea-zigbee
mkdir nymea-zigbee/builddir
cd nymea-zigbee/builddir
qmake .. PREFIX=/usr/
make sudo make install
```
This module supports the following build configurations:

* debug: `CONFIG+=debug`
* release: `CONFIG+=release`

### nymea-gpio

```bash
git clone https://github.com/nymea/nymea-gpio
mkdir nymea-gpio/builddir
cd nymea-gpio/builddir
qmake .. PREFIX=/usr/
make
sudo make install
```

This module supports the following build configurations:

* debug: `CONFIG+=debug`
* release: `CONFIG+=release`

### libnymea-networkmanager

```bash
git clone https://github.com/nymea/libnymea-networkmanager
mkdir libnymea-networkmanager/builddir
cd libnymea-networkmanager/builddir
qmake .. PREFIX=/usr/
make
sudo make install
```

This module supports the following build configurations:

* debug: `CONFIG+=debug`
* release: `CONFIG+=release`

### nymea-networkmanager

> This module requires libnymea-networkmanager and nymea-gpio

```bash
git clone https://github.com/nymea/nymea-networkmanager
mkdir nymea-networkmanager/builddir
cd nymea-networkmanager/builddir
qmake .. PREFIX=/usr/
make
sudo make install
```

This module supports the following build configurations:

* debug: `CONFIG+=debug`
* release: `CONFIG+=release`

### nymea-remoteproxy

```bash
git clone https://github.com/nymea/nymea-remoteproxy
mkdir nymea-remoteproxy/builddir
cd nymea-remoteproxy/builddir
qmake .. PREFIX=/usr/
make
sudo make install
```

This module supports the following build configurations:

* debug: `CONFIG+=debug`
* release: `CONFIG+=release`

### nymea-mqtt

```bash
git clone https://github.com/nymea/nymea-mqtt
mkdir nymea-mqtt/builddir
cd nymea-mqtt/builddir
qmake .. PREFIX=/usr/
make
sudo make install
```

This module supports the following build configurations:

* debug: `CONFIG+=debug`
* release: `CONFIG+=release`

### nymea

> This module requires nymea-gpio, nymea-zigbee, libnymea-networkmanager, nymea-mqtt and nymea-remoteproxy

```bash
git clone https://github.com/nymea/nymea
mkdir nymea/builddir
cd nymea/builddir
qmake .. PREFIX=/usr/
make
sudo make install
```

This module supports the following build configurations:

* debug: `CONFIG+=debug`
* release: `CONFIG+=release`
* build without tests: `CONFIG+=disabletesting`
* enable code coverage reporting for tests: `CONFIG+=coverage`
* build with address sanitizer: `CONFIG+=asan`
* build (link) without rpath: `CONFIG+=norpath`

### nymea-plugins

The nymea-plugins repository only contains some plugins. More plugins can be found in [other plugin repositories](https://github.com/nymea/?q=nymea-plugin). The build instructions for all plugin repositories are the same.

```bash
git clone https://github.com/nymea/nymea-plugins
mkdir nymea-plugins/builddir
cd nymea-plugins/builddir
qmake .. PREFIX=/usr/
make
sudo make install
```

This module supports the following build configurations:

* debug: `CONFIG+=debug`
* release: `CONFIG+=release`
* select only specific plugins to be built: `WITH_PLUGINS=plugin1 plugin2 ...`
* exclude specific plugins from being built: `WITHOUT_PLUGINS=plugin1 plugin2 ...`


## Cross-compiling

In order to build debian packages for nymea for your target device, we provide a tool for crosscompiling called `crosscompiler`.
This tool makes helps to build a debian package inside a lxd container which can makes sure all required packages for building and deploying
are available and also for different architectures.

The `crossbuilder` tool can be started within a git source code repository and generates a brand new lxc container for the given distribution and architecture.

### Installation

Install the crossbuilder package from the nymea repositoy (see install section):
```bash
$ sudo apt-get install crossbuilder
```


### Setup

In order to set up the crossbuilder lxd environment you can run following command and follow the setup instructions:
```bash
$ crossbuilder setup-lxd
```


### Building

Assuming you are running crossbuilder on a `amd64` Ubuntu machine, and you want to build a project for `armhf` debian `stretch` you can do following steps.

You clone a project repository (in this example the `nymea` project) and change to the project directory:
```bash
$ git clone https://github.com/nymea/nymea.git
$ cd nymea
```
    
If you run the crossbuilder the first time, we need to specify the architecture and the distribution we want to build packages for:
```bash
$ crossbuilder -a armhf -u stretch
```
    
Crossbuilder will now contact the nymea lxc host server (https://jenkins.nymea.io:8443) and check if the available image for crosscompilation exists for the target achitecture and distribution (`stretch armhf`). If the image was found, a new local lxc container will be created for exactly this repository.

The next step for crossbuilder is mounting the current source directory into the new created container and will start building the packages (containing build dependencies installing). If you change the source code and want to run the build process again, crossbuilder will reuse this container and also the already created build outputs. If you change the build dependencies of the package you don't need to rebuild the container, you just need to run following command in order to install the missing build dependencies inside the container:
```bash
$ crossbuilder dependencies
```

You can check any time which containers you already have and which are running on your local build machine:
```bash
$ lxc list

+--------------------------------------------------------+---------+-------------------+------+------------+-----------+
|                          NAME                          |  STATE  |       IPV4        | IPV6 |    TYPE    | SNAPSHOTS |
+--------------------------------------------------------+---------+-------------------+------+------------+-----------+
| nymea-nymea-builder-stretch-amd64-armhf                | RUNNING | 10.0.1.106 (eth0) |      | PERSISTENT | 0         |
+--------------------------------------------------------+---------+-------------------+------+------------+-----------+
```

Her you can see the created container for building nymea. The naming of the container is `<project>-nymea-builder-<distribution>-<host-architecture>-<target-architecture>`.

### Cleaning the build

Once the crossbuilder has finished, you can find all build results in the source tree (since the packages where created in the mounted source tree). If you want to clean up the source directory again you can run:
```bash
$ crossbuilder clean
```

### Build output

A compressed file containing the debian packages and also the source packages will be the output of script. You can take a look at the built packages by extracting the file and check the content:
```bash
$ tar xfv debs_*

libnymea1_0.9.0+201803271733~c348a6b~stretch_armhf.deb
libnymea1-dev_0.9.0+201803271733~c348a6b~stretch_armhf.deb
nymea_0.9.0+201803271733~c348a6b~stretch_armhf.deb
nymead_0.9.0+201803271733~c348a6b~stretch_armhf.deb
nymea-dbg_0.9.0+201803271733~c348a6b~stretch_armhf.deb
nymea-tests_0.9.0+201803271733~c348a6b~stretch_armhf.deb
nymea-translations_0.9.0+201803271733~c348a6b~stretch_all.deb
source_repository/nymea_0.9.0+201803271733~c348a6b~stretch.dsc
source_repository/nymea_0.9.0+201803271733~c348a6b~stretch_source.changes
source_repository/nymea_0.9.0+201803271733~c348a6b~stretch.tar.xz
```

The content will be extracted in the source directory. If you want to see the content of the resulting packages you can use the `dpkg` command:
```bash
$ dpkg -c libnymea1_0.9.0+201803271733~c348a6b~stretch_armhf.deb

drwxr-xr-x root/root         0 2018-03-27 17:36 ./
drwxr-xr-x root/root         0 2018-03-27 17:36 ./usr/
drwxr-xr-x root/root         0 2018-03-27 17:36 ./usr/lib/
drwxr-xr-x root/root         0 2018-03-27 17:36 ./usr/lib/arm-linux-gnueabihf/
-rw-r--r-- root/root    539272 2018-03-27 17:36 ./usr/lib/arm-linux-gnueabihf/libnymea.so.1.0.0
drwxr-xr-x root/root         0 2018-03-27 17:36 ./usr/share/
drwxr-xr-x root/root         0 2018-03-27 17:36 ./usr/share/doc/
drwxr-xr-x root/root         0 2018-03-27 17:36 ./usr/share/doc/libnymea1/
-rw-r--r-- root/root      1436 2018-03-27 17:36 ./usr/share/doc/libnymea1/changelog.gz
-rw-r--r-- root/root      1942 2018-03-27 17:30 ./usr/share/doc/libnymea1/copyright
lrwxrwxrwx root/root         0 2018-03-27 17:36 ./usr/lib/arm-linux-gnueabihf/libnymea.so.1 -> libnymea.so.1.0.0
lrwxrwxrwx root/root         0 2018-03-27 17:36 ./usr/lib/arm-linux-gnueabihf/libnymea.so.1.0 -> libnymea.so.1.0.0
```


### Login into container

If you want to login into the build container you can simply run:
```bash
$ crossbuilder shell
```

### Cache

If you run the crossbuilder a second time, you just need to run `crossbuilder`, since the first time a configuration file for the container has been created. Crossbuilder will also make use of the host `ccache` independent form the architecture and distribution. In this example you can find the `crossbuilder` cached information here:
```bash
$ cat .crossbuilder/cache.conf

TARGET_ARCH=armhf
TARGET_UBUNTU=stretch
```

### Delete the container

If you are finished and the container will not be needed any more you can delete the container by running:
```bash
$ crossbuilder delete
```

### Deploy on target machine

If you want crossbuilder to deploy the packages to a remote machine and install them, you can create following configuration file:
```bash
$ nano .crossbuilder/deploy.conf
```

Here you can add the remote information of the target machine (in this example an `armhf stretch` machine running on `10.10.10.10` where you want to install the debian packages built with the `crosscompiler`.

> Note: the packages need to be already installed once on the target machine, since crossbuilder is just updating them, not installing them from scretch. If that is not the case, you can install them manually after crossbuilder copied them to the target and created the local repository: on the target `sudo dpkg -i /tmp/repo/*.deb`.

```bash
DEPLOY_IP=10.10.10.10
DEPLOY_USER=nymea
DEPLOY_KEY=~/.ssh/id_rsa
```

Each new build will from now on be installed automatically on the target machine until you delete the configuration file.

### Interacting with the containers

Remove a container if the source repositoy does not exist any more:

> Note: the `--force` is only needed if the container is still running.

```bash
$ lxc list

+--------------------------------------------------------+---------+-------------------+------+------------+-----------+
|                          NAME                          |  STATE  |       IPV4        | IPV6 |    TYPE    | SNAPSHOTS |
+--------------------------------------------------------+---------+-------------------+------+------------+-----------+
| nymea-nymea-builder-stretch-amd64-armhf                | RUNNING | 10.0.1.106 (eth0) |      | PERSISTENT | 0         |
+--------------------------------------------------------+---------+-------------------+------+------------+-----------+

$ lxc delete nymea-nymea-builder-stretch-amd64-armhf --force
```


## Building with Yocto

nymea can be built with yocto. For that, we offer a meta layer which can be found on [GitHub](https://github.com/nymea/meta-nymea).

This meta layer can be added to a yocto image and offers the following packages:

* nymea-mqtt
* nymea-networkmanager
* nymea-remoteproxy
* nymea-gpio
* nymead
* nymea-plugins
