.. _doc-users-installation-core:

nymea:core
==========

nymea:core is typically installed on a low-power machine in the local network, such as a Raspberry Pi,
an embedded gateway or a small PC. nymea provides ready-to-use Raspberry Pi images and packaged builds
for Debian and Ubuntu systems.

.. _doc-users-installation-core-debian-ubuntu:

Debian GNU/Linux and Ubuntu
---------------------------

nymea provides apt repositories for Debian and Ubuntu.

.. include:: ../../_includes/repository-stable.rst

Install nymea:core
------------------

Once the repository has been configured, update the package index and install nymea:core:

::

   sudo apt update
   sudo apt install nymea nymea-plugins

Once this command completes, nymea:core should be up and running.

Raspberry Pi
------------

The recommended way to install nymea on a Raspberry Pi is to use the nymea:core image in
`Raspberry Pi Imager <https://www.raspberrypi.com/software/>`__. In the imager, select
``Other specific-purpose OS`` -> ``Home Automation`` -> ``nymea``. The current image is based on
Debian 13.

Write the image to an SD card, insert the card into the Raspberry Pi and connect the power supply.
nymea:core starts automatically on boot.

.. note::

   The Raspberry Pi images have SSH enabled by default with username ``nymea`` and password ``nymea``.
   Change the credentials before using the system in a publicly accessible network.

After the first boot, continue with :doc:`the first steps guide <../usage/first-steps>`.

Manual installation on Raspberry Pi
-----------------------------------

If the nymea Raspberry Pi image is not used, nymea:core can also be installed manually on Raspberry Pi
OS using the apt repository.

Currently, the following Raspberry Pi models are supported:

* Raspberry Pi 2
* Raspberry Pi 3
* Raspberry Pi 4
* Raspberry Pi 5
* Raspberry Pi Zero 2 W

For manual installation, use the :ref:`Debian repository instructions <doc-users-installation-core-debian-ubuntu>` above. Current Raspberry Pi OS based
installations should use the Debian 13 ``trixie`` repository.

Yocto
-----

nymea:core can also be integrated into Yocto based images using the
`meta-nymea layer <https://github.com/nymea/meta-nymea>`__. The layer currently supports the following
Yocto releases:

* ``kirkstone``
* ``scarthgap``
* ``wrynose``

Clone the matching branch of ``meta-nymea`` into your Yocto workspace and add it to your build
configuration:

::

   git clone -b wrynose https://github.com/nymea/meta-nymea.git
   bitbake-layers add-layer meta-nymea

Replace ``wrynose`` with the Yocto release used by your build. After adding the layer, include the
nymea packages in your image according to your product requirements.

Other distributions or architectures
------------------------------------

To install nymea:core on other distributions or architectures, nymea:core needs to be built manually from
source. See :doc:`the developer build documentation <../../developers/build-nymea>` for instructions.

Joining the beta tests
----------------------

.. note::

   Running experimental or testing builds of nymea is not recommended for users expecting a stable setup.

nymea provides three repository channels:

* ``stable``: The current stable release. This is the default repository described above.
* ``landing``: The next release candidate. This is where testing for new releases happens.
* ``experimental``: The current development channel. It can be unstable and may break a setup.

Landing and experimental repositories
-------------------------------------

Choose the repository format for your distribution version.

.. raw:: html

   <div class="nymea-tabs">
     <div class="nymea-tab-list" role="tablist" aria-label="Testing repository format">
       <button class="nymea-tab" id="testing-list-tab" type="button" role="tab" aria-selected="true" aria-controls="testing-list-panel">Debian 12 / Ubuntu 20.04-24.04</button>
       <button class="nymea-tab" id="testing-sources-tab" type="button" role="tab" aria-selected="false" aria-controls="testing-sources-panel">Debian 13 / Ubuntu 26.04</button>
     </div>
     <div class="nymea-tab-panel" id="testing-list-panel" role="tabpanel" aria-labelledby="testing-list-tab">
       <p>Use the classic list format. Replace <code>bookworm</code> with the matching distribution codename.</p>
       <p><strong>Landing</strong></p>
       <div class="nymea-code-block"><pre><code>sudo tee /etc/apt/sources.list.d/nymea-landing.list &gt; /dev/null &lt;&lt;EOM
   deb http://repository.nymea.io/landing bookworm main non-free
   deb-src http://repository.nymea.io/landing bookworm main non-free
   EOM</code></pre></div>
       <p><strong>Experimental</strong></p>
       <div class="nymea-code-block"><pre><code>sudo tee /etc/apt/sources.list.d/nymea-experimental.list &gt; /dev/null &lt;&lt;EOM
   deb http://repository.nymea.io/experimental bookworm main non-free
   deb-src http://repository.nymea.io/experimental bookworm main non-free
   EOM</code></pre></div>
     </div>
     <div class="nymea-tab-panel" id="testing-sources-panel" role="tabpanel" aria-labelledby="testing-sources-tab" hidden>
       <p>Use the deb822 source format. Replace <code>trixie</code> with <code>resolute</code> when using Ubuntu 26.04.</p>
       <p><strong>Landing</strong></p>
       <div class="nymea-code-block"><pre><code>sudo tee /etc/apt/sources.list.d/nymea-landing.sources &gt; /dev/null &lt;&lt;EOM
   Types: deb deb-src
   URIs: http://repository.nymea.io/landing
   Suites: trixie
   Components: main non-free
   Signed-By: /etc/apt/trusted.gpg.d/nymea.gpg
   EOM</code></pre></div>
       <p><strong>Experimental</strong></p>
       <div class="nymea-code-block"><pre><code>sudo tee /etc/apt/sources.list.d/nymea-experimental.sources &gt; /dev/null &lt;&lt;EOM
   Types: deb deb-src
   URIs: http://repository.nymea.io/experimental
   Suites: trixie
   Components: main non-free
   Signed-By: /etc/apt/trusted.gpg.d/nymea.gpg
   EOM</code></pre></div>
     </div>
   </div>

After adding or changing repository channels, run:

::

   sudo apt update
   sudo apt upgrade
