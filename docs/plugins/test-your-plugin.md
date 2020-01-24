---
id: test-your-plugin
title: Test your plugin
---

In order to make nymea load your plugin, you have two options. Either install it into the system or make nymea load it from your plugin build directory.

To install the plugin into the system, run:

```bash
$ make install
```

To make nymea load the plugin from the plugins build directory, run nymea with an environment variable exported

```bash
$ NYMEA_PLUGINS_PATH=/path/to/plugin/ nymead -n
```
In order to easier debug things, it is advised to enable debug output for the device manager and your plugin. E.g.

```bash
$ NYMEA_PLUGINS_PATH=/path/to/plugin nymead -n -d DeviceManager -d YourPlugin
```
