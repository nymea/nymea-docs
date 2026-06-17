Currently supported versions
----------------------------

Debian:

* Debian 12 ("bookworm")
* Debian 13 ("trixie")

Ubuntu:

* Ubuntu 20.04 ("focal")
* Ubuntu 22.04 ("jammy")
* Ubuntu 24.04 ("noble")
* Ubuntu 26.04 ("resolute")

For each repository, the following architectures are provided:

* amd64
* armhf
* arm64
* riscv64

Import the repository key
-------------------------

The packages in the nymea repository are signed with nymea's GPG key. Import it before adding the
repository:

::

   sudo curl -fsSL -o /etc/apt/trusted.gpg.d/nymea.gpg https://repository.nymea.io/repository.gpg

Optionally, the key fingerprint can be verified with:

::

   gpg --show-keys --with-fingerprint /etc/apt/trusted.gpg.d/nymea.gpg

::

   pub   rsa4096 2016-04-08 [SC]
         B1C8 9C2A E70D 2FC8 27DF  0BFF 457A 6EE4 A1A1 9ED6
   uid                      nymea GmbH <developer@nymea.io>
   sub   rsa4096 2016-04-08 [E]
   sub   rsa4096 2016-04-08 [S]

Repository setup
----------------

Choose the repository format for your distribution version.

.. raw:: html

   <div class="nymea-tabs">
     <div class="nymea-tab-list" role="tablist" aria-label="Repository format">
       <button class="nymea-tab" id="stable-list-tab" type="button" role="tab" aria-selected="true" aria-controls="stable-list-panel">Debian 12 / Ubuntu 20.04-24.04</button>
       <button class="nymea-tab" id="stable-sources-tab" type="button" role="tab" aria-selected="false" aria-controls="stable-sources-panel">Debian 13 / Ubuntu 26.04</button>
     </div>
     <div class="nymea-tab-panel" id="stable-list-panel" role="tabpanel" aria-labelledby="stable-list-tab">
       <p>Use the classic list format. Replace <code>bookworm</code> with the matching distribution codename: <code>focal</code>, <code>jammy</code> or <code>noble</code>.</p>
       <div class="nymea-code-block"><pre><code>sudo tee /etc/apt/sources.list.d/nymea.list &gt; /dev/null &lt;&lt;EOM
   deb http://repository.nymea.io bookworm main non-free
   deb-src http://repository.nymea.io bookworm main non-free
   EOM</code></pre></div>
     </div>
     <div class="nymea-tab-panel" id="stable-sources-panel" role="tabpanel" aria-labelledby="stable-sources-tab" hidden>
       <p>Use the deb822 source format. Replace <code>trixie</code> with <code>resolute</code> when installing on Ubuntu 26.04.</p>
       <div class="nymea-code-block"><pre><code>sudo tee /etc/apt/sources.list.d/nymea.sources &gt; /dev/null &lt;&lt;EOM
   Types: deb deb-src
   URIs: http://repository.nymea.io
   Suites: trixie
   Components: main non-free
   Signed-By: /etc/apt/trusted.gpg.d/nymea.gpg
   EOM</code></pre></div>
     </div>
   </div>
