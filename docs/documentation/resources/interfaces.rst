Interfaces
==========

.. _interface-accesscontrol:

accesscontrol
-------------

.. code-block:: json

   {
     "events": [
       {
         "name": "accessGranted"
       },
       {
         "name": "accessDenied"
       }
     ]
   }

.. _interface-account:

account
-------

This is used to flag a thing that manages user a user account. It is similar to the gateway interface. For example, if there is a remote API that requires logging in but doesn't really offer any more functionality than that, this account shall be used. It inherits "connectable" which is used to flag if the remote server is unreachable. In addition, the "loggedIn" state indicates if the login fails. While logged in, the "userDisplayName" state should give the user's name in a pretty printed form. A client may reconfigure the device then to login again. Such device classes usually will cause auto-devices implementing the actual features as child devices.

.. code-block:: json

   {
     "description": "This is used to flag a thing that manages user a user account. It is similar to the gateway interface. For example, if there is a remote API that requires logging in but doesn't really offer any more functionality than that, this account shall be used. It inherits \"connectable\" which is used to flag if the remote server is unreachable. In addition, the \"loggedIn\" state indicates if the login fails. While logged in, the \"userDisplayName\" state should give the user's name in a pretty printed form. A client may reconfigure the device then to login again. Such device classes usually will cause auto-devices implementing the actual features as child devices.",
     "extends": "connectable",
     "states": [
       {
         "name": "loggedIn",
         "type": "bool"
       },
       {
         "name": "userDisplayName",
         "type": "QString",
         "optional": true
       }
     ]
   }

See also: `connectable <#interface-connectable>`__

.. _interface-alarm:

alarm
-----

An interface for alarms, such as fire or intruder alarms.

.. code-block:: json

   {
     "description": "An interface for alarms, such as fire or intruder alarms.",
     "actions": [
       {
         "name": "alarm",
         "logged": true
       }
     ]
   }

.. _interface-alert:

alert
-----

Used for things that have some sort of alert. For instance, light bulbs may be able to blink on alert actions, or speaker might be able to play an alert sound.

.. code-block:: json

   {
     "description": "Used for things that have some sort of alert. For instance, light bulbs may be able to blink on alert actions, or speaker might be able to play an alert sound.",
     "actions": [
       {
         "name": "alert"
       }
     ]
   }

.. _interface-awning:

awning
------

Simple awnings which can be opened and closed. Note that awnings operate inverted compared to other closables.

.. code-block:: json

   {
     "description": "Simple awnings which can be opened and closed. Note that awnings operate inverted compared to other closables.",
     "extends": "closable"
   }

See also: `closable <#interface-closable>`__

.. _interface-barcodescanner:

barcodescanner
--------------

.. code-block:: json

   {
     "events": [
       {
         "name": "codeScanned",
         "params": [
           {
             "name": "content",
             "type": "QString"
           }
         ],
         "logged": true
       }
     ]
   }

.. _interface-battery:

battery
-------

.. code-block:: json

   {
     "states": [
       {
         "name": "batteryCritical",
         "type": "bool",
         "logged": true
       },
       {
         "name": "batteryLevel",
         "type": "int",
         "minValue": 0,
         "maxValue": 100,
         "unit": "Percentage",
         "optional": true,
         "logged": true
       },
       {
         "name": "pluggedIn",
         "type": "bool",
         "optional": true
       },
       {
         "name": "chargingState",
         "type": "QString",
         "allowedValues": [
           "idle",
           "charging",
           "discharging"
         ],
         "optional": true
       }
     ]
   }

.. _interface-blind:

blind
-----

Simple blinds which can be opened and closed.

.. code-block:: json

   {
     "description": "Simple blinds which can be opened and closed.",
     "extends": "closable"
   }

See also: `closable <#interface-closable>`__

.. _interface-button:

button
------

The base for all buttons that emit a pressed event.

.. code-block:: json

   {
     "description": "The base for all buttons that emit a pressed event.",
     "events": [
       {
         "name": "pressed",
         "logged": true
       }
     ]
   }

.. _interface-childlock:

childlock
---------

Interface for devices that support a child lock on physical keys.

.. code-block:: json

   {
     "description": "Interface for devices that support a child lock on physical keys.",
     "states": [
       {
         "name": "childLock",
         "type": "bool",
         "writable": true,
         "logged": true
       }
     ]
   }

.. _interface-cleaningrobot:

cleaningrobot
-------------

An interface for cleaning robots. A paused robot is unpaused by calling pauseCleaning again. Calling startCleaning on a paused robot should restart the activity (or start a different one) if possible, else it should unpause the current activity. Cleaning robots may be browsable for "maps" to return a list of maps with map images in their thumbnail urls and "zones" (as child items of maps) returning a list of zones that can be cleaned by executing the according browser items. Zone items should provide JSON objects in their description, containing "vertices" to draw the zones in the image and "color" properties

.. code-block:: json

   {
     "description": "An interface for cleaning robots. A paused robot is unpaused by calling pauseCleaning again. Calling startCleaning on a paused robot should restart the activity (or start a different one) if possible, else it should unpause the current activity. Cleaning robots may be browsable for \"maps\" to return a list of maps with map images in their thumbnail urls and \"zones\" (as child items of maps) returning a list of zones that can be cleaned by executing the according browser items. Zone items should provide JSON objects in their description, containing \"vertices\" to draw the zones in the image and \"color\" properties",
     "states": [
       {
         "name": "robotState",
         "type": "QString",
         "possibleValues": [
           "docked",
           "cleaning",
           "paused",
           "traveling",
           "stopped",
           "error"
         ]
       },
       {
         "name": "errorMessage",
         "type": "QString",
         "optional": true
       }
     ],
     "actions": [
       {
         "name": "startCleaning"
       },
       {
         "name": "pauseCleaning"
       },
       {
         "name": "stopCleaning"
       },
       {
         "name": "returnToBase"
       }
     ]
   }

.. _interface-closable:

closable
--------

Interface for generic devices that can be opened and closed. The process of opening or closing can be interrupted by the stop action.

.. code-block:: json

   {
     "description": "Interface for generic devices that can be opened and closed. The process of opening or closing can be interrupted by the stop action.",
     "extends": "simpleclosable",
     "actions": [
       {
         "name": "stop"
       }
     ]
   }

See also: `simpleclosable <#interface-simpleclosable>`__

.. _interface-closablesensor:

closablesensor
--------------

This interface can be used for i.e. magnetic window/door sensors

.. code-block:: json

   {
     "description": "This interface can be used for i.e. magnetic window/door sensors",
     "extends": "sensor",
     "states": [
       {
         "name": "closed",
         "type": "bool",
         "logged": true
       }
     ]
   }

See also: `sensor <#interface-sensor>`__

.. _interface-co2sensor:

co2sensor
---------

CO2 (carbon dioxide) sensors. Measures co2 in parts per million.

.. code-block:: json

   {
     "extends": "sensor",
     "description": "CO2 (carbon dioxide) sensors. Measures co2 in parts per million.",
     "states": [
       {
         "name": "co2",
         "type": "double",
         "unit": "PartsPerMillion",
         "logged": true,
         "minValue": "any",
         "maxValue": "any"
       }
     ]
   }

See also: `sensor <#interface-sensor>`__

.. _interface-colorlight:

colorlight
----------

.. code-block:: json

   {
     "extends": "colortemperaturelight",
     "states": [
       {
         "name": "color",
         "type": "QColor",
         "writable": true
       }
     ]
   }

See also: `colortemperaturelight <#interface-colortemperaturelight>`__

.. _interface-colortemperaturelight:

colortemperaturelight
---------------------

