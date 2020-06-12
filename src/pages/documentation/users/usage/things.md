---
id: things
title: Connecting things
---

Now that nymea is up and running it's time to add some things to it, such as devices or services. Adding new things 
is done from the main menu in the *Configure things* view. From there, select the `+` button in the upper right 
corner and pick the type of thing to add.

For example, adding a TP-Link Kasa smart plugin would be done like this:

![](/img/add-thing.gif)

After the thing has been added, it will appear in the main screen. In this case a power socket that can be switched 
on and off, and a smart meter that allows to monitor the power consumption on the smart plug.

### General purpose devices

Sometimes there is a need to connect gneral purpose devices. Examples for such devices are smart plugs or GPIOs. A smart plug for example
will be shown in nymea as power socket and can be turned on and off. However, in practice, a user will connect some other device to the
smart plug, for instance a light. In order to also have the light showing up in nymea as an individual thing, a generic light can be created
and connected to the smart plug in nymea. When nymea:app is then used to switch the light, nymea will know that it needs to control power
on the smart plug to actually turn on and off the light:

![](/img/generic-io.gif)
