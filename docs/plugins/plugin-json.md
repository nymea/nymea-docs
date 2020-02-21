---
id:plugin-json
title: The plugin JSON file
---

The first entry point for integration plugins in nymea is the plugin JSON file. This file describes all the capabilities of this plugin. It will list all the information about the things it supports and how those things look like in the nymea system.


## Identification properties

Throughout the plugin JSON file, most entities will contain some properties which are always to be used in the same manner. Those are `id`, `name` and `displayName`. 

* `id`: Whenever an `id` field is required, a new, unique UUID is to be created and inserted. This UUID must stay the same throughout the lifetime of a integration plugin as settings, log entries and all will be linked using this ID. A plugin developer should use the `uuidgen` command to create a new uuid once and never change it again. 

* `name`: The `name` property is used to define variables which will be used in the code to refer to certain parts of the JSON file. It must not contain whitespaces or special characters. This name can be changed at any time without breaking existing setups when a plugin is updated. For instance, if a device vendor renames a product, the name in nymea can be aligned without causing issues on existing setups. The name will update for the user but all settings will continue to work as they are linked using the `id`, not the `name`. Worth noting that changing the name will require also the plugin code to be updated. 

* `displayName`: This name should reflect the `name` property but will be presented to the user when the user interacts with nymea. Because of this it should be nicely formatted to match the vendor / device / service name as close as possible, including whitespaces and special characters. Also, this property can be localized to the users language.
    
## Type properties

### Type

As the plugin JSON file defines how the system will interact with a thing, it often will need to define data types to be used when exchanging data. Like identification properties, those type properties can appear at various places in the file but they will always follow the same structure:

    {
        ...
        "type": <string>,
        ...
    }
    
The `type` field defines the actual data type to be used. The value for this field can be one of: 
* `bool`: For boolean (true/false) data types.
* `int`: For integer number data types.
* `uint`: For unsigned integer data types.
* `double`: For floating point data types.
* `QString`: For character strings.
* `QColor`: For color types. Can be either #RRGGBB, #AARRGGBB or a svg color scheme name such as `red`.
* `QStringList` For list types.

### Unit

### Input type

## Parameters

Many entities can have parameters. Parameters are options that can be modified by the user and change the behavior of a certain entity. Those parameters are defined in the JSON file by adding `paramTypes` definitions. Those definitions look like this:

    "paramTypes: [
        {
            "id": <uuid>,
            "name": <string>,
            "displayName": <string>,
            "type": <type>,
            "unit": <string>,
            "inputType": <string>,
            "defaultValue": <value>,
            "minValue": <value>,
            "maxValue": <value>,
            "allowedValues": <list of values>
        },
        ...
    ]

Required properties:

* `id`: See [Identification properties](#identification-properties)
* `name`: See [Identification properties](#identification-properties)
* `displayName`: See [Identification properties](#identification-properties)
* `type`: See [Type properties](#type-properties)
* `defaultValue`: The default value for this paramter. Depending on the type, this might be a number, a string, a color etc.

Optional properties:

* `minValue`: The minimum value for this parameter. This is only applicable to number paramter types, such as `int`, `uint` and `double`.
* `maxValue`: The maximum value for this parameter. This is only applicable to number parameter types.
* `allowedValues`: A list of allowed values the user can assign to this parameter.

## Plugin information

The contents of the plugin JSON file is a json object. This JSON object contains some information about the plugin itself.

    {
        "id": <uuid>,
        "name: <string>
        "displayName": <string>,
        ...
    }
    
The information about a plugin consists of an `id`, a `name` and a `displayName`. Those should be filled in by the plugin developer as described above. For instance, an integration plugin that adds support for various online services might use something like this:

    {
        "id": "35fb22d3-e4f0-4bbf-85d1-d7531111cacd",
        "name: "onlineServices",
        "displayName": "Online services,
        ...
    }

## Vendor information

## Thing classes

    {
        "id": <uuid>,
        "name": <string>,
        "displayName": <string>,
        "paramTypes": <list of param types>
        "settingsTypes": <list of param types>
        "createMethods": <list of strings>,
        "setupMethod": <string>,
        "discoveryParamTypes": <list of param types>,
        "interfaces": <list of string>,
        "browsable": <bool>,
        "eventTypes": <list of event types>,
        "stateTypes": <list of state types>,
        "actionTypes": <list of action types>,
        "browsable": <bool>,
        "browserItemActionTypes>: <list of action types>
    }

Required:

* `id`: See [Identification properties](#identification-properties)
* `name`: See [Identification properties](#identification-properties)
* `displayName`: See [Identification properties](#identification-properties)

Optional:

* `paramTypes`: Parameters to be used when setting up a thing. For example, this could be a parameter for an IP address for a device. See [Parameters](#parameters) for their definition. Parameters cannot be changed by the user at run time, only when setting up or reconfiguring a thing.
* `settingsTypes`: Settings for a thing. Settings can be changed by the user at run time. For example, this could be a timeout or refresh rate setting for a thing. See [Parameters](#parameters) for their definition.
* `createMethods`: Defines how a thing of this thing class can be created. See [Create methods](#create-methods) for more details.
* `discoveryParamTypes`: Only applicable if `createMethods` includes `CreateMethodDiscovery`. See [Create methods](#create-methods) for more details.
* `setupMethod`: Defines how a thing of this thing class is set up. See [Setup method](#setup-method) for more details.
* `interfaces`: A list of interfaces a certain thing class implements. For instance, a wifi light bulb would use `"interfaces: ["light", "connectable"]` to indicate to the system that it can control a light and indicate whether it is connected or not. See [Interfaces](docs/plugins/interfaces) for more information on interfaces. Note that adding interfaces here will require this thing class to also provide other properties as required by the interfaces used.
* `browsable`: A boolean value. Set this to `true` if the thing can be browsed. Defaults to `false`.
* `eventTypes`
* `stateTypes`
* `actionTypes`
* `browsable`
* `browserItemActionTypes`

### Create methods

### Setup method

### Events

### States

### Actions

### Browsing
