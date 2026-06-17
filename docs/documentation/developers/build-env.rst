.. _doc-developers-build-env:

Build environment
=================


This page assumes you are working on one of the supported Debian or Ubuntu versions. Other Linux
distributions should work too, however installation of the build dependencies may vary.

Like with a regular nymea installation, all the required packages can be obtained from the same nymea
repository that is used for nymea:core:

.. include:: ../_includes/repository-stable.rst


Now the nymea SDK can be installed with this command:

::

   sudo apt update
   sudo apt install nymea-sdk


This will install nymea and all the development packages in order to build a nymea-plugin. It will also install QtCreator as the recommended IDE.

If you wish to use a different IDE, you may install the SDK with the following command instead:

::

   sudo apt install --no-install-recommends nymea-sdk


In order to build existing plugins additional dependencies might be required. Those vary
between plugins. All the required dependencies for building the main nymea-plugins repository can
be installed with this command:

::

   sudo apt build-dep nymea-plugins
