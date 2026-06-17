.. _doc-developers-build-nymea:

Building nymea
==============


This section assumes that the build environment has already been set up. Please refer to the previous
section if the build environment has not been set up yet.

Depending on the need, nymea can be built using a graphical IDE or via command line. If the purpose of
building nymea from source is to install nymea on a new system, or do only small modifications like
applying patches, building via the command line might be the better choice. A developer changing the
code will most likely want to use QtCreator as it offers code completion, inline documentation and all
the other features that are expected from an IDE.

For day-to-day development, it is usually easier to keep all nymea repositories in one shared
workspace and run the binaries directly from their build directories instead of installing each build
into the system. The same workspace can also be used from Qt Creator and for debugging.

.. include:: _includes/development-workspace.rst

Building natively
-----------------

The nymea source code can be obtained from `GitHub <https://github.com/nymea/>`__ and consists of
multiple modules, distributed across multiple code repositories. The modules have dependencies between
each other. This means that some repositories will be required to be built before others can be
built. However, if the objective is to just develop with a single repository or apply a single patch
to a particular module, the dependencies may also be installed from the binary package repository
instead.

The build options may vary a bit between modules. In order to activate particular options, append the given option to the ``qmake`` line. For
example: ``qmake .. PREFIX=/usr CONFIG+=release``.

nymea-zigbee
------------


::

   git clone https://github.com/nymea/nymea-zigbee
   mkdir nymea-zigbee/builddir
   cd nymea-zigbee/builddir
   qmake .. PREFIX=/usr/
   make 
   sudo make install

This module supports the following build configurations:

* debug: ``CONFIG+=debug``

* release: ``CONFIG+=release``


nymea-gpio
----------


::

   git clone https://github.com/nymea/nymea-gpio
   mkdir nymea-gpio/builddir
   cd nymea-gpio/builddir
   qmake .. PREFIX=/usr/
   make
   sudo make install


This module supports the following build configurations:

* debug: ``CONFIG+=debug``

* release: ``CONFIG+=release``


libnymea-networkmanager
-----------------------


::

   git clone https://github.com/nymea/libnymea-networkmanager
   mkdir libnymea-networkmanager/builddir
   cd libnymea-networkmanager/builddir
   qmake .. PREFIX=/usr/
   make
   sudo make install


This module supports the following build configurations:

* debug: ``CONFIG+=debug``

* release: ``CONFIG+=release``


nymea-networkmanager
--------------------


.. note::

   This module requires libnymea-networkmanager and nymea-gpio


::

   git clone https://github.com/nymea/nymea-networkmanager
   mkdir nymea-networkmanager/builddir
   cd nymea-networkmanager/builddir
   qmake .. PREFIX=/usr/
   make
   sudo make install


This module supports the following build configurations:

* debug: ``CONFIG+=debug``

* release: ``CONFIG+=release``


nymea-remoteproxy
-----------------


::

   git clone https://github.com/nymea/nymea-remoteproxy
   mkdir nymea-remoteproxy/builddir
   cd nymea-remoteproxy/builddir
   qmake .. PREFIX=/usr/
   make
   sudo make install


This module supports the following build configurations:

* debug: ``CONFIG+=debug``

* release: ``CONFIG+=release``

* build without tests: ``CONFIG+=disabletesting``

* enable code coverage reporting for tests: ``CONFIG+=coverage``


nymea-mqtt
----------


::

   git clone https://github.com/nymea/nymea-mqtt
   mkdir nymea-mqtt/builddir
   cd nymea-mqtt/builddir
   qmake .. PREFIX=/usr/
   make
   sudo make install


This module supports the following build configurations:

* debug: ``CONFIG+=debug``

* release: ``CONFIG+=release``

* build without tests: ``CONFIG+=disabletesting``


nymea
-----


.. note::

   This module requires nymea-gpio, nymea-zigbee, libnymea-networkmanager, nymea-mqtt and nymea-remoteproxy


::

   git clone https://github.com/nymea/nymea
   mkdir nymea/builddir
   cd nymea/builddir
   qmake .. PREFIX=/usr/
   make
   sudo make install


This module supports the following build configurations:

* debug: ``CONFIG+=debug``

* release: ``CONFIG+=release``

* set the server version: ``NYMEA_VERSION=1.2.3-custom``

