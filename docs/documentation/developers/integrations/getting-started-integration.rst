.. _doc-developers-integrations-getting-started-integration:

Getting started
===============

Integration plugins in nymea add support for hardware devices and online services, collectively
referred to as "things". A plugin is responsible for translating nymea's internal things API into
the device- or service-specific protocol. This mainly consists of handling setup, connecting to a
thing, monitoring it for state changes, and forwarding actions triggered by nymea.

Basic concepts
--------------

A single plugin can support multiple things and multiple vendors. In practice, a plugin typically
covers one vendor or one product category to keep the code manageable.

When the user configures a connection to a device or service, a new thing object is created in the
system. Each thing is defined by a :doc:`thing class <thing-class>` which describes the thing's
features and how the user and the system interact with it.

IDs and names
-------------

Everything in nymea is identified by a unique ID and a name. IDs are assigned by the plugin
developer and must never change — nymea uses them to match thing classes, config values, and caches
across restarts and upgrades. Changing an ID is equivalent to creating a new entity; any things
configured with the old ID will stop working.

Each ID also has a name and a display name. The name is used in code and log files — it must be
letters only, no spaces or special characters. The display name is the user-visible string shown in
the UI, which will be translated. Both name and display name may change over time (for rebranding
or product renaming) without breaking existing setups, because the ID remains stable.

The plugin JSON file
--------------------

The first task when creating a new integration plugin is to create a :doc:`plugin JSON <plugin-json>`
file listing all vendors and thing classes the plugin supports.

The plugin code
---------------

Once the thing class is defined, the plugin implementation adds the logic behind it. Plugins can be
written in C++/Qt, Python, or JavaScript. See :doc:`plugin-code` for details.

Testing the plugin
------------------

Once the plugin is written, the next step is to build it and have nymea load it for testing. See
:doc:`building-testing` for the build and launch instructions.