.. code-block:: json

   {
     "extends": "dimmablelight",
     "states": [
       {
         "name": "colorTemperature",
         "type": "int",
         "minValue": "any",
         "maxValue": "any",
         "writable": true
       }
     ]
   }

See also: `dimmablelight <#interface-dimmablelight>`__

.. _interface-conductivitysensor:

conductivitysensor
------------------

.. code-block:: json

   {
     "extends": "sensor",
     "states": [
       {
         "name": "conductivity",
         "type": "double",
         "unit": "MicroSiemensPerCentimeter",
         "logged": true
       }
     ]
   }

See also: `sensor <#interface-sensor>`__

.. _interface-connectable:

connectable
-----------

.. code-block:: json

   {
     "states": [
       {
         "name": "connected",
         "type": "bool",
         "defaultValue": false,
         "logged": true
       }
     ]
   }

.. _interface-cooling:

cooling
-------

The cooling interface defines basic cooling appliances.

.. code-block:: json

   {
     "description": "The cooling interface defines basic cooling appliances.",
     "extends": "power",
     "states": [
       {
         "name": "percentage",
         "type": "int",
         "min": 0,
         "max": 100,
         "unit": "Percentage",
         "writable": true,
         "optional": true
       }
     ]
   }

See also: `power <#interface-power>`__

.. _interface-cosensor:

cosensor
--------

CO (carbon monoxide) sensors. Measures co in parts per million.

.. code-block:: json

   {
     "extends": "sensor",
     "description": "CO (carbon monoxide) sensors. Measures co in parts per million.",
     "states": [
       {
         "name": "co",
         "type": "double",
         "unit": "PartsPerMillion",
         "minValue": 0,
         "maxValue": 255,
         "logged": true
       }
     ]
   }

See also: `sensor <#interface-sensor>`__

.. _interface-daylightsensor:

daylightsensor
--------------

Devices implementing the daylight sensor interface have a boolean state indicating if currently is daylight. Additionally the current times for sunrise and sunset are provided.

.. code-block:: json

   {
     "extends": "sensor",
     "description": "Devices implementing the daylight sensor interface have a boolean state indicating if currently is daylight. Additionally the current times for sunrise and sunset are provided.",
     "states": [
       {
         "name": "daylight",
         "type": "bool",
         "logged": true
       },
       {
         "name": "sunriseTime",
         "unit": "UnixTime",
         "type": "int"
       },
       {
         "name": "sunsetTime",
         "unit": "UnixTime",
         "type": "int"
       }
     ]
   }

See also: `sensor <#interface-sensor>`__

.. _interface-dimmablelight:

dimmablelight
-------------

.. code-block:: json

   {
     "extends": "light",
     "states": [
       {
         "name": "brightness",
         "type": "int",
         "minValue": 0,
         "maxValue": 100,
         "writable": true
       }
     ]
   }

See also: `light <#interface-light>`__

.. _interface-doorbell:

doorbell
--------

An interface for doorbells. Emits "doorbellPressed" when the doorbell is pressed.

.. code-block:: json

   {
     "description": "An interface for doorbells. Emits \"doorbellPressed\" when the doorbell is pressed.",
     "events": [
       {
         "name": "doorbellPressed",
         "logged": true
       }
     ]
   }

.. _interface-electricvehicle:

electricvehicle
---------------

Interface for electric vehicles. Some cars require a minimum charging current to start charging (typically 6 A), and may also enforce a maximum charging current even if the charger supports more.

.. code-block:: json

   {
     "description": "Interface for electric vehicles. Some cars require a minimum charging current to start charging (typically 6 A), and may also enforce a maximum charging current even if the charger supports more.",
     "extends": [
       "battery"
     ],
     "states": [
       {
         "name": "capacity",
         "type": "double",
         "unit": "KiloWattHour"
       },
       {
         "name": "minChargingCurrent",
         "type": "uint",
         "unit": "Ampere",
         "minValue": 6,
         "maxValue": 16,
         "optional": true
       },
       {
         "name": "maxChargingCurrent",
         "type": "uint",
         "unit": "Ampere",
         "minValue": 16,
         "maxValue": 80,
         "optional": true
       },
       {
         "name": "phaseCount",
         "type": "uint",
         "minValue": 1,
         "maxValue": 3,
         "optional": true
       }
     ]
   }

See also: `battery <#interface-battery>`__

.. _interface-energymeter:

energymeter
-----------

Energy meters measure electric power consumption/production on 1, 2 or 3 phases. Often used as root measurements. If a meter uses more than 1 phase, as many states as possible for each phase shall be implemented. If there is only one phase, the total energy, total current etc. including voltage and current for phase A should be implemented.

.. code-block:: json

   {
     "description": "Energy meters measure electric power consumption/production on 1, 2 or 3 phases. Often used as root measurements. If a meter uses more than 1 phase, as many states as possible for each phase shall be implemented. If there is only one phase, the total energy, total current etc. including voltage and current for phase A should be implemented.",
     "extends": [
       "smartmeter"
     ],
     "states": [
       {
         "name": "totalEnergyConsumed",
         "type": "double",
         "unit": "KiloWattHour",
         "logged": true
       },
       {
         "name": "totalEnergyProduced",
         "type": "double",
         "unit": "KiloWattHour",
         "logged": true
       },
       {
         "name": "currentPower",
         "type": "double",
         "unit": "Watt",
         "logged": true
       },
       {
         "name": "energyConsumedPhaseA",
         "type": "double",
         "unit": "KiloWattHour",
         "optional": true
       },
       {
         "name": "energyConsumedPhaseB",
         "type": "double",
         "unit": "KiloWattHour",
         "optional": true
       },
       {
         "name": "energyConsumedPhaseC",
         "type": "double",
         "unit": "KiloWattHour",
         "optional": true
       },
       {
         "name": "energyProducedPhaseA",
         "type": "double",
         "unit": "KiloWattHour",
         "optional": true
       },
       {
         "name": "energyProducedPhaseB",
         "type": "double",
         "unit": "KiloWattHour",
         "optional": true
       },
       {
         "name": "energyProducedPhaseC",
         "type": "double",
         "unit": "KiloWattHour",
         "optional": true
       },
       {
         "name": "currentPowerPhaseA",
         "type": "double",
         "unit": "Watt",
         "optional": true
       },
       {
         "name": "currentPowerPhaseB",
         "type": "double",
         "unit": "Watt",
         "optional": true
       },
       {
         "name": "currentPowerPhaseC",
         "type": "double",
         "unit": "Watt",
         "optional": true
       },
       {
         "name": "currentPhaseA",
         "type": "double",
         "unit": "Ampere"
       },
       {
         "name": "currentPhaseB",
         "type": "double",
         "unit": "Ampere",
         "optional": true
       },
       {
         "name": "currentPhaseC",
         "type": "double",
         "unit": "Ampere",
         "optional": true
       },
       {
         "name": "voltagePhaseA",
         "type": "double",
         "unit": "Volt"
       },
       {
         "name": "voltagePhaseB",
         "type": "double",
         "unit": "Volt",
         "optional": true
       },
       {
         "name": "voltagePhaseC",
         "type": "double",
         "unit": "Volt",
         "optional": true
       }
     ]
   }

See also: `smartmeter <#interface-smartmeter>`__

.. _interface-energystorage:

energystorage
-------------

Interfaces for devices that store electrical energy and can return it at a later point, such as batteries. The currentPower state follows the usual convention that positive is 'consumed' energy and negative values represent 'produced' or in this case 'returned' energy.

