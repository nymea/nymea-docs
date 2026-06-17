.. _doc-developers-developing-with-qt-creator:

Developing with QtCreator
=========================


QtCreator is the recommended IDE to build nymea projects. If you haven't done so, make sure the build
environment is set up properly by following the guide in :doc:`Build environment <build-env>`.

The same shared workspace and environment that is described in :doc:`Build nymea <build-nymea>` can also be
used here. That makes it easier to run nymea from a build directory and keeps debugging settings in one
place.

In Qt Creator, the shared environment can be added under the project settings in ``Project ->
Build Environment``. That allows multiple dependent projects to share the same headers, libraries and
plugin paths while still being built, run and debugged independently.

When you use Qt Creator, open the projects from the shared workspace one after another and build them
in dependency order. That ensures the later projects can resolve headers and libraries from the earlier
builds.

General steps for all nymea projects
------------------------------------


1. Open QtCreator and click on *File* -> *Open file or project*


2. Navigate to the ``.pro`` file of the wanted project and open it.


3. In the next step, choose the wanted build kit. Unless you have special requirements, the default *Desktop* kit will do.


Project specific options
------------------------


The following options differ between the various projects. If the project you are looking for is not
in here, no special options are required. You should now be able to run the project using the
build/play buttons.

Nymea
-----


.. note::

   **Note:** It is advised to uninstall libnymea1 to run a self built nymea instance to avoid confusion when libraries are loaded.


To run nymea from Qt Creator, use the same run environment as the shell example in the build
documentation. Open the project settings, then use ``Project -> Build Environment`` to add the
workspace variables from the shared development workspace include. If you want to launch nymead from
Qt Creator, also copy the runtime relevant variables into ``Project -> Run Environment``.

At minimum, ``LD_LIBRARY_PATH`` must point at the build output for ``libnymea`` and ``libnymea-core``.
If you are running a larger workspace with custom plugins and libraries, also add the other variables
from the shared development workspace include. This is what makes it practical to build, run and debug
multiple dependent nymea projects from the same Qt Creator session.

Now you should be able to run *nymead* by pressing the *Play* button in Qt Creator or by pressing
``Ctrl`` + ``r``. You can follow stdout in the *Application Output* section
(``Alt`` + ``3``).

If you want to run the application in the terminal, start *nymead* from the build tree after exporting
the same environment variables.

In order to load custom plugins with this self-built nymea instance, also set ``NYMEA_PLUGINS_PATH``
pointing to the build directory of the plugin.

Nymea integration plugins
-------------------------


When developing plugins, nymea needs to be installed on the system. A run configuration for the plugin
can be created by entering the project configuration on the left hand side in Qt Creator, then
selecting the "Run" configuration for your kit and creating a run configuration with a "Custom
executable". The executable should be ``nymead`` and the command line arguments should at least
include ``-n``.
In the environment, export a variable named ``NYMEA_PLUGINS_PATH`` making it point to the build directory of the plugin.