* build without tests: ``CONFIG+=disabletesting``

* enable code coverage reporting for tests: ``CONFIG+=coverage``

* build with address sanitizer: ``CONFIG+=asan``

* build (link) without rpath: ``CONFIG+=norpath``

* build only the nymea-plugininfo-compiler: ``CONFIG+=piconly``

* build only the libraries required for building nymea-plugins: ``CONFIG+=minimal``


nymea-plugins
-------------


The nymea-plugins repository only contains some plugins. More plugins can be found in `other plugin repositories <https://github.com/nymea/?q=nymea-plugin>`__. The build instructions for all plugin repositories are the same.

::

   git clone https://github.com/nymea/nymea-plugins
   mkdir nymea-plugins/builddir
   cd nymea-plugins/builddir
   qmake .. PREFIX=/usr/
   make
   sudo make install


This module supports the following build configurations:

* debug: ``CONFIG+=debug``

* release: ``CONFIG+=release``

* select only specific plugins to be built: ``WITH_PLUGINS=plugin1 plugin2 ...``

* exclude specific plugins from being built: ``WITHOUT_PLUGINS=plugin1 plugin2 ...``

Cross-compiling
---------------


In order to build Debian packages for nymea for your target device, we provide a tool for cross
compiling called ``crossbuilder``. This tool helps build a Debian package inside an LXD container and
makes sure all required packages for building and deploying are available for different architectures.

The ``crossbuilder`` tool can be started within a git source code repository and generates a brand new lxc container for the given distribution and architecture.

Installation
------------


Install the crossbuilder package from the nymea repositoy (see install section):
::

   $ sudo apt-get install crossbuilder



Setup
-----


In order to set up the crossbuilder lxd environment you can run following command and follow the setup instructions:
::

   $ crossbuilder setup-lxd



Building
--------


Assuming you are running crossbuilder on a ``amd64`` Ubuntu machine, and you want to build a project for `` armhf`` debian `` bookworm`` you can do following steps.

You clone a project repository (in this example the ``nymea`` project) and change to the project directory:
::

   $ git clone https://github.com/nymea/nymea.git
   $ cd nymea

    
If you run the crossbuilder the first time, we need to specify the architecture and the distribution we want to build packages for:
::

   $ crossbuilder -a armhf -u bookworm


.. note::

   If your lxc container cannot reach the network and you have docker running in parallel on your host system, you can enable the networking for lxc containers with following command: ``sudo iptables -F FORWARD && sudo iptables -P FORWARD ACCEPT``. Docker seem to destroyes the firewall rules for lxc containers: https://github.com/docker/for-linux/issues/103

    