.. code-block:: json

   {
     "description": "Interfaces for devices that store electrical energy and can return it at a later point, such as batteries. The currentPower state follows the usual convention that positive is 'consumed' energy and negative values represent 'produced' or in this case 'returned' energy.",
     "extends": [
       "battery",
       "smartmeter"
     ],
     "states": [
       {
         "name": "currentPower",
         "type": "double",
         "unit": "Watt",
         "logged": true
       },
       {
         "name": "capacity",
         "type": "double",
         "unit": "KiloWattHour"
       }
     ]
   }

See also: `battery <#interface-battery>`__, `smartmeter <#interface-smartmeter>`__

.. _interface-evcharger:

evcharger
---------

An electric vehicle charger. Extends the power interface to report plug/charge state and session energy, and to optionally control charging current and phase count in addition to on/off power control.

.. code-block:: json

   {
     "description": "An electric vehicle charger. Extends the power interface to report plug/charge state and session energy, and to optionally control charging current and phase count in addition to on/off power control.",
     "extends": [
       "power"
     ],
     "states": [
       {
         "name": "maxChargingCurrent",
         "type": "double",
         "writable": true,
         "unit": "Ampere",
         "minValue": "any",
         "maxValue": "any"
       },
       {
         "name": "pluggedIn",
         "type": "bool",
         "optional": true
       },
       {
         "name": "charging",
         "type": "bool",
         "logged": true,
         "optional": true
       },
       {
         "name": "phaseCount",
         "type": "uint",
         "minValue": 1,
         "maxValue": 3,
         "optional": true
       },
       {
         "name": "desiredPhaseCount",
         "type": "uint",
         "minValue": 1,
         "maxValue": 3,
         "possibleValues": "any",
         "writable": true,
         "optional": true
       },
       {
         "name": "sessionEnergy",
         "type": "double",
         "logged": true,
         "unit": "KiloWattHour",
         "optional": true
       }
     ]
   }

See also: `power <#interface-power>`__

.. _interface-extendedawning:

extendedawning
--------------

Awnings that support indicating their position and the moving state. Note that awnings operate inverted compared to other closables.

.. code-block:: json

   {
     "description": "Awnings that support indicating their position and the moving state. Note that awnings operate inverted compared to other closables.",
     "extends": [
       "awning",
       "extendedclosable"
     ]
   }

See also: `awning <#interface-awning>`__, `extendedclosable <#interface-extendedclosable>`__

.. _interface-extendedblind:

extendedblind
-------------

Blinds that support indicating their position and the moving state.

.. code-block:: json

   {
     "description": "Blinds that support indicating their position and the moving state.",
     "extends": [
       "blind",
       "extendedclosable"
     ]
   }

See also: `blind <#interface-blind>`__, `extendedclosable <#interface-extendedclosable>`__

.. _interface-extendedclosable:

extendedclosable
----------------

A more advanced form of devices that support opening and closing in a more fine grained manner. They can report whether the opening/closing is currently in progress and provide a percentage of the opening/closing position. 0% means fully opened, while 100% indicates the device is fully closed

.. code-block:: json

   {
     "description": "A more advanced form of devices that support opening and closing in a more fine grained manner. They can report whether the opening/closing is currently in progress and provide a percentage of the opening/closing position. 0% means fully opened, while 100% indicates the device is fully closed",
     "extends": "closable",
     "states": [
       {
         "name": "moving",
         "type": "bool",
         "logged": true
       },
       {
         "name": "percentage",
         "type": "int",
         "unit": "Percentage",
         "minValue": 0,
         "maxValue": 100,
         "writable": true
       }
     ]
   }

See also: `closable <#interface-closable>`__

.. _interface-extendednavigationpad:

extendednavigationpad
---------------------

The extended media interface offers also the info and menu button of media devices.

.. code-block:: json

   {
     "description": "The extended media interface offers also the info and menu button of media devices.",
     "extends": "navigationpad",
     "actions": [
       {
         "name": "navigate",
         "params": [
           {
             "name": "to",
             "type": "QString",
             "allowedValues": [
               "up",
               "down",
               "left",
               "right",
               "enter",
               "back",
               "menu",
               "info",
               "home"
             ]
           }
         ]
       }
     ]
   }

See also: `navigationpad <#interface-navigationpad>`__

.. _interface-extendedshutter:

extendedshutter
---------------

Advanced roller shutters that support indicating their position and the moving state.

.. code-block:: json

   {
     "description": "Advanced roller shutters that support indicating their position and the moving state.",
     "extends": [
       "shutter",
       "extendedclosable"
     ]
   }

See also: `shutter <#interface-shutter>`__, `extendedclosable <#interface-extendedclosable>`__

.. _interface-extendedsmartmeterproducer:

extendedsmartmeterproducer
--------------------------

Like smartmeterproducer, but instead of only providing total produced energy, this also supports retrieving the current power supply rate. Note that currentPower is positive for producers but might also be negative if a device implements consumer and producer and currently consumes more than it produces.

.. code-block:: json

   {
     "description": "Like smartmeterproducer, but instead of only providing total produced energy, this also supports retrieving the current power supply rate. Note that currentPower is positive for producers but might also be negative if a device implements consumer and producer and currently consumes more than it produces.",
     "extends": "smartmeterproducer",
     "states": [
       {
         "name": "currentPower",
         "type": "double",
         "unit": "Watt",
         "logged": true
       }
     ]
   }

See also: `smartmeterproducer <#interface-smartmeterproducer>`__

.. _interface-extendedstatefulgaragedoor:

extendedstatefulgaragedoor
--------------------------

A garage door which can be controlled like an extended closable, that is, by reporting and taking a percentage of the position

.. code-block:: json

   {
     "description": "A garage door which can be controlled like an extended closable, that is, by reporting and taking a percentage of the position",
     "extends": [
       "statefulgaragedoor",
       "extendedclosable"
     ]
   }

See also: `statefulgaragedoor <#interface-statefulgaragedoor>`__, `extendedclosable <#interface-extendedclosable>`__

.. _interface-fingerprintreader:

fingerprintreader
-----------------

.. code-block:: json

   {
     "extends": "useraccesscontrol",
     "events": [
       {
         "name": "accessGranted",
         "params": [
           {
             "name": "userId",
             "type": "QString"
           },
           {
             "name": "finger",
             "type": "QString",
             "allowedValues": [
               "ThumbLeft",
               "IndexFingerLeft",
               "MiddleFingerLeft",
               "RingFingerLeft",
               "PinkyLeft",
               "ThumbRight",
               "IndexFingerRight",
               "MiddleFingerRight",
               "RingFingerRight",
               "PinkyRight"
             ]
           }
         ],
         "logged": true
       }
     ],
     "actions": [
       {
         "name": "addUser",
         "params": [
           {
             "name": "userId",
             "type": "QString"
           },
           {
             "name": "finger",
             "type": "QString",
             "allowedValues": [
               "ThumbLeft",
               "IndexFingerLeft",
               "MiddleFingerLeft",
               "RingFingerLeft",
               "PinkyLeft",
               "ThumbRight",
               "IndexFingerRight",
               "MiddleFingerRight",
               "RingFingerRight",
               "PinkyRight"
             ]
           }
         ]
       },
       {
         "name": "removeUser",
         "params": [
           {
             "name": "userId",
             "type": "QString"
           }
         ]
       }
     ]
   }

See also: `useraccesscontrol <#interface-useraccesscontrol>`__

.. _interface-firesensor:

firesensor
----------

An interface for fire/smoke sensors.

.. code-block:: json

   {
     "description": "An interface for fire/smoke sensors.",
     "extends": "sensor",
     "states": [
       {
         "name": "fireDetected",
         "type": "bool",
         "logged": true
       }
     ]
   }

See also: `sensor <#interface-sensor>`__

.. _interface-garagedoor:

garagedoor
----------

