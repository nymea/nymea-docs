---
id: events-actions-states
title: Events, actions and states
---

The main way of interacting with things in nymea are events, actions and states.

## Thing events

In nymea, every thing can have a set of states. For example, a device with buttons would trigger an event for `buttonPressed` whenever the user presses the button. Event can also have parameters. In the example of a remote control, the `buttonPressed` event would also contain a parameter to indicate which button has been pressed.

## Thing actions

Similar to events, but the other direction, a thing can have actions. For example, a smart speaker would have multiple actions, like `play`, `pause` and so on. The user (or some automation) can then execute those actions to control the device. Like events, also actions can have parameters. As an example for this, an online service that sends out notifications to the user would have an action named `notify` with two parameters, one for `title` and one for `body`. Those parameters will then contain the actual content of the notification.

## Thing states

Every thing can also have a set of states. States are used to represent a set of properties that might change over time. For example a temperature sensor might have a state named "temperature" to indicate the currently measured temperature. Whenever the measured temperature changes, the plugin implemenation updates the state value in nymea.

Every state change will implicitly trigger an event in the system which will propagate the state change through the entire system.

States can be read only or writable. A read only state will only read a certain things state and make its value available to nymea. A writable state can also be changed in nymea, which would then change the state on the thing. A writable state will implicitly generate the according action which is used in nymea to set the states value.
