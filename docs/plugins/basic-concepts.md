---
id:basic-concepts
title: Basic concepts
---

Integration plugins in nymea provide support for additional integrations with hardware devices and online services, commonly referred to as "things". A single plugin can provide support for multiple things.

A plugin is responsible for translating the nymea internal things api into the device or service specific protocol. This mainly consists of handling setup and connecting to a given thing and then monitoring it for state changes and forwarding actions triggered by nymea to it.

Integration plugins can be written either using C++/Qt or using JavaScript. However, either way a [plugin JSON](plugin-json) file is required to define all the supported integrations by this plugin.

## Adding and configuring new things

Setting up a thing is done in two steps:

* Creation
* Setup

### Thing creation

There are different ways how things can be created in nymea:

#### User

This is used if a thing needs to be configured manually by the user. For example by entering an IP address to connect to it.

#### Discovery

This is used if a thing can be discovered. For example things that can be found via ZeroConf in the local network. The user can perform a discovery for such things and pick which ones should be added to the system.

Plugins supporting discovery must implement the `discoverThings` method.

#### Automatic

This is used if a device should be added to the system without the user having to interact with it at all. For example, if the user adds a bridge device to the system and then all the devices connected to this bridge will automatically appear in the system.

Plugins supporting automatic thing creation must emit the `autoThingsAppeared` signal to indicate the appearance of such things. Also, such plugins plugins may implement `startMonitoringAutoDevices` if an entry point for watching things is required.

### Thing setup

Once it is known how a thing can be created in the system, it needs to be set up. Also this offers various options:

#### JustAdd

This is used for things that do not require any sort of authentication. A user can, after having discovered or manually entered connection parameters for such a thing, just add it to the system and it will be functional.

#### Username and passwort

If a thing requires entering a username and password for nymea to interact with it, this setup method should be used. It will prompt the user to enter the login credentials upon setup.

#### Display PIN

Some things, for example smart TVs will require to use a PIN code for authentication. In this example, the TV will display the PIN to the user on the TV screen and the user can enter it in nymea upon device setup.

#### Enter PIN

Some things might have an input method (e.g. a number pad) but no display and require the user to enter a PIN on the device. Nymea can display this PIN diuring device setup and allow the user to enter it on the device.

#### Push button

For devices that have a push button it is often required to press this button during setup to grant an authorization token to nymea. Using this setup method will tell the user to press the button during setup and continue once the button has been pressed.

#### OAuth

Some things, mostly online services, use OAuth to allow the user logging in. Using this setup method will start an out of band login process. During the first step of the pairing, the plugin fetches a OAuth URL from the remote service and redirects the nymea user to this URL. The user then logs in and upon success the user is redirected back to nymea containing the information required to obtain an authorization token.

### Combinations

In general a plugin implementation can freely combine those create and setup methods to reflect the actual device or service. However, keep in mind that not all combinations of create methods and setup methods make sense. For example things that are added automatically will generally use JustAdd as setup method as they might be created in the system without user interaction at all.

Some example flows:

#### Create method "User" - setup method "JustAdd"

1. | The user selects "Add new thing" for a thing with create method "User".
2. | The user enters some parameters, for example the IP address of the thing.
3. | The plugin runs setupThing() and connects to the thing using the setup parameters.

#### Create method "User" - setup method "UserAndPassword"

1. | The user selects "Add new thing" for a thing with create method "User".
2. | The user enters some parameters, for example the IP address of the thing.
3. | The plugin runs startPairing() to prepare for pairing.
4. | The user is asked to enter username and password to authenticate for this thing.
5. | The plugin runs confirmPairing() using the given username and password, for example to obtain an authentication token from the thing.
3. | The plugin runs setupThing() and connects to the thing using the setup parameters and the login credentials.

#### Create method "Discovery" - setup method "JustAdd"

