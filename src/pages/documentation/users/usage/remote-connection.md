---
id: remote-connection
title: Cloud connection
---

Often it is useful to interact with your home when you're out. To check back whether you've turned off all the things, to start up heating before you come home and such. Nymea supports this in an easy and reliably way by using nymea:cloud to establish a connection between nymea:app and the nymea system.

### Setting up nymea:cloud

#### Connecting nymea to nymea:cloud

The nymea system needs to be configured to connect to nymea:cloud and wait for incoming connections from nymea:app. In order to do so, go to System Settings -> Cloud. If this happened before, the nymea system needs to be registered in the cloud. This means the nymea system will download a certificate from nymea:cloud which will be used to identify a system in the cloud.

> Note: Only the UUID and the name of the nymea system will be uploaded to the cloud. This is required in order to identify a system for remote connection attempts.

Once the registration happened, the cloud connection can be enabled.

![](/img/documentation/users/cloud-core.png)

#### Creating a cloud account

Along with connecting nymea systems to the cloud, a user account on nymea:cloud is required. Go to App Settings -> Cloud settings and create a new account (or log in with an existing nymea:cloud account).

![](/img/documentation/users/cloud-app.png)

When nymea:app locally connects to a nymea:core system and both have a valid cloud connection, nymea:core will grant permissions to use the remote connection to the user logged in in nymea:app.

![](/img/documentation/users/cloud-pairings.png)

Once logged in, the connected nymea:core instances will be listed. You can remove a nymea:core instance from your cloud account by longpressing or swiping an entry here.

### Connecting remotely

When a connection between nymea:app and nymea:core is established, nymea:app will automatically determine the best route. If both are in the same local network, a direct connection is used. If a local connection is not possible, nymea:app will automatically connect using the remote connection.

All the possible connection candidates (local and remote) can be seen in the very first view of nymea:app where the app scans for possible connections. Longpressing or swiping an entry in that list will allow viewing all the connection candidates and selecting the preferred connection.

![](/img/documentation/users/remote-connection.png)


### Push notifications

Another feature that's coming with nymea:cloud are push notifications. Just like the remote connection, this will start working automatically once nymea:core and nymea:app are paired through nymea:cloud. A new category for notifications will appear in the main things screen. Entering there, push notifications to the phone can be sent.


![](/img/documentation/users/pushnotifications.png)

Push notifications are supported by nymea:app on Android, iOS and Ubuntu Phone (UBPorts).

![](/img/documentation/users/push-android.jpg)

