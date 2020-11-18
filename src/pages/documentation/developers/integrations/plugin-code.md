---
id: plugin-code
title: The plugin code
---

<script>
    import Code from '../../../../_components/Code.svelte';
</script>

Once a [plugin JSON](plugin-json) file is created, the according logic is to be implemented in the plugin code. The plugin code can be created in different programming languages. Currently supported are C++/Qt, Python and JavaScript.

This section assumes that you already have the basic plugin file structure in place either by having created a new plugin using the instructions in [creating a new plugin](creating-a-new-plugin) or by cloning and editing an existing plugin.

## A word on the environment

### C++/Qt

C++/Qt plugins are loaded by nymea using [QPluginLoader](https://doc.qt.io/qt-5/qpluginloader.html). This means, they will be executed within the nymea process and will be able to make it crash. As nymea is a long running process, care must be taken to not leak memory or crash by accessing invalid memory.

Plugins are not threaded by default. This means a plugin developer must not use blocking code. There is, however, the Qt event loop, all Qt API and the nymea hardware manager API available which caters for writing event loop based asynchronous code. If for any reason blocking code must be used, a plugin developer must spawn and manage their own threads.

A plugin may link to any C/C++/Qt library but please note that for inclusion of a plugin into the nymea plugin repository, all dependencies must be available in all the supported Ubuntu and Debian versions. In some exceptions it is possible to host dependencies in the nymea package repository too.

### Python

Each Python plugin is ran in a sub-interpreter allocated explicitly for the plugin. The Python version depends on the target distribution a nymea instance is build for, it is greater 3.5 in any case though.

In addition to that, every plugin gets its own thread pool allocated with a maximum thread count matching the amount of managed things + 2. Every function call into a plugin runs in a separate thread, however, if the thread pool is exhausted, calls will be queued and may time out. This means that is is possible to run blocking code in python (e.g. fetch a url using urllib) but this still must be used with caution as it might exceed the thread pool when multiple long running blocking calls are made.

Python plugins may use asyncio. The recommended way is to call `loop.run_forever()` in the plugins `init()` function and call `loop.stop()` in the plugins `deinit()` function. In this case, the asyncio event loop will use one of the plugins allocated threads. Other calls into the plugin should then just use `asyncio.run_coroutine_threadsafe(coro, loop)` to add their tasks to the event loop.

Additional threads may be started by a Python plugin using the `threading` module but note that the plugin is responsible for managing that thread and bringing it down on system shutdown.

A plugin may import any additional Python modules. For inclusion of a plugin into the nymea plugin repository, all dependencies must be satisfyable by `pip3` or need to be shipped with the plugin code.

> Note: Python modules installed system wide (e.g. in `dist-packages` or `site-packages`) are *NOT* loaded.

The `modules` subdir in the plugins code directory will be available as import path. `pip3` may be used in the plugin source dir to install additional modules locally during development:

```Bash
$ pip3 install somemodule -t modules
```

For inclusion in the nymea-plugins repository, specify any additional modules in a `requirements.txt` file. Note that nymea will require
hashes and fixed package versions. In order to easily add a module including version and hashes, the tool `hashin` may be used:

```Bash
# Install hashin
$ sudo pip3 install hashin

# Create an empty requirements.txt file if it hasn't been create before
S touch requirements.txt

# Add "somemodule" to the requirements.txt file
$ hashin somemodule
```
Nymea will then take care of installing required dependencies.


### JavaScript

Each JavaScript plugin is ran in a separate JS engine. The JS engine is ECMA-5 compliant but does not support node.js nor has a browsers `window` object.

Additional `.mjs` modules may be imported by installing them in the plugins source code and shipping them with the plugin.

## Introduction

The main entry point for the plugin code is typically located in a file with the same name as the [plugin JSON](plugin-json) file but using the typical filename extension for the chosen programming language. For a C++/Qt plugin this is `.h`/`.cpp`, for a Python plugin `.py` and JavaScript plugin it is `.js`.

> Note: While for C++/Qt plugins the file name is only recommended, for Python and JavaScript plugins it is a requirement for the file to be named like the json file.

The basic structure of the plugin code will look similar to this:

<Code>

```C++
// integrationpluginexample.h

#ifndef INTEGRATIONPLUGINEXAMPLE_H
#define INTEGRATIONPLUGINEXAMPLE_H

#include "integrations/integrationplugin.h"

class IntegrationPluginExample: public IntegrationPlugin
{
    Q_OBJECT
    Q_PLUGIN_METADATA(IID "io.nymea.IntegrationPlugin" FILE "integrationpluginexample.json")
    Q_INTERFACES(IntegrationPlugin)

public:
    explicit ThingPluginExample();
    void setupThing(ThingSetupInfo *info) override;
    void executeAction(ThingActionInfo *info) override;
    void thingRemoved(Thing *thing) override;
};

#endif // INTEGRATIONPLUGINEXAMPLE_H

// integrationpluginexample.cpp

#include "integrationpluginexample.h"
#include "plugininfo.h"

IntegrationPluginExample::IntegrationPluginExample() { }

void  IntegrationPluginExample::setupThing(ThingSetupInfo *info) {
    qCDebug(dcExample()) << "setupThing called for" << info->thing()->name() << info->thing()->params();
    // Perform required setup here
    info->thing()->setStateValue(exampleConnectedStateTypeId, true);
    info->finish(Thing::ThingErrorNoError);
}

void IntegrationPluginExample::executeAction(ThingActionInfo *info) {
    qCDebug(dcExample()) << "executeAction called for thing" << info->thing()->name() << info->action().actionTypeId() << action.params();
    // Perform action execution here
    info->finish(Thing::ThingErrorNoError);
}

void IntegrationPluginExample::thingRemoved(Thing *thing) {
    qCDebug(dcExample()) << "removeThing called for" << thing->name();
    // Clean up all data related to this thing
}

```

```Python
# integrationpluginexample.py

import nymea

def setupThing(info):
    logger.log("setupThing called for", info.thing.name)
    # Perform required setup here
    info.thing.setStateValue(exampleConnectedStateTypeId, True)
    info.finish(nymea.ThingErrorNoError)

    
def executeAction(info):
    logger.log("executeAction called for thing", info.thing.name, info.actionTypeId, info.params)
    # Perform action executio here
    info.finish(nymea.ThingErrorNoError)
    
    
def thingRemoved(thing):
    logger.log("removeThing called for", thing.name)
    # Clean up all data related to this thing
```

```JavaScript
// integrationpluginexample.js

export function setupThing(info) {
    console.log("setupThing called for", info.thing.name);
    // Perform required setup here
    info.thing.setStateValue(exampleConnectedStateTypeId, true);
    info.finish(Thing.ThingErrorNoError);
}

export function executeAction(info) {
    console.log("executeAction called for thing", info.thing.name, info.action.actionTypeId, info.action.params);
    // Perform action execution here
    info.finish(Thing.ThingErrorNoError);
}

export function thingRemoved(thing) {
    console.log("removeThing called for", thing.name);
    // Clean up all data related to this thing
}
```

</Code>


This is a minimalistic example for a plugin. While there are lots of other methods that a plugin can implement, this is the bare minimum the average plugin will need. <!-- For the complete reference of the integration plugin API use this [link TODO!!!!!](). -->

## IDs and names

As described in the [getting started](getting-started-integration) section, every entity in a plugin is referenced by an ID and a name. A plugin can use the IDs as defined in the JSON file to identify those entities, however, this is discouraged for the sake of readability. Instead, nymea will provide definitions to those IDs in a more readable manner to the developer.

> In C++/Qt plugins, those definitions are defined in the plugininfo.h header file which can be included in the plugin code. Note that this file can only be included once per plugin. If you need to access those definitions in multiple source files, include extern-plugininfo.h and re-run qmake.

> In Python plugins, those definitions are added by the interpreter as string constants to the plugin module.

> In JavaScript plugins, those definitions are exported to the global object of the plugins JS engine.

Those definitions are generated using the following scheme:

| Entity | Definion | Example |
| :-- | :-- | :-- |
| Vendor ID | *name* + VendorId | acmeVendorId |
| ThingClass ID | *name* + ThingClassId | robotThingClassId
| ThingClass paramType ID | *thingClass* + Thing + *name* + ParamTypeId | robotThingNameParamTypeId |
| SettingsType ID | *thingClass* + Settings + *name* + ParamTypeId | robotSettingsSpeedParamTypeId |
| Discovery ParamType ID | *thingClass* + Discovery + *name* + ParamTypeId | robotDiscoveryLanguageParamTypeId |
| EventType ID | *thingClass* + *name* + EventTypeId | robotBlinkedEventTypeId |
| Event ParamType ID | *thingClass* + *event* + Event + *name* + ParamTypeId | robotBlinkedEventColorParamTypeId |
| StateType ID | *thingClass* + *name* + StateTypeId | robotConnectedStateTypeId |
| ActionType ID | *thingClass* + *name* + ActionTypeId | robotSleepActionTypeId |
| Action ParamType ID | *thingClass* + *action* + Action + *name* + ParamTypeId | robotSleepActionDurationParamTypeId |


Let's look at a fictional example for a thing class describing a robot. The first tab contains the JSON definition for the plugin, the other tabs contain the generated definitions for the according programming language.

<Code>

```JSON
// JSON definition
{
    "vendors": [
        {
            "id": "ce0d15dc-c479-438d-adb3-90d57e4b1d35",
            "name": "acme",
            "thingClasses": [
                {
                    "id": "bd2157e3-2f9c-44a5-9d08-e2da2f6aa46f",
                    "name": "robot",
                    "paramTypes": [
                        {
                            "id": "eb6eeef7-f295-427b-b88f-01bedba49da7",
                            "name": "name"
                        }
                    ],
                    "settingsTypes": [
                        {
                            "id": "b8b4aefc-e6d6-47d7-b689-35d86d79f1fc",
                            "name": "speed"
                        }
                    ],
                    "discoveryParamTypes": [
                        {
                            "id": "df487d2d-dea6-45ac-907c-01b4fae4fd9b",
                            "name": "language"
                        }
                    ],
                    "eventTypes": [
                        {
                            "id": "e0581e22-81ca-4d43-bb0b-6e57312a33e4",
                            "name": "blinked",
                            "paramTypes": [
                                {
                                    "id": "adff8dbc-db5c-4c5d-9a57-9628dfa0a7e8",
                                    "name": "color"
                                }
                            ]
                        }
                    ],
                    "stateTypes": [
                        {
                            "id": "66730571-2776-4187-b29f-d745609353cd",
                            "name": "connected"
                        }
                    ],
                    "actionTypes": [
                        {
                            "id": "33f01f72-80b4-42cf-bdbd-a3439ce8236b",
                            "name": "sleep",
                            "paramTypes": [
                                {
                                    "id": "0170952a-260a-44be-972c-cc34f8bc8f67",
                                    "name": "duration"
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}
```

```C++
// In plugininfo.h

VendorId acmeVendorId = VendorId("ce0d15dc-c479-438d-adb3-90d57e4b1d35");
ThingClassId robotThingClassId = ThingClassId("bd2157e3-2f9c-44a5-9d08-e2da2f6aa46f");
ParamTypeId robotThingNameParamTypeId = ParamTypeId("eb6eeef7-f295-427b-b88f-01bedba49da7");
ParamTypeId robotSettingsSpeedParamTypeId = ParamTypeId("b8b4aefc-e6d6-47d7-b689-35d86d79f1fc");
ParamTypeId robotDiscoveryLanguageParamTypeId = ParamTypeId("df487d2d-dea6-45ac-907c-01b4fae4fd9b");
EventTypeId robotBlinkedEventTypeId = EventTypeId("e0581e22-81ca-4d43-bb0b-6e57312a33e4");
ParamTypeId robotBlinkedEventColorParamTypeId = ParamTypeId("adff8dbc-db5c-4c5d-9a57-9628dfa0a7e8");
StateTypeId robotConnectedStateTypeId = StateTypeId("66730571-2776-4187-b29f-d745609353cd");
ActionTypeId robotSleepActionTypeId = ActionTypeId("33f01f72-80b4-42cf-bdbd-a3439ce8236b");
ParamTypeId robotSleepActionDurationParamTypeId = ParamTypeId("0170952a-260a-44be-972c-cc34f8bc8f67");
```

```Python
# Exported by the interpreter into the plugin module

acmeVendorId = "ce0d15dc-c479-438d-adb3-90d57e4b1d35";
robotThingClassId = "bd2157e3-2f9c-44a5-9d08-e2da2f6aa46f";
robotThingNameParamTypeId = "eb6eeef7-f295-427b-b88f-01bedba49da7";
robotSettingsSpeedParamTypeId = "b8b4aefc-e6d6-47d7-b689-35d86d79f1fc";
robotDiscoveryLanguageParamTypeId = "df487d2d-dea6-45ac-907c-01b4fae4fd9b";
robotBlinkedEventTypeId = "e0581e22-81ca-4d43-bb0b-6e57312a33e4";
robotBlinkedEventColorParamTypeId = "adff8dbc-db5c-4c5d-9a57-9628dfa0a7e8";
robotConnectedStateTypeId = "66730571-2776-4187-b29f-d745609353cd";
robotSleepActionTypeId = "33f01f72-80b4-42cf-bdbd-a3439ce8236b";
robotSleepActionDurationParamTypeId = "0170952a-260a-44be-972c-cc34f8bc8f67";

```

```JavaScript
// Exported in the engines global object

var acmeVendorId = "ce0d15dc-c479-438d-adb3-90d57e4b1d35";
var robotThingClassId = "bd2157e3-2f9c-44a5-9d08-e2da2f6aa46f";
var robotThingNameParamTypeId = "eb6eeef7-f295-427b-b88f-01bedba49da7";
var robotSettingsSpeedParamTypeId = "b8b4aefc-e6d6-47d7-b689-35d86d79f1fc";
var robotDiscoveryLanguageParamTypeId = "df487d2d-dea6-45ac-907c-01b4fae4fd9b";
var robotBlinkedEventTypeId = "e0581e22-81ca-4d43-bb0b-6e57312a33e4";
var robotBlinkedEventColorParamTypeId = "adff8dbc-db5c-4c5d-9a57-9628dfa0a7e8";
var robotConnectedStateTypeId = "66730571-2776-4187-b29f-d745609353cd";
var robotSleepActionTypeId = "33f01f72-80b4-42cf-bdbd-a3439ce8236b";
var robotSleepActionDurationParamTypeId = "0170952a-260a-44be-972c-cc34f8bc8f67";

```

</Code>


## Setup

The most important method is probably `setupThing()`. This is called when a new thing is configured in the system, as well as on system startup. This method should do all the required stuff to connect to the thing. The `info` parameter will contain all the information for the newly set up thing. Once the connection to the device or online service has been established, the plugin code must call the `finish()` method on the info object. Please note, that there is a timeout in place which will cause the setup to time out eventually if `finish()` is not called. A plugin implementation can react on this by connecting to the `aborted()` signal of the info object.

A more complete example for a setup implementation might look like the following snipped where a plugin sets up a fictional device on the local network by probing its REST API.

<Code>

```C++
void  IntegrationPluginExample::setupThing(ThingSetupInfo *info) {
    // Obtain the devices IP as given by the params
    QString deviceIp = info->thing()->paramValue(exampleThingIpParamTypeId).toString();
    
    // Start a network request
    QNetworkRequest request("http://" + deviceIp + "/api");
    QNetworkReply *reply = hardwareManager()->networkAccessManager()->get(request);

    // Clean up the reply object when it finishes
    connect(reply, &QNetworkReply::finished, reply, &QNetworkReply::deleteLater);
    
    // Process the network request result if it returns before "info" is destroyed
    connect(reply, &QNetworkReply::finished, info, [info, reply](){
        QByteArray data = reply->readAll();
        // Finish the setup with an appropriate result code
        if (data == "OK") {
            info->finish(Thing::ThingErrorNoError);
            info->thing()->setStateValue(exampleConnectedStateTypeId, true);
        } else {
            info->finish(Thing::ThingErrorHarwareFailure, QT_TR_NOOP("Error connecting to the device in the network."));
        }
    });
    
    // If needed, do some cleanup when the setup is aborted
    connect(info, &ThingSetupInfo::aborted, this, [](){
        qCDebug(dcExample) << "Setup timed out...";
    });
}
```

```Python
from urllib.request import urlopen, Request

def setupThing(info):
    # Obtain the devices IP as given by the params
    deviceIp = info.thing.paramValue(exampleThingIpParamTypeId)
    
    # Compose the network request
    request = Request("https://" + deviceIp + "/api")
    # Send the request
    response = urlopen(request)        
    
    # Finish the setup with an appropriate result code
    if response.status == "OK":
        info.finish(nymea.ThingErrorNoError)
    else:
        info.finish(nymea.ThingErrorHarwareFailure, "Error connecting to the device in the network.");
        
```

```JavaScript
export function setupThing(info) {
    // Obtain the devices IP as given by the params
    var deviceIp = info.thing.paramValue(exampleThingIpParamTypeId);
    
    // Compose the network request
    var request = new XMLHttpRequest()
    request.open("GET", "https://" + deviceIp + "/api");

    // Create a handler function for processing the network reply
    request.onload = function() {
        var response = JSON.parse(request.response);
        
        // Finish the setup with an appropriate result code
        if (response.status == "OK") {
            info.finish(Thing.ThingErrorNoError);
        } else {
            info.finish(Thing.ThingErrorHarwareFailure, QT_TR_NOOP("Error connecting to the device in the network."));
        }
    }
    
    // Send the network request
    request.send();
    
    // Clean up/cancel when the setup is aborted
    info.aborted.connect(function() {
        console.log("Setup timed out...");
        request.abort();
    });
}
```

</Code>

In this example a HTTP GET call to a REST API on a device would be made. The IP adress is obtained from the thing parameters (NOTE: those must be defined in the plugin's JSON file). Once the network request returns, a lambda function is executed which reads the responses payload of the GET call and if everything is as expected it calls `finish()` on the setup info object providing the `ThingErrorNoError` status code. If something has gone wrong, it'll call `finish()` but with a different error code, in this case `ThingErrorHarwareFailure` to indicate the failure to the system. If the setup times out before the GET call returns or the user cancels the setup, the `info` object will emit its `aborted` signal and destroyed.

> Note: The info object must not be accessed after it is finished or aborted. Depending on the language this will result in crashes or undefined behavior.

## Settings

Thing settings are very similar to the params used during setup, however, they can change at runtime without having to reconfigure a thing. For that, the plugin should connect to the things `settingChanged()` signal which will provide the `paramTypeId` and `value` for the changed setting and handle it accordingly.

The following example handles the settings for a Bluetooth sensor which is polled according to an interval setting.

<Code>

```C++
void IntegrationPluginExample::setupThing(ThingSetupInfo *info) {
    // Do thing setup
    ...
    
    // Update refresh schedule when the refresh rate setting is changed
    connect(thing, &Thing::settingChanged, this, [this] (const ParamTypeId &paramTypeId, const QVariant &value) {
        if (paramTypeId == myCoolDeviceSettingRefreshIntervalParamTypeId) {
            qCDebug(dcExample) << "Polling interval changed to" << value.toInt() << "minutes";
            // Reschedule polling timer here
            ...
        }
    });
}
```

```Python
def setupThing(info):
    # Do thing setup
    ...
    
    # Update refresh schedule when the refresh rate setting is changed    
    info.thing.settingChangedHandler = thingSettingCanged
    
    
def thingSettingChanged(thing, paramTypeId, value):
    if  paramTypeId == myCoolDeviceSettingRefreshIntervalParamTypeId:
        logger.log("Polling interval changed to", value, minutes)
        # Reschedule polling timer here
```

```JavaScript
export function setupThing(info) {
    // Do thing setup
    ...
    
    // Update refresh schedule when the refresh rate setting is changed
    info.thing.settingChanged.connect(function() {
        if (paramTypeId == myCoolDeviceSettingRefreshIntervalParamTypeId) {
            console.log("Polling interval changed to", value, "minutes");
            // Reschedule polling timer here
            ...
        }
    });
}
```

</Code>

## Actions

Whenever the user (or some automatism) executes an action in the system, nymea will call `executeAction` on the plugin. The `info` parameter will contain all the required information to process the request. That contains information about the thing as well as the action. Let's have a look at an example switching on/off a device using a POST call on its REST API.

<Code>

```C++
void IntegrationPluginExample::executeAction(ThingActionInfo *info) {
    // Obtain the devices IP as given by the params
    QString deviceIp = info->thing()->paramValue(exampleThingIpParamTypeId).toString();
        
    // Handle the power action
    if (info->action().actionTypeId() == examplePowerActionTypeId) {
        
        // Obtain the parameter of this action
        bool power = info->action().paramValue(examplePowerActionPowerParamTypeId).toBool();
        
        // Compose the network request
        QByteArray payload = power ? "on" : "off";
        QNetworkRequest request("http://" + deviceIp + "/api/power");
        
        // Send the request
        QNetworkReply *reply = hardwareManager()->networkAccessManager()->post(request, payload);

        // Clean up the reply object when it finishes
        connect(reply, &QNetworkReply::finished, reply, &QNetworkReply::deleteLater);

        // Process the network request result if it returns before "info" is destroyed
        connect(reply, &QNetworkReply::finished, info, [info, reply, power](){
            QByteArray data = reply->readAll();
        
            // Finish the action with an appropriate result code
            if (data == "OK") {
                info->finish(Thing::ThingErrorNoError);
                // Update the things power state accordingly
                info->thing()->setStateValue(examplePowerStateTypeId, power);
            } else {
                info->finish(Thing::ThingErrorHarwareFailure, QT_TR_NOOP("Error sending command to network device.");
            }
        });
    } else {
        // Handle other actions...
        ...
    }
}
```

```Python
def executeAction(info):
    # Obtain the devices IP as given by the params
    deviceIp = info.thing.paramValue(exampleThingIpParamTypeId)
    
    # Handle power action
    if info.actionTypeId == examplePowerActionTypeId:

        // Obtain the parameter of this action
        power = info.paramValue(examplePowerActionPowerParamTypeId)
    
    # Compose the network request
    payload = power == True ? "on": "off"
    request = Request("https://" + deviceIp + "/api", data = payload)
    # Send the request
    response = urlopen(request)        
    
    # Finish the action with an appropriate result code
    if response.status == "OK":
        info.finish(nymea.ThingErrorNoError)
    else:
        info.finish(nymea.ThingErrorHarwareFailure, "Error command to the network device.");

```

```JavaScript
export function executeAction(info) {
    // Obtain the devices IP as given by the params
    var deviceIp = info.thing.paramValue(exampleThingIpParamTypeId);

    // Handle the power action
    if (info.actionTypeId() == examplePowerActionTypeId) {

        // Obtain the parameter of this action
        var power = info.paramValue(examplePowerActionPowerParamTypeId);

        // Compose the network request
        var payload = power === true ? "on" : "off";
        var request = new XMLHttpRequest()
        request.open("POST", "https://" + deviceIp + "/api");
        
        // Create a handler function for processing the network reply
        request.onload = function() {
            var response = JSON.parse(request.response);

            // Finish the action with an appropriate result code
            if (response.status == "OK") {
                // Update the things power state accordingly
                info.thing.setStateValue(examplePowerStateTypeId, power);
                info.finish(Thing.ThingErrorNoError);
            } else {
                info.finish(Thing.ThingErrorHarwareFailure, QT_TR_NOOP("Error sending command to network device."));
            }
        }

        // Send the request
        request.send(payload);
        
        // Cancel the request if the action is aborted
        info.aborted.connect(function() {
            request.abort();
        })
    } else {
        // Handle other actions...
    }
}
```
</Code>

Again, we're obtaining the devices IP using the thing parameters, just like in `setupThing()`. In addition, we're checking out which action it is. Once we know which action it is (in this case the "power" action) we can obtain the parameters for it by calling `paramValue()` providing the param type ID we're interested in. Like in the setupThing example we're constructing a HTTP call, in this case a POST one and will be sending it to the network. The handler function for the network reply will again report the status of the execution in the `finish()` call.

There's one more thing to note: If this action is an action that changes a things state, the plugin implementation should also update the things state value accordingly. See the [states section](#states) for more information how to manipulate states.

## Events

Whenever a thing is triggering an event, for instance a button on a device is pressed, or a trigger is happening on an online service, the plugin implementation should call a things `emitEvent()` function, passing the information about the event.

Let's look at an example that would poll an online service for such triggers.

<Code>

```C++
void IntegrationPluginExample::setupThing(ThingSetupInfo *info) {
    // Doing the regular setup first...
    ...
    
    // And set up the polling
    Thing *thing = info->thing();
    m_pluginTimer = hardwareManager()->pluginTimerManager()->registerTimer(1);
    connect(m_pluginTimer, &PluginTimer::timeout, thing, [this, thing](){
        
        QNetworkRequest request("https://example.com/api");
        QNetworkReply *reply = hardwareManager()->networkAccessManager()->get(request);
        
        connect(reply, &QNetworkReply::finished, reply, &QNetworkReply::deleteLater);

        connect(reply, &QNetworkReply::finished, thing, [thing, reply](){
            QByteArray data = reply->readAll();
        
            if (data == "eventHappened") {
                // When appropriate, compose an event and emit it in the system
                Event event(exampleEventTypeId, thing->id());
                emitEvent(event);
            }
        });
    });
}

void IntegrationPlugin::thingRemoved(Thing *thing) {
    // Unregister the timer when the thing is removed
    hardwareManager()->pluginTimerManager()->unregisterTimer(m_pluginTimer);
}
```

```Python
# We'll be using threading.timers to do repeating polling in this example
import threading
timer = None

def setupThing(info):
    # Doing the regular setup first...
    ...
    
    # And set up the polling
    global timer
    timer = threading.Timer(10, pollService, [info.thing])
    timer.start()
    info.finish(nymea.ThingErrorNoError)
    
    
def pollService(thing):
    request = Request("https://" + deviceIp + "/api")
    response = urlopen(request)        
    if response.data == "eventHappened":
        # When appropriate, compose an event and emit it in the system
       thing.emitEvent(exampleEventTypeId)

        
def thingRemoved(thing):
    # Stop the timer thread when the thing is removed
    global timer
    timer.cancel()
    
    
def deinit():
    # Also make sure to stop all threads on shutdown
    global timer
    timer.cancel()
```

```JavaScript
var pluginTimer;

export function setupThing(info) {
    // Doing the regular setup first...
    ...
    
    // And set up the polling
    var thing = info.thing;
    pluginTimer = hardwareManager.pluginTimerManager.registerTimer(5);
    pluginTimer.timeout.connect(function() {
    
        var request = new XMLHttpRequest()
        request.open("GET", "https://" + deviceIp + "/api");
        request.onload = function() {
            if (request.response == "eventHappened") {
                // When appropriate, compose an event and emit it in the system
                emitEvent(thing.id, exampleEventTypeId, []);
            }
        }
        request.send();
    })
}

export function thingRemoved(thing) {
    // Unregister the timer when the thing is removed
    hardwareManager.pluginTimerManager.unregisterTimer(pluginTimer);
}
```

</Code>
    
In `setupThing()` we're doing the regular setup first. If that succeeds, the plugin is registering a timer which whill emit the `timeout()` signal every second. Connected to this timeout signal of the timer, the plugin will poll an online API. If the response of that polling operation contains data that indicates the happening of an event, the plugin constructs an `Event` with the required data. In this case it will contain the event type id which as usual has been defined in the plugin's JSON. In addition to that, it will contain the ID of the thing this event is for. The event could also have additional parameters but in this example we're omitting that for simplicity. Finally, the plugin calls `emitEvent()` to indicate the event to the system.

One more thing to notice here is that the registering of a timer will require the plugin also to unregister it again when it's not needed any more. For that it uses the `thingRemoved()` method.

## States

States are handled very similar to events. But instead of creating an Event object, the plugin would call `thing->setStateValue()`. Let's look at an example that would poll the current temperature from some online API.

<Code>

```C++
void IntegrationPluginExample::setupThing(ThingSetupInfo *info) {
    // Doing the regular setup first...
    ...
    
    // And set up the polling
    m_pluginTimer = hardwareManager()->pluginTimerManager()->registerTimer(1);
    
    Thing *thing = info->thing();
    connect(m_pluginTimer, &PluginTimer::timeout, thing, [this, thing](){
        
        QNetworkRequest request("https://example.com/api/temperature");
        QNetworkReply *reply = hardwareManager()->networkAccessManager()->get(request);
        
        connect(reply, &QNetworkReply::finished, reply, &QNetworkReply::deleteLater);

        connect(reply, &QNetworkReply::finished, thing, [thing, reply](){
            QByteArray data = reply->readAll();
            int temperature = data.toInt();
            
            // Update the things state value accordingly
            thing->setStateValue(temperatureStateTypeId, temperature);
        });
    });
}
```

```Python

def setupThing(info):
    # Doung the regular setup first...
    ...
    
    # And set up the polling
    threading.Timer(10, pollService, [info.thing])
    info.finish(nymea.ThingErrorNoError)

def pollService:
    request = Request("https://" + deviceIp + "/api")
    response = urlopen(request)        
    temperature = int(response.data)
    # Update the things state value accordingly
    thing.setStateValue(temperatureStateTypeId, temperature):
    
```

```JavaScript
var pluginTimer;

export function setupDevice(info) {
    // Doing the regular setup first...
    ...
    
    // And set up the polling
    var thing = info.thing;
    pluginTimer = hardwareManager.pluginTimerManager.registerTimer(1);
    
    pluginTimer.timeout.connect(function(){
        
        var request = new XMLHttpRequest()

        request.open("GET", "https://example.com/api/temperature");
        request.onload = function() {
            var temperature = request.response;

            // Update the things state value accordingly
            thing.setStateValue(temperatureStateTypeId, temperature)
        }
        request.send();
    });
}
```

</Code>

Also this example would poll the API every second. Whenever the reply comes back, it'll set the things state value using the id for the temperature state which is defined in the plugin's JSON file and the actual new value.

## Discovery

For things that can be discovered (either in the local network or on the internet) will use a `createMethod` of `CreateMethodDiscovery` in the plugin's JSON file. For such things, nymea will call `discoverThings()` on the plugin. For this, an integration plugin must implement that method and deliver discovery results back to the system. Similar as to the setup, an info object is passed to the method which is used to report results and indicate progress.

A plugin implementation shall use `addThingDescriptor()` of the discovery info object in order to add newly discovered things to the results and as usual call `finish()` with the appropriate status code on it when done.

One important note is that such a discovery should report all the found things, even those that are already added to the system but it is important to mark them as such. This is done by setting the ThingId of the existing thing on the ThingDescriptor.


<Code>

```C++
void IntegrationPluginExample::discoverThings(ThingDiscoveryInfo *info)
{
    // In this example we'd be looking for devices in the local network via ZeroConf:
    ZeroConfServiceBrowser *zeroconfBrowser = hardwareManager()->zeroConfController()->createServiceBrowser("_http._tcp");

    // Walk through all the found entries on the zeroconf browser
    foreach (const ZeroConfServiceEntry &entry, zeroconfBrowser->serviceEntries()) {

        // Skip unrelated entries
        if (entry.name() != "MyCoolDevice") {
            continue;
        }

        // Create the ThingDescriptor and set the IP address to the params
        ThingDescriptor descriptor(info->thingClassId(), entry.name(), entry.hostAddress().toString());
        ParamList params;
        params << Param(myCoolDeviceThingIpParamTypeId, entry.hostAddress().toString());
        descriptor.setParams(params);

        // Let's see if we already have that device in the system. If so, set thingId accordingly to indicate that it's already known
        Thing *existingThing = myThings().findByParams(params);
        if (existingThing) {
            descriptor.setThingId(existingThing->id());
        }

        // Add the discovery result to the result list
        info->addThingDescriptor(descriptor);

    }

    // And tell the system when we're done.
    info->finish(Thing::ThingErrorNoError);
    
    // don't forget to delete the browser when finished
    delete zeroconfBrowser;
}
```

```Python
def discoverThings(info):
    # Discover things by scanning the network or quering an API etc...
    results = ...
    # Add all the discovery results to the info object
    for result in results:
        # Create a new ThingDescriptor
        descriptor = nymea.ThingDescriptor(exampleThingClassId, result.name, "Some more info"))
        # Set a unique ID for this discovery result in the params (Param type needs to be defined in the JSON file)
        descriptor.params = [nymea.Param(exampleThingIdParamTypeId, result.id)]
        # Check if we already have this thing in the system
        for existingThing in myThings():
            if existingThing.paramValue(exampleThingThingIdParamTypeId) == result.id:
                # If so, set the thingId so nymea can match this discovery result to the existing thing
                descriptor.thingId = existingThing.id

        # Add the new descriptor to the info object
        info.addDescriptor(descriptor)

    # Finish the discovery
    info.finish(nymea.ThingErrorNoError)

```

```JavaScript
export function discoverThings(info) {
    // Perform a discovery by scanning the network or quering an API etc...
    performDiscovery( (response) => {
        // Add all found results in the response to the info object
        for (var i = 0; i < response.length; i++) {
            // Add a unique ID to the params (paramTypeId needs to be definen in the plugin JSON)
            var params = [{paramTypeId: exampleThingIdParamTypeId, value: response[i].id}];
            info.addThingDescriptor(exampleThingClassId, response[i].name, "Some more info", params);
       };
       // Finish the discovery
       info.finish(Thing.ThingErrorNoError);
    });
}
```

</Code>

## Pairing

Often network devices or online services require a some sort of authentication, be it a simple username/password login, push button authentication or more complex sceanarios like OAuth. Nymea provides support for that by implementing a two step pairing procedure. Such a pairing always consists of of nymea calling `startPairing()` and `confirmPairing()` sequentially. As usual, an info object is passed to the methods. In this case a `ThingPairingInfo`.

The actual implementation of a plugin looks different depending on the used mechanism. In any case, each step must be finished by calling `info->finish()` reporting success or failure.

The plugin should store the credentials in the plugin storage.

### Username and Password authentication

Let's look at the simplest form of it which is username and password authentication.

The `startPairing()` call is pretty much a no-operation in this case. The only thing a plugin implementation can do here is to provide an informational text to the client.

<Code>

```C++
void IntegrationPluginExample::startPairing(ThingPairingInfo *info)
{
    info->finish(Thing::ThingErrorNoError, QT_TR_NOOP("Please enter the login credentials for your device."));
}
```

```Python
def startPairing(info):
    info.finish(nymea.ThingErrorNoError, "Please enter the login credentials for your device.");
```

```JavaScript
export function startPairing(info) {
    info.finish(Thing.ThingErrorNoError, "Please enter the login credentials for your device");
}
```

</Code>

This will advance the pairing process to the next step immediately, presenting the user with a login interface containing the above informational text. Make sure to use QT_TR_NOOP to wrap the text in order to allow nymea to translate the text to the client's language on the fly.

Once the user has inserted the credentials, nymea will pass them on to the plugin like here:

<Code>

```C++
void IntegrationPluginExample::confirmPairing(ThingPairingInfo *info, const QString &username, const QString &password)
{
    // Get the things connection parameters from the thing params.
    QString ipAddress = info->params().paramValue(m_ipAddressParamTypeIdMap.value(info->thingClassId())).toString();
    int port = info->params().paramValue(m_portParamTypeIdMap.value(info->thingClassId())).toInt();

    // Now let's compose a network request to the device and provide the given username and password in the request's Authorization header.
    QNetworkRequest request;
    request.setUrl(QUrl(QString("http://%1:%2/setup").arg(ipAddress).arg(port)));
    request.setRawHeader("Authorization", "Basic " + QString("%1:%2").arg(username).arg(password).toUtf8().toBase64());

    // Send the request
    QNetworkReply *reply = hardwareManager()->networkManager()->get(request);
    connect(reply, &QNetworkReply::finished, reply, &QNetworkReply::deleteLater);
    connect(reply, &QNetworkReply::finished, info, [this, info, reply, username, password](){
    
        // Upon success, store the username and password for later use
        if (reply->error() == QNetworkReply::NoError) {
            pluginStorage()->beginGroup(info->thingId().toString());
            pluginStorage()->setValue("username", username);
            pluginStorage()->setValue("password", password);
            pluginStorage()->endGroup();
            
            // And indicate success to the system by calling info->finish()
            info->finish(Thing::ThingErrorNoError);
        } else {
            // In case of failure, report that, optionally with a user friendly error message.
            info->finish(Thing::ThingErrorAuthenticationFailure, QT_TR_NOOP("Wrong username or password."));
        }
    });
}
```

```Python
def confirmPairing(info, username, secret):
    logger.log("confirming pairing for", info.thingName, username, secret)
    # Compose a request with the credentials set to test the API for a successful login
    request = Request("https://" + info.paramValue(exampleThingIPParamTypeId) + "/api")
    base64string = base64.b64encode('%s:%s' % (username, secret))
    request.add_header("Authorization", "Basic %s" % base64string)
    response = urlopen(request)
    # Finish the pairing procedure
    if response.data == "SUCCESS":
        info.finish(nymea.ThingErrorNoError)
    else:
        info.finish(nymea.ThingErrorAuthenticationFailure, "Error logging in!")
```

```JavaScript
export function confirmPairing(info, username, secret) {
    // Compose a request with the credentials set to test the API for a successful login

    var request = new XMLHttpRequest()
    request.open("GET", "https://" + info.paramValue(exampleThingIPParamTypeId) + "/api");
    req.setRequestHeader("Authorization", "Basic " + btoa(username + ":" + secret)); 
    request.onload = function() {
        // Update the things state value accordingly
        if (request.response == "SUCCESS") {
            info.finish(Thing.ThingErrorNoError)
        } else {
            info.finish(Thing.ThingErrorNoError, "Error logging in")
        }
    }
    request.send();
}
    
```

</Code>

### Push button authentication

This example would pair a device that uses push button authentication:

<Code>

```C++
void IntegrationPluginExample::startPairing(ThingPairingInfo *info)
{
    info->finish(Thing::ThingErrorNoError, QT_TR_NOOP("Please press the push button on the device and then continue this setup."));
}
```

```Python
def startPairing(info):
    info.finish(nymea.ThingErrorNoError, "Please press the push button on the device and then continue this setup.");
```

```JavaScript
export function startPairing(info) {
    info.finish(Thing.ThingErrorNoError, "Please press the push button on the device and then continue this setup.");
}
```

</Code>

Again, the `startPairing` call is mostly informative to the user. It tells the user to press the button on the device now and then continue the setup process in nymea.

Once done, nymea will call `confirmPairing` again. In this case neither the `username` nor the `password` arguements will contain meaningful data. Instead, the pairing key (normally a token) can be obtained directly from the device.

```C++
void IntegrationPluginExample::confirmPairing(ThingPairingInfo *info, const QString &username, const QString &secret)
{
    Q_UNUSED(username)
    Q_UNUSED(secret)

    // Obtain the connectivity information from the thing params
    QString host = info->params().paramValue(myCoolDeviceThingIpParamTypeId).toString();
    QNetworkRequest request(QUrl("http://" + host + "/api"));
    request.setHeader(QNetworkRequest::ContentTypeHeader, "application/json");
    
    // And send the network request to the device
    QNetworkReply *reply = hardwareManager()->networkManager()->post(request, jsonDoc.toJson());
    connect(reply, &QNetworkReply::finished, reply, &QNetworkReply::deleteLater);

    connect(reply, &QNetworkReply::finished, info, [this, info, reply](){

        // Check the response for errors
        if (reply->error() != QNetworkReply::NoError) {
            info->finish(Thing::ThingErrorHardwareFailure, QT_TR_NOOP("Error connecting to the device."));
            return;
        }
        QByteArray data = reply->readAll();
        if (data.isEmpty()) {
            qCWarning(dcExample) << "Failed to pair with device: did not get any key from the bridge";
            return info->finish(Thing::ThingErrorAuthenticationFailure, QT_TR_NOOP("The device has rejected the connection request."));
        }

        // All good. Store the API key
        pluginStorage()->beginGroup(info->thingId().toString());
        pluginStorage()->setValue("apiKey", data);
        pluginStorage()->endGroup();

        info->finish(Thing::ThingErrorNoError);
    });
}
```

### OAuth

OAuth is a little more complex than the previous examples, however, the basic flow is just the same. The ThingPairingInfo has a `oAuthUrl` property for that which is to be filled in in the `startPairing()` call. The user will then be redirected to this URL where a login mask will appear for the user to sign in. After a successful login, the remote server will return with a callback URL containing a PIN as URL query parameters. This callback URL will be passed on to the plugin developer in `confirmPairing()` in the `secret` parameter where the plugin can extract the PIN and complete the OAuth procedure.

This example shows the OAuth procedure for the google OAuth service. The plugin developer must obtain the clientId and clientSecret from the remote service, usually by signing up for a developer account. When registering for such a developer account, a callback URL must be provided. Nymea requires this callback url to start with "https://127.0.0.1". The rest of the callback URL is not relevant to nymea.

```C++
void IntegrationPluginExample::startPairing(ThingPairingInfo *info)
{
    // Those credentials need to be obtained from the service provider
    QString clientId= "937667874529-pr6s5ciu6sfnnqmt2sppvb6rokbkjjta.apps.googleusercontent.com";
    QString clientSecret = "1ByBRmNqaK08VC54eEVcnGf1";

    // Compose the OAuth redirect url. Make sure to start the callback/redirect URL with https://127.0.0.1
    QUrl url("https://accounts.google.com/o/oauth2/v2/auth");
    QUrlQuery queryParams;
    queryParams.addQueryItem("client_id", clientId);
    queryParams.addQueryItem("redirect_uri", "https://127.0.0.1:8888");
    queryParams.addQueryItem("response_type", "code");
    queryParams.addQueryItem("scope", "profile email");
    queryParams.addQueryItem("state", "ya-ya");
    url.setQuery(queryParams);

    // Set the OAuth url to the info object
    info->setOAuthUrl(url);

    // And finish the startPairing procedure
    info->finish(Thing::ThingErrorNoError);
}
```

When the client app completed the OAuth login the procedure continues with `confirmPairing()`

```C++
void IntegrationPluginExample::confirmPairing(ThingPairingInfo *info, const QString &username, const QString &secret)
{
    Q_UNUSED(username)
    // Extract the code from the callback URL
    QUrl url(secret);
    QUrlQuery query(url);
    QString accessCode = query.queryItemValue("code");

    // Compose the network request to obtain the access token from the remote server
    QString clientId = "937667874529-pr6s5ciu6sfnnqmt2sppvb6rokbkjjta.apps.googleusercontent.com";
    QString clientSecret = "1ByBRmNqaK08VC54eEVcnGf1";

    url = QUrl("https://www.googleapis.com/oauth2/v4/token");
    query.clear();
    query.addQueryItem("code", accessCode);
    query.addQueryItem("client_id", clientId);
    query.addQueryItem("client_secret", clientSecret);
    query.addQueryItem("grant_type", "authorization_code");
    query.addQueryItem("redirect_uri", QByteArray("https://127.0.0.1:8888").toPercentEncoding());
    url.setQuery(query);

    QNetworkRequest request(url);

    // Send the request
    QNetworkReply *reply = hardwareManager()->networkManager()->post(request, QByteArray());
    connect(reply, &QNetworkReply::finished, reply, &QNetworkReply::deleteLater);
    connect(reply, &QNetworkReply::finished, info, [this, reply, info](){

        QJsonDocument jsonDoc = QJsonDocument::fromJson(reply->readAll());

        // If successful, extract the tokens
        QByteArray accessToken = jsonDoc.toVariant().toMap().value("access_token").toByteArray();
        QDateTime expiryTime = QDateTime::currentDateTime().addSecs(jsonDoc.toVariant().toMap().value("expires_in").toInt());
        QByteArray refreshToken = jsonDoc.toVariant().toMap().value("refresh_token").toByteArray();
        QByteArray idToken = jsonDoc.toVariant().toMap().value("id_token").toByteArray();
        

        // Store things in the plugin storage
        pluginStorage()->beginGroup(info->thingId().toString());
        pluginStorage()->setValue("accessToken", accessToken);
        pluginStorage()->setValue("refreshToken", refreshToken);
        pluginStorage()->setValue("expiryTime", expeiryTime);
        pluginStorage()->setValue("idToken", idToken);
        pluginStorage()->endGroup();

        // And finish the procedure
        info->finish(Thing::ThingErrorNoError);
    });
}
```

### DisplayPin

Some devices are capable of displaying a PIN code. For example smart TVs. Those devices can be handled as following:

```C++
void IntegrationPluginExample::startPairing(ThingPairingInfo *info)
{
    // Compose a network request that would trigger displayig the PIN on the remote device
    QString host = info->params().paramValue(myCoolDeviceThingIpParamTypeId).toString();
    QNetworkRequest request(QUrl("http://" + host + "/displayPin"));

    // Send the request
    QNetworkReply *reply = hardwareManager()->networkManager()->post(request, QByteArray());
    connect(reply, &QNetworkReply::finished, reply, &QNetworkReply::deleteLater);
    connect(reply, &QNetworkReply::finished, info, [this, reply, info](){
    
        // Check the response for errors
        if (reply->error() != QNetworkReply::NoError) {
            info->finish(Thing::ThingErrorHardwareFailure, QT_TR_NOOP("Error connecting to the device."));
            return;
        }

        // And finish the startPairing procedure
        info->finish(Thing::ThingErrorNoError);
    }
}
```

The user is then asked to enter the PIN on the client app. Once that is completed, the plugin's `completePairing()` will be called. The PIN is provided in the `secret` parameter.

```C++
void IntegrationPluginExample::confirmPairing(ThingPairingInfo *info, const QString &username, const QString &secret)
{
    Q_UNUSED(username)

    // Obtain the connectivity information from the thing params
    QString host = info->params().paramValue(myCoolDeviceThingIpParamTypeId).toString();
    
    QUrl url("http://" + host + "/completePairing");
    QUrlQuery query;
    query.addQueryItem("pin", secret);
    url.setQuery(query);
    QNetworkRequest request(url);
    
    // And send the network request to the device
    QNetworkReply *reply = hardwareManager()->networkManager()->get(request);
    connect(reply, &QNetworkReply::finished, reply, &QNetworkReply::deleteLater);

    connect(reply, &QNetworkReply::finished, info, [this, info, reply](){

        // Check the response for errors
        if (reply->error() != QNetworkReply::NoError) {
            info->finish(Thing::ThingErrorHardwareFailure, QT_TR_NOOP("Error connecting to the device."));
            return;
        }
        QByteArray data = reply->readAll();
        if (data.isEmpty()) {
            qCWarning(dcExample) << "Failed to pair with device: did not get any key from the bridge";
            return info->finish(Thing::ThingErrorAuthenticationFailure, QT_TR_NOOP("The device has rejected the connection request."));
        }

        // All good. Store the API key
        pluginStorage()->beginGroup(info->thingId().toString());
        pluginStorage()->setValue("apiKey", data);
        pluginStorage()->endGroup();

        info->finish(Thing::ThingErrorNoError);
    });
}
```

    
## Browsing

Things that can be browsed, for example media players, need to have `browsable` set to true in their plugin JSON file. In additon to that, at least 2 methods must be implemented: `browseThing()` and `browserItem()`.

`browseThing()` will be used to actually browse the device or service, while `browserItem()` is used to retrieve a single item from the browser. The browsed items can be flat (i.e. just a list of items) or structured in a tree (i.e. a file system with folders and subfolders). Every item returned in `browseThing()` must be uniquely identifiable so that it can be retrieved at any time in `browserItem()`. This following example would return results from a an object tree:

```C++
void IntegrationPluginMock::browseThing(BrowseResult *result)
{
    VirtualFsNode *node = m_virtualFs->findNode(result->itemId());
    if (!node) {
        result->finish(Thing::ThingErrorItemNotFound);
        return;
    }

    foreach (VirtualFsNode *child, node->childs) {
        result->addItem(child->item);
    }
    result->finish(Thing::ThingErrorNoError);
}
```

The given `result` object contains the starting point given by `result->itemId()`. First the plugin tries to find that item in the file system. For the first time this method is called, `result->itemId()` will be empty. That indicates the root item. Once the item has been found in the file system, a list of child items is added to the result by using `BrowseResult::addItem(const BrowserItem &item)`. Each of the added items needs to have the item id filled in properly, for example "/item1", "/item2" and so on. If the user enters item1, this method will be called again, but the `result`'s itemId will contain "/item1". The plugin again finds this item in its file system and returns the list of its childs. In this case the item ids might be something like "/item1/subitem1", "/item1/subitem2" etc...

The plugin calls the `finish()` method as usual to indicate when it's done.

At a later point, nymea might retrieve info for a particular item again. This is done by calling `browserItem()` on the plugin:

```C++
void IntegrationPluginExample::browserItem(BrowserItemResult *result)
{
    VirtualFsNode *node = m_virtualFs->findNode(result->itemId());
    if (!node) {
        result->finish(Thing::ThingErrorItemNotFound);
        return;
    }
    result->finish(node->item);
}
```

Again, the result object will contain the requested item id. Once the item is found, it is returned in the finish() call. If the item can't be found, the finish() method is to be called with the appropriate error as usual.
