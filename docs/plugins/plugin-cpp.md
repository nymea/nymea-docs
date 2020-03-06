---
id:plugin-cpp
title: The plugin code (C++/Qt)
---

Once a [plugin JSON](plugin-json) file is created, the according logic is to be implemented in the plugin code. This page will describe how to work with the C++/Qt plugin API. If a plugin is implemented using JavaScript, please refer to [this page](plugin-js).

## Introduction

The plugin codes main entry point is defined by subclassing the [IntegrationPlugin](broken) class. The header file accordingly looks similar to this:


    #ifndef INTEGRATIONPLUGINEXAMPLE_H
    #define INTEGRATiONPLUGINEXAMPLE_H

    #include "integrations/integrationplugin.h"

    class IntegrationPluginExample: public IntegrationPlugin
    {
        Q_OBJECT

        Q_PLUGIN_METADATA(IID "io.nymea.IntegrationPlugin" FILE "integrationpluginexample.json")
        Q_INTERFACES(IntegrationPlugin)


    public:
        explicit DevicePluginExample();

        void setupThing(ThingSetupInfo *info) override;

        void executeAction(ThingActionInfo *info) override;

        void thingRemoved(Thing *thing) override;

    };

    #endif // INTEGRATiONPLUGINEXAMPLE_H

The according .cpp file would look similar to this:


    #include "integrationpluginexample.h"
    #include "plugininfo.h"

    IntegrationPluginExample::IntegrationPluginExample()
    {

    }

    void  IntegrationPluginExample::setupThing(ThingSetupInfo *info)
    {
        qCDebug(dcExample()) << "Setup thing" << info->thing()->name() << info->thing()->params();

        ...
        
        info->thing()->setStateValue(exampleConnectedStateTypeId, true);
        
        info->finish(Thing::ThingErrorNoError);
    }

    void IntegrationPluginExample::executeAction(ThingActionInfo *info)
    {
        qCDebug(dcExample()) << "Executing action for thing" << info->thing()->name() << action.actionTypeId().toString() << action.params();

        info->finish(Thing::ThingErrorNoError);
    }

    void IntegrationPluginExample::thingRemoved(Thing *thing)
    {
        qCDebug(dcExample()) << "Remove thing" << thing->name() << thing->params();

        // Clean up all data related to this thing
    }


This is a minimalistic example for a plugin. While there are lots of other methods that a plugin can implement, this is the bare minimum the average plugin will need. For the complete reference of the integration plugin API use this [link TODO!!!!!]().

## Setup

The most important method is probably `setupThing()`. This is called when a new thing is configured in the system, as well as on system startup. This method should do all the required stuff to connect to the thing. The `info` parameter will contain all the information for the newly set up thing. Once the connection to the device or online service has been established, the plugin code must call the `finish()` method on the info object. Please note, that there is a timeout in place which will cause the setup to time out eventually if `finish()` is not called. A plugin implementation can react on this by connecting to the `ThingSetupInfo::aborted()` signal. A more complete example for a setup implementation might look like this:


    void  IntegrationPluginExample::setupThing(ThingSetupInfo *info)
    {
        QString deviceIp = info->thing()->paramValue(exampleThingIpParamTypeId).toString();
        
        QNetworkRequest request("http://" + deviceIp + "/api");
        QNetworkReply *reply = hardwareManager()->networkAccessManager()->get(request);

        connect(reply, &QNetworkReply::finished, reply, &QNetworkReply::deleteLater);

        connect(reply, &QNetworkReply::finished, info, [info, reply](){
            QByteArray data = reply->readAll();
            
            if (data == "OK") {
                info->finish(Thing::ThingErrorNoError);
                info->thing()->setStateValue(exampleConnectedStateTypeId, true);
            } else {
                info->finish(Thing::ThingErrorHarwareFailure);
            }
        });
        
        connect(info, &ThingSetupInfo::aborted, this, [](){
            qCDebug(dcExample) << "Setup timed out...";
        });
    }

