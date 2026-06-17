.. _doc-developers-environment:

Environment variables
=====================

``nymead`` reads several environment variables at startup. They are useful for development,
debugging and for deployments where the configuration or plugin directories need to be relocated.

The tables below group the variables by purpose. Path-based variables use a colon-separated list on
Unix-like systems.

Runtime configuration
---------------------

.. rst-class:: nymea-env-table

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Variable
     - Description
   * - ``NYMEA_CONFIG_PATH``
     - Overrides the runtime configuration directory. This is the directory where ``nymead`` reads
       and writes its live configuration files. The ``--configuration`` option overrides this
       variable.
   * - ``NYMEA_DEFAULT_CONFIG_PATH``
     - Overrides the read-only default configuration directory used to seed missing configuration
       files.
   * - ``NYMEA_TRANSLATIONS_PATH``
     - Overrides the directory used to load translation files.
   * - ``NYMEA_INSECURE_INTERFACES_DISABLED``
     - If set to a value other than ``0``, ``nymead`` disables insecure core interfaces, including
       unauthenticated or unencrypted interfaces.

Integration plugins
-------------------

.. rst-class:: nymea-env-table

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Variable
     - Description
   * - ``NYMEA_PLUGINS_PATH``
     - Colon-separated list of integration plugin directories. If set, it replaces the built-in
       default integration plugin search path.
   * - ``NYMEA_PLUGINS_EXTRA_PATH``
     - Colon-separated list of additional integration plugin directories searched before the
       default integration plugin path.

Platform plugins
----------------

.. rst-class:: nymea-env-table

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Variable
     - Description
   * - ``NYMEA_PLATFORM_PLUGINS_PATH``
     - Colon-separated list of platform plugin directories. If set, it replaces the built-in default
       platform plugin search path.
   * - ``NYMEA_PLATFORM_PLUGINS_EXTRA_PATH``
     - Colon-separated list of additional platform plugin directories searched before the default
       platform plugin path.

API keys plugins
----------------

.. rst-class:: nymea-env-table

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Variable
     - Description
   * - ``NYMEA_APIKEYS_PLUGINS_PATH``
     - Colon-separated list of API keys provider plugin directories. If set, it replaces the
       built-in default API keys provider search path.
   * - ``NYMEA_APIKEYS_PLUGINS_EXTRA_PATH``
     - Colon-separated list of additional API keys provider plugin directories searched before the
       default API keys provider path.

Experience plugins
------------------

.. rst-class:: nymea-env-table

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Variable
     - Description
   * - ``NYMEA_EXPERIENCE_PLUGINS_PATH``
     - Colon-separated list of experience plugin directories. If set, it replaces the built-in
       default experience plugin search path.
   * - ``NYMEA_EXPERIENCE_PLUGINS_EXTRA_PATH``
     - Colon-separated list of additional experience plugin directories searched before the default
       experience plugin path.

Z-Wave
------

.. rst-class:: nymea-env-table

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Variable
     - Description
   * - ``NYMEA_ZWAVE_PLUGIN_PATH``
     - Colon-separated list of Z-Wave backend plugin directories searched before the built-in default
       Z-Wave backend locations.

Other
-----

.. rst-class:: nymea-env-table

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Variable
     - Description
   * - ``DEVICE_SERIAL``
     - Provides a fallback device serial number if the active platform plugin does not implement one.
