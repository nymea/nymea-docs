---
id: things
title: Connecting things
---

## Add things to nymea

Now that nymea is up and running it's time to add some things to it, such as devices or services. Adding new things 
is done from the main menu in the *Configure things* view. From there, select the `+` button in the upper right 
corner and pick the type of thing to add.

After selecting the type of thing to add, nymea will start a wizard to guid you through the steps of adding the thing.
The actual content of the wizard may vary between types of things. The basic flow however is the same for all. For example, adding a TP-Link Kasa smart plugin would be done like this:

![](/img/documentation/users/connecting-things.gif)

> For documentation on individual things, please check out the documentation for the appropriate integration which can be found in the [integrations](/documentation/resources/integrations) page.


After the thing has been added, it will appear in the main screen. In this case a power socket that can be switched 
on and off, and a smart meter that allows to monitor the power consumption on the smart plug.

![](/img/documentation/users/controlling-things.gif)


## General purpose devices

Sometimes there is a need to connect general purpose devices. Examples for such devices are smart plugs or GPIOs. A smart plug for example
will be shown in nymea as power socket and can be turned on and off. However, in practice, a user will connect some other device to the
smart plug, for instance a light. In order to also have the light showing up in nymea as an individual thing, a generic light can be created
and connected to the smart plug in nymea. When nymea:app is then used to switch the light, nymea will know that it needs to control power
on the smart plug to actually turn on and off the light:

![](/img/documentation/users/generic-things.gif)


## Installing more plugins

By default, nymea comes with a selection of preinstalled plugins. However, those are not all the available ones. If you can't find something in your nymea setup but it's listed on the [integrations](/documentation/resources/integrations) page, you can install it by entering the *System settings* and opening the *Software update* section. From there, move to *Install or remove software* and you'll find a list of available integration plugins to be installed.

![](/img/documentation/users/installing-plugins.gif)

> Note: At this point nymea will require a restart after installing new plugins!
