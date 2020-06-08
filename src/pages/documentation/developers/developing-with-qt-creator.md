---
id: qtcreator
title: Developing with QtCreator
---

QtCreator is the recommended IDE to build nymea projects. If you haven't done so, make sure the build environment is set up
property by following the guide in [Build environment](build-env).

### General steps for all nymea projects

1. Open QtCreator and click on *File* -> *Open file or project*

2. Navigate to the `.pro` file of the wanted project and open it.

3. In the next step, choose the wanted build kit. Unless you have special requirements, the default *Desktop* kit will do.

### Project specific options

The following options differ between the various projects. If the project you are looking for is not in here, no special options
are required. You should now be able to run the project using the build/play buttons.

#### Nymea

> **Note:** It is advised to uninstall libnymea1 to run a self built nymea instance to avoid confusion when libraries are loaded.

In order to run nymea from QtCreator, the library path needs to be set accordingly or starting nymead will fail with this message:

```bash
$ nymead: error while loading shared libraries: libnymea.so.1: cannot open shared object file: No such file or directory
```

Go to the Project settings on the left hand pane in QtCreator, select the "Run" configuration for your kit on the left and add
`LD_LIBRARY_PATH` to the environment, pointing to the libnymea and libnymea-core folders.

LD_LIBRARY_PATH: /PATH_TO_NYMEA/build-nymea-Desktop-Debug/libnymea/:PATH_TO_NYMEA/build-nymea-Desktop-Debug/libnymea-core/

Now you should be able to run *nymead* by pressing the *Play* button in the QtCreator (or you can press <kbd>Ctrl</kbd> + <kbd>r</kbd>). You can follow the stdout in the *Application Output* section (<kbd>Alt</kbd> + <kbd>3</kbd>).

If you want to run the application in the terminal you can start *nymead* with following command:

```bash
$ cd build-nymea-Desktop-Debug/server/
$ LD_LIBRARY_PATH=../libnymea:../libnymea-core ./nymead -n
```

In order to load custom plugins with this self built nymea instance, also set `NYMEA_PLUGINS_PATH` pointing to the build directory of
the plugin.

#### Nymea integration plugins

When developing plugins, nymea needs to be installed on the system. A run configuration for the plugin can be created by entering the
project configuration on the left hand side in QtCreator, then selecting the "Run" configuration for your kit and the left and creating
a run configuration with a "Custom executable". The executable shold be `nymead` and the command line arguments should at least include `-n`.
In the environment, export a variable named `NYMEA_PLUGINS_PATH` making it point to the build directory of the plugin.
