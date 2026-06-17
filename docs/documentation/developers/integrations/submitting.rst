.. _doc-developers-integrations-submitting:

Submitting your plugin
======================


Once a plugin is created, you're welcome to share your plugin with others in the community.

At this point, nymea doesn't offer an "app store" for plugins yet, so plugins are currently distributed as packages in the nymea repository and need to follow the nymea release cycle. For now, that means the plugin code is hosted in one of the nymea-plugins repositories.

Create a pull request on github against `the nymea plugins repository <https://github.com/nymea/nymea-plugins>`__ or one of the other plugin repositories on https://github.com/nymea. Contact us if in doubt where your plugin would fit.

The pull request will be reviewed and once it passes the review it can be integrated in upcoming nymea releases.

There are a few guidelines that need to be followed in order for a plugin to be included:

License
-------

Plugins in the nymea-plugins repositories are licensed under GPLv3 or LGPLv3. Your contribution must be submitted under one of these licenses.


Metadata
--------


As plugins in the nymea-plugins repository will be advertised on the nymea website, there is the need to have a meta.json file and a README.md file added. Those files are fairly self explanatory, please check other plugins for examples on those.

.. note::

   The README.md should be a user guide for end users, not a developer guide. For developer
   notes, create a separate ``README-DEV.md`` file.
