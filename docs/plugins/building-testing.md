---
id:building-testing
title: Building & testing
---

Once the code for the plugin has been created, the next step is to build the plugin and make nymea load it for testing. Those steps differ between C++/Qt and JS plugins.

## Building C++/Qt plugins

### Using QtCreator

If a plugin is created using QtCreator, clicking the build button in QtCreator should be all that's needed. QtCreator will typically create a build directory next to the project directory named `build-<project>-Desktop-Debug` (Note: the actual name might differ depending on the QtCreator setup and the selected build type).

Once the build succeeded, the build directory should contain a file named `libnymea_thingplugin<name>.so`. This is the plugin file and unless the actual implementation requires any additional resources is all that's needed to load the plugin in nymea.

### Manual compilation

If QtCreator is not used, the plugin can be compiled manually on the command line. It is recommended to create a new build directory instead of directly building in the source directory.


.... TODO....


## Building JS plugins


## Loading the plugin in nymea


## Debug categories

