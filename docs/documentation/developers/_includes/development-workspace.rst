Development workspace
---------------------

For day-to-day development, it is easier to keep all related nymea repositories in one parent
directory and build them from there. A workspace layout like this works well:

* ``~/development/nymea/nymea-zigbee``
* ``~/development/nymea/nymea-mqtt``
* ``~/development/nymea/nymea-remoteproxy``
* ``~/development/nymea/nymea-gpio``
* ``~/development/nymea/libnymea-networkmanager``
* ``~/development/nymea/nymea``

The other projects can be like ``nymea-plugins`` require the minimal nymea setup

* ``~/development/nymea/nymea-*plugins*``

When the repositories are built inside the same workspace, the build output can be reused both from
the shell and from Qt Creator.

When working in Qt Creator, open and build the projects in dependency order:

1. ``nymea-zigbee``
2. ``nymea-mqtt``
3. ``nymea-remoteproxy``
4. ``nymea-gpio``
5. ``libnymea-networkmanager``
6. ``nymea``

After that, open and build any additional plugin or support repositories you want to work on in the
same workspace.

An example runtime and build environment could look like this:

.. code-block:: bash

   export PROJECT_PATH=~/development/nymea/
   export PROJECT_BUILDDIR=build/Desktop_Qt_<version>-Debug

   # Use the build directory name that Qt Creator generates for the selected Qt version and kit.
   # Adjust PROJECT_BUILDDIR whenever you switch to a different desktop Qt version.

   export NYMEA_MQTT=${PROJECT_PATH}/nymea-mqtt
   export NYMEA_ZIGBEE=${PROJECT_PATH}/nymea-zigbee
   export NYMEA_NETWORKMANAGER=${PROJECT_PATH}/libnymea-networkmanager
   export NYMEA_GPIO=${PROJECT_PATH}/nymea-gpio
   export NYMEA_REMOTEPROXY=${PROJECT_PATH}/nymea-remoteproxy
   export NYMEA_MODBUS_LIBS=${PROJECT_PATH}/nymea-plugins-modbus/${PROJECT_BUILDDIR}/libnymea-modbus:${PROJECT_PATH}/nymea-plugins-modbus/${PROJECT_BUILDDIR}/libnymea-sunspec
   export NYMEA_ENERGY_LIB=${PROJECT_PATH}/nymea-experience-plugin-energy/${PROJECT_BUILDDIR}/libnymea-energy

   export CPATH=${NYMEA_MQTT}/libnymea-mqtt:${NYMEA_NETWORKMANAGER}/libnymea-networkmanager:${NYMEA_GPIO}/libnymea-gpio:${NYMEA_REMOTEPROXY}/libnymea-remoteproxyclient:${NYMEA_ZIGBEE}/libnymea-zigbee
   export LD_LIBRARY_PATH=${NYMEA_MQTT}/${PROJECT_BUILDDIR}/libnymea-mqtt:${NYMEA_NETWORKMANAGER}/${PROJECT_BUILDDIR}/libnymea-networkmanager:${NYMEA_GPIO}/${PROJECT_BUILDDIR}/libnymea-gpio:${NYMEA_REMOTEPROXY}/${PROJECT_BUILDDIR}/libnymea-remoteproxyclient:${NYMEA_ZIGBEE}/${PROJECT_BUILDDIR}/libnymea-zigbee:${NYMEA_MODBUS_LIBS}:${NYMEA_ENERGY_LIB}
   export LIBRARY_PATH=${NYMEA_MQTT}/${PROJECT_BUILDDIR}/libnymea-mqtt:${NYMEA_NETWORKMANAGER}/${PROJECT_BUILDDIR}/libnymea-networkmanager:${NYMEA_GPIO}/${PROJECT_BUILDDIR}/libnymea-gpio:${NYMEA_REMOTEPROXY}/${PROJECT_BUILDDIR}/libnymea-remoteproxyclient:${NYMEA_ZIGBEE}/${PROJECT_BUILDDIR}/libnymea-zigbee:${NYMEA_MODBUS_LIBS}:${NYMEA_ENERGY_LIB}
   export PKG_CONFIG_PATH=${NYMEA_MQTT}/${PROJECT_BUILDDIR}/libnymea-mqtt/pkgconfig:${NYMEA_NETWORKMANAGER}/${PROJECT_BUILDDIR}/libnymea-networkmanager/pkgconfig:${NYMEA_GPIO}/${PROJECT_BUILDDIR}/libnymea-gpio/pkgconfig:${NYMEA_REMOTEPROXY}/${PROJECT_BUILDDIR}/libnymea-remoteproxyclient/pkgconfig:${NYMEA_ZIGBEE}/${PROJECT_BUILDDIR}/libnymea-zigbee/pkgconfig

   export NYMEA_APIKEYS_PLUGINS_EXTRA_PATH=${PROJECT_PATH}/nymea-apikeysprovider-plugin-community/${PROJECT_BUILDDIR}
   export NYMEA_EXPERIENCE_PLUGINS_EXTRA_PATH=${PROJECT_PATH}/nymea-experience-plugin-energy/${PROJECT_BUILDDIR}/plugin:${PROJECT_PATH}/nymea-experience-plugin-evdash/${PROJECT_BUILDDIR}/plugin:${PROJECT_PATH}/nymea-experience-plugin-airconditioning/${PROJECT_BUILDDIR}
   export NYMEA_PLATFORM_PLUGINS_EXTRA_PATH=${PROJECT_PATH}/nymea-zeroconf-plugin-avahi/${PROJECT_BUILDDIR}
   export NYMEA_ENERGY_PLUGINS_PATH=${PROJECT_PATH}/nymea-energy-plugin-nymea/${PROJECT_BUILDDIR}/energyplugin:${PROJECT_PATH}/nymea-energy-plugin-chargingsessions/${PROJECT_BUILDDIR}/energyplugin
   export NYMEA_PLUGINS_EXTRA_PATH=${PROJECT_PATH}/nymea-plugins/${PROJECT_BUILDDIR}:${PROJECT_PATH}/nymea-plugins-zigbee/${PROJECT_BUILDDIR}:${PROJECT_PATH}/nymea-plugins-modbus/${PROJECT_BUILDDIR}:${PROJECT_PATH}/nymea-plugin-streamunlimited/${PROJECT_BUILDDIR}:${PROJECT_PATH}/nymea-plugins-simulation/${PROJECT_BUILDDIR}
