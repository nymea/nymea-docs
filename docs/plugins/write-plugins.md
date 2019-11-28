---
id: write-plugins
title: Plug-in development
---

## Plug-Ins
------------------------------------------

Plugins in nymea are used to expand the functionality and capabilities of the nymea server. A plugin is basically a shared library, which will be loaded dynamically by the nymea server during the start up process. Each plugin has a name, a UUID and a list of supported vendors which will be visible in the system once the plugin is loaded. Each of those Vendors contains a list of supported DeviceClasses. A DeviceClass describes how the supported Device looks like, how it will be created (CreateMethod), how the setup (SetupMethod) looks like and what you can do with the Device.

A plug-in is needed to abstact the services and devices into nymeas internal [ABI](https://en.wikipedia.org/wiki/Application_binary_interface).

A _device_ in nymea can represent a _real_ devices such as lightbulbs, gateways or garage door openers, but can also represent online service, for example a weather service, or an E-Mail service. When you want to add support for your own device/service in nymea, you should try to abstract that device and think in terms like:

## Terms definition

### Params

Params will be needed to set up the device. Common params are IP address, port or device identificatio. Params give the needed  information to setup and load a device.

### Settings

Settings are like params, with the exception that the user (and also the plugin developer) can change them at runtime. Settings should be used to change the behavior of a device. An example would be the refresh interval for polling a web server

### States    

States basically represent a value of a Device, for example the temperature of a thermostat, the brightness of a bulb.
Sometimes actions and states needs to be combined, for example a brightness slider that needs a state to know where the slider 
is and needs an action to send the brightness to the bulb. For that there are _writable_ states, where nymea creates automatically
an action out of the state.

### Events

Events basically represent a signal, for example a button pressed, or motion detected. 
Like actions, events can have Params too, to give the possibility to pass information with the signal, another example: Email received, an event with a subject text line and a body text field.

### Actions

Actions represent basically a method for the Device which the user can execute. An example of an Action could be: Set temperature. 
An Action can have params to give the possibility to parameterize the action, like Send Email has the action param "subject", and "body" so you can add a subject line and text to the body before you can send it.

### Interfaces

Interface define the character of a device/service, and require certain actions, states and events so that device category is always the same. An example, an interface that defines a simple light bulb, needs to have at leas an on/off action - so in the app this device will be displayed as a light with a toggle button and if nymea is connected to Alexa and co this services also recognice this device as a light.

### Setup Methods

Setup methods are the answer to your question _How do I get my device into the system?_
There are 3 setup methods, User, Discovery and Auto. Some Examples

* User: Email service, the user is required to fill in the email server credentials
* Discovery: Within a local area network to dsicover the ZigBee bridge.
* Auto: After the ZigBee bridge is connected, the ZigBee devices apear automaticall without any involvement of the user.

### Create Methods

Well known from Bluetooth 

###

The libnymea provides a list of HardwareResources, which can be used in every plugin. When sou start writing a plugin, you need to know which resource you will need. Each resource provides it's own interface for a DevicePlugin. In the plugin you don't have to take care about the resource.
