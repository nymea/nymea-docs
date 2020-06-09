---
id: building-testing
title: Building & testing
---

Once the code for the plugin has been created, the next step is to build the plugin and make nymea load it for testing. Those steps differ between C++/Qt and JS plugins.

## Building C++/Qt plugins

### Using QtCreator

If a plugin is created using QtCreator, clicking the build button in QtCreator should be all that's needed. QtCreator will typically create a build directory next to the project directory named `build-<project>-Desktop-Debug` (Note: the actual name might differ depending on the QtCreator setup and the selected build type).

Once the build succeeded, the build directory will contain the plugin file named `libnymea_inteagrationplugin<name>.so`. Unless the actual implementation requires any additional resources is all that's needed to load the plugin in nymea.

### Manual compilation

If QtCreator is not used, the plugin can be compiled manually on the command line. It is recommended to create a new build directory instead of directly building in the source directory. For example as a subdirectory named `builddir` in the source directory. From there it is requried to run `qmake` and `make`:

```bash
$ cd /path/to/plugin/source
$ mkdir builddir
$ cd builddir
$ qmake ..
$ make
```
    
Once the build succeeded, the build directory will contain the plugin file named `libnymea_integrationplugin<name>.so`. Unless the actual implementation requires any additional resources is all that's needed to load the plugin in nymea.

## Building JS plugins

JavaScript plugins do not require to be compiled. However, `nymea-plugininfocompiler` can be used to validate the [JSON file](plugin-json). Run `nymea-plugincompiler` on the plugins `.json` file.

```bash
$ nymea-plugininfocompiler integrationplugintemplate.json
```
    
If the command exits without any output, all went fine. If the JSON file contains any errors they will be printed out.


## Loading the plugin in nymea

Now that we have built the plugin, we want to start up nymea and make it load this plugin for testing. For that, we manually launch nymead, passing it the path where to look for additional plugins.

nymead can be started from the command line using this command

```bash
nymead -n
```
    
The `-n` parameter is important to make nymea run in foreground, as opposed to a background service. We want that in order to see the logs. This will make nymea start up, but it won't load your freshly built plugin yet. For that, we need to let it know where the plugin can be found. We can export `NYMEA_PLUGINS_PATH` in the environment to do so:

```bash
NYMEA_PLUGINS_PATH=/path/to/plugin/builddir nymead -n
```


## Debug categories

By default, nymead will only print warning messages, that is messages that have been produced by `qCWarning()` (C++/Qt) or `console.warn()` (JS). In order to also see debug messages produced by `qCDebug()` (C++/JS) or `console.log()` (JS), each plugin has its own debug category. The debug category for a plugin is defined by the `name` property in the plugins [JSON file](plugin-json). In order to see a plugins debug messages nymead can be started by passing the `-d <Name>` option. For example:

```bash
NYMEA_PLUGINS_PATH=/path/to/plugin/builddir nymead -n -d Example
```

When working with integration plugins, it is useful to enable more debug output from the ThingManager:

```bash
NYMEA_PLUGINS_PATH=/path/to/plugin/builddir nymead -n -d Example -d ThingManager
```
