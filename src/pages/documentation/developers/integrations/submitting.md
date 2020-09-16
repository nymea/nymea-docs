---
id: submitting
title: Submitting your plugin
---

Once a plugin is created, you're welcome to share your plugin with others in the community.

At this point, nymea doesn't offer an "app store" for plugins yet, so plugins are currently distributed as packages in the nymea repository and need to follow the nymea release cycle. For now, that means the plugin code is hosted in one of the nymea-plugins repositories.

Create a pull request on github against [the nymea plugins repository](https://github.com/nymea/nymea-plugins) or one of the other plugin repositories on https://github.com/nymea. Contact us if in doubt where your plugin would fit.

The pull request will be reviewed and once it passes the review it can be integrated in upcoming nymea releases.

There are a few guidelines that need to be followed in order for a plugin to be included:

### Compatible license

The plugin needs to be licenced under a compatible Open Source license. If in doubt, please contact us.

### CLA signing

In order to keep everyone involved happy, at this point we obliged to ask you to sign our CLA to contribute to the nymea-plugins repository. The CLA Assistant will automatically ask you to do so when filing the pull request.


### Metadata

As plugins in the nymea-plugins repository will be advertised on the nymea website, there is the need to have a meta.json file and a README.md file added. Those files are fairly self explanatory, please check other plugins for examples on those.

>NOTE: The README.md should be a user guide on how to use the plugin, not a developer guide for developing on it. If you require any instructions for developing on the plugin, please create a README-DEV.md file for that.