1. | The user selects "Add new thing" for a thing with create method "Discovery".
2. | The plugin runs discoverThings() and returns a list of discovered things of this type.
3. | The user selects one thing of the discovery results.
4. | The plugin runs setupThing() and connects to the thing using the setup parameters which have been discovered before.


#### Create method "User" - setup method "PushButton"

1. | The user selects "Add new thing" for a thing with create method "User".
2. | The user enters some parameters, for example the IP address of the thing.
3. | The plugin runs startPairing() and - if needed - indicates to the device that a new pairing is about to happen.
4. | The user is asked to push the button on the hardware.
5. | The plugin runs confirmPairing() to finish the pairing procedure.
6. | The plugin runs setupThing() and connects to the thing using the setup parameters.

#### Create method "Auto" - setup method "JustAdd"

1. | The user previously added a bridge device in a previous setup flow.
2. | The plugin detects there are multiple devices connected to the bridge.
3. | The plugin emits autoThingsAppeared() to indicate to nymea that new things have been detected.
4. | The plugin runs setupThing() for each of the devices connected to the bridge to set them up without user interaction.


#### Create method "Discovery" - setup method "DisplayPin"

1. | The user selects "Add new thing" for a thing with create method "Discovery", for example a smart TV.
2. | The plugin runs discoverThings() and returns a list of discovered smart TVs of this type.
3. | The user selects one of the discovery results.
4. | The plugin runs startPairing() and instructs the smart TV to display the PIN code.
5. | The user is asked to enter the PIN code displayed on the smart TV.
6. | The plugin runs confirmPairing() using the user entered PIN and requests an authentication token at the TV.
4. | The plugin runs setupThing() and connects to the smart TV using the authentication token obtained before.

#### Create method "User" - setup method "OAuth"

1. | The user selects "Add new thing" for a thing with create method "User".
2. | The plugin runs startPairing() and obtains the OAuth URL from the remote service which it returns to nymea.
3. | The user is redirected to the OAuth URL and performs the login which returns with a OAuth code.
4. | The plugin runs confirmPairing() and exchanges the OAuth code for a authorization token.
5. | The plugin runs setupThing() and connects to the remote service using the authorization token.


## Thing events

In nymea, every thing can have a set of states. For example, a device with buttons would trigger an event for `buttonPressed` whenever the user presses the button. Event can also have parameters. In the example of a remote control, the `buttonPressed` event would also contain a parameter to indicate which button has been pressed.

## Thing actions

Similar to events, but the other direction, a thing can have actions. For example, a smart speaker would have multiple actions, like `play`, `pause` and so on. The user (or some automation) can then execute those actions to control the device. Like events, also actions can have parameters. As an example for this, an online service that sends out notifications to the user would have an action named `notify` with two parameters, one for `title` and one for `body`. Those parameters will then contain the actual content of the notification.

## Thing states

Every thing can also have a set of states. States are used to represent a set of properties that might change over time. For example a temperature sensor might have a state named "temperature" to indicate the currently measured temperature. Whenever the measured temperature changes, the plugin implemenation updates the state value in nymea.

Every state change will implicitly trigger an event in the system which will propagate the state change through the entire system.

States can be read only or writable. A read only state will only read a certain things state and make its value available to nymea. A writable state can also be changed in nymea, which would then change the state on the thing. A writable state will implicitly generate the according action which is used in nymea to set the states value.


## Browsing things

Some things might offer the feature to be browsable. For example, a smart speaker can allow the user to browse the available playlists. Browsing a thing is like browsing a file system. It can be a simple list of entries, but also an entire tree which can be entered.

## Parent child relationships

Configured things in the system may have parent-child relationships. This is expressed by some things having a parent thing. If a thing does not have any parents it either is a standalone thing or it may be a parent to other things. If a thing does have a parent id set, it is a child of the given parent. One thing can be a parent to many others.

This parent-child relationship mostly has effect when managing things. If a parent is removed from the system, all its childs will be removed too.
