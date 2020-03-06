---
id:plugin-js
title: The plugin code (JS)
---

Once a [plugin JSON](plugin-json) file is created, the according logic is to be implemented in the plugin code. This page will describe how to work with the JavaScript plugin API. If a plugin is implemented using C++/Qt, please refer to [this page](plugin-cpp).


## Introduction

The plugin codes main entry point is a file named `integrationplugin<name>.js`. The file name must match the plugin's JSON file name with the exception of the file name extension. So the very minimum required are two files, `integrationplugin<name>.json` and `integrationplugin<name>.js`.


    export function setupThing(info) {
        console.log("Setup called");
        ...
        info.finish(Thing.ThingErrorNoError);
    }

    export function executeAction(info) {
        console.log("Execute action called");
        ...
        info.finish(Thing.ThingErrorNoError);
    }


This is a minimalistic example for a plugin. The functions called by nymea must be marked with `export`. Nymea offers a ECMA-Script version 5 compliant engine. Please note that non-standard engines like for instance node.js are not supported.

## Working with modules

ECMA compliant modules can be used. Those must be provided as `.mjs` files and can export functions to be used in the main plugin's file. For instance a `worker.mjs` module might look like this:

    export function doStuff(someValue) {
        console.log("module function called!");
        return someValue;
    }

and can be imported in the main plugin by using:

    import { doStuff } from "./worker.mjs";
    
    ...
    
    export function init() {
        doStuff();
    }


## Setup

The most important method is probably `setupThing()`. This is called when a new thing is configured in the system, as well as on system startup. This method should do all the required stuff to connect to the thing. The `info` parameter will contain all the information for the newly set up thing. Once the connection to the device or online service has been established, the plugin code must call the `finish()` method on the info object. Please note, that there is a timeout in place which will cause the setup to time out eventually if `finish()` is not called. A plugin implementation can react on this by connecting to the `aborted()` signal. A more complete example for a setup implementation might look like this:


    export function setupThing(info) {
        
        var deviceIp = info.device.paramValue("1d10b8e2-aea4-495c-8b1f-f44ef088f667");
        
        var request = new XMLHttpRequest()
        request.open("GET", "https://" + deviceIp" + "/api");
        request.onload = function() {
            var response = JSON.parse(request.response);
            if (response.status == "OK") {
                info.finish(Thing.ThingErrorNoError);
            } else {
                info.finish(Thing.ThingErrorHarwareFailure);
            }
        }
        request.send();
    }
    
In this example a http GET call to a REST API on a device would be made. The IP adress is obtained from the thing parameters (NOTE: those must be defined in the plugin's JSON file). For the request, an `XMLHttpRequest` is created and sent to the network with `send()`. The response is parsed and if everything is as expected, the plugin will call `info.finish(Thing.ThingErrorNoError)`. If something has gone wrong, it'll call `info.finish(Thing.ThingErrorHarwareFailure)` instead to indicate the failure to the system. If the setup times out before the GET call returns, the `info` object will be destroyed and the the execution will stop processing. If the code should be made more robust against this behavior, a plugin developer may connect to the info's aborted signal in such a manner:

    info.aborted.connect(function() {
        console.warn("setup timed out and aborted.");
        // error handling here...
    })

## Actions

Whenever the user (or some automatism) executes an action in th system, the plugin will get `executeAction` called. The `info` parameter will contain all the required information to process the request. That contains information about the thing as well as the action. Let's have a look at an example switching on/off a device using a REST API.

    export function executeAction(info) {
        var deviceIp = info.thing.paramValue("1d10b8e2-aea4-495c-8b1f-f44ef088f667");

        if (info.actionTypeId() == "3e8c9056-bb35-4168-a37c-135e6e1e7989") {

            var request = new XMLHttpRequest()
            request.open("POST", "https://" + deviceIp" + "/api");
            
            request.onload = function() {
                var response = JSON.parse(request.response);
                if (response.status == "OK") {
                    info.finish(Thing.ThingErrorNoError);
                } else {
                    info.finish(Thing.ThingErrorHarwareFailure);
                }
            }

            var paramValue = info.paramValue("3e8c9056-bb35-4168-a37c-135e6e1e7989");
            
            request.send(paramValue == true ? "on" : "off");
        }
    }

Again, we're obtaining the device's IP using the thing parameters, just like in `setupThing`. In addition, we're checking out which action it is. The action types are defined in the plugin's JSON file. Once we know which action it is (in this case the "power" action) we can obtain the parameters for it by accessing `info.paramValue(paramTypeId)`. Again, the actual parameter values can be obtained by using the paramType id defined in the plugin's JSON file. Like in the setupThing example we're constructing a HTTP call, in this case a POST one and using the `XMLHttpRequest` to send it to the network and waiting on the callback to return to `finish()` the action.

## Events

Whenever a thing is triggering an event, for instance a button on a device is pressed, or a trigger is happening on an online service, the plugin implementation should call `emitEvent` passing the information about the event. Let's look at an example that would poll an online service for such triggers.

    var pluginTimer;
    
    export function setupDevice(info) {

        // Doing the regular setup first...
        ...
        
        // And set up the polling
        
        pluginTimer = hardwareManager.pluginTimerManager.registerTimer(5);
        pluginTimer.timeout.connect(function() {
        
            var request = new XMLHttpRequest()
            request.open("GET", "https://" + deviceIp" + "/api");
            request.onload = function() {
                if (request.response == "eventHappened") {
                    emitEvent(info.thing.id, "3e8c9056-bb35-4168-a37c-135e6e1e7989", []);
                }
            }
            request.send();
        })
    }

    export function thingRemoved(thing) {
        hardwareManager.pluginTimerManager.unregisterTimer(pluginTimer);
    }
    
In `setupThing` we're doing the regular setup first. If that succeeds, the plugin is registering a timer which whill emit the `timeout` signal every second. Connected to this timeout signal of the timer, the plugin will poll an online API. If the response of that polling operation contains data that indicates the happening of an event, the plugin constructs an `Event` with the required data. In this case it will contain the event type id which as usual has been defined in the plugin's JSON. In addition to that, it will contain the ID of the thing this event is for. The event could also have additional parameters but in this example we're omitting that for simplicity. Finally, the plugin calls `emitEvent(thingId, eventTypeId, params)` to indicate the event to the system.

One more thing to notice here is that the registering of a timer will require the plugin also to unregister it again when it's not needed any more. For that it uses the `thingRemoved()` method.

## States

States are handled very similar to events. But instead of creating an Event object, the plugin would call `thing->setStateValue()`. Let's look at an example that would poll the current temperature from some online API.

    void IntegrationPluginExample::setupDevice(ThingSetupInfo *info) {

        // Doing the regular setup first...
        ...
        
        // And set up the polling
        
        Thing *thing = info->thing();
        m_pluginTimer = hardwareManager()->pluginTimerManager()->registerTimer(1);
        
        connect(m_pluginTimer, &PluginTimer::timeout, thing, [this, thing](){
            
            QNetworkRequest request("https://example.com/api/temperature");
            QNetworkReply *reply = hardwareManager()->networkAccessManager()->get(request);
            
            connect(reply, &QNetworkReply::finished, reply, &QNetworkReply::deleteLater);

            connect(reply, &QNetworkReply::finished, thing, [thing, reply](){
                QByteArray data = reply->readAll();
                int temperature = data.toInt();
                
                thing->setStateValue(exampleTemperatureStateTypeId, temperature);
            });
        });
    }

Also this example would poll the API every second. Whenever the reply comes back, it'll set the thing's state value using the id for the temperature state which is defined in the plugin's JSON file and the actual new value.
