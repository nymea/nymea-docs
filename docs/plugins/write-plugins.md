---
id: write-plugins
title: Plug-in Development
---

Plugins in nymea are used to expand the functionality and capabilities of nymea. A plugin is basically a shared library, which will be loaded dynamically by nymea during the start up process. It abstact the services and devices into nymeas internal [ABI](https://en.wikipedia.org/wiki/Application_binary_interface). 

Once a device is abstracted inside of nymea, the Rule-Engine can be used to create rules, the Log-Engine logs everythings automatically and it can be controlled by the nymea:app without changing single line of the App. 

Each plugin has a name, a [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) and a list of supported vendors which will be visible in the system once the plugin is loaded. Each of those Vendors contains a list of supported Device types.

A _device_ in nymea can represent a _real_ devices such as lightbulbs, gateways or garage door openers, but can also represent online service, like weather-, or E-Mail services.
