.. _doc-developers-clients:

Client development
==================

nymea exposes its full functionality through a JSON-RPC API. Client applications can interact with
nymea in three ways, depending on target platform and language.

JSON-RPC API
------------

The JSON-RPC API is the primary interface between clients and nymea:core. It runs over TCP sockets
or WebSockets, with or without SSL encryption. For a description of the wire protocol, connection
setup, authentication flow, and message format, see :doc:`json-rpc`. The full API reference is
available under :doc:`/documentation/resources/api/index`.

C++/Qt/QML
----------

For C++ or Qt/QML client applications, ``libnymea-app`` provides a complete Qt-style wrapper around
the JSON-RPC API. See :doc:`nymea-app-lib` for build instructions and usage examples.

Command-line client
-------------------

``nymea-cli`` is a terminal application for browsing, monitoring, and managing a connected nymea
system interactively. See :doc:`nymea-cli-dev` for details.

.. toctree::
   :maxdepth: 2
   :hidden:

   json-rpc
   nymea-app-lib
   nymea-cli-dev