The base for all garage door interfaces. Can be used by the client to filter for garage doors in the system.

.. code-block:: json

   {
     "description": "The base for all garage door interfaces. Can be used by the client to filter for garage doors in the system."
   }

.. _interface-garagegate:

garagegate
----------

.. code-block:: json

   {
     "deprecated": "Use statefulgaragedoor instead",
     "extends": [
       "garagedoor",
       "closable"
     ],
     "states": [
       {
         "name": "state",
         "type": "QString",
         "allowedValues": [
           "open",
           "closed",
           "opening",
           "closing"
         ],
         "logged": true
       },
       {
         "name": "intermediatePosition",
         "type": "bool"
       }
     ]
   }

See also: `garagedoor <#interface-garagedoor>`__, `closable <#interface-closable>`__

.. _interface-gassensor:

gassensor
---------

Flammable gas (LPG, Propane, Methane etc) sensors. Measures co2 in parts per million.

.. code-block:: json

   {
     "extends": "sensor",
     "description": "Flammable gas (LPG, Propane, Methane etc) sensors. Measures co2 in parts per million.",
     "states": [
       {
         "name": "gasLevel",
         "type": "double",
         "unit": "PartsPerMillion",
         "logged": true
       }
     ]
   }

See also: `sensor <#interface-sensor>`__

.. _interface-gateway:

gateway
-------

The gateway interface is used for gateway devices like bridges to other networks. For instance Ethernet to Zigbee bridges, Ethernet to RF bridges or similar. Typically such device classes implement the actual functionality in child devices that will auto-appear after successful connection to the gateway/bridge.

.. code-block:: json

   {
     "description": "The gateway interface is used for gateway devices like bridges to other networks. For instance Ethernet to Zigbee bridges, Ethernet to RF bridges or similar. Typically such device classes implement the actual functionality in child devices that will auto-appear after successful connection to the gateway/bridge.",
     "extends": "connectable"
   }

See also: `connectable <#interface-connectable>`__

.. _interface-heating:

heating
-------

The heating interface defines basic heating appliances.

.. code-block:: json

   {
     "description": "The heating interface defines basic heating appliances.",
     "extends": "power",
     "states": [
       {
         "name": "percentage",
         "type": "int",
         "min": 0,
         "max": 100,
         "unit": "Percentage",
         "writable": true,
         "optional": true
       }
     ]
   }

See also: `power <#interface-power>`__

.. _interface-heatpump:

heatpump
--------

The base for all heat pump interfaces. Can be used by the client to filter for heat pumps in the system.

.. code-block:: json

   {
     "description": "The base for all heat pump interfaces. Can be used by the client to filter for heat pumps in the system.",
     "states": [
       {
         "name": "outdoorTemperature",
         "type": "double",
         "unit": "DegreeCelsius",
         "logged": true,
         "optional": true
       },
       {
         "name": "hotWaterTemperature",
         "type": "double",
         "unit": "DegreeCelsius",
         "logged": true,
         "optional": true
       },
       {
         "name": "returnTemperature",
         "type": "double",
         "unit": "DegreeCelsius",
         "logged": true,
         "optional": true
       },
       {
         "name": "flowTemperature",
         "type": "double",
         "unit": "DegreeCelsius",
         "logged": true,
         "optional": true
       }
     ]
   }

.. _interface-humiditysensor:

humiditysensor
--------------

.. code-block:: json

   {
     "extends": "sensor",
     "states": [
       {
         "name": "humidity",
         "type": "double",
         "unit": "Percentage",
         "minValue": 0,
         "maxValue": 100,
         "logged": true
       }
     ]
   }

See also: `sensor <#interface-sensor>`__

.. _interface-impulsegaragedoor:

impulsegaragedoor
-----------------

This interface is for the simplest form of garage doors which can be controlled only via an impulse. Triggering the impulse will start moving the door, triggering it again will stop the movement. Triggering it yet another time will start movement in the reverse direction. Note that there is no feedback channel on such devices. The system has no chance of knowing the current state this device is actually in.

.. code-block:: json

   {
     "extends": "garagedoor",
     "description": "This interface is for the simplest form of garage doors which can be controlled only via an impulse. Triggering the impulse will start moving the door, triggering it again will stop the movement. Triggering it yet another time will start movement in the reverse direction. Note that there is no feedback channel on such devices. The system has no chance of knowing the current state this device is actually in.",
     "actions": [
       {
         "name": "triggerImpulse",
         "logged": true
       }
     ]
   }

See also: `garagedoor <#interface-garagedoor>`__

.. _interface-inputtrigger:

inputtrigger
------------

.. code-block:: json

   {
     "events": [
       {
         "name": "triggered",
         "logged": true
       }
     ]
   }

.. _interface-irrigation:

irrigation
----------

The irrigation interface is used for irrigation systems. It is used for water pumps or valves that supply any sort of irrigation. The power state turns irrigation on and off.

.. code-block:: json

   {
     "extends": "power",
     "description": "The irrigation interface is used for irrigation systems. It is used for water pumps or valves that supply any sort of irrigation. The power state turns irrigation on and off."
   }

See also: `power <#interface-power>`__

.. _interface-light:

light
-----

.. code-block:: json

   {
     "extends": "power"
   }

See also: `power <#interface-power>`__

.. _interface-lightsensor:

lightsensor
-----------

.. code-block:: json

   {
     "extends": "sensor",
     "states": [
       {
         "name": "lightIntensity",
         "type": "double",
         "unit": "Lux",
         "logged": true
       }
     ]
   }

See also: `sensor <#interface-sensor>`__

.. _interface-longpressbutton:

longpressbutton
---------------

A button that emits different events, pressed and longpressed, depending on how long the user presses it. Note that the button should only emit one of them at a time. I.e. don't emit pressed on botton down and later longPressed if the user keeps on holding the button. Such a longpress should only emit longPressed. Common practice is to emit pressed if a release event is received before a timeout expires, else emit longpress when the timeout expires.

.. code-block:: json

   {
     "description": "A button that emits different events, pressed and longpressed, depending on how long the user presses it. Note that the button should only emit one of them at a time. I.e. don't emit pressed on botton down and later longPressed if the user keeps on holding the button. Such a longpress should only emit longPressed. Common practice is to emit pressed if a release event is received before a timeout expires, else emit longpress when the timeout expires.",
     "extends": "button",
     "events": [
       {
         "name": "longPressed",
         "logged": true
       }
     ]
   }

See also: `button <#interface-button>`__

.. _interface-longpressmultibutton:

longpressmultibutton
--------------------

A remote control with multiple buttons that can distinguish between short and long presses. Note that the button should only emit one of them at a time. I.e. don't emit pressed on botton down and later longPressed if the user keeps on holding the button. Such a longpress should only emit longPressed. Common practice is to emit pressed if a release event is received before a timeout expires, else emit longpress when the timeout expires.

.. code-block:: json

   {
     "description": "A remote control with multiple buttons that can distinguish between short and long presses. Note that the button should only emit one of them at a time. I.e. don't emit pressed on botton down and later longPressed if the user keeps on holding the button. Such a longpress should only emit longPressed. Common practice is to emit pressed if a release event is received before a timeout expires, else emit longpress when the timeout expires.",
     "extends": "simplemultibutton",
     "events": [
       {
         "name": "longPressed",
         "params": [
           {
             "name": "buttonName",
             "type": "QString"
           }
         ],
         "logged": true
       }
     ]
   }

See also: `simplemultibutton <#interface-simplemultibutton>`__

.. _interface-media:

media
-----

The base for all media interfaces. Client applications might use this to group/filter things supporting media playback/control. When implementing a plugin use mediaplayer or mediacontroller for actual devices.