Crossbuilder will now contact the nymea lxc host server (https://images.nymea.io:8443) and check if the available image for crosscompilation exists for the target achitecture and distribution (``bookworm armhf``). If the image was found, a new local lxc container will be created for exactly this repository.

The next step for crossbuilder is mounting the current source directory into the new created container and will start building the packages (containing build dependencies installing). If you change the source code and want to run the build process again, crossbuilder will reuse this container and also the already created build outputs. If you change the build dependencies of the package you don't need to rebuild the container, you just need to run following command in order to install the missing build dependencies inside the container:
::

   $ crossbuilder dependencies


You can check any time which containers you already have and which are running on your local build machine:
::

   $ lxc list
   
   +--------------------------------------------------------+---------+-------------------+------+------------+-----------+
   |                          NAME                          |  STATE  |       IPV4        | IPV6 |    TYPE    | SNAPSHOTS |
   +--------------------------------------------------------+---------+-------------------+------+------------+-----------+
   | nymea-nymea-bookworm-amd64-armhf                       | RUNNING | 10.0.1.106 (eth0) |      | PERSISTENT | 0         |
   +--------------------------------------------------------+---------+-------------------+------+------------+-----------+


Her you can see the created container for building nymea. The naming of the container is ``<project>-nymea-<distribution>-<host-architecture>-<target-architecture>``.

Cleaning the build
------------------


Once the crossbuilder has finished, you can find all build results in the source tree (since the packages where created in the mounted source tree). If you want to clean up the source directory again you can run:
::

   $ crossbuilder clean


Build output
------------


A compressed file containing the debian packages and also the source packages will be the output of script. You can take a look at the built packages by extracting the file and check the content:
::

   $ tar xfv debs_*
   
   libnymea1_1.9.1+202402090827~cb960749~bookworm_armhf.deb
   libnymea1-dbgsym_1.9.1+202402090827~cb960749~bookworm_armhf.deb
   libnymea-core_1.9.1+202402090827~cb960749~bookworm_armhf.deb
   libnymea-core-dbgsym_1.9.1+202402090827~cb960749~bookworm_armhf.deb
   libnymea-core-dev_1.9.1+202402090827~cb960749~bookworm_armhf.deb
   libnymea-dev_1.9.1+202402090827~cb960749~bookworm_armhf.deb
   libnymea-tests_1.9.1+202402090827~cb960749~bookworm_armhf.deb
   libnymea-tests-dbgsym_1.9.1+202402090827~cb960749~bookworm_armhf.deb
   libnymea-tests-dev_1.9.1+202402090827~cb960749~bookworm_armhf.deb
   nymea_1.9.1+202402090827~cb960749~bookworm_armhf.deb
   nymead_1.9.1+202402090827~cb960749~bookworm_armhf.deb
   nymea-data_1.9.1+202402090827~cb960749~bookworm_all.deb
   nymead-dbgsym_1.9.1+202402090827~cb960749~bookworm_armhf.deb
   nymea-dev-tools_1.9.1+202402090827~cb960749~bookworm_armhf.deb
   nymea-dev-tools-dbgsym_1.9.1+202402090827~cb960749~bookworm_armhf.deb
   nymea-sdk_1.9.1+202402090827~cb960749~bookworm_all.deb
   nymea-tests_1.9.1+202402090827~cb960749~bookworm_armhf.deb
   nymea-tests-dbgsym_1.9.1+202402090827~cb960749~bookworm_armhf.deb
   nymea-translations_1.9.1+202402090827~cb960749~bookworm_all.deb


The content will be extracted in the source directory. If you want to see the content of the resulting packages you can use the ``dpkg`` command:
::

   $ dpkg -c libnymea1_1.9.1+202402090827~cb960749~bookworm_armhf.deb
   
   drwxr-xr-x root/root         0 2024-02-09 09:34 ./
   drwxr-xr-x root/root         0 2024-02-09 09:34 ./usr/
   drwxr-xr-x root/root         0 2024-02-09 09:34 ./usr/lib/
   drwxr-xr-x root/root         0 2024-02-09 09:34 ./usr/lib/arm-linux-gnueabihf/
   -rw-r--r-- root/root   1138248 2024-02-09 09:34 ./usr/lib/arm-linux-gnueabihf/libnymea.so.1.0.0
   drwxr-xr-x root/root         0 2024-02-09 09:34 ./usr/share/
   drwxr-xr-x root/root         0 2024-02-09 09:34 ./usr/share/doc/
   drwxr-xr-x root/root         0 2024-02-09 09:34 ./usr/share/doc/libnymea1/
   -rw-r--r-- root/root      8435 2024-02-09 09:34 ./usr/share/doc/libnymea1/changelog.gz
   -rw-r--r-- root/root      1340 2020-08-07 07:56 ./usr/share/doc/libnymea1/copyright
   lrwxrwxrwx root/root         0 2024-02-09 09:34 ./usr/lib/arm-linux-gnueabihf/libnymea.so.1 -> libnymea.so.1.0.0
   lrwxrwxrwx root/root         0 2024-02-09 09:34 ./usr/lib/arm-linux-gnueabihf/libnymea.so.1.0 -> libnymea.so.1.0.0



Login into container
--------------------


If you want to login into the build container you can simply run:
::

   $ crossbuilder shell


Cache
-----


If you run the crossbuilder a second time, you just need to run ``crossbuilder``, since the first time a configuration file for the container has been created. Crossbuilder will also make use of the host `` ccache`` independent form the architecture and distribution. In this example you can find the `` crossbuilder`` cached information here:
::

   $ cat .crossbuilder/cache.conf
   
   TARGET_ARCH=armhf
   TARGET_UBUNTU=bookworm


Delete the container
--------------------


If you are finished and the container will not be needed any more you can delete the container by running:
::

   $ crossbuilder delete


Deploy on target machine
------------------------


If you want crossbuilder to deploy the packages to a remote machine and install them, you can create following configuration file:
::

   $ nano .crossbuilder/deploy.conf


Here you can add the remote information of the target machine (in this example an ``armhf bookworm`` machine running on `` 10.10.10.10`` where you want to install the debian packages built with the `` crosscompiler``.

.. note::

   The packages need to be already installed once on the target machine, since crossbuilder is just updating them, not installing them from scretch. If that is not the case, you can install them manually after crossbuilder copied them to the target and created the local repository: on the target ``sudo dpkg -i /tmp/repo/*.deb``.


::

   DEPLOY_IP=10.10.10.10
   DEPLOY_USER=nymea
   DEPLOY_KEY=~/.ssh/id_rsa


Each new build will from now on be installed automatically on the target machine until you delete the configuration file.

Interacting with the containers
-------------------------------


Remove a container if the source repositoy does not exist any more:

.. note::

   The ``--force`` is only needed if the container is still running.


::

   $ lxc list
   
   +--------------------------------------------------------+---------+-------------------+------+------------+-----------+
   |                          NAME                          |  STATE  |       IPV4        | IPV6 |    TYPE    | SNAPSHOTS |
   +--------------------------------------------------------+---------+-------------------+------+------------+-----------+
   | nymea-nymea-bookworm-amd64-armhf                       | RUNNING | 10.0.1.106 (eth0) |      | PERSISTENT | 0         |
   +--------------------------------------------------------+---------+-------------------+------+------------+-----------+
   
   $ lxc delete nymea-nymea-bookworm-amd64-armhf --force



Building with Yocto
-------------------

nymea can be built with Yocto. For that, we offer a meta layer which can be found on
`GitHub <https://github.com/nymea/meta-nymea>`__.

The meta-nymea layer mainly builds ``nymead`` and ``nymea-plugins``. A typical development workflow
is to keep the Yocto layers in a shared workspace, add ``meta-nymea`` to the build, create a small
QEMU/KVM image and boot that image for testing.

The meta layer can be added to a Yocto image and provides the following recipes in
``recipes-nymea``:

* ``libnymea-networkmanager``
* ``nymea``
* ``nymea-experience-plugin-energy``
* ``nymea-gpio``
* ``nymea-mqtt``
* ``nymea-plugins``
* ``nymea-plugins-genericthings``
* ``nymea-plugins-modbus``
* ``nymea-plugins-simulation``
* ``nymea-plugins-zigbee``
* ``nymea-remoteproxy``
* ``nymea-system-plugin-systemd``
* ``nymea-update-plugin-rauc``
* ``nymea-zeroconf-plugin-avahi``
* ``nymea-zigbee``

Example: build a QEMU/KVM image
-------------------------------

The following example shows a minimal development setup based on a QEMU/KVM image. The exact layer
names and image recipe may differ in your own workspace, but the overall flow stays the same. For a
full upstream walkthrough, see the `meta-nymea QEMU guide <https://github.com/nymea/meta-nymea/blob/wrynose/docs/build-yocto-nymea-image-qemu.md>`__.

1. Create a Yocto workspace and clone ``poky`` and the other layers you need.
2. Clone ``meta-nymea`` into the same workspace and add it to ``bblayers.conf``.
3. Create or extend an image recipe that installs ``nymead`` and, if desired, ``nymea-plugins`` and
   ``avahi-daemon``.
4. Build the image with ``bitbake``.
5. Boot the image with ``runqemu`` or your preferred KVM/QEMU setup.
6. Start or inspect ``nymead`` inside the image.

An example image recipe could look like this:

::

   SUMMARY = "nymea development image for QEMU/KVM"
   LICENSE = "MIT"

   require recipes-core/images/core-image-minimal.bb

   IMAGE_INSTALL:append = " nymead nymea-plugins avahi-daemon"

Build the image with:

::

   bitbake nymea-image-qemu

Then boot it with QEMU/KVM:

::

   runqemu qemux86-64 kvm nographic slirp

Once the image has booted, ``nymead`` should start automatically if it is enabled in the image. You
can inspect the service with:

::

   systemctl status nymead
   journalctl -u nymead -f

If you want to run ``nymead`` manually inside the image while debugging, stop the service first and
start it in the foreground:

::

   systemctl stop nymead
   nymead -n
