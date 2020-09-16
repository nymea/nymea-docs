---
id: building-testing
title: Building & testing
---

Once the code for the plugin has been created, the next step is to build the plugin and make nymea load it for testing. Those steps differ depending on the chosen program language.

## Building C++/Qt plugins

### Using QtCreator

If a plugin is created using QtCreator, clicking the build button in QtCreator should be all that's needed. QtCreator will typically create a build directory next to the project directory named `build-<project>-Desktop-Debug` (Note: the actual name might differ depending on the QtCreator setup and the selected build type).

Once the build succeeded, the build directory will contain the plugin file named `libnymea_inteagrationplugin<name>.so`. Unless the actual implementation requires any additional resources, this file is all that's needed to load the plugin in nymea.

### Manual compilation

If QtCreator is not used, the plugin can be compiled manually on the command line. It is recommended to create a new build directory instead of directly building in the source directory. For example as a subdirectory named `builddir` in the source directory. From there it is requried to run `qmake` and `make`:

```bash
$ cd /path/to/plugin/source
$ mkdir builddir
$ cd builddir
$ qmake ..
$ make
```
    
Once the build succeeded, the build directory will contain the plugin file named `libnymea_integrationplugin<name>.so`. Unless the actual implementation requires any additional resources, this file is all that's needed to load the plugin in nymea.

## Building Python plugins

Python, being an interpreted language, doesn't require any compilation. However, depending on what `import` statements have been used, there may be the need to install dependencies. Dependencies are installed in the plugin source folder using the command:

```Bash
$ pip3 install somemodule -t modules
```

Finally the plugin code directory needs to contain those files:
* integrationpluginexample.py
* integrationpluginexample.json
* A `modules` subdirectory containing any imported python modules
* Any other .py files that have been created along with this plugin

### Validating the JSON file

Optionally, `nymea-plugininfocompiler` can be used to validate the [JSON file](plugin-json). Run `nymea-plugincompiler` on the plugins `.json` file.

```bash
$ nymea-plugininfocompiler integrationplugintemplate.json
```
    
If the command exits without any output, all went fine. If the JSON file contains any errors they will be printed.

## Building JS plugins

JavaScript plugins do not require to be compiled.

Finally the plugin code directory needs to contain those files:
* integrationpluginexample.js
* integrationpluginexample.json
* Any .mjs module files that have been imported

### Validating the JSON file

Optionally, `nymea-plugininfocompiler` can be used to validate the [JSON file](plugin-json). Run `nymea-plugincompiler` on the plugins `.json` file.

```bash
$ nymea-plugininfocompiler integrationplugintemplate.json
```
    
If the command exits without any output, all went fine. If the JSON file contains any errors they will be printed.

## Loading the plugin in nymea

Now that we have built the plugin, we want to start up nymea and make it load this plugin for testing. For that, we manually launch nymead, passing it the path where to look for additional plugins.

nymead can be started from the command line using this command

```bash
nymead -n
```
    
The `-n` parameter is important to make nymea run in foreground, as opposed to a background service. We want that in order to see the logs. This will make nymea start up, but it won't load your freshly built plugin yet. For that, we need to let it know where the plugin can be found. We can export `NYMEA_PLUGINS_PATH` in the environment to do so:

For C++ plugins, the path should point to the build directory, for Python and C++ plugins, this path should point to the plugin source directory.

```bash
NYMEA_PLUGINS_PATH=/path/to/plugin/dir nymead -n
```

## Debug categories

By default, nymead will only print warning messages, that is messages that have been produced by `qCWarning()` (C++/Qt), `logger.warn()` (Python) or `console.warn()` (JS). In order to also see debug messages produced by `qCDebug()` (C++/Qt), `logger.log()` (Python) or `console.log()` (JS), each plugin has its own debug category. The debug category for a plugin is defined by the `name` property in the plugins [JSON file](plugin-json). In order to see a plugins debug messages, nymead can be started by passing the `-d <Name>` option. For example:

```bash
NYMEA_PLUGINS_PATH=/path/to/plugin/builddir nymead -n -d Example
```

When working with integration plugins, it is useful to enable more debug output from the ThingManager:

```bash
NYMEA_PLUGINS_PATH=/path/to/plugin/builddir nymead -n -d Example -d ThingManager
```

## Troubleshoothing

### My plugin isn't loaded

If your plugin isn’t loaded, there are a few common pitfalls that are worth checking:

#### Wrong NYMEA_PLUGINS_PATH?

Start nymead with the `-d ThingManager` argument to get more debug information about the situation.

Check the output for messages like 

```bash
Loading plugins from: ...
```

Ensure the path containing your plugin is listed there. If not, most likely the NYMEA_PLUGINS_PATH environment variable isn’t set properly.

#### Unsatisfied dependencies?

If nymea finds the plugin but still isn't able to load it, watch out for warning messages like “undefined symbol” or “module not found” which should give clues about missing linker flags (C++/Qt) or missing import modules (Python/JavaScript).

#### API mismatch?

This one (currently) only applies to C++ plugins. When loading a plugin, nymead will check against which plugin API version the plugin has been built. If you've upgraded your nymea sdk during plugin development and there has been a major change in the Plugin API in the meantime, a plugin might fail to load because of this. Nymea would tell about it in a message similar to this:

```bash
W: ThingManager: Libnymea API mismatch for libnymea_integrationpluginexample.so. Core API: 4.1, Plugin API: 3.4
```
    
In this case, the plugin requires a rebuild.

> Note: While Python and JS plugins would not complain about an API mismatch at loading time due to the nature of scripting languages, they may still fail later if the changed API is used. Such plugins should be tested thoroughly on major nymea API changes.
