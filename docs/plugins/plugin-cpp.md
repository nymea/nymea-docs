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

For things that can be discovered (either in the local network or on the internet) will use a `createMethod` of `CreateMethodDiscovery` in the plugin's JSON file. For such things, nymea will call `discoverThings()` on the plugin. For this, an integration plugin must implement that method and deliver discovery results back to the system. Similar as to the setup, an info object is passed to the method which is used to report results and indicate progress.

A plugin implementation shall use `ThingDiscoveryInfo::addThingDescriptor(const ThingDescriptor &descriptor)` in order to add newly discovered things to the results and as usual call `ThingDiscoveryInfo::(Thing::ThingError)` on it when done.

One important note is that such a discovery should report all the found things, even those that are already added to the system but it is important to mark them as such. This is done by setting the ThingId of the existing thing on the ThingDescriptor.

A plugin can use arbitrary code to discover devices or services. However, nymea provides some utilities to support the developer with this by providing ZeroConf/mDNS and UPnP discovery apis.

In this example we'd be looking for devices in the local network via ZeroConf:

    void IntegrationPluginExample::discoverThings(ThingDiscoveryInfo *info)
    {
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


## Pairing

Often network devices or online services require a some sort of authentication, be it a simple username/password login, push button authentication or more complex sceanarios like OAuth. Nymea provides support for that by implementing a two step pairing procedure. Such a pairing always consists of of nymea calling `startPairing()` and `confirmPairing()` sequentially. As usual, an info object is passed to the methods. In this case a `ThingPairingInfo`.

The actual implementation of a plugin looks different depending on the used mechanism. In any case, each step must be finished by calling `info->finish()` reporting success or failure.

The plugin should store the credentials in the plugin storage.

### Username and Password authentication

Let's look at the simplest form of it which is username and password authentication.

The `startThing()` call is pretty much a no-operation in this case. The only thing a plugin implementation can do here is to provide an informational text to the client.

    void IntegrationPluginExample::startPairing(ThingPairingInfo *info)
    {
        info->finish(Thing::ThingErrorNoError, QT_TR_NOOP("Please enter the login credentials for your device."));
    }

This will advance the pairing process to the next step immediately, presenting the user with a login interface containing the above informational text. Make sure to use QT_TR_NOOP to wrap the text in order to allow nymea to translate the text to the client's language on the fly.

Once the user has inserted the credentials, nymea will pass them on to the plugin like here:

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

### Push button authentication

This example would pair a device that uses push button authentication:

    void IntegrationPluginExample::startPairing(ThingPairingInfo *info)
    {
        info->finish(Thing::ThingErrorNoError, QT_TR_NOOP("Please press the push button on the device and then continue this setup."));
    }

Again, the `startPairing` call is mostly informative to the user. It tells the user to press the button on the device now and then continue the setup process in nymea.

Once done, nymea will call `confirmPairing` again. In this case neither the `username` nor the `password` arguements will contain meaningful data. Instead, the pairing key (normally a token) can be obtained directly from the device.

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
            pluginStorage()->setValue("apiKey", apiKey);
            pluginStorage()->endGroup();

            info->finish(Thing::ThingErrorNoError);
        });
    }

### OAuth

OAuth is a little more complex than the previous examples, however, the basic flow is just the same. The ThingPairingInfo has a `oAuthUrl` property for that which is to be filled in in the `startPairing()` call. The user will then be redirected to this URL where a login mask will appear for the user to sign in. After a successful login, the remote server will return with a callback URL containing a PIN as URL query parameters. This callback URL will be passed on to the plugin developer in `confirmPairing()` in the `secret` parameter where the plugin can extract the PIN and complete the OAuth procedure.

This example shows the OAuth procedure for the google OAuth service. The plugin developer must obtain the clientId and clientSecret from the remote service, usually by signing up for a developer account. When registering for such a developer account, a callback URL must be provided. Nymea requires this callback url to start with "https://127.0.0.1". The rest of the callback URL is not relevant to nymea.

    void IntegrationPluginMock::startPairing(ThingPairingInfo *info)
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

When the client app completed the OAuth login the procedure continues with `confirmPairing()`

    void IntegrationPluginMock::confirmPairing(ThingPairingInfo *info, const QString &username, const QString &secret)
    {
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


## Browsing

TODO

## Settings

TODO
