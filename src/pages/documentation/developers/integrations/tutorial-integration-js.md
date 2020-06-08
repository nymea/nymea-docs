---
id: tutorial-integration-js
title: Tutorial (JS)
---

This is a tutorial to show the very basic concept of nymea plugins. You will learn how to setup the initial plug-in file structure, modify the code, build, test and install the plug-in.

Any editor can be used to modify the files.

At this point nymea should be installed on the ddevelopment computer. Please follow the steps in [Build environment](../build-env) if you haven't done so yet.

### Initialize the plugin structure

At first, clone the template from the nymea-plugin-examples repository.

```bash
git clone https://github.com/nymea/nymea-plugin-examples.git
```

The repository contains a folder named template with a subdirectory named js. Copy the entire folder contents and start by renaming the files to the desired name. The terms "template" and "example" should be renamed to the plugins name.

### Adjust the plugin's JSON file

Now open the plugins json file and start adding thing classes, states, actions as desired. Please refer to the 
[Plugin json](../plugin-json) documentation on detailed informations on the individual entries.

### Edit the plugin code

Once the plugin json contains the desired entries, it is time to add the actual code for the plugin. Edit the .js file and fill in
the functions. Please refer to the [Plugin code (JS)](plugin-js) section for detailed informations.

### Testing the plugin

Now that we have built the plugin, we want to start up nymea and make it load this plugin for testing. For that, we manually launch nymead, passing it the path where to look for additional plugins.

> Note: If nymea is already running on this system as a system service, it needs to be stopped first. Running two nymea instances on the same machine is not supported.

In order to stop any nymea instance running as a system service, run this command:

```bash
sudo systemctl stop nymead
```

nymead can be sttarted from the command line using this command

```bash
nymead -n
```

The -n parameter is important to make nymea run in foreground, as opposed to a background service. We want that in order to see the logs. This will make nymea start up, but it won't load your freshly built plugin yet. For that, we need to let it know where the plugin can be found. We can export NYMEA_PLUGINS_PATH in the environment to do so:

```bash
NYMEA_PLUGINS_PATH=/home/user/develop/build-acme-Desktop-Debug nymead -n
```

> Note: Make sure to change the actual path to where your plugin's .so file is.

Now nymea is started, including your plugin. Use a client (e.g. nymea:app) to connect to this nymea instance and set up a new thing for this plugin.
