.. _doc-developers-write-plugins:

Plugin development
==================


Plugins in nymea are used to extend the functionality and capabilities of nymea. A plugin is a shared
library that is loaded dynamically by nymea during startup.

Integration plugins
-------------------


An integration plugin in nymea is used to add support for devices or services, commonly referred to
as "things" in nymea. It may be real devices such as light bulbs, gateways or garage door openers,
but can also represent online services like weather or email services, generally everything that can
represent a "thing" in IoT, the internet of things. The list of currently available integrations can
be found on the :doc:`integrations page <../resources/integrations/index>`.

Once an integration plugin is loaded by nymea, all of its provided things can be used in all parts of nymea. Be it creating rules to automatically trigger behaviors using this device or service, logging data for later evaluation or controlling things through client applications.

An integration plugin is confined within its context. That means such a plugin cannot obtain
information about other integrations in the system, cannot interact with things that are not managed
by this integration, cannot manipulate logs and has no insight into what is going on in the nymea
system. Its only purpose is to "translate" between nymea and third-party devices or services.

See the guide on creating :doc:`integration plugins <integrations/getting-started-integration>`.

Platform plugins
----------------


Platform plugins are used to allow nymea to integrate better into a given system. For instance, if
nymea is ported to a system that does not run ``avahi``, a platform plugin for that system might be
implemented to integrate with zeroconf using libdns-sd or Bonjour. Another example would be a
system platform plugin. On a ``systemd`` based operating system, the
``nymea-platform-plugin-systemd`` would be used to allow nymea to control the system's time settings
and take control over rebooting the machine. On a different system, where systemd is not available,
this might be a platform plugin that talks to any other system for those features.

Experience plugins
------------------


Experience plugins allow custom functionality to be injected into nymea. Unlike device plugins, they
are not isolated within a single device/service context, but can integrate very deeply into nymea. An
experience plugin can be used to

* Extend the JSON-RPC API
* Access all things using the thing manager
* Access logging database


If nymea's intended use is a very specific use case, with a custom client application tailored for that
use case, additional JSON-RPC API can be exposed. One example could be a service API which might be
used to expose service data for all connected devices and provide that to a service app.

* Directly interact with multiple devices
* Implement custom usecases and mechanics


An experience plugin can interact directly with device plugins. In the above example of a service
plugin, it could iterate over all loaded devices and collect the service data to be exposed to
JSON-RPC.

More experience plugin examples can be found in the `GitHub <https://github.com/nymea?q=experience-plugin>`__.

Update plugins
--------------

Update plugins are used to update nymea systems on the target device. On package-based systems this
may mean managing operating system updates, while on image-based systems it often means switching to a
new firmware or root filesystem image.

For apt-based systems, `PackageKit <https://www.freedesktop.org/software/PackageKit/>`__ can be used
as a common abstraction layer for package management and system updates.

For image-based systems, `RAUC <https://rauc.io/>`__ provides a robust update framework for embedded
Linux devices and is commonly used for A/B style update flows.

More update plugin examples can be found in the `GitHub <https://github.com/nymea?q=update-plugin>`__.