.. code-block:: json

   {
     "description": "The base for all media interfaces. Client applications might use this to group/filter things supporting media playback/control. When implementing a plugin use mediaplayer or mediacontroller for actual devices."
   }

.. _interface-mediacontroller:

mediacontroller
---------------

The mediacontroller interface contains actions to control media streams.

.. code-block:: json

   {
     "description": "The mediacontroller interface contains actions to control media streams.",
     "extends": "media",
     "states": [
       {
         "name": "shuffle",
         "type": "bool",
         "writable": true,
         "optional": true
       },
       {
         "name": "repeat",
         "type": "QString",
         "allowedValues": [
           "None",
           "One",
           "All"
         ],
         "writable": true,
         "optional": true
       },
       {
         "name": "like",
         "type": "bool",
         "writable": true,
         "optional": true
       },
       {
         "name": "equalizerPreset",
         "type": "QString",
         "allowedValues": "any",
         "writable": true,
         "optional": true
       },
       {
         "name": "nightMode",
         "type": "bool",
         "writable": true,
         "optional": true
       }
     ],
     "actions": [
       {
         "name": "skipBack"
       },
       {
         "name": "stop"
       },
       {
         "name": "play"
       },
       {
         "name": "pause"
       },
       {
         "name": "skipNext"
       },
       {
         "name": "fastForward",
         "optional": true
       },
       {
         "name": "fastRewind",
         "optional": true
       }
     ]
   }

See also: `media <#interface-media>`__

.. _interface-mediametadataprovider:

mediametadataprovider
---------------------

Provide media information, meant to be used in combination with mediaplayer. For music players, use collection to provide the album/compilation, for video players fill in the series name or a movie collection name there. Artwork can be a URL to a artwork image.

.. code-block:: json

   {
     "description": "Provide media information, meant to be used in combination with mediaplayer. For music players, use collection to provide the album/compilation, for video players fill in the series name or a movie collection name there. Artwork can be a URL to a artwork image.",
     "extends": "media",
     "states": [
       {
         "name": "title",
         "type": "QString"
       },
       {
         "name": "artist",
         "type": "QString"
       },
       {
         "name": "collection",
         "type": "QString"
       },
       {
         "name": "artwork",
         "type": "QString"
       }
     ]
   }

See also: `media <#interface-media>`__

.. _interface-mediaplayer:

mediaplayer
-----------

Media player interface. Used by devices/services which can play back media. Even if a device only supports e.g. audio, the playerType state must still be added to the metadata. It may default to a single value and never change in this case. Players supporting duration and play time should provide those values in seconds.

.. code-block:: json

   {
     "description": "Media player interface. Used by devices/services which can play back media. Even if a device only supports e.g. audio, the playerType state must still be added to the metadata. It may default to a single value and never change in this case. Players supporting duration and play time should provide those values in seconds.",
     "extends": "media",
     "states": [
       {
         "name": "playbackStatus",
         "type": "QString",
         "allowedValues": [
           "Playing",
           "Paused",
           "Stopped"
         ]
       },
       {
         "name": "playerType",
         "type": "QString",
         "allowedValues": [
           "audio",
           "video"
         ]
       },
       {
         "name": "inputSource",
         "type": "QString",
         "allowedValues": "any",
         "writable": true,
         "optional": true
       },
       {
         "name": "playDuration",
         "type": "uint",
         "unit": "Seconds",
         "optional": true
       },
       {
         "name": "playTime",
         "type": "uint",
         "unit": "Seconds",
         "optional": true
       }
     ]
   }

See also: `media <#interface-media>`__

.. _interface-moisturesensor:

moisturesensor
--------------

.. code-block:: json

   {
     "extends": "sensor",
     "states": [
       {
         "name": "moisture",
         "type": "double",
         "logged": true
       }
     ]
   }

See also: `sensor <#interface-sensor>`__

.. _interface-multibutton:

multibutton
-----------

A remote control with multiple buttons. Emits pressed(buttonName) on button presses.

.. code-block:: json

   {
     "description": "A remote control with multiple buttons. Emits pressed(buttonName) on button presses.",
     "extends": "button",
     "events": [
       {
         "name": "pressed",
         "params": [
           {
             "name": "buttonName",
             "type": "QString"
           }
         ],
         "logged": true
       }
     ]
   }

See also: `button <#interface-button>`__

.. _interface-navigationpad:

navigationpad
-------------

Many media devices have a navigation pad for browsing a library or a menu. This interface represents a basic navigation pad.

.. code-block:: json

   {
     "description": "Many media devices have a navigation pad for browsing a library or a menu. This interface represents a basic navigation pad.",
     "extends": "media",
     "actions": [
       {
         "name": "navigate",
         "params": [
           {
             "name": "to",
             "type": "QString",
             "allowedValues": [
               "up",
               "down",
               "left",
               "right",
               "enter",
               "back"
             ]
           }
         ]
       }
     ]
   }

See also: `media <#interface-media>`__

.. _interface-networkdevice:

networkdevice
-------------

Things implementing this interface make use of the network device discovery resource and the network device monitor. This interface makes sure all relevant information will be stored. Depending on the MonitorMode of the discovered NetworkDeviceInfo the params of this thing shall be filled in. This makes sure the monitor uses the correct method to monitor the network device presence and IP. If the Mode is MAC, just sotre the mac address param and leave the others empty. If the Mode is HostName, just fill in the host name parameter. If the Mode is IP, just the address.

.. code-block:: json

   {
     "description": "Things implementing this interface make use of the network device discovery resource and the network device monitor. This interface makes sure all relevant information will be stored. Depending on the MonitorMode of the discovered NetworkDeviceInfo the params of this thing shall be filled in. This makes sure the monitor uses the correct method to monitor the network device presence and IP. If the Mode is MAC, just sotre the mac address param and leave the others empty. If the Mode is HostName, just fill in the host name parameter. If the Mode is IP, just the address.",
     "params": [
       {
         "name": "address",
         "type": "QString"
       },
       {
         "name": "hostName",
         "type": "QString"
       },
       {
         "name": "macAddress",
         "type": "QString"
       }
     ]
   }

.. _interface-no2sensor:

no2sensor
---------

Interface for nitrogen dioxide sensors. NO2 is measured in µg/m3.

.. code-block:: json

   {
     "description": "Interface for nitrogen dioxide sensors. NO2 is measured in \u00b5g/m3.",
     "extends": "sensor",
     "states": [
       {
         "name": "no2",
         "type": "double",
         "unit": "MicroGrammPerCubicalMeter",
         "minValue": 0,
         "maxValue": 800,
         "logged": true
       }
     ]
   }

See also: `sensor <#interface-sensor>`__

.. _interface-noisesensor:

noisesensor
-----------

A sensor interface for noise sensors. Should deliver a median noise level in regular intervals. This is meant for overall noise level monitoring (e.g. in buildings) and not real time audio processing.

.. code-block:: json

   {
     "extends": "sensor",
     "description": "A sensor interface for noise sensors. Should deliver a median noise level in regular intervals. This is meant for overall noise level monitoring (e.g. in buildings) and not real time audio processing.",
     "states": [
       {
         "name": "noise",
         "type": "double",
         "unit": "Dezibel",
         "logged": true
       }
     ]
   }

See also: `sensor <#interface-sensor>`__

.. _interface-notifications:

notifications
-------------

.. code-block:: json

   {
     "actions": [
       {
         "name": "notify",
         "params": [
           {
             "name": "title",
             "type": "QString"
           },
           {
             "name": "body",
             "type": "QString"
           }
         ],
         "logged": true
       }
     ]
   }

.. _interface-o2sensor:

o2sensor
--------

