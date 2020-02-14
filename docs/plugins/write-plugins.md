---
id: write-plugins
title: Plug-in Development
---

Plugins in nymea are used to extend the functionality and capabilities of nymea. A plugin is basically a shared library, which will be loaded dynamically by nymea during the start up process.

## Integration plugins

An integration plugin in nymea is used to add support for devices or services, commonly referred to as "things" in nymea. I might be real devices such as light bulbs, gateways or garage door openers, but can also represent online services, like weather-, or e-mail services, generally everything that can represent a "thing" in IoT - the internet of things.

Once an integration plugin is loaded by nymea, all of its provided things can be used in all parts of nymea. Be it creating rules to automatically trigger behaviors using this device or service, logging data for later evaluation or controlling things through client applications.

An integration plugin is confined within its context. That means, such a plugin cannot obtain information about other integrations in the system, it cannot interact with things that are not managed by this integration, manipulate logs or have any other insights on what is going on in the nymea system. Its only purpose is to "translate" between nymea and 3rd party devices or services.

## Platform plugins

Platform plugins are used to allow nymea to integrate better into a given system. For instance, if nymea is ported to a system that does not run avahi, a platform plugin for that system might be implented to integrate with zeroconf using libdns-sd or Bonjour. Another example would be a system platform plugins. On a Raspberry Pi, the nymea-platform-plugin-systemd would be used to allow nymea controlling the systen's time settings and allow taking control over rebooting the machine. On a different system, where systemd is not available, this might be a platform plugin that talks to any other system for those features.

## Experience plugins

Experience plugins allow to inject custom functionality into nymea. Unlike device plugins, they are not isoleted within a single device/service context, but allow to integrate very deeply into nymea. An experience plugin can be used to

* Extend the JSON-RPC API

If nymea's intended use is a very specific use case, with a custom client application tailored for this very specific use case, addditional JSONRPC API can be exposed. One example could be a service API which might be used to expose service data for all connected devices and provide that to a service app.

* Directly interact with multiple devices

An experience plugin can interact directly with device plugins. In the above example of a service plugin, it could iterate over all loaded devices, collect the service data to be exposed to JSON-RPC.
