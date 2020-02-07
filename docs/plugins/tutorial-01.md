---
id: tutorial-01
title: First Plug-In
---

This is a tutorial to show the very basic concept of nymea plugins. You will learn how to setup the initial plug-in file structure, modify the code, build, test and install the plug-in.

In this tutorial we'll be using QtCreator and the nymea plugin wizard to get started. Using QtCreator is not required and all the files can be created manually using your favorite text editor too. However, using QtCreator is the recommended way as it integrates best with the nymea sdk.

At this point you should already have set up the basic build environment following the [Build environment](docs/plugins/plugin-build-environment/) page.

## Initialize the plugin structure

Open QtCreator and create a new project. In the Wizard, there is an option for nymea. Selecting that, the option to create a new plugin for nymea will show up.

![Wizard](/img/wizard1.png)

Select the nymea plugin template and click next. In the next screen the project name and location will be chosen. Pick a location of your liking and enter the project name. In this example we'll create a plugin for a fictional device from the fictional company ACME Inc. So we'll call the project `acme`.

![Wizard](/img/wizard2.png)

Advancing to the next page, we'll set the properties for the vendor of this device. We'll use `acme` as the code identifier for our vendor and put the pretty printed string `ACME Inc.` into the vendor display name field. The display name field will be shown to the user later on. So make sure to match it as close as possible to the actual vendor name so the user will be able to recognize it.

![Wizard](/img/wizard3.png)

On the next page we'll fill in the details for the first device this plugin will be supporting. We'll call it `acmeGaddget` in the code identifier and again put a more pretty printed value into the display name field, being `ACME Gadget`. This page also allows us to select the create method and setup method for this device. Please refer to the [Create and setup methods documentation](http://docs-preview.nymea.io/docs/plugins/create-setup-methods/) for more details regarding those values. For this plugin we'll stay with the simplest combination, being create method `User` and setup method `JustAdd`.

![Wizard](/img/wizard4.png)

The next page will ask details about the developer. It will be used for the copyright and contact information in various files in the project.

![Wizard](/img/wizard5.png)

After a summary page, the last page is to configure QtCreators build settings. Choose `Desktop` here.

![Wizard](/img/wizard6.png)

When the wizard exits, we'll be left with the branch new project. There is one more thing to do before we can start building. Open the plugin info json file, named `deviceplugin<projectname>.json`. There will be some "id" values which are initialized to `00000000-0000-0000-0000-000000000000`. Open a terminal windows and type the command `uuidgen` to generate a new UUID. Copy/paste that a new UUID for each of the `id` fields, replacing the default value. The only exception would be if you create an additional plugin for an already existing vendor. In that case you'd want to use the same vendor id as the other plugin does in order group them for the end user.

## Building the plugin

Now the project is ready to be built. Click the build button in QtCreator.

## Testing the plugin

TODO: start nymea, NYMEA_PLUGINS_PATH