Interface for oxygen sensors. O2 saturation in percentage is mandatory, optionally more advanced sensors may offer O2 values in milligrams per liter (mg/L).

.. code-block:: json

   {
     "description": "Interface for oxygen sensors. O2 saturation in percentage is mandatory, optionally more advanced sensors may offer O2 values in milligrams per liter (mg/L).",
     "extends": "sensor",
     "states": [
       {
         "name": "o2saturation",
         "type": "double",
         "unit": "Percentage",
         "logged": true
       },
       {
         "name": "o2",
         "type": "double",
         "unit": "MilligramPerLiter",
         "logged": true,
         "optional": true
       }
     ]
   }

See also: `sensor <#interface-sensor>`__

.. _interface-o3sensor:

o3sensor
--------

O3 (ozone) sensors. Measures o3 in parts per million.

.. code-block:: json

   {
     "extends": "sensor",
     "description": "O3 (ozone) sensors. Measures o3 in parts per million.",
     "states": [
       {
         "name": "o3",
         "type": "double",
         "unit": "MicroGrammPerCubicalMeter",
         "minValue": 0,
         "maxValue": 500,
         "logged": true
       }
     ]
   }

See also: `sensor <#interface-sensor>`__

.. _interface-orpsensor:

orpsensor
---------

Interface for ORP (Oxidation Reduction Potential) sensors.

.. code-block:: json

   {
     "description": "Interface for ORP (Oxidation Reduction Potential) sensors.",
     "extends": "sensor",
     "states": [
       {
         "name": "orp",
         "type": "double",
         "unit": "MilliVolt",
         "logged": true
       }
     ]
   }

See also: `sensor <#interface-sensor>`__

.. _interface-outputtrigger:

outputtrigger
-------------

.. code-block:: json

   {
     "actions": [
       {
         "name": "trigger"
       }
     ]
   }

.. _interface-phsensor:

phsensor
--------

Interface for PH sensors.

.. code-block:: json

   {
     "description": "Interface for PH sensors.",
     "extends": "sensor",
     "states": [
       {
         "name": "ph",
         "type": "double",
         "minValue": 0,
         "maxValue": 14,
         "logged": true
       }
     ]
   }

See also: `sensor <#interface-sensor>`__

.. _interface-pm10sensor:

pm10sensor
----------

PM10 (Coarse particles) sensors. Measures PM10 particles in µg/m3.

.. code-block:: json

   {
     "extends": "sensor",
     "description": "PM10 (Coarse particles) sensors. Measures PM10 particles in \u00b5g/m3.",
     "states": [
       {
         "name": "pm10",
         "type": "double",
         "unit": "MicroGrammPerCubicalMeter",
         "minValue": 0,
         "maxValue": 500,
         "logged": true
       }
     ]
   }

See also: `sensor <#interface-sensor>`__

.. _interface-pm25sensor:

pm25sensor
----------

PM2.5 (Fine particles) sensors. Measures PM2.5 particles in µg/m3.

.. code-block:: json

   {
     "extends": "sensor",
     "description": "PM2.5 (Fine particles) sensors. Measures PM2.5 particles in \u00b5g/m3.",
     "states": [
       {
         "name": "pm25",
         "type": "double",
         "unit": "MicroGrammPerCubicalMeter",
         "minValue": 0,
         "maxValue": 500,
         "logged": true
       }
     ]
   }

See also: `sensor <#interface-sensor>`__

.. _interface-power:

power
-----

.. code-block:: json

   {
     "states": [
       {
         "name": "power",
         "type": "bool",
         "writable": true,
         "logged": true
       }
     ]
   }

.. _interface-powersocket:

powersocket
-----------

The powersocket interface is used for smart power sockets and just extends the simple power interface.

.. code-block:: json

   {
     "extends": "power",
     "description": "The powersocket interface is used for smart power sockets and just extends the simple power interface."
   }

See also: `power <#interface-power>`__

.. _interface-powerswitch:

powerswitch
-----------

The powerswitch interface is used for smart power switches and just extends the simple button interface. Use this for switches that can be on or off.

.. code-block:: json

   {
     "extends": "button",
     "description": "The powerswitch interface is used for smart power switches and just extends the simple button interface. Use this for switches that can be on or off.",
     "states": [
       {
         "name": "power",
         "type": "bool"
       }
     ]
   }

See also: `button <#interface-button>`__

.. _interface-presencesensor:

presencesensor
--------------

The presence sensor interface provides information whether a certain thing, for instance a human person, a tracked animal, a tracked mobile phone or smart watch is currently present. Additionally it gives information about the last time the tracked thing has been seen.

.. code-block:: json

   {
     "extends": "sensor",
     "description": "The presence sensor interface provides information whether a certain thing, for instance a human person, a tracked animal, a tracked mobile phone or smart watch is currently present. Additionally it gives information about the last time the tracked thing has been seen.",
     "states": [
       {
         "name": "isPresent",
         "type": "bool",
         "logged": true
       }
     ]
   }

See also: `sensor <#interface-sensor>`__

.. _interface-pressuresensor:

pressuresensor
--------------

.. code-block:: json

   {
     "extends": "sensor",
     "states": [
       {
         "name": "pressure",
         "type": "double",
         "unit": "MilliBar",
         "minValue": "any",
         "maxValue": "any",
         "logged": true
       }
     ]
   }

See also: `sensor <#interface-sensor>`__

.. _interface-sensor:

sensor
------

.. code-block:: json

   {}

.. _interface-shutter:

shutter
-------

Simple roller shutters which can be opened and closed.

.. code-block:: json

   {
     "description": "Simple roller shutters which can be opened and closed.",
     "extends": "closable"
   }

See also: `closable <#interface-closable>`__

.. _interface-simplebutton:

simplebutton
------------

Deprecated - Use button instead.

.. code-block:: json

   {
     "extends": "button",
     "description": "Deprecated - Use button instead."
   }

See also: `button <#interface-button>`__

.. _interface-simpleclosable:

simpleclosable
--------------

Interface for very basic devices that support opening and closing.

.. code-block:: json

   {
     "description": "Interface for very basic devices that support opening and closing.",
     "actions": [
       {
         "name": "open"
       },
       {
         "name": "close"
       }
     ]
   }

.. _interface-simplegaragedoor:

simplegaragedoor
----------------

A Garage door that can take up and down as commands but cannot provide state information

.. code-block:: json

   {
     "description": "A Garage door that can take up and down as commands but cannot provide state information",
     "extends": [
       "garagedoor",
       "closable"
     ]
   }

See also: `garagedoor <#interface-garagedoor>`__, `closable <#interface-closable>`__

.. _interface-simpleheatpump:

simpleheatpump
--------------

This interface can be used for heat pumps offering one digital input for switching on and off the entire heatpump. Some heat pumps have only this possibility to be controlled. Be aware what you are doing if you switch of a heat pump and for how long.

.. code-block:: json

   {
     "description": "This interface can be used for heat pumps offering one digital input for switching on and off the entire heatpump. Some heat pumps have only this possibility to be controlled. Be aware what you are doing if you switch of a heat pump and for how long.",
     "extends": [
       "heatpump",
       "power"
     ]
   }

See also: `heatpump <#interface-heatpump>`__, `power <#interface-power>`__

.. _interface-simplemultibutton:

simplemultibutton
-----------------

Deprecated - Use multibutton instead

.. code-block:: json

   {
     "description": "Deprecated - Use multibutton instead",
     "extends": "multibutton"
   }

See also: `multibutton <#interface-multibutton>`__

.. _interface-smartgridheatpump:

smartgridheatpump
-----------------