In this example a http GET call to a REST API on a device would be made. The IP adress is obtained from the thing parameters (NOTE: those must be defined in the plugin's JSON file). The `finished` signal of the QNetworkReply is connected to two slots: For one, it will call `deleteLater` on the reply object itself. This is just to clean up the call and prevent to leak memory. More importantly, it is also connected to a lambda function which ready the payload of the GET call and if everything is as expected it calls `info->finish(Thing::ThingErrorNoError)`. If something has gone wrong, it'll call `info->finish(Thing::ThingErrorHarwareFailure)` instead to indicate the failure to the system. Note that the lambda is only invoked if the `info` object is still existing (the 3rd argument in the `connect` method). If the setup times out before the GET call returns, the `info` object will be destroyed and the lambda is never invoked. This is also the reason why we're connecting `deleteLater` separately, as we want that to be called in any case.

## Actions

Whenever the user (or some automatism) executes an action in th system, the plugin will get `executeAction` called. The `info` parameter will contain all the required information to process the request. That contains information about the thing as well as the action. Let's have a look at an example switching on/off a device using a REST API.

    void IntegrationPluginExample::executeAction(ThingActionInfo *info)
    {
        QString deviceIp = info->thing()->paramValue(exampleThingIpParamTypeId).toString();
        
        ActionTypeId actionTypeId = info->action().actionTypeId();
        
        if (actionTypeId == examplePowerActionTypeId) {
            bool power = info->action().paramValue(exampleActionPowerParamTypeId).toBool();
            
            QNetworkRequest request("http://" + deviceIp + "/api/power");
            QNetworkReply *reply = hardwareManager()->networkAccessManager()->post(request, power ? "on" : "off");

            connect(reply, &QNetworkReply::finished, reply, &QNetworkReply::deleteLater);

            connect(reply, &QNetworkReply::finished, info, [info, reply, power](){
                QByteArray data = reply->readAll();
            
                if (data == "OK") {
                    info->finish(Thing::ThingErrorNoError);
                    info->thing()->setStateValue(examplePowerStateTypeId, power);
                } else {
                    info->finish(Thing::ThingErrorHarwareFailure);
                }
            });
        } else {
            // Handle other actions...
            ...
        }
    }

Again, we're obtaining the device's IP using the thing parameters, just like in `setupThing`. In addition, we're checking out which action it is. The action types are defined in the plugin's JSON file. Once we know which action it is (in this case the "power" action) we can obtain the parameters for it by accessing `info->action().params()`. Again, the actual parameter values can be obtained by using the name for the paramType defined in the plugin's JSON file. Like in the setupThing example we're constructing a HTTP call, in this case a POST one and using the `networkAccessManager` to send it to the network and waiting on the `QNetworkReply` to return to `finish` the action.

## Events

Whenever a thing is triggering an event, for instance a button on a device is pressed, or a trigger is happening on an online service, the plugin implementation should call `emitEvent` passing the information about the event. Let's look at an example that would poll an online service for such triggers.

    void IntegrationPluginExample::setupDevice(ThingSetupInfo *info) {

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

                    Event event(exampleEventTypeId, thing->id());
                    emitEvent(event);
                }
            });
        });
    }

    void IntegrationPlugin::thingRemoved(Thing *thing) {
        hardwareManager()->pluginTimerManager()->unregisterTimer(m_pluginTimer);
    }
    
In `setupThing` we're doing the regular setup first. If that succeeds, the plugin is registering a timer which whill emit the `timeout` signal every second. Connected to this timeout signal of the timer, the plugin will poll an online API. If the response of that polling operation contains data that indicates the happening of an event, the plugin constructs an `Event` with the required data. In this case it will contain the event type id which as usual has been defined in the plugin's JSON. In addition to that, it will contain the ID of the thing this event is for. The event could also have additional parameters but in this example we're omitting that for simplicity. Finally, the plugin calls `emitEvent(event)` to indicate the event to the system.

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

## Discovery

TODO

## Pairing

TODO

## Browsing

TODO

## Settings

TODO
