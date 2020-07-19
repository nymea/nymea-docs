---
id: thing-class
title: Things classes
---

The thing class describes how a certain thing will look like, what features it offers and how the user and the system interact with it. In order to add support for a new device or service to nymea, the developer has a certain set of options at hand to create such a thing class and inform nymea about the capabilities of the device or service. This section will list the available properties of Thing classes and explain what they are used for.

Thing classes are defined using the `thingClasses` property in the [plugins JSON](plugin-json#thing-classes) file.

## Parameters

A thing class may or may not have parameters. Parameters are used to hold the very basic information required to connect (or generally "use") a device or service. Normally a thing class will have at least one parameter. For instance, when creating a thing class which will describe a device on the local network, it may have a parameter holding its IP address. A device connected via USB might hold the device ID as presented on the USB. A thing class describing an online service might have the URL for the server as parameter.

When a thing is configured in the system, nymea (or the user) will fill the parameters and hand them over to the plugin developer in order to perform the needed tasks to perform the required set up.

Once a parameter is set during the setup, it will stay the same over the the entire lifetime of the thing. It will only change if the user reconfigures a thing which basically comes down to removing the thing from the system and re-adding a new one with the new parameters.

> NOTE: In general it is advisable to keep this to the very minimum set of information required to render the thing usable.

> NOTE: Try to use persistent information here. For example a LAN IP address of a device might change when the DHCP lease renews. A better way would be to find some persistent device ID and perform a discovery of the given device on the network, e.g. via mDNS or UPnP.

Parameters are defined using the `paramTypes` property in the [plugins JSON](plugin-json#thing-classes) file and will be attached to every thing created in the system. The plugin developer may read those parameters during the [setup](plugin-code#setup) or any later point. If the parameters of a thing change, the setup will be performed again.

## Settings

Things can have settings. Thing settings are very similar to the params used during setup, however, they can be changed at runtime, without having to reconfigure a thing. Settings can be used allow changing the behavior of a thing by the user. Settings must not affect the basic connectivity to a thing or impair the basic functionality.

For instance, a Buetooth device with a small battery might not be possible to be connected all the time in order to not drain the battery. Such a device might need to be polled regularly. However, for some use cases (i.e. measuring a plant’s soil moisture) a polling interval of once per hour might be enough, while for other use cases (i.e. triggering an alarm when water leakage is detected) a much more frequent interval might be required. To have the plugin catering for both use cases, thing settings can be implemented to provide a "polling interval" setting.

Settings are defined using the `settingsTypes` property in the [plugins JSON](plugin-json#thing-classes) file and will be attached to every thing created in the system. The plugin developer may [access those settings](plugin-code#settings) during the [setup](plugin-code#setup) or any later point. If the settings of a thing change, the plugin will be notified about the change. 

## Setup

There are a set of properties for thing classes which define how the setup is done in nymea. When a thing is created in nymea, it walks through a setup flow. The thing class also specifies how this actual flow looks like.

The properties of a thing class defining the setup process are the create methods and the setup method. Depending on the create method, a thing class might also have discovery parameters.

The detailed description of the setup flow is described in the [things setup](thing-setup) page.

## Events

In nymea, every thing can have a set of states. For example, a device with buttons would trigger an event for `buttonPressed` whenever the user presses the button. Event can also have parameters. In the example of a remote control, the `buttonPressed` event would also contain a parameter to indicate which button has been pressed.

Events are defined using the `eventTypes` property in the [plugins JSON](plugin-json#thing-classes) file and [emitted in the plugin code](plugin-code#events) whenever the event occurs.

## Actions

Similar to events, but the other direction, a thing can have actions. For example, a smart speaker would have multiple actions, like `play`, `pause` and so on. The user (or some automation) can then execute those actions to control the device. Like events, also actions can have parameters. As an example for this, an online service that sends out notifications to the user would have an action named `notify` with two parameters, one for `title` and one for `body`. Those parameters will then contain the actual content of the notification.

Actions are defined using the `actionTypes` property in the [plugins JSON](plugin-json#thing-classes) file and executed in the plugin code by implementing the [executeAction](plugin-code#actions) method.

## States

Every thing can also have a set of states. States are used to represent a set of properties that might change over time. For example a temperature sensor might have a state named "temperature" to indicate the currently measured temperature. Whenever the measured temperature changes, the plugin implemenation updates the state value in nymea.

Every state change will implicitly trigger an event in the system which will propagate the state change through the entire system.

States can be read only or writable. A read only state will only read a certain things state and make its value available to nymea. A writable state can also be changed in nymea, which would then change the state on the thing. A writable state will implicitly generate the according action which is used in nymea to set the states value.

States are defined using the `stateTypes` property in the [plugins JSON](plugin-json#thing-classes) file and can be updated in the plugin code by calling [setStateValue](plugin-code#states) whenever the thing changes a state. If a state is writable, an according [executeAction](plugin-code#actions) call to the plugin will be made by nymea when the user (or some automation) triggers a state change.

## Interfaces

When creating a thing class, the interfaces property can be used to specify a list of interfaces this thing class implements.

The main purpose of interfaces is to provide for a better user experience. Using interfaces, a plugin developer can suggest the ui to be used for this thing. For example, having a thing class that can control a dimmable light would likely have a state named “power” of type boolean and one named “brightness” of type int, ranging from 0 to 100%. Having just this information, the ui would create a generic switch component to flip the bool state and a generic slider component to allow adjusting the brightness because it can’t know what the actual switch or slider do. For a better user experience though, the plugin developer could add the interface “dimmablelight” to this thing class and this way tell the ui that this actually is a dimmable light. The ui can use this information to paint a pretty light bulb and a brightness slider and group all lights together.

When adding an interface to the thing class, the thing class must follow the interface specification for the according interface. This means the thing class needs to have at least all the states, actions and events the given interface requires. A thing class may add custom states, actions or events, or even implement multiple interfaces.

In general it is a good idea to follow as many interfaces as possible in order to provide for the best user experience.

An interface can extend another interface. For example, the light interface only requires one state called powered of type bool. A dimmablelight extends this type and adds a brightness property to it. This means, if a thing class implements dimmablelight, it also needs to cater for the light interfaces states.

The complete list of available interfaces can be found in the [interfaces](interfaces) page.

## Generic inputs and outputs

A state in a thing class can be marked as being a generic input or output for when it's not clear what type of interface should be used.

A good example for this is a smart plug. When creating an integration plugin for a smart plug the plugin developer would naturally add the `powersocket` interface to it. This makes sense as a user will want the smart plug to appear as a power socket in the UI. However, the plugin developer cannot know what the user is actually going to plug into it. The user might connect a light bulb to it but this light bulb will not appear in the lights category of the user interface as nymea is actually controlling the smart plug and not the light. This will have a bad impact on the user experience. To solve this situation, the `power` state of the smart plug can be marked as a generic output. The user can then add a virtual light thing to the system and connect it to the smart plug thing. Now, whenever the user controls the light, nymea will forward this control event to the smart plug.

The possible options for such generic inputs and outputs are `digitalInput`, `digitalOutput`, `analogInput` or `analogOutput`. A digital input can only be connected to a digital output (and vice versa) just like an analog input can only be connected to an analog output (and vice versa).

Generic inputs and outputs are defined using the `stateTypes` property in the [plugins JSON](plugin-json#thing-classes) file.

## Browsing

Some things might offer the feature to be browsable. For example, a smart speaker can allow the user to browse the available playlists. Browsing a thing is like browsing a file system. It can be a simple list of entries, but also an entire tree which can be entered.

Currently nymea supports two types of browsers. File browsers and media browsers. In principle they work exactly the same. The difference is only that media browsers support a wider range of media related metadata for each entry.

![Media browser showing music artists](/img/browsing.png)

Entries in a browser can be executable and browsable. If an item is executable, it can be launched (or played for media browsers). If an item is browsable, it means that it can be entered, for instance a folder.

In addition to that, each entry can have context menus which allow the plugin developer to add arbitrary actions to each item.

![](/img/browsing2.png)


Browing can be enabled using the `browsable` property in the [plugin JSON](plugin-json#thing-classes) file and implementing the [browsing related methods](plugin-code#browsing) in the plugin code.