This interface can be used for heat pumps offering the smart grid label "SG-Ready". The modes can be set to the heatpump either through 2 digital outputs or directly using modbus registers. These modes should be used by an energy manager and are not intended to be set by a user since there are certain rules to consider when switching the SG mode.

.. code-block:: json

   {
     "description": "This interface can be used for heat pumps offering the smart grid label \"SG-Ready\". The modes can be set to the heatpump either through 2 digital outputs or directly using modbus registers. These modes should be used by an energy manager and are not intended to be set by a user since there are certain rules to consider when switching the SG mode.",
     "extends": "heatpump",
     "states": [
       {
         "name": "sgReadyMode",
         "type": "QString",
         "possibleValues": [
           "Off",
           "Low",
           "Standard",
           "High"
         ],
         "writable": true,
         "logged": true
       }
     ]
   }

See also: `heatpump <#interface-heatpump>`__

.. _interface-smartlock:

smartlock
---------

The smartlock interface is used for locks which can be opened digitally. The simplest form is a door opener which just unlatches the door lock for a few seconds so a person can enter. Implement the unlatch action and set the state to "unlatching" while opening. Set the state back to "locked" when done. More advanced devices might also allow keeping a door unlatched or distinguish between locked and unlocked. Fully electric doors might even support opening and closing the entire door by combining this interface with the "simpleclosable" interface.

.. code-block:: json

   {
     "description": "The smartlock interface is used for locks which can be opened digitally. The simplest form is a door opener which just unlatches the door lock for a few seconds so a person can enter. Implement the unlatch action and set the state to \"unlatching\" while opening. Set the state back to \"locked\" when done. More advanced devices might also allow keeping a door unlatched or distinguish between locked and unlocked. Fully electric doors might even support opening and closing the entire door by combining this interface with the \"simpleclosable\" interface.",
     "states": [
       {
         "name": "state",
         "type": "QString",
         "allowedValues": [
           "locked",
           "locking",
           "unlocked",
           "unlocking",
           "unlatched",
           "unlatching"
         ],
         "logged": true,
         "optional": true
       }
     ],
     "actions": [
       {
         "name": "lock"
       },
       {
         "name": "unlock"
       },
       {
         "name": "unlatch",
         "optional": true
       }
     ]
   }

.. _interface-smartmeter:

smartmeter
----------

Base interface for things that can monitor energy consumption/production.

.. code-block:: json

   {
     "description": "Base interface for things that can monitor energy consumption/production."
   }

.. _interface-smartmeterconsumer:

smartmeterconsumer
------------------

This interface is used for things that can monitor energy consumption. At least the grand total of the consumer energy is provided, optionally live monitoring of the current usage may be available.

.. code-block:: json

   {
     "description": "This interface is used for things that can monitor energy consumption. At least the grand total of the consumer energy is provided, optionally live monitoring of the current usage may be available.",
     "extends": "smartmeter",
     "states": [
       {
         "name": "totalEnergyConsumed",
         "type": "double",
         "unit": "KiloWattHour",
         "logged": true
       },
       {
         "name": "currentPower",
         "type": "double",
         "unit": "Watt",
         "logged": true
       }
     ]
   }

See also: `smartmeter <#interface-smartmeter>`__

.. _interface-smartmeterproducer:

smartmeterproducer
------------------

This interface is used for things that can monitor energy production. At least the grand total of the returned energy is provided, optionally live monitoring of the current production may be available. Please note that currentPower is always from a consumer perspective. Thus it will be a negative value for producing devices.

.. code-block:: json

   {
     "description": "This interface is used for things that can monitor energy production. At least the grand total of the returned energy is provided, optionally live monitoring of the current production may be available. Please note that currentPower is always from a consumer perspective. Thus it will be a negative value for producing devices.",
     "extends": "smartmeter",
     "states": [
       {
         "name": "totalEnergyProduced",
         "type": "double",
         "unit": "KiloWattHour",
         "logged": true
       },
       {
         "name": "currentPower",
         "type": "double",
         "unit": "Watt",
         "logged": true
       }
     ]
   }

See also: `smartmeter <#interface-smartmeter>`__

.. _interface-solarinverter:

solarinverter
-------------

Interface for solar inverters

.. code-block:: json

   {
     "description": "Interface for solar inverters",
     "extends": "smartmeterproducer"
   }

See also: `smartmeterproducer <#interface-smartmeterproducer>`__

.. _interface-statefulgaragedoor:

statefulgaragedoor
------------------

A garagedoor which can be controller like a closable, with open and close actions. It can report whether it's opened or closed or standing still something in between (intermediate position) as well as reporting that it's moving (opening/closing).

.. code-block:: json

   {
     "description": "A garagedoor which can be controller like a closable, with open and close actions. It can report whether it's opened or closed or standing still something in between (intermediate position) as well as reporting that it's moving (opening/closing).",
     "extends": [
       "garagedoor",
       "closable"
     ],
     "states": [
       {
         "name": "state",
         "type": "QString",
         "allowedValues": [
           "open",
           "closed",
           "opening",
           "closing",
           "intermediate"
         ],
         "logged": true
       }
     ]
   }

See also: `garagedoor <#interface-garagedoor>`__, `closable <#interface-closable>`__

.. _interface-system:

system
------

This interface is used to mark device classes as system-internal. The user interface will likely hide it.

.. code-block:: json

   {
     "description": "This interface is used to mark device classes as system-internal. The user interface will likely hide it."
   }

.. _interface-temperaturesensor:

temperaturesensor
-----------------

.. code-block:: json

   {
     "extends": "sensor",
     "states": [
       {
         "name": "temperature",
         "type": "double",
         "unit": "DegreeCelsius",
         "logged": true
       }
     ]
   }

See also: `sensor <#interface-sensor>`__

.. _interface-thermostat:

thermostat
----------

The thermostat interface describes devices which have a target temperature value and regulate themselves to match that target temperature. A thermostat may support detecting for open windows in which case the windowOpenDetected state should be implemented. On the other hand, a thermostat may allow setting a window open lock in which case the windowOpen state should be implemented.

.. code-block:: json

   {
     "description": "The thermostat interface describes devices which have a target temperature value and regulate themselves to match that target temperature. A thermostat may support detecting for open windows in which case the windowOpenDetected state should be implemented. On the other hand, a thermostat may allow setting a window open lock in which case the windowOpen state should be implemented.",
     "states": [
       {
         "name": "targetTemperature",
         "type": "double",
         "unit": "DegreeCelsius",
         "minValue": "any",
         "maxValue": "any",
         "writable": true,
         "logged": true
       },
       {
         "name": "temperature",
         "type": "double",
         "unit": "DegreeCelsius",
         "optional": true,
         "logged": true
       },
       {
         "name": "heatingOn",
         "type": "bool",
         "optional": true,
         "logged": true
       },
       {
         "name": "coolingOn",
         "type": "bool",
         "optional": true,
         "logged": true
       },
       {
         "name": "boost",
         "type": "bool",
         "optional": true,
         "logged": true
       },
       {
         "name": "windowOpen",
         "type": "bool",
         "writable": true,
         "optional": true,
         "logged": true
       },
       {
         "name": "windowOpenDetected",
         "type": "bool",
         "optional": true,
         "logged": true
       }
     ]
   }

.. _interface-update:

update
------

The update interface is used for things that support being updated by nymea.

.. code-block:: json

   {
     "description": "The update interface is used for things that support being updated by nymea.",
     "states": [
       {
         "name": "updateStatus",
         "type": "QString",
         "allowedValues": [
           "idle",
           "available",
           "updating"
         ]
       },
       {
         "name": "currentVersion",
         "type": "QString",
         "logged": true
       },
       {
         "name": "availableVersion",
         "type": "QString",
         "optional": true
       },
       {
         "name": "updateProgress",
         "type": "uint",
         "unit": "Percentage",
         "min": 0,
         "max": 100,
         "optional": true
       }
     ],
     "actions": [
       {
         "name": "performUpdate"
       }
     ]
   }

