---
id: getting-started-integration
title: Getting started
---

Integration plugins in nymea provide support for additional integrations with hardware devices and online services, commonly referred to as "things". A plugin is responsible for translating the nymea internal things api into the device or service specific protocol. This mainly consists of handling setup and connecting to a given thing and then monitoring it for state changes and forwarding actions triggered by nymea to it.

## Basic concepts

A single plugin can provide support for multiple things and also multiple vendors. Normally however, a single plugin would only add support for thing of a single vendor, or even only for a certain product category to keep the plugin code small and manageable.

When the user configures a connection to a device or online service, a new thing object is created in the system. Each thing is defined by a [thing class](thing-class). The thing class describes how a certain thing will look like, what features it offers and how the user and the system interact with it.

## ID and name

Pretty much everyting in nymea is identified using a unique ID and a name. The IDs are generated and set by the plugin developer and used to refer to a particular entity throughout the system. Note that once generated, the ID must remain the same forever in order to allow nymea to match between thing classes, config values, caches and so on. If the ID of an entity is changed (for example on an upgrade), nymea will treat it as a new entity and things created with the old ID will cease to work.

As IDs are not nice to work with, neither for the developer nor the user, each ID also comes with a name. And not only with a name, but also with a display name. The name is used when referring to something in log files, in code and similar. It must consist only of letters and not contain spaces or special characters. Think of it as a variable name for the ID. The display name on the other hand is a pretty printed string that is shown to the user and will be translated to different languages. Both, the name and display name might be changed over time to reflect on rebranding, renaming or similar of an actual product, service or company while still being able to continue to use setups that were configured before the change. Given the ID will be persistent, nymea will still be able to match configurations and properly reflect such changes in the names.

## The plugin JSON file

The first task for creating a new integration plugin is to create a [plugin JSON](plugin-json) file. This JSON file will list all vendors and thing classes this plugin supports.


## The plugin code

Once the thing class is defined, the plugin implementation needs to be added in order to actually implement the features described in the thing class. The plugin implementation can be written using C++/Qt or JavaScript and is documented [the plugin code](plugin-code) section.

## Testing the plugin

Once the code for the plugin has been created, the next step is to build the plugin and make nymea load it for testing as described [here](building-testing)

