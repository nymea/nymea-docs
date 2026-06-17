.. _integration-zigbeetradfri:

Connect and control ZigBee IKEA TRÅDFRI devices without TRÅDFRI gateway.

**Categories:** light, sensor, switch, socket

**Technologies:** zigbee

ZigBee TRÅDFRI
==============

ZigBee IKEA TRÅDFRI
-------------------


This plugin allows to interact with IKEA TRÅDFRI ZigBee devices using a native ZigBee network controller in nymea.

Supported Things
----------------


* TRADFRI bulb E27 CWS opal 600lm (color light)

* TRADFRI bulb E27 WS clear 806lm (color temperature light)

* `Wireless dimmer <https://www.ikea.com/us/en/p/tradfri-wireless-dimmer-white-10408598/>`__ *

* `Shortcut Button <https://www.ikea.com/us/en/p/tradfri-shortcut-button-white-20356382/>`__ *

* `Remote control <https://zigbee.blakadder.com/Ikea_E1810.html>`__ **May be discontinued.**

* `Symfonisk sound remote <https://www.ikea.com/us/en/p/symfonisk-sound-remote-white-20370482/>`__

* `Motion sensor <https://www.ikea.com/us/en/p/tradfri-wireless-motion-sensor-white-60377655/>`__

* `Signal repeater <https://www.ikea.com/us/en/p/tradfri-signal-repeater-30400407/>`__ -**DISCONTINUED**

* `Control outlet <https://www.ikea.com/us/en/p/tradfri-wireless-control-outlet-30356169/>`__

* `Starkvind air purifier <https://www.ikea.com/us/en/p/starkvind-air-purifier-black-smart-40501967/>`__

* `Fyrtur block-out roller blind <https://www.ikea.com/us/en/p/fyrtur-black-out-roller-blind-smart-wireless-battery-operated-gray-50417459/>`__

 
(*) Known working device firmware version: ``2.2.008``
(**) Known working device firmware version: ``2.3.014``

Pairing instructions
--------------------


Lights
------

Open the ZigBee network for joining. Switch the light off and on 6 times in a 1 second rythm. Once the light start flashing/dimming, the pairing process has been started successfully and the lamp will join the nymea ZigBee network.

Remotes/Sockets/Other
---------------------

Open the ZigBee network for joining. Click the connect button 4 times within 5 seconds.