.. _interface-useraccesscontrol:

useraccesscontrol
-----------------

.. code-block:: json

   {
     "extends": "accesscontrol",
     "states": [
       {
         "name": "users",
         "type": "QStringList"
       }
     ],
     "events": [
       {
         "name": "accessGranted",
         "params": [
           {
             "name": "userId",
             "type": "QString"
           }
         ],
         "logged": true
       }
     ],
     "actions": [
       {
         "name": "addUser",
         "params": [
           {
             "name": "userId",
             "type": "QString"
           }
         ],
         "logged": true
       },
       {
         "name": "removeUser",
         "params": [
           {
             "name": "userId",
             "type": "QString"
           }
         ],
         "logged": true
       }
     ]
   }

See also: `accesscontrol <#interface-accesscontrol>`__

.. _interface-venetianblind:

venetianblind
-------------

Venetian blinds that can be tilted. Venetian blinds must support an angle and specify the minimum and maximum supported angle. For instance, if a venetian blinds supports tilting from horizontal to vertical by 90°, the minValue should be set to 0° and the maxValue to 90°. For venetian blinds that support tilting both direction, that is, a total of 180°, the minValue should be -90° and the maxValue should be 90°. 0° is always the horizontal position. Note that the "moving" state should be true when either the percentage or the angle are moving.

.. code-block:: json

   {
     "description": "Venetian blinds that can be tilted. Venetian blinds must support an angle and specify the minimum and maximum supported angle. For instance, if a venetian blinds supports tilting from horizontal to vertical by 90\u00b0, the minValue should be set to 0\u00b0 and the maxValue to 90\u00b0. For venetian blinds that support tilting both direction, that is, a total of 180\u00b0, the minValue should be -90\u00b0 and the maxValue should be 90\u00b0. 0\u00b0 is always the horizontal position. Note that the \"moving\" state should be true when either the percentage or the angle are moving.",
     "extends": "extendedblind",
     "states": [
       {
         "name": "angle",
         "type": "int",
         "unit": "Degree",
         "minValue": "any",
         "maxValue": "any",
         "writable": true
       }
     ]
   }

See also: `extendedblind <#interface-extendedblind>`__

.. _interface-ventilation:

ventilation
-----------

The ventilation interface is used for any sort of ventilation. It extends the "power" interface and thus can be turned on or off. Optionally, the air flow can be controlled. The thing class must specify the minimum and maximum values for the flow control.

.. code-block:: json

   {
     "description": "The ventilation interface is used for any sort of ventilation. It extends the \"power\" interface and thus can be turned on or off. Optionally, the air flow can be controlled. The thing class must specify the minimum and maximum values for the flow control.",
     "extends": "power",
     "states": [
       {
         "name": "flowRate",
         "type": "int",
         "minValue": "any",
         "maxValue": "any",
         "writable": true,
         "optional": true,
         "logged": true
       }
     ]
   }

See also: `power <#interface-power>`__

.. _interface-vibrationsensor:

vibrationsensor
---------------

An interface for vibration sensors.

.. code-block:: json

   {
     "description": "An interface for vibration sensors.",
     "extends": "sensor",
     "events": [
       {
         "name": "vibrationDetected",
         "logged": true
       }
     ]
   }

See also: `sensor <#interface-sensor>`__

.. _interface-vocsensor:

vocsensor
---------

Sensor for volatile organic compounds (VOC).

.. code-block:: json

   {
     "description": "Sensor for volatile organic compounds (VOC).",
     "extends": "sensor",
     "states": [
       {
         "name": "voc",
         "type": "uint",
         "unit": "PartsPerBillion",
         "minValue": 0,
         "maxValue": 65353,
         "logged": true
       }
     ]
   }

See also: `sensor <#interface-sensor>`__

.. _interface-volumecontroller:

volumecontroller
----------------

.. code-block:: json

   {
     "desciption": "A volume controller allows to control volume and mute. At the very least, increaseVolume and decreaseVolume are to be implemented for devices that don't have a way to fetch the current volume. For devices allowing to set an absolute volume value, the volume and mute states should be implemented as well.",
     "extends": "media",
     "states": [
       {
         "name": "mute",
         "type": "bool",
         "writable": true,
         "optional": true
       },
       {
         "name": "volume",
         "type": "int",
         "minValue": "any",
         "maxValue": "any",
         "writable": true,
         "optional": true
       }
     ],
     "actions": [
       {
         "name": "increaseVolume"
       },
       {
         "name": "decreaseVolume"
       }
     ]
   }

See also: `media <#interface-media>`__

.. _interface-waterlevelsensor:

waterlevelsensor
----------------

Sensors that can measure water fill levels.

.. code-block:: json

   {
     "description": "Sensors that can measure water fill levels.",
     "extends": "sensor",
     "states": [
       {
         "name": "waterLevel",
         "type": "double",
         "unit": "Liter",
         "logged": true
       }
     ]
   }

See also: `sensor <#interface-sensor>`__

.. _interface-watersensor:

watersensor
-----------

Interface for water sensors.

.. code-block:: json

   {
     "description": "Interface for water sensors.",
     "extends": "sensor",
     "states": [
       {
         "name": "waterDetected",
         "type": "bool",
         "logged": true
       }
     ]
   }

See also: `sensor <#interface-sensor>`__

.. _interface-weather:

weather
-------

.. code-block:: json

   {
     "states": [
       {
         "name": "weatherDescription",
         "type": "QString",
         "logged": true
       },
       {
         "name": "weatherCondition",
         "type": "QString",
         "allowedValues": [
           "clear-day",
           "clear-night",
           "few-clouds-day",
           "few-clouds-night",
           "clouds",
           "overcast",
           "light-rain",
           "shower-rain",
           "thunderstorm",
           "snow",
           "fog"
         ],
         "logged": true
       },
       {
         "name": "temperature",
         "type": "double",
         "unit": "DegreeCelsius",
         "logged": true
       },
       {
         "name": "humidity",
         "type": "int",
         "unit": "Percentage",
         "logged": true
       },
       {
         "name": "pressure",
         "type": "double",
         "unit": "HectoPascal",
         "logged": true
       },
       {
         "name": "windSpeed",
         "type": "double",
         "unit": "MeterPerSecond",
         "logged": true
       },
       {
         "name": "windDirection",
         "type": "int",
         "unit": "Degree",
         "logged": true
       }
     ]
   }

.. _interface-windspeedsensor:

windspeedsensor
---------------

This interface represents a wind sensor measurment and has the unit [m/s].

.. code-block:: json

   {
     "extends": "sensor",
     "description": "This interface represents a wind sensor measurment and has the unit [m/s].",
     "states": [
       {
         "name": "windSpeed",
         "type": "double",
         "unit": "MeterPerSecond",
         "logged": true
       }
     ]
   }

See also: `sensor <#interface-sensor>`__

.. _interface-wirelessconnectable:

wirelessconnectable
-------------------

Interface for wireless connectable devices. If reporting the signal strength is supported, the optional signalStrength state should be implemented.

.. code-block:: json

   {
     "description": "Interface for wireless connectable devices. If reporting the signal strength is supported, the optional signalStrength state should be implemented.",
     "extends": "connectable",
     "states": [
       {
         "name": "signalStrength",
         "type": "uint",
         "unit": "Percentage",
         "minValue": 0,
         "maxValue": 100,
         "optional": true,
         "logged": true
       }
     ]
   }

See also: `connectable <#interface-connectable>`__

