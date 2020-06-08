---
id: tutorial-integration-cpp
title: Tutorial (C++/Qt)
---

This is a tutorial to show the very basic concept of nymea plugins. You will learn how to setup the initial plug-in file structure, modify the code, build, test and install the plug-in.

In this tutorial we'll be using QtCreator and the nymea plugin wizard to get started. Using QtCreator is not required and all the files can be created manually using your favorite text editor too. However, using QtCreator is the recommended way as it integrates best with the nymea sdk.

At this point you should already have set up the basic build environment following the [Build environment](docs/plugins/plugin-build-environment/) page.

## Initialize the plugin structure

Open QtCreator and create a new project. In the Wizard, there is an option for nymea. Selecting that, the option to create a new plugin for nymea will show up.

![Wizard](/img/wizard1.png)

Select the nymea plugin template and click next. In the next screen the project name and location will be chosen. Pick a location of your liking and enter the project name. In this example we'll create a plugin for a fictional thing from the fictional company ACME Inc. So we'll call the project `acme`.

![Wizard](/img/wizard2.png)

Advancing to the next page, we'll set the properties for the vendor of this thing. We'll use `acme` as the code identifier for our vendor and put the pretty printed string `ACME Inc.` into the vendor display name field. The display name field will be shown to the user later on. So make sure to match it as close as possible to the actual vendor name so the user will be able to recognize it.

![Wizard](/img/wizard3.png)

On the next page we'll fill in the details for the first thing this plugin will be supporting. We'll call it `acmeGaddget` in the code identifier and again put a more pretty printed value into the display name field, being `ACME Gadget`. This page also allows us to select the create method and setup method for this thing. Please refer to the [Create and setup methods documentation](http://docs-preview.nymea.io/docs/plugins/create-setup-methods/) for more details regarding those values. For this plugin we'll stay with the simplest combination, being create method `User` and setup method `JustAdd`.

![Wizard](/img/wizard4.png)

The next page will ask details about the developer. It will be used for the copyright and contact information in various files in the project.

![Wizard](/img/wizard5.png)

After a summary page, the last page is to configure QtCreators build settings. Choose `Desktop` here.

![Wizard](/img/wizard6.png)

When the wizard exits, we'll be left with the branch new project. There is one more thing to do before we can start building. Open the plugin info json file, named `integrationplugin<projectname>.json`. There will be some "id" values which are initialized to `00000000-0000-0000-0000-000000000000`. Open a terminal windows and type the command `uuidgen` to generate a new UUID. Copy/paste that a new UUID for each of the `id` fields, replacing the default value. The only exception would be if you create an additional plugin for an already existing vendor. In that case you'd want to use the same vendor id as the other plugin does in order group them for the end user.

## Building the plugin

Now the project is ready to be built. Click the build button in QtCreator. After a short while, the build process should finish successfully and the plugin binary file will be placed in the build directory. By default, the build directory can be found next to the source directory. For example, if you started the plugin in `/home/user/develop/acme`, the build output can be found in `/home/user/develop/build-acme-Desktop-Debug` or similar. The plugin binary file is called `libnymea_integrationplugin<name>.so`. In this example, the plugin name being `acme`, the file name is `libnymea_integrationpluginacme.so`.

```bash
user@hostname:~/develop/build-acme-Desktop-Debug$ ls -l
total 2376
-rw-rw-r-- 1 user user 816408 Feb 14 12:59 integrationpluginacme.o
-rwxrwxr-x 1 user user 742208 Feb 14 12:59 libnymea_integrationpluginacme.so
-rw-rw-r-- 1 user user  31607 Feb 14 12:59 Makefile
-rw-rw-r-- 1 user user  14476 Feb 14 12:59 moc_integrationpluginacme.cpp
-rw-rw-r-- 1 user user 797480 Feb 14 12:59 moc_integrationpluginacme.o
-rw-rw-r-- 1 user user  13604 Feb 14 12:59 moc_predefs.h
-rw-rw-r-- 1 user user   1095 Feb 14 12:59 plugininfo.h
```


## Testing the plugin

Now that we have built the plugin, we want to start up nymea and make it load this plugin for testing. For that, we manually launch nymead, passing it the path where to look for additional plugins.

> **Note:** If nymea is already running on this system as a system service, it needs to be stopped first. Running two nymea instances on the same machine is not supported.

In order to stop any nymea instance running as a system service, run this command:

```bash
sudo systemctl stop nymead
``` 

nymead can be sttarted from the command line using this command

```bash
nymead -n
```
    
The `-n` parameter is important to make nymea run in foreground, as opposed to a background service. We want that in order to see the logs. This will make nymea start up, but it won't load your freshly built plugin yet. For that, we need to let it know where the plugin can be found. We can export `NYMEA_PLUGINS_PATH` in the environment to do so:

```bash
NYMEA_PLUGINS_PATH=/home/user/develop/build-acme-Desktop-Debug nymead -n
```
    
> **Note:** Make sure to change the actual path to where your plugin's .so file is.

Now nymea is started, including your plugin. Use a client (e.g. nymea:app) to connect to this nymea instance and set up a new thing for this plugin.

## Troubleshoothing

### Errors during plugin loading

If something goes wrong, check the output that nymead prints for an error related to your plugin. Especially the lines starting with `ThingManager` are of interest here. If nymea fails to load the plugin for some reason, a line similar to this would be printed:

```bash
W: ThingManager: Libnymea API mismatch for libnymea_integrationpluginacme.so. Core API: 4.1, Plugin API: 3.4
```
    
This message should give you more information. In the above example, it would indicate that the libnymea used to compile the plugin is not the same as the one used to start up nymea. The resolution would be to make sure that the plugin is compiled with the same libnymea as the one used to run it now.


### Wrong plugins path?

If no error related to the plugin loading is to be seen but the plugin would still not appear in the app, the issue might be that nymea could not find the plugin. The way to track down such an issue would be to enable more debug output. Nymea can be started with more debug output using the `-d` passing the debug categories if interest. When debugging issues in regard to plugin loading, the `ThingManager` category is the one of interest. The startup command would look like this:

```bash
NYMEA_PLUGINS_PATH=/home/user/develop/build-acme-Desktop-Debug nymead -n -d ThingeManager
```
    
After starting this, nymea will print much more than in the previous run. Watch out for such messages:

```bash
Loading plugins from: ...
```
    
This line will be printed for each directory that nymea scans for plugins. In this example we want to make sure that it does print a line containing our path of `/home/user/develop/build-acme-Desktop-Debug`. So the exact debug line to look for would be:

```bash
Loading plugins from: /home/user/develop/build-acme-Desktop-Debug
```
    
If this line can't be found in the output, verify that there isn't a typo in `NYMEA_PLUGINS_PATH`. If this line is found, but the plugin is still not loaded, verify that the passed path is actually correct.

### The plugin is loading, but is not behaving properly

At this point the ThingManager did already do its job and an error might be in the plugin itself. In order to get more debug output from the plugin itself, nymea should be started with an additional `-d` parameter, passing the plugin name. In this example, the plugin name is `acme`. The matching debug category would be `Acme`. Thus, a useful startup command for this would be

```bash
NYMEA_PLUGINS_PATH=/home/user/develop/build-acme-Desktop-Debug nymead -n -d ThingManager -d Acme
``` 
