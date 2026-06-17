:orphan:

The complete API
================

In the following section you can find a detailed description of the current API version ``9.0``.

Enums
-----

.. _raw-api-basic-type:

BasicType
~~~~~~~~~

.. code-block:: json

   [
     "Uuid",
     "String",
     "StringList",
     "Int",
     "Uint",
     "Double",
     "Bool",
     "Variant",
     "Color",
     "Time",
     "Object"
   ]

.. _raw-api-browser-icon:

BrowserIcon
~~~~~~~~~~~

.. code-block:: json

   [
     "BrowserIconNone",
     "BrowserIconFolder",
     "BrowserIconFile",
     "BrowserIconMusic",
     "BrowserIconVideo",
     "BrowserIconPictures",
     "BrowserIconApplication",
     "BrowserIconDocument",
     "BrowserIconPackage",
     "BrowserIconFavorites"
   ]

.. _raw-api-configuration-error:

ConfigurationError
~~~~~~~~~~~~~~~~~~

.. code-block:: json

   [
     "ConfigurationErrorNoError",
     "ConfigurationErrorInvalidTimeZone",
     "ConfigurationErrorInvalidStationName",
     "ConfigurationErrorInvalidId",
     "ConfigurationErrorInvalidPort",
     "ConfigurationErrorInvalidHostAddress",
     "ConfigurationErrorInvalidDestinationDir",
     "ConfigurationErrorInvalidFileName",
     "ConfigurationErrorBluetoothHardwareNotAvailable",
     "ConfigurationErrorInvalidCertificate",
     "ConfigurationErrorUnsupported",
     "ConfigurationErrorBackupFailed"
   ]

.. _raw-api-create-method:

CreateMethod
~~~~~~~~~~~~

.. code-block:: json

   [
     "CreateMethodUser",
     "CreateMethodAuto",
     "CreateMethodDiscovery"
   ]

.. _raw-api-debug-error:

DebugError
~~~~~~~~~~

.. code-block:: json

   [
     "DebugErrorNoError"
   ]

.. _raw-api-discovery-type:

DiscoveryType
~~~~~~~~~~~~~

.. code-block:: json

   [
     "DiscoveryTypePrecise",
     "DiscoveryTypeWeak"
   ]

.. _raw-api-i-o-type:

IOType
~~~~~~

.. code-block:: json

   [
     "IOTypeNone",
     "IOTypeDigitalInput",
     "IOTypeDigitalOutput",
     "IOTypeAnalogInput",
     "IOTypeAnalogOutput"
   ]

.. _raw-api-input-type:

InputType
~~~~~~~~~

.. code-block:: json

   [
     "InputTypeNone",
     "InputTypeTextLine",
     "InputTypeTextArea",
     "InputTypePassword",
     "InputTypeSearch",
     "InputTypeMail",
     "InputTypeIPv4Address",
     "InputTypeIPv6Address",
     "InputTypeUrl",
     "InputTypeMacAddress"
   ]

.. _raw-api-logging-category-type:

LoggingCategoryType
~~~~~~~~~~~~~~~~~~~

.. code-block:: json

   [
     "LoggingCategoryTypeSystem",
     "LoggingCategoryTypePlugin",
     "LoggingCategoryTypeCustom"
   ]

.. _raw-api-logging-level:

LoggingLevel
~~~~~~~~~~~~

.. code-block:: json

   [
     "LoggingLevelCritical",
     "LoggingLevelWarning",
     "LoggingLevelInfo",
     "LoggingLevelDebug"
   ]

.. _raw-api-media-browser-icon:

MediaBrowserIcon
~~~~~~~~~~~~~~~~

.. code-block:: json

   [
     "MediaBrowserIconNone",
     "MediaBrowserIconPlaylist",
     "MediaBrowserIconRecentlyPlayed",
     "MediaBrowserIconLibrary",
     "MediaBrowserIconMusicLibrary",
     "MediaBrowserIconVideoLibrary",
     "MediaBrowserIconPictureLibrary",
     "MediaBrowserIconDisk",
     "MediaBrowserIconUSB",
     "MediaBrowserIconNetwork",
     "MediaBrowserIconAux",
     "MediaBrowserIconBluetooth",
     "MediaBrowserIconSpotify",
     "MediaBrowserIconAmazon",
     "MediaBrowserIconTuneIn",
     "MediaBrowserIconSiriusXM",
     "MediaBrowserIconVTuner",
     "MediaBrowserIconTidal",
     "MediaBrowserIconAirable",
     "MediaBrowserIconDeezer",
     "MediaBrowserIconNapster",
     "MediaBrowserIconSoundCloud",
     "MediaBrowserIconRadioParadise"
   ]

.. _raw-api-modbus-rtu-error:

ModbusRtuError
~~~~~~~~~~~~~~

.. code-block:: json

   [
     "ModbusRtuErrorNoError",
     "ModbusRtuErrorNotAvailable",
     "ModbusRtuErrorUuidNotFound",
     "ModbusRtuErrorHardwareNotFound",
     "ModbusRtuErrorResourceBusy",
     "ModbusRtuErrorNotSupported",
     "ModbusRtuErrorInvalidTimeoutValue",
     "ModbusRtuErrorConnectionFailed"
   ]

.. _raw-api-network-device-state:

NetworkDeviceState
~~~~~~~~~~~~~~~~~~

.. code-block:: json

   [
     "NetworkDeviceStateUnknown",
     "NetworkDeviceStateUnmanaged",
     "NetworkDeviceStateUnavailable",
     "NetworkDeviceStateDisconnected",
     "NetworkDeviceStatePrepare",
     "NetworkDeviceStateConfig",
     "NetworkDeviceStateNeedAuth",
     "NetworkDeviceStateIpConfig",
     "NetworkDeviceStateIpCheck",
     "NetworkDeviceStateSecondaries",
     "NetworkDeviceStateActivated",
     "NetworkDeviceStateDeactivating",
     "NetworkDeviceStateFailed"
   ]

.. _raw-api-network-manager-error:

NetworkManagerError
~~~~~~~~~~~~~~~~~~~

.. code-block:: json

   [
     "NetworkManagerErrorNoError",
     "NetworkManagerErrorUnknownError",
     "NetworkManagerErrorWirelessNotAvailable",
     "NetworkManagerErrorAccessPointNotFound",
     "NetworkManagerErrorNetworkInterfaceNotFound",
     "NetworkManagerErrorInvalidNetworkDeviceType",
     "NetworkManagerErrorWirelessNetworkingDisabled",
     "NetworkManagerErrorWirelessConnectionFailed",
     "NetworkManagerErrorNetworkingDisabled",
     "NetworkManagerErrorNetworkManagerNotAvailable",
     "NetworkManagerErrorInvalidConfiguration",
     "NetworkManagerErrorUnsupportedFeature"
   ]

.. _raw-api-network-manager-state:

NetworkManagerState
~~~~~~~~~~~~~~~~~~~

.. code-block:: json

   [
     "NetworkManagerStateUnknown",
     "NetworkManagerStateAsleep",
     "NetworkManagerStateDisconnected",
     "NetworkManagerStateDisconnecting",
     "NetworkManagerStateConnecting",
     "NetworkManagerStateConnectedLocal",
     "NetworkManagerStateConnectedSite",
     "NetworkManagerStateConnectedGlobal"
   ]

.. _raw-api-permission-scope:

PermissionScope
~~~~~~~~~~~~~~~

.. code-block:: json

   [
     "PermissionScopeNone",
     "PermissionScopeControlThings",
     "PermissionScopeConfigureThings",
     "PermissionScopeAccessAllThings",
     "PermissionScopeExecuteRules",
     "PermissionScopeConfigureRules",
     "PermissionScopeAdmin"
   ]

.. _raw-api-repeating-mode:

RepeatingMode
~~~~~~~~~~~~~

.. code-block:: json

   [
     "RepeatingModeNone",
     "RepeatingModeHourly",
     "RepeatingModeDaily",
     "RepeatingModeWeekly",
     "RepeatingModeMonthly",
     "RepeatingModeYearly"
   ]

.. _raw-api-rule-error:

RuleError
~~~~~~~~~

.. code-block:: json

   [
     "RuleErrorNoError",
     "RuleErrorInvalidRuleId",
     "RuleErrorRuleNotFound",
     "RuleErrorThingNotFound",
     "RuleErrorEventTypeNotFound",
     "RuleErrorStateTypeNotFound",
     "RuleErrorActionTypeNotFound",
     "RuleErrorInvalidParameter",
     "RuleErrorInvalidRuleFormat",
     "RuleErrorMissingParameter",
     "RuleErrorInvalidRuleActionParameter",
     "RuleErrorInvalidStateEvaluatorValue",
     "RuleErrorTypesNotMatching",
     "RuleErrorNotExecutable",
     "RuleErrorInvalidTimeDescriptor",
     "RuleErrorInvalidRepeatingOption",
     "RuleErrorInvalidCalendarItem",
     "RuleErrorInvalidTimeEventItem",
     "RuleErrorContainsEventBasesAction",
     "RuleErrorNoExitActions",
     "RuleErrorInterfaceNotFound"
   ]

.. _raw-api-sample-rate:

SampleRate
~~~~~~~~~~

.. code-block:: json

   [
     "SampleRateAny",
     "SampleRate1Min",
     "SampleRate15Mins",
     "SampleRate1Hour",
     "SampleRate3Hours",
     "SampleRate1Day",
     "SampleRate1Week",
     "SampleRate1Month",
     "SampleRate1Year"
   ]

.. _raw-api-script-error:

ScriptError
~~~~~~~~~~~

.. code-block:: json

   [
     "ScriptErrorNoError",
     "ScriptErrorScriptNotFound",
     "ScriptErrorInvalidScript",
     "ScriptErrorHardwareFailure"
   ]

.. _raw-api-script-message-type:

ScriptMessageType
~~~~~~~~~~~~~~~~~

.. code-block:: json

   [
     "ScriptMessageTypeLog",
     "ScriptMessageTypeWarning"
   ]

.. _raw-api-serial-port-data-bits:

SerialPortDataBits
~~~~~~~~~~~~~~~~~~

.. code-block:: json

   [
     "SerialPortDataBitsData5",
     "SerialPortDataBitsData6",
     "SerialPortDataBitsData7",
     "SerialPortDataBitsData8",
     "SerialPortDataBitsUnknownDataBits"
   ]

.. _raw-api-serial-port-parity:

SerialPortParity
~~~~~~~~~~~~~~~~

.. code-block:: json

   [
     "SerialPortParityNoParity",
     "SerialPortParityEvenParity",
     "SerialPortParityOddParity",
     "SerialPortParitySpaceParity",
     "SerialPortParityMarkParity",
     "SerialPortParityUnknownParity"
   ]

.. _raw-api-serial-port-stop-bits:

SerialPortStopBits
~~~~~~~~~~~~~~~~~~

.. code-block:: json

   [
     "SerialPortStopBitsOneStop",
     "SerialPortStopBitsOneAndHalfStop",
     "SerialPortStopBitsTwoStop",
     "SerialPortStopBitsUnknownStopBits"
   ]

.. _raw-api-setup-method:

SetupMethod
~~~~~~~~~~~

.. code-block:: json

   [
     "SetupMethodJustAdd",
     "SetupMethodDisplayPin",
     "SetupMethodEnterPin",
     "SetupMethodPushButton",
     "SetupMethodUserAndPassword",
     "SetupMethodOAuth"
   ]

.. _raw-api-sort-order:

SortOrder
~~~~~~~~~

.. code-block:: json

   [
     "AscendingOrder",
     "DescendingOrder"
   ]

.. _raw-api-state-operator:

StateOperator
~~~~~~~~~~~~~

.. code-block:: json

   [
     "StateOperatorAnd",
     "StateOperatorOr"
   ]

.. _raw-api-state-value-filter:

StateValueFilter
~~~~~~~~~~~~~~~~

.. code-block:: json

   [
     "StateValueFilterNone",
     "StateValueFilterAdaptive"
   ]

.. _raw-api-tag-error:

TagError
~~~~~~~~

.. code-block:: json

   [
     "TagErrorNoError",
     "TagErrorThingNotFound",
     "TagErrorRuleNotFound",
     "TagErrorTagNotFound"
   ]

.. _raw-api-thing-error:

ThingError
~~~~~~~~~~

.. code-block:: json

   [
     "ThingErrorNoError",
     "ThingErrorPluginNotFound",
     "ThingErrorVendorNotFound",
     "ThingErrorThingNotFound",
     "ThingErrorThingClassNotFound",
     "ThingErrorActionTypeNotFound",
     "ThingErrorStateTypeNotFound",
     "ThingErrorEventTypeNotFound",
     "ThingErrorThingDescriptorNotFound",
     "ThingErrorMissingParameter",
     "ThingErrorInvalidParameter",
     "ThingErrorSetupFailed",
     "ThingErrorDuplicateUuid",
     "ThingErrorCreationMethodNotSupported",
     "ThingErrorSetupMethodNotSupported",
     "ThingErrorHardwareNotAvailable",
     "ThingErrorHardwareFailure",
     "ThingErrorAuthenticationFailure",
     "ThingErrorThingInUse",
     "ThingErrorThingInRule",
     "ThingErrorThingIsChild",
     "ThingErrorPairingTransactionIdNotFound",
     "ThingErrorParameterNotWritable",
     "ThingErrorItemNotFound",
     "ThingErrorItemNotExecutable",
     "ThingErrorUnsupportedFeature",
     "ThingErrorTimeout"
   ]

.. _raw-api-thing-setup-status:

ThingSetupStatus
~~~~~~~~~~~~~~~~

.. code-block:: json

   [
     "ThingSetupStatusNone",
     "ThingSetupStatusInProgress",
     "ThingSetupStatusComplete",
     "ThingSetupStatusFailed"
   ]

.. _raw-api-unit:

Unit
~~~~

.. code-block:: json

   [
     "UnitNone",
     "UnitMilliSeconds",
     "UnitSeconds",
     "UnitMinutes",
     "UnitHours",
     "UnitUnixTime",
     "UnitMeterPerSecond",
     "UnitKiloMeterPerHour",
     "UnitDegree",
     "UnitRadiant",
     "UnitDegreeCelsius",
     "UnitDegreeKelvin",
     "UnitMired",
     "UnitMilliBar",
     "UnitBar",
     "UnitPascal",
     "UnitHectoPascal",
     "UnitAtmosphere",
     "UnitLumen",
     "UnitLux",
     "UnitCandela",
     "UnitMilliMeter",
     "UnitCentiMeter",
     "UnitMeter",
     "UnitKiloMeter",
     "UnitGram",
     "UnitKiloGram",
     "UnitDezibel",
     "UnitBpm",
     "UnitKiloByte",
     "UnitMegaByte",
     "UnitGigaByte",
     "UnitTeraByte",
     "UnitMilliWatt",
     "UnitWatt",
     "UnitKiloWatt",
     "UnitKiloWattHour",
     "UnitEuroPerMegaWattHour",
     "UnitEuroCentPerKiloWattHour",
     "UnitPercentage",
     "UnitPartsPerMillion",
     "UnitPartsPerBillion",
     "UnitEuro",
     "UnitDollar",
     "UnitHertz",
     "UnitAmpere",
     "UnitMilliAmpere",
     "UnitVolt",
     "UnitMilliVolt",
     "UnitVoltAmpere",
     "UnitVoltAmpereReactive",
     "UnitAmpereHour",
     "UnitOhm",
     "UnitMicroSiemensPerCentimeter",
     "UnitDuration",
     "UnitNewton",
     "UnitNewtonMeter",
     "UnitRpm",
     "UnitMilligramPerLiter",
     "UnitLiter",
     "UnitMicroGrammPerCubicalMeter"
   ]

.. _raw-api-update-type:

UpdateType
~~~~~~~~~~

.. code-block:: json

   [
     "UpdateTypeNone",
     "UpdateTypeSystem",
     "UpdateTypePackageManager"
   ]

.. _raw-api-user-error:

UserError
~~~~~~~~~

.. code-block:: json

   [
     "UserErrorNoError",
     "UserErrorBackendError",
     "UserErrorInvalidUserId",
     "UserErrorDuplicateUserId",
     "UserErrorBadPassword",
     "UserErrorTokenNotFound",
     "UserErrorPermissionDenied",
     "UserErrorInconsistantScopes"
   ]

.. _raw-api-value-operator:

ValueOperator
~~~~~~~~~~~~~

.. code-block:: json

   [
     "ValueOperatorEquals",
     "ValueOperatorNotEquals",
     "ValueOperatorLess",
     "ValueOperatorGreater",
     "ValueOperatorLessOrEqual",
     "ValueOperatorGreaterOrEqual"
   ]

.. _raw-api-wired-network-connection-type:

WiredNetworkConnectionType
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

   [
     "WiredNetworkConnectionTypeDHCP",
     "WiredNetworkConnectionTypeManual",
     "WiredNetworkConnectionTypeShared"
   ]

.. _raw-api-wireless-capability:

WirelessCapability
~~~~~~~~~~~~~~~~~~

.. code-block:: json

   [
     "WirelessCapabilityNone",
     "WirelessCapabilityCipherWEP40",
     "WirelessCapabilityCipherWEP104",
     "WirelessCapabilityCipherTKIP",
     "WirelessCapabilityCipherCCMP",
     "WirelessCapabilityWPA",
     "WirelessCapabilityRSN",
     "WirelessCapabilityAP",
     "WirelessCapabilityAdHoc",
     "WirelessCapabilityFreqValid",
     "WirelessCapability2Ghz",
     "WirelessCapability5Ghz"
   ]

.. _raw-api-wireless-mode:

WirelessMode
~~~~~~~~~~~~

.. code-block:: json

   [
     "WirelessModeUnknown",
     "WirelessModeAdhoc",
     "WirelessModeInfrastructure",
     "WirelessModeAccessPoint"
   ]

.. _raw-api-z-wave-device-type:

ZWaveDeviceType
~~~~~~~~~~~~~~~

.. code-block:: json

   [
     "ZWaveDeviceTypeUnknown",
     "ZWaveDeviceTypeCentralController",
     "ZWaveDeviceTypeDisplaySimple",
     "ZWaveDeviceTypeDoorLockKeypad",
     "ZWaveDeviceTypeFanSwitch",
     "ZWaveDeviceTypeGateway",
     "ZWaveDeviceTypeLightDimmerSwitch",
     "ZWaveDeviceTypeOnOffPowerSwitch",
     "ZWaveDeviceTypePowerStrip",
     "ZWaveDeviceTypeRemoteControlAV",
     "ZWaveDeviceTypeRemoteControlMultiPurpose",
     "ZWaveDeviceTypeRemoteControlSimple",
     "ZWaveDeviceTypeKeyFob",
     "ZWaveDeviceTypeSensorNotification",
     "ZWaveDeviceTypeSmokeAlarmSensor",
     "ZWaveDeviceTypeCOAlarmSensor",
     "ZWaveDeviceTypeCO2AlarmSensor",
     "ZWaveDeviceTypeHeatAlarmSensor",
     "ZWaveDeviceTypeWaterAlarmSensor",
     "ZWaveDeviceTypeAccessControlSensor",
     "ZWaveDeviceTypeHomeSecuritySensor",
     "ZWaveDeviceTypePowerManagementSensor",
     "ZWaveDeviceTypeSystemSensor",
     "ZWaveDeviceTypeEmergencyAlarmSensor",
     "ZWaveDeviceTypeClockSensor",
     "ZWaveDeviceTypeMultiDeviceAlarmSensor",
     "ZWaveDeviceTypeMultilevelSensor",
     "ZWaveDeviceTypeAirTemperatureSensor",
     "ZWaveDeviceTypeGeneralPurposeSensor",
     "ZWaveDeviceTypeLuminanceSensor",
     "ZWaveDeviceTypePowerSensor",
     "ZWaveDeviceTypeHumiditySensor",
     "ZWaveDeviceTypeVelocitySensor",
     "ZWaveDeviceTypeDirectionSensor",
     "ZWaveDeviceTypeAtmosphericPressureSensor",
     "ZWaveDeviceTypeBarometricPressureSensor",
     "ZWaveDeviceTypeSolarRadiationSensor",
     "ZWaveDeviceTypeDewPointSensor",
     "ZWaveDeviceTypeRainRateSensor",
     "ZWaveDeviceTypeTideLevelSensor",
     "ZWaveDeviceTypeWeightSensor",
     "ZWaveDeviceTypeVoltageSensor",
     "ZWaveDeviceTypeCurrentSensor",
     "ZWaveDeviceTypeCO2LevelSensor",
     "ZWaveDeviceTypeAirFlowSensor",
     "ZWaveDeviceTypeTankCapacitySensor",
     "ZWaveDeviceTypeDistanceSensor",
     "ZWaveDeviceTypeAnglePositionSensor",
     "ZWaveDeviceTypeRotationSensor",
     "ZWaveDeviceTypeWaterTemperatureSensor",
     "ZWaveDeviceTypeSoilTemperatureSensor",
     "ZWaveDeviceTypeSeismicIntensitySensor",
     "ZWaveDeviceTypeSeismicMagnitudeSensor",
     "ZWaveDeviceTypeUltraVioletSensor",
     "ZWaveDeviceTypeElectricalResistivitySensor",
     "ZWaveDeviceTypeElectricalConductivitySensor",
     "ZWaveDeviceTypeLoudnessSensor",
     "ZWaveDeviceTypeMoistureSensor",
     "ZWaveDeviceTypeFrequencySensor",
     "ZWaveDeviceTypeTimeSensor",
     "ZWaveDeviceTypeTargetTemperatureSensor",
     "ZWaveDeviceTypeMultiDeviceSensor",
     "ZWaveDeviceTypeSetTopBox",
     "ZWaveDeviceTypeSiren",
     "ZWaveDeviceTypeSubEnergyMeter",
     "ZWaveDeviceTypeSubSystemController",
     "ZWaveDeviceTypeThermostatHVAC",
     "ZWaveDeviceTypeThermostatSetback",
     "ZWaveDeviceTypeTV",
     "ZWaveDeviceTypeValveOpenClose",
     "ZWaveDeviceTypeWallController",
     "ZWaveDeviceTypeWholeHomeMeterSimple",
     "ZWaveDeviceTypeWindowCoveringNoPosEndpoint",
     "ZWaveDeviceTypeWindowCoveringEndpointAware",
     "ZWaveDeviceTypeWindowCoveringPositionEndpointAware"
   ]

.. _raw-api-z-wave-error:

ZWaveError
~~~~~~~~~~

.. code-block:: json

   [
     "ZWaveErrorNoError",
     "ZWaveErrorInUse",
     "ZWaveErrorNetworkUuidNotFound",
     "ZWaveErrorNodeIdNotFound",
     "ZWaveErrorTimeout",
     "ZWaveErrorBackendError"
   ]

.. _raw-api-z-wave-network-state:

ZWaveNetworkState
~~~~~~~~~~~~~~~~~

.. code-block:: json

   [
     "ZWaveNetworkStateOffline",
     "ZWaveNetworkStateStarting",
     "ZWaveNetworkStateOnline",
     "ZWaveNetworkStateError"
   ]

.. _raw-api-z-wave-node-role:

ZWaveNodeRole
~~~~~~~~~~~~~

.. code-block:: json

   [
     "ZWaveNodeRoleUnknown",
     "ZWaveNodeRoleCentralController",
     "ZWaveNodeRoleSubController",
     "ZWaveNodeRolePortableController",
     "ZWaveNodeRolePortableReportingController",
     "ZWaveNodeRolePortableSlave",
     "ZWaveNodeRoleAlwaysOnSlabe",
     "ZWaveNodeRoleReportingSleepingSlave",
     "ZWaveNodeRoleListeningSleepingSlave"
   ]

.. _raw-api-z-wave-node-type:

ZWaveNodeType
~~~~~~~~~~~~~

.. code-block:: json

   [
     "ZWaveNodeTypeUnknown",
     "ZWaveNodeTypeController",
     "ZWaveNodeTypeStaticController",
     "ZWaveNodeTypeSlave",
     "ZWaveNodeTypeRoutingSlave"
   ]

.. _raw-api-zigbee-cluster-direction:

ZigbeeClusterDirection
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

   [
     "ZigbeeClusterDirectionServer",
     "ZigbeeClusterDirectionClient"
   ]

.. _raw-api-zigbee-error:

ZigbeeError
~~~~~~~~~~~

.. code-block:: json

   [
     "ZigbeeErrorNoError",
     "ZigbeeErrorAdapterNotAvailable",
     "ZigbeeErrorAdapterAlreadyInUse",
     "ZigbeeErrorNetworkUuidNotFound",
     "ZigbeeErrorDurationOutOfRange",
     "ZigbeeErrorNetworkOffline",
     "ZigbeeErrorUnknownBackend",
     "ZigbeeErrorNodeNotFound",
     "ZigbeeErrorForbidden",
     "ZigbeeErrorInvalidChannel",
     "ZigbeeErrorNetworkError",
     "ZigbeeErrorTimeoutError",
     "ZigbeeErrorNotSupported"
   ]

.. _raw-api-zigbee-network-state:

ZigbeeNetworkState
~~~~~~~~~~~~~~~~~~

.. code-block:: json

   [
     "ZigbeeNetworkStateOffline",
     "ZigbeeNetworkStateStarting",
     "ZigbeeNetworkStateUpdating",
     "ZigbeeNetworkStateOnline",
     "ZigbeeNetworkStateError"
   ]

.. _raw-api-zigbee-node-relationship:

ZigbeeNodeRelationship
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

   [
     "ZigbeeNodeRelationshipParent",
     "ZigbeeNodeRelationshipChild",
     "ZigbeeNodeRelationshipSibling",
     "ZigbeeNodeRelationshipNone",
     "ZigbeeNodeRelationshipPreviousChild"
   ]

.. _raw-api-zigbee-node-route-status:

ZigbeeNodeRouteStatus
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

   [
     "ZigbeeNodeRouteStatusActive",
     "ZigbeeNodeRouteStatusDiscoveryUnderway",
     "ZigbeeNodeRouteStatusDiscoveryFailed",
     "ZigbeeNodeRouteStatusInactive",
     "ZigbeeNodeRouteStatusValidationUnderway"
   ]

.. _raw-api-zigbee-node-state:

ZigbeeNodeState
~~~~~~~~~~~~~~~

.. code-block:: json

   [
     "ZigbeeNodeStateUninitialized",
     "ZigbeeNodeStateInitializing",
     "ZigbeeNodeStateInitialized",
     "ZigbeeNodeStateHandled"
   ]

.. _raw-api-zigbee-node-type:

ZigbeeNodeType
~~~~~~~~~~~~~~

.. code-block:: json

   [
     "ZigbeeNodeTypeCoordinator",
     "ZigbeeNodeTypeRouter",
     "ZigbeeNodeTypeEndDevice"
   ]

Flags
-----

.. _raw-api-create-methods:

CreateMethods
~~~~~~~~~~~~~

.. code-block:: json

   [
     "$ref:CreateMethod"
   ]

See also: `CreateMethod <#raw-api-create-method>`__

.. _raw-api-permission-scopes:

PermissionScopes
~~~~~~~~~~~~~~~~

.. code-block:: json

   [
     "$ref:PermissionScope"
   ]

See also: `PermissionScope <#raw-api-permission-scope>`__

.. _raw-api-wireless-capabilities:

WirelessCapabilities
~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

   [
     "$ref:WirelessCapability"
   ]

See also: `WirelessCapability <#raw-api-wireless-capability>`__

Types
-----

.. _raw-api-action:

Action
~~~~~~

.. code-block:: json

   {
     "actionTypeId": "Uuid",
     "o:params": "$ref:ParamList",
     "thingId": "Uuid"
   }

See also: `ParamList <#raw-api-param-list>`__

.. _raw-api-action-type:

ActionType
~~~~~~~~~~

.. code-block:: json

   {
     "displayName": "String",
     "index": "Int",
     "name": "String",
     "paramTypes": "$ref:ParamTypes",
     "r:id": "Uuid"
   }

See also: `ParamTypes <#raw-api-param-types>`__

.. _raw-api-action-types:

ActionTypes
~~~~~~~~~~~

.. code-block:: json

   [
     "$ref:ActionType"
   ]

See also: `ActionType <#raw-api-action-type>`__

.. _raw-api-backup-file:

BackupFile
~~~~~~~~~~

.. code-block:: json

   {
     "r:fileName": "String",
     "r:serverVersion": "String",
     "r:size": "Double",
     "r:timestamp": "Uint"
   }

.. _raw-api-backup-files:

BackupFiles
~~~~~~~~~~~

.. code-block:: json

   [
     "$ref:BackupFile"
   ]

See also: `BackupFile <#raw-api-backup-file>`__

.. _raw-api-browser-item:

BrowserItem
~~~~~~~~~~~

.. code-block:: json

   {
     "actionTypeIds": [
       "Uuid"
     ],
     "browsable": "Bool",
     "disabled": "Bool",
     "displayName": "String",
     "executable": "Bool",
     "icon": "$ref:BrowserIcon",
     "id": "String",
     "o:mediaIcon": "$ref:MediaBrowserIcon",
     "thumbnail": "String"
   }

See also: `BrowserIcon <#raw-api-browser-icon>`__, `MediaBrowserIcon <#raw-api-media-browser-icon>`__

.. _raw-api-cache-hash:

CacheHash
~~~~~~~~~

.. code-block:: json

   {
     "hash": "String",
     "method": "String"
   }

.. _raw-api-calendar-item:

CalendarItem
~~~~~~~~~~~~

.. code-block:: json

   {
     "duration": "Uint",
     "o:datetime": "Uint",
     "o:repeating": "$ref:RepeatingOption",
     "o:startTime": "Time"
   }

See also: `RepeatingOption <#raw-api-repeating-option>`__

.. _raw-api-calendar-items:

CalendarItems
~~~~~~~~~~~~~

.. code-block:: json

   [
     "$ref:CalendarItem"
   ]

See also: `CalendarItem <#raw-api-calendar-item>`__

.. _raw-api-event:

Event
~~~~~

.. code-block:: json

   {
     "r:eventTypeId": "Uuid",
     "r:params": "$ref:ParamList",
     "r:thingId": "Uuid"
   }

See also: `ParamList <#raw-api-param-list>`__

.. _raw-api-event-descriptor:

EventDescriptor
~~~~~~~~~~~~~~~

.. code-block:: json

   {
     "o:eventTypeId": "Uuid",
     "o:interface": "String",
     "o:interfaceEvent": "String",
     "o:paramDescriptors": "$ref:ParamDescriptors",
     "o:thingId": "Uuid"
   }

See also: `ParamDescriptors <#raw-api-param-descriptors>`__

.. _raw-api-event-descriptors:

EventDescriptors
~~~~~~~~~~~~~~~~

.. code-block:: json

   [
     "$ref:EventDescriptor"
   ]

See also: `EventDescriptor <#raw-api-event-descriptor>`__

.. _raw-api-event-type:

EventType
~~~~~~~~~

.. code-block:: json

   {
     "displayName": "String",
     "name": "String",
     "paramTypes": "$ref:ParamTypes",
     "r:id": "Uuid",
     "r:index": "Int"
   }

See also: `ParamTypes <#raw-api-param-types>`__

.. _raw-api-event-types:

EventTypes
~~~~~~~~~~

.. code-block:: json

   [
     "$ref:EventType"
   ]

See also: `EventType <#raw-api-event-type>`__

.. _raw-api-experience:

Experience
~~~~~~~~~~

.. code-block:: json

   {
     "name": "String",
     "version": "String"
   }

.. _raw-api-i-o-connection:

IOConnection
~~~~~~~~~~~~

.. code-block:: json

   {
     "r:id": "Uuid",
     "r:inputStateTypeId": "Uuid",
     "r:inputThingId": "Uuid",
     "r:inverted": "Bool",
     "r:outputStateTypeId": "Uuid",
     "r:outputThingId": "Uuid"
   }

.. _raw-api-i-o-connections:

IOConnections
~~~~~~~~~~~~~

.. code-block:: json

   [
     "$ref:IOConnection"
   ]

See also: `IOConnection <#raw-api-i-o-connection>`__

.. _raw-api-integration-plugin:

IntegrationPlugin
~~~~~~~~~~~~~~~~~

.. code-block:: json

   {
     "r:displayName": "String",
     "r:id": "Uuid",
     "r:name": "String",
     "r:paramTypes": "$ref:ParamTypes"
   }

See also: `ParamTypes <#raw-api-param-types>`__

.. _raw-api-integration-plugins:

IntegrationPlugins
~~~~~~~~~~~~~~~~~~

.. code-block:: json

   [
     "$ref:IntegrationPlugin"
   ]

See also: `IntegrationPlugin <#raw-api-integration-plugin>`__

.. _raw-api-log-entries:

LogEntries
~~~~~~~~~~

.. code-block:: json

   [
     "$ref:LogEntry"
   ]

See also: `LogEntry <#raw-api-log-entry>`__

.. _raw-api-log-entry:

LogEntry
~~~~~~~~

.. code-block:: json

   {
     "r:source": "String",
     "r:timestamp": "Uint",
     "r:values": "Object"
   }

.. _raw-api-logging-category:

LoggingCategory
~~~~~~~~~~~~~~~

.. code-block:: json

   {
     "level": "$ref:LoggingLevel",
     "name": "String",
     "type": "$ref:LoggingCategoryType"
   }

See also: `LoggingCategoryType <#raw-api-logging-category-type>`__, `LoggingLevel <#raw-api-logging-level>`__

.. _raw-api-modbus-rtu-master:

ModbusRtuMaster
~~~~~~~~~~~~~~~

.. code-block:: json

   {
     "baudrate": "Uint",
     "connected": "Bool",
     "dataBits": "$ref:SerialPortDataBits",
     "modbusUuid": "Uuid",
     "numberOfRetries": "Uint",
     "parity": "$ref:SerialPortParity",
     "serialPort": "String",
     "stopBits": "$ref:SerialPortStopBits",
     "timeout": "Uint"
   }

See also: `SerialPortDataBits <#raw-api-serial-port-data-bits>`__, `SerialPortParity <#raw-api-serial-port-parity>`__, `SerialPortStopBits <#raw-api-serial-port-stop-bits>`__

.. _raw-api-mqtt-policy:

MqttPolicy
~~~~~~~~~~

.. code-block:: json

   {
     "allowedPublishTopicFilters": "StringList",
     "allowedSubscribeTopicFilters": "StringList",
     "clientId": "String",
     "password": "String",
     "username": "String"
   }

.. _raw-api-package:

Package
~~~~~~~

.. code-block:: json

   {
     "r:canRemove": "Bool",
     "r:candidateVersion": "String",
     "r:changelog": "String",
     "r:displayName": "String",
     "r:id": "String",
     "r:installedVersion": "String",
     "r:rollbackAvailable": "Bool",
     "r:summary": "String",
     "r:updateAvailable": "Bool"
   }

.. _raw-api-packages:

Packages
~~~~~~~~

.. code-block:: json

   [
     "$ref:Package"
   ]

See also: `Package <#raw-api-package>`__

.. _raw-api-param:

Param
~~~~~

.. code-block:: json

   {
     "o:paramTypeId": "Uuid",
     "value": "Variant"
   }

.. _raw-api-param-descriptor:

ParamDescriptor
~~~~~~~~~~~~~~~

.. code-block:: json

   {
     "o:paramName": "String",
     "o:paramTypeId": "Uuid",
     "operator": "$ref:ValueOperator",
     "value": "Variant"
   }

See also: `ValueOperator <#raw-api-value-operator>`__

.. _raw-api-param-descriptors:

ParamDescriptors
~~~~~~~~~~~~~~~~

.. code-block:: json

   [
     "$ref:ParamDescriptor"
   ]

See also: `ParamDescriptor <#raw-api-param-descriptor>`__

.. _raw-api-param-list:

ParamList
~~~~~~~~~

.. code-block:: json

   [
     "$ref:Param"
   ]

See also: `Param <#raw-api-param>`__

.. _raw-api-param-type:

ParamType
~~~~~~~~~

.. code-block:: json

   {
     "displayName": "String",
     "index": "Int",
     "name": "String",
     "o:allowedValues": [
       "Variant"
     ],
     "o:defaultValue": "Variant",
     "o:inputType": "$ref:InputType",
     "o:maxValue": "Variant",
     "o:minValue": "Variant",
     "o:readOnly": "Bool",
     "o:stepSize": "Double",
     "o:unit": "$ref:Unit",
     "r:id": "Uuid",
     "type": "$ref:BasicType"
   }

See also: `BasicType <#raw-api-basic-type>`__, `InputType <#raw-api-input-type>`__, `Unit <#raw-api-unit>`__

.. _raw-api-param-types:

ParamTypes
~~~~~~~~~~

.. code-block:: json

   [
     "$ref:ParamType"
   ]

See also: `ParamType <#raw-api-param-type>`__

.. _raw-api-repeating-option:

RepeatingOption
~~~~~~~~~~~~~~~

.. code-block:: json

   {
     "mode": "$ref:RepeatingMode",
     "o:monthDays": [
       "Int"
     ],
     "o:weekDays": [
       "Int"
     ]
   }

See also: `RepeatingMode <#raw-api-repeating-mode>`__

.. _raw-api-repositories:

Repositories
~~~~~~~~~~~~

.. code-block:: json

   [
     "$ref:Repository"
   ]

See also: `Repository <#raw-api-repository>`__

.. _raw-api-repository:

Repository
~~~~~~~~~~

.. code-block:: json

   {
     "enabled": "Bool",
     "r:displayName": "String",
     "r:id": "String"
   }

.. _raw-api-rule:

Rule
~~~~

.. code-block:: json

   {
     "actions": "$ref:RuleActions",
     "name": "String",
     "o:enabled": "Bool",
     "o:eventDescriptors": "$ref:EventDescriptors",
     "o:executable": "Bool",
     "o:exitActions": "$ref:RuleActions",
     "o:stateEvaluator": "$ref:StateEvaluator",
     "o:timeDescriptor": "$ref:TimeDescriptor",
     "r:active": "Bool",
     "r:id": "Uuid"
   }

See also: `EventDescriptors <#raw-api-event-descriptors>`__, `RuleActions <#raw-api-rule-actions>`__, `StateEvaluator <#raw-api-state-evaluator>`__, `TimeDescriptor <#raw-api-time-descriptor>`__

.. _raw-api-rule-action:

RuleAction
~~~~~~~~~~

.. code-block:: json

   {
     "o:actionTypeId": "Uuid",
     "o:browserItemId": "String",
     "o:interface": "String",
     "o:interfaceAction": "String",
     "o:ruleActionParams": "$ref:RuleActionParams",
     "o:thingId": "Uuid"
   }

See also: `RuleActionParams <#raw-api-rule-action-params>`__

.. _raw-api-rule-action-param:

RuleActionParam
~~~~~~~~~~~~~~~

.. code-block:: json

   {
     "o:eventParamTypeId": "Uuid",
     "o:eventTypeId": "Uuid",
     "o:paramName": "String",
     "o:paramTypeId": "Uuid",
     "o:stateThingId": "Uuid",
     "o:stateTypeId": "Uuid",
     "o:value": "Variant"
   }

.. _raw-api-rule-action-params:

RuleActionParams
~~~~~~~~~~~~~~~~

.. code-block:: json

   [
     "$ref:RuleActionParam"
   ]

See also: `RuleActionParam <#raw-api-rule-action-param>`__

.. _raw-api-rule-actions:

RuleActions
~~~~~~~~~~~

.. code-block:: json

   [
     "$ref:RuleAction"
   ]

See also: `RuleAction <#raw-api-rule-action>`__

.. _raw-api-rule-description:

RuleDescription
~~~~~~~~~~~~~~~

.. code-block:: json

   {
     "active": "Bool",
     "enabled": "Bool",
     "executable": "Bool",
     "id": "Uuid",
     "name": "String"
   }

.. _raw-api-rules:

Rules
~~~~~

.. code-block:: json

   [
     "$ref:Rule"
   ]

See also: `Rule <#raw-api-rule>`__

.. _raw-api-script:

Script
~~~~~~

.. code-block:: json

   {
     "name": "String",
     "r:id": "Uuid"
   }

.. _raw-api-scripts:

Scripts
~~~~~~~

.. code-block:: json

   [
     "$ref:Script"
   ]

See also: `Script <#raw-api-script>`__

.. _raw-api-serial-port:

SerialPort
~~~~~~~~~~

.. code-block:: json

   {
     "r:description": "String",
     "r:manufacturer": "String",
     "r:serialNumber": "String",
     "r:systemLocation": "String"
   }

.. _raw-api-serial-ports:

SerialPorts
~~~~~~~~~~~

.. code-block:: json

   [
     "$ref:SerialPort"
   ]

See also: `SerialPort <#raw-api-serial-port>`__

.. _raw-api-server-configuration:

ServerConfiguration
~~~~~~~~~~~~~~~~~~~

.. code-block:: json

   {
     "address": "String",
     "authenticationEnabled": "Bool",
     "id": "String",
     "port": "Uint",
     "sslEnabled": "Bool"
   }

.. _raw-api-state:

State
~~~~~

.. code-block:: json

   {
     "r:filter": "$ref:StateValueFilter",
     "r:o:maxValue": "Variant",
     "r:o:minValue": "Variant",
     "r:o:possibleValues": [
       "Variant"
     ],
     "r:stateTypeId": "Uuid",
     "r:value": "Variant"
   }

See also: `StateValueFilter <#raw-api-state-value-filter>`__

.. _raw-api-state-descriptor:

StateDescriptor
~~~~~~~~~~~~~~~

.. code-block:: json

   {
     "o:interface": "String",
     "o:interfaceState": "String",
     "o:stateTypeId": "Uuid",
     "o:thingId": "Uuid",
     "o:value": "Variant",
     "o:valueStateTypeId": "Uuid",
     "o:valueThingId": "Uuid",
     "operator": "$ref:ValueOperator"
   }

See also: `ValueOperator <#raw-api-value-operator>`__

.. _raw-api-state-evaluator:

StateEvaluator
~~~~~~~~~~~~~~

.. code-block:: json

   {
     "o:childEvaluators": "$ref:StateEvaluators",
     "o:operator": "$ref:StateOperator",
     "o:stateDescriptor": "$ref:StateDescriptor"
   }

See also: `StateDescriptor <#raw-api-state-descriptor>`__, `StateEvaluators <#raw-api-state-evaluators>`__, `StateOperator <#raw-api-state-operator>`__

.. _raw-api-state-evaluators:

StateEvaluators
~~~~~~~~~~~~~~~

.. code-block:: json

   [
     "$ref:StateEvaluator"
   ]

See also: `StateEvaluator <#raw-api-state-evaluator>`__

.. _raw-api-state-type:

StateType
~~~~~~~~~

.. code-block:: json

   {
     "defaultValue": "Variant",
     "displayName": "String",
     "index": "Int",
     "name": "String",
     "o:ioType": "$ref:IOType",
     "o:maxValue": "Variant",
     "o:minValue": "Variant",
     "o:possibleValues": [
       "Variant"
     ],
     "o:possibleValuesDisplayNames": "StringList",
     "o:stepSize": "Double",
     "o:unit": "$ref:Unit",
     "r:id": "Uuid",
     "type": "$ref:BasicType"
   }

See also: `BasicType <#raw-api-basic-type>`__, `IOType <#raw-api-i-o-type>`__, `Unit <#raw-api-unit>`__

.. _raw-api-state-types:

StateTypes
~~~~~~~~~~

.. code-block:: json

   [
     "$ref:StateType"
   ]

See also: `StateType <#raw-api-state-type>`__

.. _raw-api-states:

States
~~~~~~

.. code-block:: json

   [
     "$ref:State"
   ]

See also: `State <#raw-api-state>`__

.. _raw-api-tag:

Tag
~~~

.. code-block:: json

   {
     "appId": "String",
     "o:ruleId": "Uuid",
     "o:thingId": "Uuid",
     "o:value": "String",
     "tagId": "String"
   }

.. _raw-api-tags:

Tags
~~~~

.. code-block:: json

   [
     "$ref:Tag"
   ]

See also: `Tag <#raw-api-tag>`__

.. _raw-api-thing:

Thing
~~~~~

.. code-block:: json

   {
     "d:r:setupComplete": "Bool",
     "o:name": "String",
     "o:settings": "$ref:ParamList",
     "r:id": "Uuid",
     "r:o:loggedActionTypeIds": [
       "Uuid"
     ],
     "r:o:loggedEventTypeIds": [
       "Uuid"
     ],
     "r:o:loggedStateTypeIds": [
       "Uuid"
     ],
     "r:o:parentId": "Uuid",
     "r:o:setupDisplayMessage": "String",
     "r:params": "$ref:ParamList",
     "r:setupError": "$ref:ThingError",
     "r:setupStatus": "$ref:ThingSetupStatus",
     "r:states": "$ref:States",
     "r:thingClassId": "Uuid"
   }

See also: `ParamList <#raw-api-param-list>`__, `States <#raw-api-states>`__, `ThingError <#raw-api-thing-error>`__, `ThingSetupStatus <#raw-api-thing-setup-status>`__

.. _raw-api-thing-class:

ThingClass
~~~~~~~~~~

.. code-block:: json

   {
     "r:actionTypes": "$ref:ActionTypes",
     "r:browsable": "Bool",
     "r:browserItemActionTypes": "$ref:ActionTypes",
     "r:createMethods": "$ref:CreateMethods",
     "r:discoveryParamTypes": "$ref:ParamTypes",
     "r:discoveryType": "$ref:DiscoveryType",
     "r:displayName": "String",
     "r:eventTypes": "$ref:EventTypes",
     "r:id": "Uuid",
     "r:interfaces": "StringList",
     "r:name": "String",
     "r:paramTypes": "$ref:ParamTypes",
     "r:pluginId": "Uuid",
     "r:providedInterfaces": "StringList",
     "r:settingsTypes": "$ref:ParamTypes",
     "r:setupMethod": "$ref:SetupMethod",
     "r:stateTypes": "$ref:StateTypes",
     "r:vendorId": "Uuid"
   }

See also: `ActionTypes <#raw-api-action-types>`__, `CreateMethods <#raw-api-create-methods>`__, `DiscoveryType <#raw-api-discovery-type>`__, `EventTypes <#raw-api-event-types>`__, `ParamTypes <#raw-api-param-types>`__, `SetupMethod <#raw-api-setup-method>`__, `StateTypes <#raw-api-state-types>`__

.. _raw-api-thing-classes:

ThingClasses
~~~~~~~~~~~~

.. code-block:: json

   [
     "$ref:ThingClass"
   ]

See also: `ThingClass <#raw-api-thing-class>`__

.. _raw-api-thing-descriptor:

ThingDescriptor
~~~~~~~~~~~~~~~

.. code-block:: json

   {
     "r:description": "String",
     "r:id": "Uuid",
     "r:o:thingId": "Uuid",
     "r:params": "$ref:ParamList",
     "r:thingClassId": "Uuid",
     "r:title": "String"
   }

See also: `ParamList <#raw-api-param-list>`__

.. _raw-api-thing-descriptors:

ThingDescriptors
~~~~~~~~~~~~~~~~

.. code-block:: json

   [
     "$ref:ThingDescriptor"
   ]

See also: `ThingDescriptor <#raw-api-thing-descriptor>`__

.. _raw-api-things:

Things
~~~~~~

.. code-block:: json

   [
     "$ref:Thing"
   ]

See also: `Thing <#raw-api-thing>`__

.. _raw-api-time-descriptor:

TimeDescriptor
~~~~~~~~~~~~~~

.. code-block:: json

   {
     "o:calendarItems": "$ref:CalendarItems",
     "o:timeEventItems": "$ref:TimeEventItems"
   }

See also: `CalendarItems <#raw-api-calendar-items>`__, `TimeEventItems <#raw-api-time-event-items>`__

.. _raw-api-time-event-item:

TimeEventItem
~~~~~~~~~~~~~

.. code-block:: json

   {
     "o:datetime": "Uint",
     "o:repeating": "$ref:RepeatingOption",
     "o:time": "Time"
   }

See also: `RepeatingOption <#raw-api-repeating-option>`__

.. _raw-api-time-event-items:

TimeEventItems
~~~~~~~~~~~~~~

.. code-block:: json

   [
     "$ref:TimeEventItem"
   ]

See also: `TimeEventItem <#raw-api-time-event-item>`__

.. _raw-api-token-info:

TokenInfo
~~~~~~~~~

.. code-block:: json

   {
     "r:creationTime": "Uint",
     "r:deviceName": "String",
     "r:id": "Uuid",
     "r:username": "String"
   }

.. _raw-api-token-info-list:

TokenInfoList
~~~~~~~~~~~~~

.. code-block:: json

   [
     "$ref:TokenInfo"
   ]

See also: `TokenInfo <#raw-api-token-info>`__

.. _raw-api-tunnel-proxy-server-configuration:

TunnelProxyServerConfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

   {
     "address": "String",
     "authenticationEnabled": "Bool",
     "id": "String",
     "ignoreSslErrors": "Bool",
     "port": "Uint",
     "sslEnabled": "Bool"
   }

.. _raw-api-user-info:

UserInfo
~~~~~~~~

.. code-block:: json

   {
     "r:allowedThingIds": [
       "Uuid"
     ],
     "r:displayName": "String",
     "r:email": "String",
     "r:scopes": "$ref:PermissionScopes",
     "r:username": "String"
   }

See also: `PermissionScopes <#raw-api-permission-scopes>`__

.. _raw-api-user-info-list:

UserInfoList
~~~~~~~~~~~~

.. code-block:: json

   [
     "$ref:UserInfo"
   ]

See also: `UserInfo <#raw-api-user-info>`__

.. _raw-api-vendor:

Vendor
~~~~~~

.. code-block:: json

   {
     "displayName": "String",
     "id": "Uuid",
     "name": "String"
   }

.. _raw-api-vendors:

Vendors
~~~~~~~

.. code-block:: json

   [
     "$ref:Vendor"
   ]

See also: `Vendor <#raw-api-vendor>`__

.. _raw-api-web-server-configuration:

WebServerConfiguration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

   {
     "address": "String",
     "authenticationEnabled": "Bool",
     "id": "String",
     "port": "Uint",
     "publicFolder": "String",
     "sslEnabled": "Bool"
   }

.. _raw-api-wired-network-device:

WiredNetworkDevice
~~~~~~~~~~~~~~~~~~

.. code-block:: json

   {
     "r:bitRate": "String",
     "r:interface": "String",
     "r:ipv4Addresses": "StringList",
     "r:ipv6Addresses": "StringList",
     "r:macAddress": "String",
     "r:pluggedIn": "Bool",
     "r:state": "$ref:NetworkDeviceState"
   }

See also: `NetworkDeviceState <#raw-api-network-device-state>`__

.. _raw-api-wireless-access-point:

WirelessAccessPoint
~~~~~~~~~~~~~~~~~~~

.. code-block:: json

   {
     "r:frequency": "Double",
     "r:macAddress": "String",
     "r:protected": "Bool",
     "r:signalStrength": "Int",
     "r:ssid": "String"
   }

.. _raw-api-wireless-network-device:

WirelessNetworkDevice
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

   {
     "r:bitRate": "String",
     "r:capabilities": "$ref:WirelessCapabilities",
     "r:interface": "String",
     "r:ipv4Addresses": "StringList",
     "r:ipv6Addresses": "StringList",
     "r:macAddress": "String",
     "r:mode": "$ref:WirelessMode",
     "r:o:currentAccessPoint": "$ref:WirelessAccessPoint",
     "r:state": "$ref:NetworkDeviceState"
   }

See also: `NetworkDeviceState <#raw-api-network-device-state>`__, `WirelessAccessPoint <#raw-api-wireless-access-point>`__, `WirelessCapabilities <#raw-api-wireless-capabilities>`__, `WirelessMode <#raw-api-wireless-mode>`__

.. _raw-api-z-wave-network:

ZWaveNetwork
~~~~~~~~~~~~

.. code-block:: json

   {
     "homeId": "Uint",
     "isBridgeController": "Bool",
     "isPrimaryController": "Bool",
     "isStaticUpdateController": "Bool",
     "isZWavePlus": "Bool",
     "networkState": "$ref:ZWaveNetworkState",
     "networkUuid": "Uuid",
     "serialPort": "String",
     "waitingForNodeAddition": "Bool",
     "waitingForNodeRemoval": "Bool"
   }

See also: `ZWaveNetworkState <#raw-api-z-wave-network-state>`__

.. _raw-api-z-wave-node:

ZWaveNode
~~~~~~~~~

.. code-block:: json

   {
     "deviceType": "$ref:ZWaveDeviceType",
     "failed": "Bool",
     "initialized": "Bool",
     "isBeamingDevice": "Bool",
     "isSecurityDevice": "Bool",
     "isZWavePlusDevice": "Bool",
     "linkQuality": "Uint",
     "manufacturerId": "Uint",
     "manufacturerName": "String",
     "networkUuid": "Uuid",
     "nodeId": "Uint",
     "nodeType": "$ref:ZWaveNodeType",
     "productId": "Uint",
     "productName": "String",
     "productType": "Uint",
     "reachable": "Bool",
     "role": "$ref:ZWaveNodeRole",
     "securityMode": "Uint",
     "sleeping": "Bool",
     "version": "String"
   }

See also: `ZWaveDeviceType <#raw-api-z-wave-device-type>`__, `ZWaveNodeRole <#raw-api-z-wave-node-role>`__, `ZWaveNodeType <#raw-api-z-wave-node-type>`__

.. _raw-api-zigbee-adapter:

ZigbeeAdapter
~~~~~~~~~~~~~

.. code-block:: json

   {
     "r:backend": "String",
     "r:baudRate": "Int",
     "r:description": "String",
     "r:hardwareRecognized": "Bool",
     "r:name": "String",
     "r:serialNumber": "String",
     "r:serialPort": "String"
   }

.. _raw-api-zigbee-adapters:

ZigbeeAdapters
~~~~~~~~~~~~~~

.. code-block:: json

   [
     "$ref:ZigbeeAdapter"
   ]

See also: `ZigbeeAdapter <#raw-api-zigbee-adapter>`__

.. _raw-api-zigbee-binding-table-record:

ZigbeeBindingTableRecord
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

   {
     "clusterId": "Uint",
     "o:destinationAddress": "String",
     "o:destinationEndpointId": "Uint",
     "o:destinationGroupAddress": "Uint",
     "sourceAddress": "String",
     "sourceEndpointId": "Uint"
   }

.. _raw-api-zigbee-cluster:

ZigbeeCluster
~~~~~~~~~~~~~

.. code-block:: json

   {
     "clusterId": "Uint",
     "direction": "$ref:ZigbeeClusterDirection"
   }

See also: `ZigbeeClusterDirection <#raw-api-zigbee-cluster-direction>`__

.. _raw-api-zigbee-neighbor-table-record:

ZigbeeNeighborTableRecord
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

   {
     "depth": "Uint",
     "lqi": "Uint",
     "networkAddress": "Uint",
     "permitJoining": "Bool",
     "relationship": "$ref:ZigbeeNodeRelationship"
   }

See also: `ZigbeeNodeRelationship <#raw-api-zigbee-node-relationship>`__

.. _raw-api-zigbee-network:

ZigbeeNetwork
~~~~~~~~~~~~~

.. code-block:: json

   {
     "backend": "String",
     "baudRate": "Uint",
     "channel": "Uint",
     "channelMask": "Uint",
     "enabled": "Bool",
     "firmwareVersion": "String",
     "macAddress": "String",
     "networkState": "$ref:ZigbeeNetworkState",
     "networkUuid": "Uuid",
     "panId": "Uint",
     "permitJoiningDuration": "Uint",
     "permitJoiningEnabled": "Bool",
     "permitJoiningRemaining": "Uint",
     "serialPort": "String"
   }

See also: `ZigbeeNetworkState <#raw-api-zigbee-network-state>`__

.. _raw-api-zigbee-node:

ZigbeeNode
~~~~~~~~~~

.. code-block:: json

   {
     "bindingTableRecords": [
       "$ref:ZigbeeBindingTableRecord"
     ],
     "endpoints": [
       "$ref:ZigbeeNodeEndpoint"
     ],
     "ieeeAddress": "String",
     "lastSeen": "Uint",
     "lqi": "Uint",
     "manufacturer": "String",
     "model": "String",
     "neighborTableRecords": [
       "$ref:ZigbeeNeighborTableRecord"
     ],
     "networkAddress": "Uint",
     "networkUuid": "Uuid",
     "reachable": "Bool",
     "receiverOnWhileIdle": "Bool",
     "routingTableRecords": [
       "$ref:ZigbeeRoutingTableRecord"
     ],
     "state": "$ref:ZigbeeNodeState",
     "type": "$ref:ZigbeeNodeType",
     "version": "String"
   }

See also: `ZigbeeBindingTableRecord <#raw-api-zigbee-binding-table-record>`__, `ZigbeeNeighborTableRecord <#raw-api-zigbee-neighbor-table-record>`__, `ZigbeeNodeEndpoint <#raw-api-zigbee-node-endpoint>`__, `ZigbeeNodeState <#raw-api-zigbee-node-state>`__, `ZigbeeNodeType <#raw-api-zigbee-node-type>`__, `ZigbeeRoutingTableRecord <#raw-api-zigbee-routing-table-record>`__

.. _raw-api-zigbee-node-endpoint:

ZigbeeNodeEndpoint
~~~~~~~~~~~~~~~~~~

.. code-block:: json

   {
     "endpointId": "Uint",
     "inputClusters": [
       "$ref:ZigbeeCluster"
     ],
     "outputClusters": [
       "$ref:ZigbeeCluster"
     ]
   }

See also: `ZigbeeCluster <#raw-api-zigbee-cluster>`__

.. _raw-api-zigbee-routing-table-record:

ZigbeeRoutingTableRecord
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

   {
     "destinationAddress": "Uint",
     "manyToOne": "Bool",
     "memoryConstrained": "Bool",
     "nextHopAddress": "Uint",
     "status": "$ref:ZigbeeNodeRouteStatus"
   }

See also: `ZigbeeNodeRouteStatus <#raw-api-zigbee-node-route-status>`__

Methods
-------

.. _raw-api-app-data-load:

AppData.Load
~~~~~~~~~~~~

Retrieve an app data storage value that has previously been set with Store(). If no value had been set for this appId/key combination before, an empty value will be returned.

Params
^^^^^^

.. code-block:: json

   {
     "appId": "String",
     "key": "String",
     "o:group": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "value": "String"
   }

.. _raw-api-app-data-store:

AppData.Store
~~~~~~~~~~~~~

Store an app data entry to the server. App data can be used by the client application to store configuration values. The app data storage is a key-value pair storage. Each entry value is identified by an appId, a key and optionally a group. The value data is a bytearray and can contain arbitrary data, such as a JSON map or image data, however, be aware of the maximum packet size for the used transport.

This might be useful to a client application to sync settings across multiple instances of the same application.

The group parameter might be used to create groups for this application.

IMPORTANT: Currently no verification of the appId is done. The appid is merely a mechanism to prevent different different client apps from colliding by using the same key for data entries. This implies that the app data storage may not be suited for sensitive data given that anyone with a valid server token can read it.

 

Params
^^^^^^

.. code-block:: json

   {
     "appId": "String",
     "key": "String",
     "o:group": "String",
     "value": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {}

.. _raw-api-configuration-create-and-download-backup:

Configuration.CreateAndDownloadBackup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a backup of the current configuration and generate a download entry for the dedicated transfer connection.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "configurationError": "$ref:ConfigurationError",
     "downloadId": "String",
     "fileName": "String",
     "size": "Int"
   }

See also: `ConfigurationError <#raw-api-configuration-error>`__

.. _raw-api-configuration-create-backup:

Configuration.CreateBackup
~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a backup of the current configuration. It will be stored in the configured destination directory. Also the maxCout configuration will be considered.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "configurationError": "$ref:ConfigurationError"
   }

See also: `ConfigurationError <#raw-api-configuration-error>`__

.. _raw-api-configuration-delete-backup-file:

Configuration.DeleteBackupFile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Delete an existing configuration backup file.

Params
^^^^^^

.. code-block:: json

   {
     "fileName": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "configurationError": "$ref:ConfigurationError"
   }

See also: `ConfigurationError <#raw-api-configuration-error>`__

.. _raw-api-configuration-delete-mqtt-policy:

Configuration.DeleteMqttPolicy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Delete a MQTT policy from the broker.

Params
^^^^^^

.. code-block:: json

   {
     "clientId": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "configurationError": "$ref:ConfigurationError"
   }

See also: `ConfigurationError <#raw-api-configuration-error>`__

.. _raw-api-configuration-delete-mqtt-server-configuration:

Configuration.DeleteMqttServerConfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Delete a MQTT Server interface of the server.

Params
^^^^^^

.. code-block:: json

   {
     "id": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "configurationError": "$ref:ConfigurationError"
   }

See also: `ConfigurationError <#raw-api-configuration-error>`__

.. _raw-api-configuration-delete-tcp-server-configuration:

Configuration.DeleteTcpServerConfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Delete a TCP interface of the server. Note: if you are deleting the configuration for the interface you are currently connected to, the connection will be dropped.

Params
^^^^^^

.. code-block:: json

   {
     "id": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "configurationError": "$ref:ConfigurationError"
   }

See also: `ConfigurationError <#raw-api-configuration-error>`__

.. _raw-api-configuration-delete-tunnel-proxy-server-configuration:

Configuration.DeleteTunnelProxyServerConfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Delete a Tunnel Proxy Server interface of the server. Note: if you are deleting the configuration for the interface you are currently connected to, the connection will be dropped.

Params
^^^^^^

.. code-block:: json

   {
     "id": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "configurationError": "$ref:ConfigurationError"
   }

See also: `ConfigurationError <#raw-api-configuration-error>`__

.. _raw-api-configuration-delete-web-server-configuration:

Configuration.DeleteWebServerConfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Delete a WebServer interface of the server.

Params
^^^^^^

.. code-block:: json

   {
     "id": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "configurationError": "$ref:ConfigurationError"
   }

See also: `ConfigurationError <#raw-api-configuration-error>`__

.. _raw-api-configuration-delete-web-socket-server-configuration:

Configuration.DeleteWebSocketServerConfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Delete a WebSocket Server interface of the server. Note: if you are deleting the configuration for the interface you are currently connected to, the connection will be dropped.

Params
^^^^^^

.. code-block:: json

   {
     "id": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "configurationError": "$ref:ConfigurationError"
   }

See also: `ConfigurationError <#raw-api-configuration-error>`__

.. _raw-api-configuration-download-backup-file:

Configuration.DownloadBackupFile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Generate a download entry for an existing configuration backup file.

Params
^^^^^^

.. code-block:: json

   {
     "fileName": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "configurationError": "$ref:ConfigurationError",
     "o:downloadId": "String",
     "o:fileName": "String",
     "o:size": "Int"
   }

See also: `ConfigurationError <#raw-api-configuration-error>`__

.. _raw-api-configuration-get-available-languages:

Configuration.GetAvailableLanguages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns a list of locale codes available for the server. i.e. en_US, de_AT

.. note:: Deprecated. Use the locale property in the Handshake message instead.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "languages": [
       "String"
     ]
   }

.. _raw-api-configuration-get-backup-files:

Configuration.GetBackupFiles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get the list of configuration backup files from the configured destination directory.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "backupFiles": [
       "$ref:BackupFile"
     ]
   }

See also: `BackupFile <#raw-api-backup-file>`__

.. _raw-api-configuration-get-configurations:

Configuration.GetConfigurations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get all configuration parameters of the server.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "backupConfigurations": {
       "autoBackupEnabled": "Bool",
       "autoBackupInterval": "Int",
       "destinationDirectory": "String",
       "maxCount": "Uint"
     },
     "basicConfiguration": {
       "d:language": "String",
       "d:location": {
         "latitude": "Double",
         "longitude": "Double",
         "name": "String"
       },
       "d:serverTime": "Uint",
       "d:timeZone": "String",
       "debugServerEnabled": "Bool",
       "serverName": "String",
       "serverUuid": "Uuid"
     },
     "mqttServerConfigurations": [
       "$ref:ServerConfiguration"
     ],
     "tcpServerConfigurations": [
       "$ref:ServerConfiguration"
     ],
     "tunnelProxyServerConfigurations": [
       "$ref:TunnelProxyServerConfiguration"
     ],
     "webServerConfigurations": [
       "$ref:WebServerConfiguration"
     ],
     "webSocketServerConfigurations": [
       "$ref:ServerConfiguration"
     ]
   }

See also: `ServerConfiguration <#raw-api-server-configuration>`__, `TunnelProxyServerConfiguration <#raw-api-tunnel-proxy-server-configuration>`__, `WebServerConfiguration <#raw-api-web-server-configuration>`__

.. _raw-api-configuration-get-mqtt-policies:

Configuration.GetMqttPolicies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get all MQTT broker policies.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "mqttPolicies": [
       "$ref:MqttPolicy"
     ]
   }

See also: `MqttPolicy <#raw-api-mqtt-policy>`__

.. _raw-api-configuration-get-mqtt-server-configurations:

Configuration.GetMqttServerConfigurations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get all MQTT Server configurations.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "mqttServerConfigurations": [
       "$ref:ServerConfiguration"
     ]
   }

See also: `ServerConfiguration <#raw-api-server-configuration>`__

.. _raw-api-configuration-get-time-zones:

Configuration.GetTimeZones
~~~~~~~~~~~~~~~~~~~~~~~~~~

Get the list of available timezones.

.. note:: Deprecated. Use System.GetTimeZones instead.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "timeZones": [
       "String"
     ]
   }

.. _raw-api-configuration-restore-backup-file:

Configuration.RestoreBackupFile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Restore an existing configuration backup file. Clients should warn the user before calling this method because the current configuration data will be wiped, the server will restart immediately afterwards and it will come back up using the restored backup.

Params
^^^^^^

.. code-block:: json

   {
     "fileName": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "configurationError": "$ref:ConfigurationError"
   }

See also: `ConfigurationError <#raw-api-configuration-error>`__

.. _raw-api-configuration-set-backup-configuration:

Configuration.SetBackupConfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set the backup configuration. The destination directory is the location where the archives will be saved, the maxCount is the number of backups which will be kept. If maxCount is 0, all backups will be kept. The autoBackupEnabled property controls periodic configuration backups and autoBackupInterval defines the interval in hours.

Params
^^^^^^

.. code-block:: json

   {
     "autoBackupEnabled": "Bool",
     "autoBackupInterval": "Int",
     "destinationDirectory": "String",
     "maxCount": "Uint"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "configurationError": "$ref:ConfigurationError"
   }

See also: `ConfigurationError <#raw-api-configuration-error>`__

.. _raw-api-configuration-set-debug-server-enabled:

Configuration.SetDebugServerEnabled
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enable or disable the debug server.

Params
^^^^^^

.. code-block:: json

   {
     "enabled": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "configurationError": "$ref:ConfigurationError"
   }

See also: `ConfigurationError <#raw-api-configuration-error>`__

.. _raw-api-configuration-set-language:

Configuration.SetLanguage
~~~~~~~~~~~~~~~~~~~~~~~~~

Sets the server language to the given language. See also: "GetAvailableLanguages"

.. note:: Deprecated. Use the locale property in the Handshake message instead.

Params
^^^^^^

.. code-block:: json

   {
     "language": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "configurationError": "$ref:ConfigurationError"
   }

See also: `ConfigurationError <#raw-api-configuration-error>`__

.. _raw-api-configuration-set-location:

Configuration.SetLocation
~~~~~~~~~~~~~~~~~~~~~~~~~

Sets the server location.

Params
^^^^^^

.. code-block:: json

   {
     "location": {
       "latitude": "Double",
       "longitude": "Double",
       "name": "String"
     }
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "configurationError": "$ref:ConfigurationError"
   }

See also: `ConfigurationError <#raw-api-configuration-error>`__

.. _raw-api-configuration-set-mqtt-policy:

Configuration.SetMqttPolicy
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure a MQTT broker policy. If the ID is an existing one, the existing policy will be modified, otherwise a new one will be added.

Params
^^^^^^

.. code-block:: json

   {
     "policy": "$ref:MqttPolicy"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "configurationError": "$ref:ConfigurationError"
   }

See also: `ConfigurationError <#raw-api-configuration-error>`__, `MqttPolicy <#raw-api-mqtt-policy>`__

.. _raw-api-configuration-set-mqtt-server-configuration:

Configuration.SetMqttServerConfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure a MQTT Server interface on the MQTT broker. If the ID is an existing one, the existing config will be modified, otherwise a new one will be added. Setting authenticationEnabled to true will require MQTT clients to use credentials set in the MQTT broker policies.

Params
^^^^^^

.. code-block:: json

   {
     "configuration": "$ref:ServerConfiguration"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "configurationError": "$ref:ConfigurationError"
   }

See also: `ConfigurationError <#raw-api-configuration-error>`__, `ServerConfiguration <#raw-api-server-configuration>`__

.. _raw-api-configuration-set-server-name:

Configuration.SetServerName
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set the name of the server. Default is nymea.

Params
^^^^^^

.. code-block:: json

   {
     "serverName": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "configurationError": "$ref:ConfigurationError"
   }

See also: `ConfigurationError <#raw-api-configuration-error>`__

.. _raw-api-configuration-set-tcp-server-configuration:

Configuration.SetTcpServerConfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure a TCP interface of the server. If the ID is an existing one, the existing config will be modified, otherwise a new one will be added. Note: if you are changing the configuration for the interface you are currently connected to, the connection will be dropped.

Params
^^^^^^

.. code-block:: json

   {
     "configuration": "$ref:ServerConfiguration"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "configurationError": "$ref:ConfigurationError"
   }

See also: `ConfigurationError <#raw-api-configuration-error>`__, `ServerConfiguration <#raw-api-server-configuration>`__

.. _raw-api-configuration-set-time-zone:

Configuration.SetTimeZone
~~~~~~~~~~~~~~~~~~~~~~~~~

Set the time zone of the server. See also: "GetTimeZones"

.. note:: Deprecated. Use System.SetTimeZone instead.

Params
^^^^^^

.. code-block:: json

   {
     "timeZone": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "configurationError": "$ref:ConfigurationError"
   }

See also: `ConfigurationError <#raw-api-configuration-error>`__

.. _raw-api-configuration-set-tunnel-proxy-server-configuration:

Configuration.SetTunnelProxyServerConfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure a Tunnel Proxy Server interface of the server. If the ID is an existing one, the existing config will be modified, otherwise a new one will be added. Note: if you are changing the configuration for the interface you are currently connected to, the connection will be dropped.

Params
^^^^^^

.. code-block:: json

   {
     "configuration": "$ref:TunnelProxyServerConfiguration"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "configurationError": "$ref:ConfigurationError"
   }

See also: `ConfigurationError <#raw-api-configuration-error>`__, `TunnelProxyServerConfiguration <#raw-api-tunnel-proxy-server-configuration>`__

.. _raw-api-configuration-set-web-server-configuration:

Configuration.SetWebServerConfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure a WebServer interface of the server. If the ID is an existing one, the existing config will be modified, otherwise a new one will be added.

Params
^^^^^^

.. code-block:: json

   {
     "configuration": "$ref:WebServerConfiguration"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "configurationError": "$ref:ConfigurationError"
   }

See also: `ConfigurationError <#raw-api-configuration-error>`__, `WebServerConfiguration <#raw-api-web-server-configuration>`__

.. _raw-api-configuration-set-web-socket-server-configuration:

Configuration.SetWebSocketServerConfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure a WebSocket Server interface of the server. If the ID is an existing one, the existing config will be modified, otherwise a new one will be added. Note: if you are changing the configuration for the interface you are currently connected to, the connection will be dropped.

Params
^^^^^^

.. code-block:: json

   {
     "configuration": "$ref:ServerConfiguration"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "configurationError": "$ref:ConfigurationError"
   }

See also: `ConfigurationError <#raw-api-configuration-error>`__, `ServerConfiguration <#raw-api-server-configuration>`__

.. _raw-api-configuration-upload-and-restore-backup:

Configuration.UploadAndRestoreBackup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create an upload session for a configuration backup archive. The uploaded file will be stored temporarily under /tmp, the current configuration will be wiped after the upload finishes and the server will restart immediately using the restored backup. Clients should warn the user before calling this method because all current configuration data will be lost.

Params
^^^^^^

.. code-block:: json

   {
     "fileName": "String",
     "size": "Int"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "configurationError": "$ref:ConfigurationError",
     "o:fileName": "String",
     "o:size": "Int",
     "o:transferId": "String",
     "o:transferToken": "String"
   }

See also: `ConfigurationError <#raw-api-configuration-error>`__

.. _raw-api-debug-get-logging-categories:

Debug.GetLoggingCategories
~~~~~~~~~~~~~~~~~~~~~~~~~~

Get all available logging categories.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "loggingCategories": [
       "$ref:LoggingCategory"
     ]
   }

See also: `LoggingCategory <#raw-api-logging-category>`__

.. _raw-api-debug-set-logging-category-level:

Debug.SetLoggingCategoryLevel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set the logging category with the given name to the given logging level.

Params
^^^^^^

.. code-block:: json

   {
     "level": "$ref:LoggingLevel",
     "name": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "debugError": "$ref:DebugError"
   }

See also: `DebugError <#raw-api-debug-error>`__, `LoggingLevel <#raw-api-logging-level>`__

.. _raw-api-integrations-add-thing:

Integrations.AddThing
~~~~~~~~~~~~~~~~~~~~~

Add a new thing to the system. Only things with a setupMethod of SetupMethodJustAdd can be added this way. For things with a setupMethod different than SetupMethodJustAdd, use PairThing. Things with CreateMethodJustAdd require all parameters to be supplied here. Things with CreateMethodDiscovery require the use of a thingDescriptorId. For discovered things, params are not required and will be taken from the ThingDescriptor, however, they may be overridden by supplying thingParams.

Params
^^^^^^

.. code-block:: json

   {
     "name": "String",
     "o:thingClassId": "Uuid",
     "o:thingDescriptorId": "Uuid",
     "o:thingParams": "$ref:ParamList"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "o:displayMessage": "String",
     "o:thingId": "Uuid",
     "thingError": "$ref:ThingError"
   }

See also: `ParamList <#raw-api-param-list>`__, `ThingError <#raw-api-thing-error>`__

.. _raw-api-integrations-browse-thing:

Integrations.BrowseThing
~~~~~~~~~~~~~~~~~~~~~~~~

Browse a thing. If a ThingClass indicates a thing is browsable, this method will return the BrowserItems. If no parameter besides the thingId is used, the root node of this thingwill be returned. Any returned item which is browsable can be passed as node. Results will be children of the given node.

In case of an error during browsing, the error will be indicated and the displayMessage may contain additional information for the user. The displayMessage will be translated. A client UI showing this message to the user should be prepared for empty, but also longer strings.

Params
^^^^^^

.. code-block:: json

   {
     "o:itemId": "String",
     "thingId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "o:displayMessage": "String",
     "o:items": [
       "$ref:BrowserItem"
     ],
     "thingError": "$ref:ThingError"
   }

See also: `BrowserItem <#raw-api-browser-item>`__, `ThingError <#raw-api-thing-error>`__

.. _raw-api-integrations-confirm-pairing:

Integrations.ConfirmPairing
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Confirm an ongoing pairing. For SetupMethodUserAndPassword, provide the username in the "username" field and the password in the "secret" field. For SetupMethodEnterPin and provide the PIN in the "secret" field. In case of SetupMethodOAuth, the previously opened web view will eventually be redirected to http://128.0.0.1:8888 and the OAuth code as query parameters to this url. Provide the entire unmodified URL in the secret field.

Params
^^^^^^

.. code-block:: json

   {
     "o:secret": "String",
     "o:username": "String",
     "pairingTransactionId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "o:displayMessage": "String",
     "o:thingId": "Uuid",
     "thingError": "$ref:ThingError"
   }

See also: `ThingError <#raw-api-thing-error>`__

.. _raw-api-integrations-connect-i-o:

Integrations.ConnectIO
~~~~~~~~~~~~~~~~~~~~~~

Connect two generic IO states. Input and output need to be compatible, that is, either a digital input and a digital output, or an analog input and an analog output. If successful, the connectionId will be returned.

Params
^^^^^^

.. code-block:: json

   {
     "inputStateTypeId": "Uuid",
     "inputThingId": "Uuid",
     "o:inverted": "Bool",
     "outputStateTypeId": "Uuid",
     "outputThingId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "o:ioConnectionId": "Uuid",
     "thingError": "$ref:ThingError"
   }

See also: `ThingError <#raw-api-thing-error>`__

.. _raw-api-integrations-disconnect-i-o:

Integrations.DisconnectIO
~~~~~~~~~~~~~~~~~~~~~~~~~

Disconnect an existing IO connection.

Params
^^^^^^

.. code-block:: json

   {
     "ioConnectionId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "thingError": "$ref:ThingError"
   }

See also: `ThingError <#raw-api-thing-error>`__

.. _raw-api-integrations-discover-things:

Integrations.DiscoverThings
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Performs a thing discovery for things of the given thingClassId and returns the results. This function may take a while to return. Note that this method will include all the found things, that is, including things that may already have been added. Those things will have thingId set to the id of the already added thing. Such results may be used to reconfigure existing things and might be filtered in cases where only unknown things are of interest.

Params
^^^^^^

.. code-block:: json

   {
     "o:discoveryParams": "$ref:ParamList",
     "thingClassId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "o:displayMessage": "String",
     "o:thingDescriptors": "$ref:ThingDescriptors",
     "thingError": "$ref:ThingError"
   }

See also: `ParamList <#raw-api-param-list>`__, `ThingDescriptors <#raw-api-thing-descriptors>`__, `ThingError <#raw-api-thing-error>`__

.. _raw-api-integrations-edit-thing:

Integrations.EditThing
~~~~~~~~~~~~~~~~~~~~~~

Edit the name of a thing.

Params
^^^^^^

.. code-block:: json

   {
     "name": "String",
     "thingId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "thingError": "$ref:ThingError"
   }

See also: `ThingError <#raw-api-thing-error>`__

.. _raw-api-integrations-execute-action:

Integrations.ExecuteAction
~~~~~~~~~~~~~~~~~~~~~~~~~~

Execute a single action.

Params
^^^^^^

.. code-block:: json

   {
     "actionTypeId": "Uuid",
     "o:params": "$ref:ParamList",
     "thingId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "o:displayMessage": "String",
     "thingError": "$ref:ThingError"
   }

See also: `ParamList <#raw-api-param-list>`__, `ThingError <#raw-api-thing-error>`__

.. _raw-api-integrations-execute-browser-item:

Integrations.ExecuteBrowserItem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Execute the item identified by itemId on the given thing.

In case of an error during execution, the error will be indicated and the displayMessage may contain additional information for the user. The displayMessage will be translated. A client UI showing this message to the user should be prepared for empty, but also longer strings.

Params
^^^^^^

.. code-block:: json

   {
     "itemId": "String",
     "thingId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "o:displayMessage": "String",
     "thingError": "$ref:ThingError"
   }

See also: `ThingError <#raw-api-thing-error>`__

.. _raw-api-integrations-execute-browser-item-action:

Integrations.ExecuteBrowserItemAction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Execute the action for the browser item identified by actionTypeId and the itemId on the given thing.

In case of an error during execution, the error will be indicated and the displayMessage may contain additional information for the user. The displayMessage will be translated. A client UI showing this message to the user should be prepared for empty, but also longer strings.

Params
^^^^^^

.. code-block:: json

   {
     "actionTypeId": "Uuid",
     "itemId": "String",
     "o:params": "$ref:ParamList",
     "thingId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "o:displayMessage": "String",
     "thingError": "$ref:ThingError"
   }

See also: `ParamList <#raw-api-param-list>`__, `ThingError <#raw-api-thing-error>`__

.. _raw-api-integrations-get-action-types:

Integrations.GetActionTypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get action types for a specified thingClassId.

Params
^^^^^^

.. code-block:: json

   {
     "thingClassId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "actionTypes": "$ref:ActionTypes"
   }

See also: `ActionTypes <#raw-api-action-types>`__

.. _raw-api-integrations-get-browser-item:

Integrations.GetBrowserItem
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get a single item from the browser. This won't give any more info on an item than a regular BrowseThing call, but it allows to fetch details of an item if only the ID is known.

In case of an error during browsing, the error will be indicated and the displayMessage may contain additional information for the user. The displayMessage will be translated. A client UI showing this message to the user should be prepared for empty, but also longer strings.

Params
^^^^^^

.. code-block:: json

   {
     "o:itemId": "String",
     "thingId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "o:displayMessage": "String",
     "o:item": "$ref:BrowserItem",
     "thingError": "$ref:ThingError"
   }

See also: `BrowserItem <#raw-api-browser-item>`__, `ThingError <#raw-api-thing-error>`__

.. _raw-api-integrations-get-event-types:

Integrations.GetEventTypes
~~~~~~~~~~~~~~~~~~~~~~~~~~

Get event types for a specified thingClassId.

Params
^^^^^^

.. code-block:: json

   {
     "thingClassId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "eventTypes": "$ref:EventTypes"
   }

See also: `EventTypes <#raw-api-event-types>`__

.. _raw-api-integrations-get-i-o-connections:

Integrations.GetIOConnections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fetch IO connections. Optionally filtered by thingId and stateTypeId.

Params
^^^^^^

.. code-block:: json

   {
     "o:thingId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "o:ioConnections": "$ref:IOConnections",
     "thingError": "$ref:ThingError"
   }

See also: `IOConnections <#raw-api-i-o-connections>`__, `ThingError <#raw-api-thing-error>`__

.. _raw-api-integrations-get-plugin-configuration:

Integrations.GetPluginConfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get a plugin's params.

Params
^^^^^^

.. code-block:: json

   {
     "pluginId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "o:configuration": "$ref:ParamList",
     "thingError": "$ref:ThingError"
   }

See also: `ParamList <#raw-api-param-list>`__, `ThingError <#raw-api-thing-error>`__

.. _raw-api-integrations-get-plugins:

Integrations.GetPlugins
~~~~~~~~~~~~~~~~~~~~~~~

Returns a list of loaded plugins.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "plugins": "$ref:IntegrationPlugins"
   }

See also: `IntegrationPlugins <#raw-api-integration-plugins>`__

.. _raw-api-integrations-get-state-types:

Integrations.GetStateTypes
~~~~~~~~~~~~~~~~~~~~~~~~~~

Get state types for a specified thingClassId.

Params
^^^^^^

.. code-block:: json

   {
     "thingClassId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "stateTypes": "$ref:StateTypes"
   }

See also: `StateTypes <#raw-api-state-types>`__

.. _raw-api-integrations-get-state-value:

Integrations.GetStateValue
~~~~~~~~~~~~~~~~~~~~~~~~~~

Get the value of the given thing and the given stateType

Params
^^^^^^

.. code-block:: json

   {
     "stateTypeId": "Uuid",
     "thingId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "o:value": "Variant",
     "thingError": "$ref:ThingError"
   }

See also: `ThingError <#raw-api-thing-error>`__

.. _raw-api-integrations-get-state-values:

Integrations.GetStateValues
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get all the state values of the given thing.

Params
^^^^^^

.. code-block:: json

   {
     "thingId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "o:values": "$ref:States",
     "thingError": "$ref:ThingError"
   }

See also: `States <#raw-api-states>`__, `ThingError <#raw-api-thing-error>`__

.. _raw-api-integrations-get-thing-classes:

Integrations.GetThingClasses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns a list of supported thing classes, optionally filtered by vendorId or by a list of thing class ids.

Params
^^^^^^

.. code-block:: json

   {
     "o:thingClassIds": [
       "Uuid"
     ],
     "o:vendorId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "o:thingClasses": "$ref:ThingClasses",
     "thingError": "$ref:ThingError"
   }

See also: `ThingClasses <#raw-api-thing-classes>`__, `ThingError <#raw-api-thing-error>`__

.. _raw-api-integrations-get-things:

Integrations.GetThings
~~~~~~~~~~~~~~~~~~~~~~

Returns a list of configured things, optionally filtered by thingId.

Params
^^^^^^

.. code-block:: json

   {
     "o:thingId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "o:things": "$ref:Things",
     "thingError": "$ref:ThingError"
   }

See also: `ThingError <#raw-api-thing-error>`__, `Things <#raw-api-things>`__

.. _raw-api-integrations-get-vendors:

Integrations.GetVendors
~~~~~~~~~~~~~~~~~~~~~~~

Returns a list of supported Vendors.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "vendors": "$ref:Vendors"
   }

See also: `Vendors <#raw-api-vendors>`__

.. _raw-api-integrations-pair-thing:

Integrations.PairThing
~~~~~~~~~~~~~~~~~~~~~~

Pair a new thing. Use this to set up or reconfigure things for ThingClasses with a setupMethod different than SetupMethodJustAdd. Depending on the CreateMethod and whether a new thing is set up or an existing one is reconfigured, different parameters are required:

CreateMethodJustAdd takes the thingClassId and the parameters you want to have with that thing. If an existing thing should be reconfigured, the thingId of said thing should be given additionally.

CreateMethodDiscovery requires the use of a thingDescriptorId, previously obtained with DiscoverThings. Optionally, parameters can be overridden with the give thingParams. ThingDescriptors containing a thingId will reconfigure an existing thing, descriptors without a thingId will add a new thing to the system.

If success is true, the return values will contain a pairingTransactionId, a displayMessage and the setupMethod. Depending on the setupMethod, the application should present the use an appropriate login mask, that is, For SetupMethodDisplayPin the user should enter a pin that is displayed on the device or online service, for SetupMethodEnterPin the application should present the given PIN so the user can enter it on the device or online service. For SetupMethodPushButton, the displayMessage shall be presented to the user as informational hints to press a button on the device. For SetupMethodUserAndPassword a login mask for a user and password login should be presented to the user. In case of SetupMethodOAuth, an OAuth URL will be returned which shall be opened in a web view to allow the user logging in.

Once the login procedure has completed, the application shall proceed with ConfirmPairing, providing the results of the pairing procedure.

Params
^^^^^^

.. code-block:: json

   {
     "o:name": "String",
     "o:thingClassId": "Uuid",
     "o:thingDescriptorId": "Uuid",
     "o:thingId": "Uuid",
     "o:thingParams": "$ref:ParamList"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "o:displayMessage": "String",
     "o:oAuthUrl": "String",
     "o:pairingTransactionId": "Uuid",
     "o:pin": "String",
     "o:setupMethod": "$ref:SetupMethod",
     "thingError": "$ref:ThingError"
   }

See also: `ParamList <#raw-api-param-list>`__, `SetupMethod <#raw-api-setup-method>`__, `ThingError <#raw-api-thing-error>`__

.. _raw-api-integrations-reconfigure-thing:

Integrations.ReconfigureThing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reconfigure a thing. This comes down to removing and recreating a thing with new parameters but keeping its thing id the same (and with that keeping rules, tags etc). For things with create method CreateMethodDiscovery, a discovery (DiscoverThings) shall be performed first and this method is to be called with a thingDescriptorId of the re-discovered thing instead of the thingId directly. Thing parameters will be taken from the discovery, but can be overridden individually here by providing them in the thingParams parameter. Only writable parameters can be changed.

Params
^^^^^^

.. code-block:: json

   {
     "o:thingDescriptorId": "Uuid",
     "o:thingId": "Uuid",
     "o:thingParams": "$ref:ParamList"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "o:displayMessage": "String",
     "thingError": "$ref:ThingError"
   }

See also: `ParamList <#raw-api-param-list>`__, `ThingError <#raw-api-thing-error>`__

.. _raw-api-integrations-remove-thing:

Integrations.RemoveThing
~~~~~~~~~~~~~~~~~~~~~~~~

Remove a thing and all its childs from the system. RemovePolicy is deprecated and has no effect any more.

Params
^^^^^^

.. code-block:: json

   {
     "d:o:removePolicy": "String",
     "thingId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "thingError": "$ref:ThingError"
   }

See also: `ThingError <#raw-api-thing-error>`__

.. _raw-api-integrations-set-action-logging:

Integrations.SetActionLogging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enable/disable logging for the given action type on the given thing.

Params
^^^^^^

.. code-block:: json

   {
     "actionTypeId": "Uuid",
     "enabled": "Bool",
     "thingId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "thingError": "$ref:ThingError"
   }

See also: `ThingError <#raw-api-thing-error>`__

.. _raw-api-integrations-set-event-logging:

Integrations.SetEventLogging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enable/disable logging for the given event type on the given thing.

Params
^^^^^^

.. code-block:: json

   {
     "enabled": "Bool",
     "eventTypeId": "Uuid",
     "thingId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "thingError": "$ref:ThingError"
   }

See also: `ThingError <#raw-api-thing-error>`__

.. _raw-api-integrations-set-plugin-configuration:

Integrations.SetPluginConfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set a plugin's params.

Params
^^^^^^

.. code-block:: json

   {
     "configuration": "$ref:ParamList",
     "pluginId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "thingError": "$ref:ThingError"
   }

See also: `ParamList <#raw-api-param-list>`__, `ThingError <#raw-api-thing-error>`__

.. _raw-api-integrations-set-state-filter:

Integrations.SetStateFilter
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set the filter for the given state on the given thing.

Params
^^^^^^

.. code-block:: json

   {
     "filter": "$ref:StateValueFilter",
     "stateTypeId": "Uuid",
     "thingId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "thingError": "$ref:ThingError"
   }

See also: `StateValueFilter <#raw-api-state-value-filter>`__, `ThingError <#raw-api-thing-error>`__

.. _raw-api-integrations-set-state-logging:

Integrations.SetStateLogging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enable/disable logging for the given state type on the given thing.

Params
^^^^^^

.. code-block:: json

   {
     "enabled": "Bool",
     "stateTypeId": "Uuid",
     "thingId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "thingError": "$ref:ThingError"
   }

See also: `ThingError <#raw-api-thing-error>`__

.. _raw-api-integrations-set-thing-settings:

Integrations.SetThingSettings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Change the settings of a thing.

Params
^^^^^^

.. code-block:: json

   {
     "settings": "$ref:ParamList",
     "thingId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "thingError": "$ref:ThingError"
   }

See also: `ParamList <#raw-api-param-list>`__, `ThingError <#raw-api-thing-error>`__

.. _raw-api-j-s-o-n-r-p-c-authenticate:

JSONRPC.Authenticate
~~~~~~~~~~~~~~~~~~~~

Authenticate a client to the api via user & password challenge. Provide a device name which allows the user to identify the client and revoke the token in case the device is lost or stolen. This will return a new token to be used to authorize a client at the API.

Params
^^^^^^

.. code-block:: json

   {
     "deviceName": "String",
     "password": "String",
     "username": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "o:scopes": "$ref:PermissionScopes",
     "o:token": "String",
     "o:username": "String",
     "success": "Bool"
   }

See also: `PermissionScopes <#raw-api-permission-scopes>`__

.. _raw-api-j-s-o-n-r-p-c-create-user:

JSONRPC.CreateUser
~~~~~~~~~~~~~~~~~~

Create a new user in the API. This is only allowed to be called when the initial setup is required. To create additional users, use Users.CreateUser instead. Call Authenticate after this to obtain a device token for the newly created user.

Params
^^^^^^

.. code-block:: json

   {
     "o:displayName": "String",
     "o:email": "String",
     "password": "String",
     "username": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "error": "$ref:UserError"
   }

See also: `UserError <#raw-api-user-error>`__

.. _raw-api-j-s-o-n-r-p-c-hello:

JSONRPC.Hello
~~~~~~~~~~~~~

Initiates a connection. Use this method to perform an initial handshake of the connection. Optionally, a parameter "locale" is can be passed to set up the used locale for this connection. Strings such as ThingClass displayNames etc will be localized to this locale. If this parameter is omitted, the default system locale (depending on the configuration) is used. The reply of this method contains information about this core instance such as version information, uuid and its name. The locale valueindicates the locale used for this connection. Note: This method can be called multiple times. The locale used in the last call for this connection will be used. Other values, like initialSetupRequired might change if the setup has been performed in the meantime.

 The field cacheHashes may contain a map of methods and MD5 hashes. As long as the hash for a method does not change, a client may use a previously cached copy of the call instead of fetching the content again. While the Hello call doesn't necessarily require a token, this can be called with a token. If a token is provided, it will be verified and the reply contains information about the tokens validity and the user and permissions for the given token.

Params
^^^^^^

.. code-block:: json

   {
     "o:locale": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "authenticationRequired": "Bool",
     "initialSetupRequired": "Bool",
     "language": "String",
     "locale": "String",
     "name": "String",
     "o:authenticated": "Bool",
     "o:cacheHashes": [
       "$ref:CacheHash"
     ],
     "o:experiences": [
       "$ref:Experience"
     ],
     "o:permissionScopes": "$ref:PermissionScopes",
     "o:username": "String",
     "protocol version": "String",
     "pushButtonAuthAvailable": "Bool",
     "server": "String",
     "uuid": "Uuid",
     "version": "String"
   }

See also: `CacheHash <#raw-api-cache-hash>`__, `Experience <#raw-api-experience>`__, `PermissionScopes <#raw-api-permission-scopes>`__

.. _raw-api-j-s-o-n-r-p-c-introspect:

JSONRPC.Introspect
~~~~~~~~~~~~~~~~~~

Introspect this API.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "methods": "Object",
     "notifications": "Object",
     "types": "Object"
   }

.. _raw-api-j-s-o-n-r-p-c-keep-alive:

JSONRPC.KeepAlive
~~~~~~~~~~~~~~~~~

This is basically a Ping/Pong mechanism a client app may use to check server connectivity. Currently, the server does not actually do anything with this information and will return the call providing the given sessionId back to the caller. It is up to the client whether to use this or not and not required by the server to keep the connection alive.

Params
^^^^^^

.. code-block:: json

   {
     "sessionId": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "sessionId": "String",
     "success": "Bool"
   }

.. _raw-api-j-s-o-n-r-p-c-request-push-button-auth:

JSONRPC.RequestPushButtonAuth
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Authenticate a client to the api via Push Button method. Provide a device name which allows the user to identify the client and revoke the token in case the device is lost or stolen. If push button hardware is available, this will return with success and start listening for push button presses. When the push button is pressed, the PushButtonAuthFinished notification will be sent to the requesting client. The procedure will be cancelled when the connection is interrupted. If another client requests push button authentication while a procedure is still going on, the second call will take over and the first one will be notified by the PushButtonAuthFinished signal about the error. The application should make it clear to the user to not press the button when the procedure fails as this can happen for 2 reasons: a) a second user is trying to auth at the same time and only the currently active user should press the button or b) it might indicate an attacker trying to take over and snooping in for tokens.

Params
^^^^^^

.. code-block:: json

   {
     "deviceName": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "success": "Bool",
     "transactionId": "Int"
   }

.. _raw-api-j-s-o-n-r-p-c-set-notification-status:

JSONRPC.SetNotificationStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enable/Disable notifications for this connections. Either "enabled" or "namespaces" needs to be given but not both of them. The boolean based "enabled" parameter will enable/disable all notifications at once. If instead the list-based "namespaces" parameter is provided, all given namespaceswill be enabled, the others will be disabled. The return value of "success" will indicate success of the operation. The "enabled" property in the return value is deprecated and used for legacy compatibilty only. It will be set to true if at least one namespace has been enabled.

Params
^^^^^^

.. code-block:: json

   {
     "d:o:enabled": "Bool",
     "o:namespaces": "StringList"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "d:enabled": "Bool",
     "namespaces": "StringList"
   }

.. _raw-api-j-s-o-n-r-p-c-version:

JSONRPC.Version
~~~~~~~~~~~~~~~

Version of this nymea/JSONRPC interface.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "protocol version": "String",
     "qtBuildVersion": "String",
     "qtVersion": "String",
     "version": "String"
   }

.. _raw-api-logging-get-log-entries:

Logging.GetLogEntries
~~~~~~~~~~~~~~~~~~~~~

Get the LogEntries matching the given filter. 

"sources": Builtin sources are: "core", "rules", "scripts", "integrations". May be extended by experience plugins.

"columns": Columns to be returned.

"filter": A map of column:value entries. Only = is supported currently.

"startTime": The datetime of the oldest entry, in ms.

"endTime": The datetime of the newest entry, in ms.

"sampleRate": If given, returns a sampled series of the values, filling in gaps with the previous value.

"sortOrder": Sort order of results. Note that this impacts the filling of gaps when resampling.

"limit": Maximum amount of entries to be returned.

"offset": Offset to be skipped before returning entries.

Params
^^^^^^

.. code-block:: json

   {
     "o:columns": [
       "String"
     ],
     "o:endTime": "Uint",
     "o:filter": "Variant",
     "o:limit": "Int",
     "o:offset": "Int",
     "o:sampleRate": "$ref:SampleRate",
     "o:sortOrder": "$ref:SortOrder",
     "o:startTime": "Uint",
     "sources": [
       "String"
     ]
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "count": "Int",
     "o:logEntries": "$ref:LogEntries",
     "offset": "Int"
   }

See also: `LogEntries <#raw-api-log-entries>`__, `SampleRate <#raw-api-sample-rate>`__, `SortOrder <#raw-api-sort-order>`__

.. _raw-api-modbus-rtu-add-modbus-rtu-master:

ModbusRtu.AddModbusRtuMaster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add a new modbus RTU master with the given configuration. The timeout value is in milli seconds and the minimum value is 10 ms.

Params
^^^^^^

.. code-block:: json

   {
     "baudrate": "Uint",
     "dataBits": "$ref:SerialPortDataBits",
     "numberOfRetries": "Uint",
     "parity": "$ref:SerialPortParity",
     "serialPort": "String",
     "stopBits": "$ref:SerialPortStopBits",
     "timeout": "Uint"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "modbusError": "$ref:ModbusRtuError",
     "o:modbusUuid": "Uuid"
   }

See also: `ModbusRtuError <#raw-api-modbus-rtu-error>`__, `SerialPortDataBits <#raw-api-serial-port-data-bits>`__, `SerialPortParity <#raw-api-serial-port-parity>`__, `SerialPortStopBits <#raw-api-serial-port-stop-bits>`__

.. _raw-api-modbus-rtu-get-modbus-rtu-masters:

ModbusRtu.GetModbusRtuMasters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get the list of configured modbus RTU masters.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "modbusError": "$ref:ModbusRtuError",
     "o:modbusRtuMasters": [
       "$ref:ModbusRtuMaster"
     ]
   }

See also: `ModbusRtuError <#raw-api-modbus-rtu-error>`__, `ModbusRtuMaster <#raw-api-modbus-rtu-master>`__

.. _raw-api-modbus-rtu-get-serial-ports:

ModbusRtu.GetSerialPorts
~~~~~~~~~~~~~~~~~~~~~~~~

Get the list of available serial ports from the host system.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "serialPorts": "$ref:SerialPorts"
   }

See also: `SerialPorts <#raw-api-serial-ports>`__

.. _raw-api-modbus-rtu-reconfigure-modbus-rtu-master:

ModbusRtu.ReconfigureModbusRtuMaster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reconfigure the modbus RTU master with the given UUID and configuration.

Params
^^^^^^

.. code-block:: json

   {
     "baudrate": "Uint",
     "dataBits": "$ref:SerialPortDataBits",
     "modbusUuid": "Uuid",
     "numberOfRetries": "Uint",
     "parity": "$ref:SerialPortParity",
     "serialPort": "String",
     "stopBits": "$ref:SerialPortStopBits",
     "timeout": "Uint"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "modbusError": "$ref:ModbusRtuError"
   }

See also: `ModbusRtuError <#raw-api-modbus-rtu-error>`__, `SerialPortDataBits <#raw-api-serial-port-data-bits>`__, `SerialPortParity <#raw-api-serial-port-parity>`__, `SerialPortStopBits <#raw-api-serial-port-stop-bits>`__

.. _raw-api-modbus-rtu-remove-modbus-rtu-master:

ModbusRtu.RemoveModbusRtuMaster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove the modbus RTU master with the given modbus UUID.

Params
^^^^^^

.. code-block:: json

   {
     "modbusUuid": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "modbusError": "$ref:ModbusRtuError"
   }

See also: `ModbusRtuError <#raw-api-modbus-rtu-error>`__

.. _raw-api-network-manager-connect-wifi-network:

NetworkManager.ConnectWifiNetwork
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connect to the wifi network with the given ssid and password.

Params
^^^^^^

.. code-block:: json

   {
     "interface": "String",
     "o:password": "String",
     "ssid": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "networkManagerError": "$ref:NetworkManagerError"
   }

See also: `NetworkManagerError <#raw-api-network-manager-error>`__

.. _raw-api-network-manager-create-wired-connection:

NetworkManager.CreateWiredConnection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a wired connection.

Params
^^^^^^

.. code-block:: json

   {
     "interface": "String",
     "o:dns": "String",
     "o:gateway": "String",
     "o:ip": "String",
     "o:prefix": "Uint",
     "type": "$ref:WiredNetworkConnectionType"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "networkManagerError": "$ref:NetworkManagerError"
   }

See also: `NetworkManagerError <#raw-api-network-manager-error>`__, `WiredNetworkConnectionType <#raw-api-wired-network-connection-type>`__

.. _raw-api-network-manager-disconnect-interface:

NetworkManager.DisconnectInterface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Disconnect the given network interface. The interface will remain disconnected until the user connect it again.

Params
^^^^^^

.. code-block:: json

   {
     "interface": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "networkManagerError": "$ref:NetworkManagerError"
   }

See also: `NetworkManagerError <#raw-api-network-manager-error>`__

.. _raw-api-network-manager-enable-networking:

NetworkManager.EnableNetworking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enable or disable networking in the NetworkManager.

Params
^^^^^^

.. code-block:: json

   {
     "enable": "Bool"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "networkManagerError": "$ref:NetworkManagerError"
   }

See also: `NetworkManagerError <#raw-api-network-manager-error>`__

.. _raw-api-network-manager-enable-wireless-networking:

NetworkManager.EnableWirelessNetworking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enable or disable wireless networking in the NetworkManager.

Params
^^^^^^

.. code-block:: json

   {
     "enable": "Bool"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "networkManagerError": "$ref:NetworkManagerError"
   }

See also: `NetworkManagerError <#raw-api-network-manager-error>`__

.. _raw-api-network-manager-get-network-devices:

NetworkManager.GetNetworkDevices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get the list of current network devices.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "networkManagerError": "$ref:NetworkManagerError",
     "o:wiredNetworkDevices": [
       "$ref:WiredNetworkDevice"
     ],
     "o:wirelessNetworkDevices": [
       "$ref:WirelessNetworkDevice"
     ]
   }

See also: `NetworkManagerError <#raw-api-network-manager-error>`__, `WiredNetworkDevice <#raw-api-wired-network-device>`__, `WirelessNetworkDevice <#raw-api-wireless-network-device>`__

.. _raw-api-network-manager-get-network-status:

NetworkManager.GetNetworkStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get the current network manager status.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "networkManagerError": "$ref:NetworkManagerError",
     "o:status": {
       "networkingEnabled": "Bool",
       "state": "$ref:NetworkManagerState",
       "wirelessNetworkingEnabled": "Bool"
     }
   }

See also: `NetworkManagerError <#raw-api-network-manager-error>`__, `NetworkManagerState <#raw-api-network-manager-state>`__

.. _raw-api-network-manager-get-wireless-access-points:

NetworkManager.GetWirelessAccessPoints
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get the current list of wireless network access points for the given interface. The interface has to be a WirelessNetworkDevice.

Params
^^^^^^

.. code-block:: json

   {
     "interface": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "networkManagerError": "$ref:NetworkManagerError",
     "o:wirelessAccessPoints": [
       "$ref:WirelessAccessPoint"
     ]
   }

See also: `NetworkManagerError <#raw-api-network-manager-error>`__, `WirelessAccessPoint <#raw-api-wireless-access-point>`__

.. _raw-api-network-manager-scan-wifi-networks:

NetworkManager.ScanWifiNetworks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Start a wifi scan for searching new networks.

Params
^^^^^^

.. code-block:: json

   {
     "interface": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "networkManagerError": "$ref:NetworkManagerError"
   }

See also: `NetworkManagerError <#raw-api-network-manager-error>`__

.. _raw-api-network-manager-start-access-point:

NetworkManager.StartAccessPoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Start a WiFi Access point on the given interface with the given SSID and password. Use DisconnectInterface to stop it again.

Params
^^^^^^

.. code-block:: json

   {
     "interface": "String",
     "password": "String",
     "ssid": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "networkManagerError": "$ref:NetworkManagerError"
   }

See also: `NetworkManagerError <#raw-api-network-manager-error>`__

.. _raw-api-rules-add-rule:

Rules.AddRule
~~~~~~~~~~~~~

Add a rule. You can describe rules by one or many EventDesciptors and a StateEvaluator. Note that only one of either eventDescriptor or eventDescriptorList may be passed at a time. A rule can be created but left disabled, meaning it won't actually be executed until set to enabled. If not given, enabled defaults to true. A rule can have a list of actions and exitActions. It must have at least one Action. For state based rules, actions will be executed when the system enters a state matching the stateDescriptor. The exitActions will be executed when the system leaves the described state again. For event based rules, actions will be executed when a matching event happens and if the stateEvaluator matches the system's state. ExitActions for such rules will be executed when a matching event happens and the stateEvaluator is not matching the system's state. A rule marked as executable can be executed via the API using Rules.ExecuteRule, that means, its actions will be executed regardless of the eventDescriptor and stateEvaluators.

Params
^^^^^^

.. code-block:: json

   {
     "actions": [
       "$ref:RuleAction"
     ],
     "name": "String",
     "o:enabled": "Bool",
     "o:eventDescriptors": [
       "$ref:EventDescriptor"
     ],
     "o:executable": "Bool",
     "o:exitActions": [
       "$ref:RuleAction"
     ],
     "o:stateEvaluator": "$ref:StateEvaluator",
     "o:timeDescriptor": "$ref:TimeDescriptor"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "o:ruleId": "Uuid",
     "ruleError": "$ref:RuleError"
   }

See also: `EventDescriptor <#raw-api-event-descriptor>`__, `RuleAction <#raw-api-rule-action>`__, `RuleError <#raw-api-rule-error>`__, `StateEvaluator <#raw-api-state-evaluator>`__, `TimeDescriptor <#raw-api-time-descriptor>`__

.. _raw-api-rules-disable-rule:

Rules.DisableRule
~~~~~~~~~~~~~~~~~

Disable a rule. The rule won't be triggered by it's events or state changes while it is disabled. If successful, the notification "Rule.RuleConfigurationChanged" will be emitted.

Params
^^^^^^

.. code-block:: json

   {
     "ruleId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "ruleError": "$ref:RuleError"
   }

See also: `RuleError <#raw-api-rule-error>`__

.. _raw-api-rules-edit-rule:

Rules.EditRule
~~~~~~~~~~~~~~

Edit the parameters of a rule. The configuration of the rule with the given ruleId will be replaced with the new given configuration. In ordert to enable or disable a Rule, please use the methods "Rules.EnableRule" and "Rules.DisableRule". If successful, the notification "Rule.RuleConfigurationChanged" will be emitted.

Params
^^^^^^

.. code-block:: json

   {
     "actions": [
       "$ref:RuleAction"
     ],
     "name": "String",
     "o:enabled": "Bool",
     "o:eventDescriptors": [
       "$ref:EventDescriptor"
     ],
     "o:executable": "Bool",
     "o:exitActions": [
       "$ref:RuleAction"
     ],
     "o:stateEvaluator": "$ref:StateEvaluator",
     "o:timeDescriptor": "$ref:TimeDescriptor",
     "ruleId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "o:rule": "$ref:Rule",
     "ruleError": "$ref:RuleError"
   }

See also: `EventDescriptor <#raw-api-event-descriptor>`__, `Rule <#raw-api-rule>`__, `RuleAction <#raw-api-rule-action>`__, `RuleError <#raw-api-rule-error>`__, `StateEvaluator <#raw-api-state-evaluator>`__, `TimeDescriptor <#raw-api-time-descriptor>`__

.. _raw-api-rules-enable-rule:

Rules.EnableRule
~~~~~~~~~~~~~~~~

Enabled a rule that has previously been disabled.If successful, the notification "Rule.RuleConfigurationChanged" will be emitted.

Params
^^^^^^

.. code-block:: json

   {
     "ruleId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "ruleError": "$ref:RuleError"
   }

See also: `RuleError <#raw-api-rule-error>`__

.. _raw-api-rules-execute-actions:

Rules.ExecuteActions
~~~~~~~~~~~~~~~~~~~~

Execute the action list of the rule with the given ruleId.

Params
^^^^^^

.. code-block:: json

   {
     "ruleId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "ruleError": "$ref:RuleError"
   }

See also: `RuleError <#raw-api-rule-error>`__

.. _raw-api-rules-execute-exit-actions:

Rules.ExecuteExitActions
~~~~~~~~~~~~~~~~~~~~~~~~

Execute the exit action list of the rule with the given ruleId.

Params
^^^^^^

.. code-block:: json

   {
     "ruleId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "ruleError": "$ref:RuleError"
   }

See also: `RuleError <#raw-api-rule-error>`__

.. _raw-api-rules-find-rules:

Rules.FindRules
~~~~~~~~~~~~~~~

Find a list of rules containing any of the given parameters.

Params
^^^^^^

.. code-block:: json

   {
     "thingId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "ruleIds": [
       "Uuid"
     ]
   }

.. _raw-api-rules-get-rule-details:

Rules.GetRuleDetails
~~~~~~~~~~~~~~~~~~~~

Get details for the rule identified by ruleId

Params
^^^^^^

.. code-block:: json

   {
     "ruleId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "o:rule": "$ref:Rule",
     "ruleError": "$ref:RuleError"
   }

See also: `Rule <#raw-api-rule>`__, `RuleError <#raw-api-rule-error>`__

.. _raw-api-rules-get-rules:

Rules.GetRules
~~~~~~~~~~~~~~

Get the descriptions of all configured rules. If you need more information about a specific rule use the method Rules.GetRuleDetails.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "ruleDescriptions": [
       "$ref:RuleDescription"
     ]
   }

See also: `RuleDescription <#raw-api-rule-description>`__

.. _raw-api-rules-remove-rule:

Rules.RemoveRule
~~~~~~~~~~~~~~~~

Remove a rule

Params
^^^^^^

.. code-block:: json

   {
     "ruleId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "ruleError": "$ref:RuleError"
   }

See also: `RuleError <#raw-api-rule-error>`__

.. _raw-api-scripts-add-script:

Scripts.AddScript
~~~~~~~~~~~~~~~~~

Add a script

Params
^^^^^^

.. code-block:: json

   {
     "content": "String",
     "name": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "o:errors": "StringList",
     "o:script": "$ref:Script",
     "scriptError": "$ref:ScriptError"
   }

See also: `Script <#raw-api-script>`__, `ScriptError <#raw-api-script-error>`__

.. _raw-api-scripts-edit-script:

Scripts.EditScript
~~~~~~~~~~~~~~~~~~

Edit a script

Params
^^^^^^

.. code-block:: json

   {
     "id": "Uuid",
     "o:content": "String",
     "o:name": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "o:errors": "StringList",
     "scriptError": "$ref:ScriptError"
   }

See also: `ScriptError <#raw-api-script-error>`__

.. _raw-api-scripts-get-script-content:

Scripts.GetScriptContent
~~~~~~~~~~~~~~~~~~~~~~~~

Get a scripts content.

Params
^^^^^^

.. code-block:: json

   {
     "id": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "o:content": "String",
     "scriptError": "$ref:ScriptError"
   }

See also: `ScriptError <#raw-api-script-error>`__

.. _raw-api-scripts-get-scripts:

Scripts.GetScripts
~~~~~~~~~~~~~~~~~~

Get all script, that is, their names and properties, but no content.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "scripts": "$ref:Scripts"
   }

See also: `Scripts <#raw-api-scripts>`__

.. _raw-api-scripts-remove-script:

Scripts.RemoveScript
~~~~~~~~~~~~~~~~~~~~

remove a script

Params
^^^^^^

.. code-block:: json

   {
     "id": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "scriptError": "$ref:ScriptError"
   }

See also: `ScriptError <#raw-api-script-error>`__

.. _raw-api-system-check-for-updates:

System.CheckForUpdates
~~~~~~~~~~~~~~~~~~~~~~

Instruct the system to poll the server for updates. Normally the system should automatically do this in regular intervals, however, if the client wants to allow the user to manually check for new updates now, this can be called. Returns true if the operation has been started successfully and the update manager will become busy. In order to know whether there are updates available, clients should walk through the list of packages retrieved from GetPackages and check whether there are packages with the updateAvailable flag set to true.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "success": "Bool"
   }

.. _raw-api-system-enable-repository:

System.EnableRepository
~~~~~~~~~~~~~~~~~~~~~~~

Enable or disable a repository.

Params
^^^^^^

.. code-block:: json

   {
     "enabled": "Bool",
     "repositoryId": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "success": "Bool"
   }

.. _raw-api-system-factory-reset:

System.FactoryReset
~~~~~~~~~~~~~~~~~~~

Reset nymea to factory defaults. Clients should warn the user before calling this method because all current configuration data will be lost, the server will restart immediately afterwards and it will come back up using the factory defaults if any are available.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "success": "Bool"
   }

.. _raw-api-system-get-capabilities:

System.GetCapabilities
~~~~~~~~~~~~~~~~~~~~~~

Get the list of capabilites on this system. The property "powerManagement" indicates whether restarting nymea and rebooting or shutting down is supported on this system. The property "updateManagement" indicates whether system update features are available in this system. The "updateManagementType" indicates which kind of update is supported on this platform. The property "timeManagement" indicates whether the system time can be configured on this system. Note that GetTime will be available in any case.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "powerManagement": "Bool",
     "timeManagement": "Bool",
     "updateManagement": "Bool",
     "updateManagementType": "$ref:UpdateType"
   }

See also: `UpdateType <#raw-api-update-type>`__

.. _raw-api-system-get-packages:

System.GetPackages
~~~~~~~~~~~~~~~~~~

Get the list of packages currently available to the system. This might include installed available but not installed packages. Installed packages will have the installedVersion set to a non-empty value.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "packages": "$ref:Packages"
   }

See also: `Packages <#raw-api-packages>`__

.. _raw-api-system-get-repositories:

System.GetRepositories
~~~~~~~~~~~~~~~~~~~~~~

Get the list of repositories currently available to the system.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "repositories": "$ref:Repositories"
   }

See also: `Repositories <#raw-api-repositories>`__

.. _raw-api-system-get-system-info:

System.GetSystemInfo
~~~~~~~~~~~~~~~~~~~~

Returns information about the system nymea is running on.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "deviceSerialNumber": "String"
   }

.. _raw-api-system-get-time:

System.GetTime
~~~~~~~~~~~~~~

Get the system time and configuraton. The "time" and "timeZone" properties give the current server time and time zone. "automaticTimeAvailable" indicates whether this system supports automatically setting the clock (e.g. using NTP). "automaticTime" will be true if the system is configured to automatically update the clock.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "automaticTime": "Bool",
     "automaticTimeAvailable": "Bool",
     "time": "Uint",
     "timeZone": "String"
   }

.. _raw-api-system-get-time-zones:

System.GetTimeZones
~~~~~~~~~~~~~~~~~~~

Returns the list of IANA specified time zone IDs which can be used to select a time zone. It is not required to use this method if the client toolkit already provides means to obtain a list of IANA time zone ids.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "timeZones": "StringList"
   }

.. _raw-api-system-get-update-status:

System.GetUpdateStatus
~~~~~~~~~~~~~~~~~~~~~~

Get the current status of the update system. "busy" indicates that the system is current busy with an operation regarding updates. This does not necessarily mean an actual update is running. When this is true, update related functions on the client should be marked as busy and no interaction with update components shall be allowed. An example for such a state is when the system queries the server if there are updates available, typically after a call to CheckForUpdates. "updateRunning" on the other hand indicates an actual update process is ongoing. The user should be informed about it, the system also might restart at any point while an update is running. The "updateProgress" property is optional, if the backend supports it, a progress >= 0 indicated the update progress in percentage.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "busy": "Bool",
     "o:updateProgress": "Int",
     "updateRunning": "Bool"
   }

.. _raw-api-system-reboot:

System.Reboot
~~~~~~~~~~~~~

Initiate a reboot of the system. The return value will indicate whether the procedure has been initiated successfully.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "success": "Bool"
   }

.. _raw-api-system-remove-packages:

System.RemovePackages
~~~~~~~~~~~~~~~~~~~~~

Starts removing a package. Returns true if the removal has been started successfully. Before calling this method, clients should check whether the package can be removed (canRemove set to true).

Params
^^^^^^

.. code-block:: json

   {
     "packageIds": [
       "String"
     ]
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "success": "Bool"
   }

.. _raw-api-system-restart:

System.Restart
~~~~~~~~~~~~~~

Initiate a restart of the nymea service. The return value will indicate whether the procedure has been initiated successfully.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "success": "Bool"
   }

.. _raw-api-system-rollback-packages:

System.RollbackPackages
~~~~~~~~~~~~~~~~~~~~~~~

Starts a rollback. Returns true if the rollback has been started successfully. Before calling this method, clients should check whether the package can be rolled back (canRollback set to true).

Params
^^^^^^

.. code-block:: json

   {
     "packageIds": [
       "String"
     ]
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "success": "Bool"
   }

.. _raw-api-system-set-time:

System.SetTime
~~~~~~~~~~~~~~

Set the system time configuraton. The system can be configured to update the time automatically by setting "automaticTime" to true. This will only work if the "timeManagement" capability is available on this system and "GetTime" indicates the availability of automatic time settings. If any of those requirements are not met, this method will return "false" in the "success" property. In order to manually configure the time, "automaticTime" should be set to false and "time" should be set. Note that if "automaticTime" is set to true and a manual "time" is still passed, the system will attempt to configure automatic time updates and only set the manual time if automatic mode fails. A time zone can always be passed optionally to change the system time zone and should be a IANA time zone id.

Params
^^^^^^

.. code-block:: json

   {
     "o:automaticTime": "Bool",
     "o:time": "Uint",
     "o:timeZone": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "success": "Bool"
   }

.. _raw-api-system-shutdown:

System.Shutdown
~~~~~~~~~~~~~~~

Initiate a shutdown of the system. The return value will indicate whether the procedure has been initiated successfully.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "success": "Bool"
   }

.. _raw-api-system-update-packages:

System.UpdatePackages
~~~~~~~~~~~~~~~~~~~~~

Starts updating/installing packages with the given ids. Returns true if the upgrade has been started successfully. Note that it might still fail later. Before calling this method, clients should check the packages whether they are in a state where they can either be installed (no installedVersion set) or upgraded (updateAvailable set to true).

Params
^^^^^^

.. code-block:: json

   {
     "o:packageIds": [
       "String"
     ]
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "success": "Bool"
   }

.. _raw-api-tags-add-tag:

Tags.AddTag
~~~~~~~~~~~

Add a Tag. A Tag must have a thingId OR a ruleId (call this method twice if you want to attach the same tag to a thing and a rule), an appId (Use the appId of your app), a tagId (e.g. "favorites") and a value. Upon success, a TagAdded notification will be emitted. Calling this method twice for the same ids (thing/rule, appId and tagId) but with a different value will update the tag's value and the TagValueChanged notification will be emitted.

Params
^^^^^^

.. code-block:: json

   {
     "tag": "$ref:Tag"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "tagError": "$ref:TagError"
   }

See also: `Tag <#raw-api-tag>`__, `TagError <#raw-api-tag-error>`__

.. _raw-api-tags-get-tags:

Tags.GetTags
~~~~~~~~~~~~

Get the Tags matching the given filter. Tags can be filtered by a thingID, a ruleId, an appId, a tagId or a combination of any (however, combining thingId and ruleId will return an empty result set).

Params
^^^^^^

.. code-block:: json

   {
     "o:appId": "String",
     "o:ruleId": "Uuid",
     "o:tagId": "String",
     "o:thingId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "o:tags": "$ref:Tags",
     "tagError": "$ref:TagError"
   }

See also: `TagError <#raw-api-tag-error>`__, `Tags <#raw-api-tags>`__

.. _raw-api-tags-remove-tag:

Tags.RemoveTag
~~~~~~~~~~~~~~

Remove a Tag. Tag value is optional and will be disregarded. If the ids match, the tag will be deleted and a TagRemoved notification will be emitted.

Params
^^^^^^

.. code-block:: json

   {
     "tag": "$ref:Tag"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "tagError": "$ref:TagError"
   }

See also: `Tag <#raw-api-tag>`__, `TagError <#raw-api-tag-error>`__

.. _raw-api-transfers-create-upload:

Transfers.CreateUpload
~~~~~~~~~~~~~~~~~~~~~~

Create an upload session on the dedicated transfer connection.

Params
^^^^^^

.. code-block:: json

   {
     "fileName": "String",
     "size": "Int"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "fileName": "String",
     "size": "Int",
     "transferId": "String",
     "transferToken": "String"
   }

.. _raw-api-transfers-start-download:

Transfers.StartDownload
~~~~~~~~~~~~~~~~~~~~~~~

Create a download session for a previously announced download.

Params
^^^^^^

.. code-block:: json

   {
     "downloadId": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "fileName": "String",
     "size": "Int",
     "transferId": "String",
     "transferToken": "String"
   }

.. _raw-api-users-change-password:

Users.ChangePassword
~~~~~~~~~~~~~~~~~~~~

Change the password for the currently logged in user.

Params
^^^^^^

.. code-block:: json

   {
     "newPassword": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "error": "$ref:UserError"
   }

See also: `UserError <#raw-api-user-error>`__

.. _raw-api-users-change-user-password:

Users.ChangeUserPassword
~~~~~~~~~~~~~~~~~~~~~~~~

Change the password for the given user. All tokens for this user will be removed in order to force all clients to log in again.

Params
^^^^^^

.. code-block:: json

   {
     "newPassword": "String",
     "username": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "error": "$ref:UserError"
   }

See also: `UserError <#raw-api-user-error>`__

.. _raw-api-users-create-user:

Users.CreateUser
~~~~~~~~~~~~~~~~

Create a new user in the API with the given username and password. Use scopes to define the permissions for the new user. If the user has not the permission "PermissionScopeAccessAllThings", the list of things this user has access to can be defined in the "allowedThingIds" property. If no scopes are given, this user will be an admin user. Call Authenticate after this to obtain a device token for this user.

Params
^^^^^^

.. code-block:: json

   {
     "o:allowedThingIds": [
       "Uuid"
     ],
     "o:displayName": "String",
     "o:email": "String",
     "o:scopes": "$ref:PermissionScopes",
     "password": "String",
     "username": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "error": "$ref:UserError"
   }

See also: `PermissionScopes <#raw-api-permission-scopes>`__, `UserError <#raw-api-user-error>`__

.. _raw-api-users-get-tokens:

Users.GetTokens
~~~~~~~~~~~~~~~

Get all the tokens for the current user.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "error": "$ref:UserError",
     "o:tokenInfoList": "$ref:TokenInfoList"
   }

See also: `TokenInfoList <#raw-api-token-info-list>`__, `UserError <#raw-api-user-error>`__

.. _raw-api-users-get-user-info:

Users.GetUserInfo
~~~~~~~~~~~~~~~~~

Get info about the current token (the currently logged in user).

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "error": "$ref:UserError",
     "o:userInfo": "$ref:UserInfo"
   }

See also: `UserError <#raw-api-user-error>`__, `UserInfo <#raw-api-user-info>`__

.. _raw-api-users-get-user-tokens:

Users.GetUserTokens
~~~~~~~~~~~~~~~~~~~

Get all the tokens for the given username.

Params
^^^^^^

.. code-block:: json

   {
     "username": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "error": "$ref:UserError",
     "o:tokenInfoList": "$ref:TokenInfoList"
   }

See also: `TokenInfoList <#raw-api-token-info-list>`__, `UserError <#raw-api-user-error>`__

.. _raw-api-users-get-users:

Users.GetUsers
~~~~~~~~~~~~~~

Return a list of all users in the system.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "users": "$ref:UserInfoList"
   }

See also: `UserInfoList <#raw-api-user-info-list>`__

.. _raw-api-users-remove-token:

Users.RemoveToken
~~~~~~~~~~~~~~~~~

Revoke access for a given token. Depending on the logged in user only the own tokens can be removed. If you are logged in as admin, any token can be removed.

Params
^^^^^^

.. code-block:: json

   {
     "tokenId": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "error": "$ref:UserError"
   }

See also: `UserError <#raw-api-user-error>`__

.. _raw-api-users-remove-user:

Users.RemoveUser
~~~~~~~~~~~~~~~~

Remove a user from the system.

Params
^^^^^^

.. code-block:: json

   {
     "username": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "error": "$ref:UserError"
   }

See also: `UserError <#raw-api-user-error>`__

.. _raw-api-users-set-user-info:

Users.SetUserInfo
~~~~~~~~~~~~~~~~~

Change user info. If username is given, info for the respective user is changed, otherwise the current user info is edited. Requires admin permissions to edit user info other than the own.

Params
^^^^^^

.. code-block:: json

   {
     "o:displayName": "String",
     "o:email": "String",
     "o:username": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "error": "$ref:UserError"
   }

See also: `UserError <#raw-api-user-error>`__

.. _raw-api-users-set-user-scopes:

Users.SetUserScopes
~~~~~~~~~~~~~~~~~~~

Set the permissions (scopes) for a given user. If the user has not the permission "PermissionScopeAccessAllThings" the list of thing IDs this user has access to can be defined in the "allowedThingIds" property.

Params
^^^^^^

.. code-block:: json

   {
     "o:allowedThingIds": [
       "Uuid"
     ],
     "scopes": "$ref:PermissionScopes",
     "username": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "error": "$ref:UserError"
   }

See also: `PermissionScopes <#raw-api-permission-scopes>`__, `UserError <#raw-api-user-error>`__

.. _raw-api-z-wave-add-network:

ZWave.AddNetwork
~~~~~~~~~~~~~~~~

Add a new Z-Wave network with the given serial port.

Params
^^^^^^

.. code-block:: json

   {
     "serialPort": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "o:networkUuid": "Uuid",
     "zwaveError": "$ref:ZWaveError"
   }

See also: `ZWaveError <#raw-api-z-wave-error>`__

.. _raw-api-z-wave-add-node:

ZWave.AddNode
~~~~~~~~~~~~~

Start the node inclusion procedure for the given Z-Wave network.

Params
^^^^^^

.. code-block:: json

   {
     "networkUuid": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "zwaveError": "$ref:ZWaveError"
   }

See also: `ZWaveError <#raw-api-z-wave-error>`__

.. _raw-api-z-wave-cancel-pending-operation:

ZWave.CancelPendingOperation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cancel any running node inclusion or removal procedure for the given Z-Wave network.

Params
^^^^^^

.. code-block:: json

   {
     "networkUuid": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "zwaveError": "$ref:ZWaveError"
   }

See also: `ZWaveError <#raw-api-z-wave-error>`__

.. _raw-api-z-wave-factory-reset-network:

ZWave.FactoryResetNetwork
~~~~~~~~~~~~~~~~~~~~~~~~~

Factory reset the controller for the given Z-Wave network.

Params
^^^^^^

.. code-block:: json

   {
     "networkUuid": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "zwaveError": "$ref:ZWaveError"
   }

See also: `ZWaveError <#raw-api-z-wave-error>`__

.. _raw-api-z-wave-get-networks:

ZWave.GetNetworks
~~~~~~~~~~~~~~~~~

Get all the Z-Wave networks in the system.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "networks": [
       "$ref:ZWaveNetwork"
     ]
   }

See also: `ZWaveNetwork <#raw-api-z-wave-network>`__

.. _raw-api-z-wave-get-nodes:

ZWave.GetNodes
~~~~~~~~~~~~~~

Get the list of nodes in a network

Params
^^^^^^

.. code-block:: json

   {
     "networkUuid": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "o:nodes": [
       "$ref:ZWaveNode"
     ],
     "zwaveError": "$ref:ZWaveError"
   }

See also: `ZWaveError <#raw-api-z-wave-error>`__, `ZWaveNode <#raw-api-z-wave-node>`__

.. _raw-api-z-wave-get-serial-ports:

ZWave.GetSerialPorts
~~~~~~~~~~~~~~~~~~~~

Get the list of available serial ports from the host system.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "serialPorts": "$ref:SerialPorts"
   }

See also: `SerialPorts <#raw-api-serial-ports>`__

.. _raw-api-z-wave-is-z-wave-available:

ZWave.IsZWaveAvailable
~~~~~~~~~~~~~~~~~~~~~~

Query if the Z-Wave subsystem is available at all.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "available": "Bool"
   }

.. _raw-api-z-wave-remove-failed-node:

ZWave.RemoveFailedNode
~~~~~~~~~~~~~~~~~~~~~~

Remove the given failed node from the given Z-Wave network. This will not work if node is not marked as failed.

Params
^^^^^^

.. code-block:: json

   {
     "networkUuid": "Uuid",
     "nodeId": "Uint"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "zwaveError": "$ref:ZWaveError"
   }

See also: `ZWaveError <#raw-api-z-wave-error>`__

.. _raw-api-z-wave-remove-network:

ZWave.RemoveNetwork
~~~~~~~~~~~~~~~~~~~

Remove the given Z-Wave network from the system.

Params
^^^^^^

.. code-block:: json

   {
     "networkUuid": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "zwaveError": "$ref:ZWaveError"
   }

See also: `ZWaveError <#raw-api-z-wave-error>`__

.. _raw-api-z-wave-remove-node:

ZWave.RemoveNode
~~~~~~~~~~~~~~~~

Start the node removal procedure for the given Z-Wave network.

Params
^^^^^^

.. code-block:: json

   {
     "networkUuid": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "zwaveError": "$ref:ZWaveError"
   }

See also: `ZWaveError <#raw-api-z-wave-error>`__

.. _raw-api-zigbee-add-network:

Zigbee.AddNetwork
~~~~~~~~~~~~~~~~~

Create a new ZigBee network for the given 'serialPort', 'baudRate' and 'backend'. The serial ports can be fetched from the available adapters. See 'GetAdapters' for more information. The available backends can be fetched using the 'GetAvailableBackends' method.

Params
^^^^^^

.. code-block:: json

   {
     "backend": "String",
     "baudRate": "Uint",
     "o:channelMask": "Uint",
     "serialPort": "String"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "o:networkUuid": "Uuid",
     "zigbeeError": "$ref:ZigbeeError"
   }

See also: `ZigbeeError <#raw-api-zigbee-error>`__

.. _raw-api-zigbee-create-binding:

Zigbee.CreateBinding
~~~~~~~~~~~~~~~~~~~~

Create a binding. Use destinationAddress and destinationEndpointId to create a node to node binding, or use destinationGroupAddress to create a group binding.

Params
^^^^^^

.. code-block:: json

   {
     "clusterId": "Uint",
     "networkUuid": "Uuid",
     "o:destinationAddress": "String",
     "o:destinationEndpointId": "Uint",
     "o:destinationGroupAddress": "Uint",
     "sourceAddress": "String",
     "sourceEndpointId": "Uint"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "zigbeeError": "$ref:ZigbeeError"
   }

See also: `ZigbeeError <#raw-api-zigbee-error>`__

.. _raw-api-zigbee-factory-reset-network:

Zigbee.FactoryResetNetwork
~~~~~~~~~~~~~~~~~~~~~~~~~~

Factory reset the network with the given 'networkUuid'. The network does not have to be online for this procedure, and all associated nodes and things will be removed permanently.

Params
^^^^^^

.. code-block:: json

   {
     "networkUuid": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "zigbeeError": "$ref:ZigbeeError"
   }

See also: `ZigbeeError <#raw-api-zigbee-error>`__

.. _raw-api-zigbee-get-adapters:

Zigbee.GetAdapters
~~~~~~~~~~~~~~~~~~

Get the list of available ZigBee adapters and serial ports in order to set up the ZigBee network on the desired interface. The 'serialPort' property can be used as unique identifier for an adapter. If an adapter hardware has been recognized as a well known ZigBee adapter, the 'hardwareRecognized' property will be true and the 'baudRate' and 'backend' configurations can be used as they where given, otherwise the user might set the backend and baud rate manually. The available backends can be fetched using the GetAvailableBackends method.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "adapters": "$ref:ZigbeeAdapters"
   }

See also: `ZigbeeAdapters <#raw-api-zigbee-adapters>`__

.. _raw-api-zigbee-get-available-backends:

Zigbee.GetAvailableBackends
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get the list of available ZigBee backends.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "backends": [
       "String"
     ]
   }

.. _raw-api-zigbee-get-networks:

Zigbee.GetNetworks
~~~~~~~~~~~~~~~~~~

Returns the list of configured ZigBee networks in the system.

Params
^^^^^^

.. code-block:: json

   {}

Returns
^^^^^^^

.. code-block:: json

   {
     "zigbeeNetworks": [
       "$ref:ZigbeeNetwork"
     ]
   }

See also: `ZigbeeNetwork <#raw-api-zigbee-network>`__

.. _raw-api-zigbee-get-nodes:

Zigbee.GetNodes
~~~~~~~~~~~~~~~

Returns the list of ZigBee nodes from the network the given 'networkUuid' in the system.

Params
^^^^^^

.. code-block:: json

   {
     "networkUuid": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "o:zigbeeNodes": [
       "$ref:ZigbeeNode"
     ],
     "zigbeeError": "$ref:ZigbeeError"
   }

See also: `ZigbeeError <#raw-api-zigbee-error>`__, `ZigbeeNode <#raw-api-zigbee-node>`__

.. _raw-api-zigbee-refresh-bindings:

Zigbee.RefreshBindings
~~~~~~~~~~~~~~~~~~~~~~

Refresh the binding table for the given node.

Params
^^^^^^

.. code-block:: json

   {
     "ieeeAddress": "String",
     "networkUuid": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "zigbeeError": "$ref:ZigbeeError"
   }

See also: `ZigbeeError <#raw-api-zigbee-error>`__

.. _raw-api-zigbee-refresh-neighbor-tables:

Zigbee.RefreshNeighborTables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Refresh the neighbor table for all nodes. Note that calling this may cause a lot of traffic in the ZigBee network.

Params
^^^^^^

.. code-block:: json

   {
     "networkUuid": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "zigbeeError": "$ref:ZigbeeError"
   }

See also: `ZigbeeError <#raw-api-zigbee-error>`__

.. _raw-api-zigbee-remove-binding:

Zigbee.RemoveBinding
~~~~~~~~~~~~~~~~~~~~

Remove a binding.

Params
^^^^^^

.. code-block:: json

   {
     "clusterId": "Uint",
     "networkUuid": "Uuid",
     "o:destinationAddress": "String",
     "o:destinationEndpointId": "Uint",
     "o:destinationGroupAddress": "Uint",
     "sourceAddress": "String",
     "sourceEndpointId": "Uint"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "zigbeeError": "$ref:ZigbeeError"
   }

See also: `ZigbeeError <#raw-api-zigbee-error>`__

.. _raw-api-zigbee-remove-network:

Zigbee.RemoveNetwork
~~~~~~~~~~~~~~~~~~~~

Remove the ZigBee network with the given network uuid.

Params
^^^^^^

.. code-block:: json

   {
     "networkUuid": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "zigbeeError": "$ref:ZigbeeError"
   }

See also: `ZigbeeError <#raw-api-zigbee-error>`__

.. _raw-api-zigbee-remove-node:

Zigbee.RemoveNode
~~~~~~~~~~~~~~~~~

Remove a ZigBee node with the given 'ieeeAddress' from the network with the given 'networkUuid'. If there is a thing configured for this node, also the thing will be removed from the system. The coordinator node cannot be removed.

Params
^^^^^^

.. code-block:: json

   {
     "ieeeAddress": "String",
     "networkUuid": "Uuid"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "zigbeeError": "$ref:ZigbeeError"
   }

See also: `ZigbeeError <#raw-api-zigbee-error>`__

.. _raw-api-zigbee-set-permit-join:

Zigbee.SetPermitJoin
~~~~~~~~~~~~~~~~~~~~

Allow or deny nodes to join the network with the given 'networkUuid' for a specific 'duration' in seconds. The duration value has to be between 0 and 255 seconds. The 'permitJoinDuration' property of ZigBee network object indicates how long permit has been enabled and the 'permitJoiningRemaining' indicates the rest of the time. Those values can be used to show a countdown or progressbar. This method can be recalled for resetting the timeout. If the duration is set to 0 seconds, joining will be disabled immediatly for the entire network. The 'shortAddress' is optional and defaults to the broadcast address 0xfffc for all routers in the network. If the short address matches the address of a router node in the network, only that specific router will be able to allow new nodes to join the network. A new node will join to the router with the best link quality index (LQI).

Params
^^^^^^

.. code-block:: json

   {
     "duration": "Uint",
     "networkUuid": "Uuid",
     "o:shortAddress": "Uint"
   }

Returns
^^^^^^^

.. code-block:: json

   {
     "zigbeeError": "$ref:ZigbeeError"
   }

See also: `ZigbeeError <#raw-api-zigbee-error>`__

Notifications
-------------

.. _raw-api-app-data-changed:

AppData.Changed
~~~~~~~~~~~~~~~

Emitted whenever the app data is changed on the server.

Params
^^^^^^

.. code-block:: json

   {
     "appId": "String",
     "key": "String",
     "o:group": "String",
     "value": "String"
   }

.. _raw-api-configuration-backup-configuration-changed:

Configuration.BackupConfigurationChanged
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever the backup configuration changes.

Params
^^^^^^

.. code-block:: json

   {
     "autoBackupEnabled": "Bool",
     "autoBackupInterval": "Int",
     "destinationDirectory": "String",
     "maxCount": "Uint"
   }

.. _raw-api-configuration-backup-files-changed:

Configuration.BackupFilesChanged
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever the list of backup files changes.

Params
^^^^^^

.. code-block:: json

   {
     "backupFiles": [
       "$ref:BackupFile"
     ]
   }

See also: `BackupFile <#raw-api-backup-file>`__

.. _raw-api-configuration-basic-configuration-changed:

Configuration.BasicConfigurationChanged
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever the basic configuration of this server changes.

Params
^^^^^^

.. code-block:: json

   {
     "basicConfiguration": {
       "d:language": "String",
       "d:location": {
         "latitude": "Double",
         "longitude": "Double",
         "name": "String"
       },
       "d:serverTime": "Uint",
       "d:timeZone": "String",
       "debugServerEnabled": "Bool",
       "serverName": "String",
       "serverUuid": "Uuid"
     }
   }

.. _raw-api-configuration-mqtt-policy-changed:

Configuration.MqttPolicyChanged
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever a MQTT broker policy is changed.

Params
^^^^^^

.. code-block:: json

   {
     "policy": "$ref:MqttPolicy"
   }

See also: `MqttPolicy <#raw-api-mqtt-policy>`__

.. _raw-api-configuration-mqtt-policy-removed:

Configuration.MqttPolicyRemoved
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever a MQTT broker policy is removed.

Params
^^^^^^

.. code-block:: json

   {
     "clientId": "String"
   }

.. _raw-api-configuration-mqtt-server-configuration-changed:

Configuration.MqttServerConfigurationChanged
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever the MQTT broker configuration is changed.

Params
^^^^^^

.. code-block:: json

   {
     "mqttServerConfiguration": "$ref:ServerConfiguration"
   }

See also: `ServerConfiguration <#raw-api-server-configuration>`__

.. _raw-api-configuration-mqtt-server-configuration-removed:

Configuration.MqttServerConfigurationRemoved
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever a MQTT server configuration is removed.

Params
^^^^^^

.. code-block:: json

   {
     "id": "String"
   }

.. _raw-api-configuration-tcp-server-configuration-changed:

Configuration.TcpServerConfigurationChanged
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever the TCP server configuration changes.

Params
^^^^^^

.. code-block:: json

   {
     "tcpServerConfiguration": "$ref:ServerConfiguration"
   }

See also: `ServerConfiguration <#raw-api-server-configuration>`__

.. _raw-api-configuration-tcp-server-configuration-removed:

Configuration.TcpServerConfigurationRemoved
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever a TCP server configuration is removed.

Params
^^^^^^

.. code-block:: json

   {
     "id": "String"
   }

.. _raw-api-configuration-tunnel-proxy-server-configuration-changed:

Configuration.TunnelProxyServerConfigurationChanged
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever the tunnel proxy server configuration changes.

Params
^^^^^^

.. code-block:: json

   {
     "tunnelProxyServerConfiguration": "$ref:TunnelProxyServerConfiguration"
   }

See also: `TunnelProxyServerConfiguration <#raw-api-tunnel-proxy-server-configuration>`__

.. _raw-api-configuration-tunnel-proxy-server-configuration-removed:

Configuration.TunnelProxyServerConfigurationRemoved
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever a tunnel proxy server configuration is removed.

Params
^^^^^^

.. code-block:: json

   {
     "id": "String"
   }

.. _raw-api-configuration-web-server-configuration-changed:

Configuration.WebServerConfigurationChanged
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever the web server configuration changes.

Params
^^^^^^

.. code-block:: json

   {
     "webServerConfiguration": "$ref:WebServerConfiguration"
   }

See also: `WebServerConfiguration <#raw-api-web-server-configuration>`__

.. _raw-api-configuration-web-server-configuration-removed:

Configuration.WebServerConfigurationRemoved
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever a Web server configuration is removed.

Params
^^^^^^

.. code-block:: json

   {
     "id": "String"
   }

.. _raw-api-configuration-web-socket-server-configuration-changed:

Configuration.WebSocketServerConfigurationChanged
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever the web socket server configuration changes.

Params
^^^^^^

.. code-block:: json

   {
     "webSocketServerConfiguration": "$ref:ServerConfiguration"
   }

See also: `ServerConfiguration <#raw-api-server-configuration>`__

.. _raw-api-configuration-web-socket-server-configuration-removed:

Configuration.WebSocketServerConfigurationRemoved
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever a WebSocket server configuration is removed.

Params
^^^^^^

.. code-block:: json

   {
     "id": "String"
   }

.. _raw-api-debug-logging-category-level-changed:

Debug.LoggingCategoryLevelChanged
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever a logging category has changed the logging level.

Params
^^^^^^

.. code-block:: json

   {
     "level": "$ref:LoggingLevel",
     "name": "String"
   }

See also: `LoggingLevel <#raw-api-logging-level>`__

.. _raw-api-integrations-event-triggered:

Integrations.EventTriggered
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever an Event is triggered.

Params
^^^^^^

.. code-block:: json

   {
     "event": "$ref:Event"
   }

See also: `Event <#raw-api-event>`__

.. _raw-api-integrations-i-o-connection-added:

Integrations.IOConnectionAdded
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever an IO connection has been added.

Params
^^^^^^

.. code-block:: json

   {
     "ioConnection": "$ref:IOConnection"
   }

See also: `IOConnection <#raw-api-i-o-connection>`__

.. _raw-api-integrations-i-o-connection-removed:

Integrations.IOConnectionRemoved
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever an IO connection has been removed.

Params
^^^^^^

.. code-block:: json

   {
     "ioConnectionId": "Uuid"
   }

.. _raw-api-integrations-plugin-configuration-changed:

Integrations.PluginConfigurationChanged
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever a plugin's configuration is changed.

Params
^^^^^^

.. code-block:: json

   {
     "configuration": "$ref:ParamList",
     "pluginId": "Uuid"
   }

See also: `ParamList <#raw-api-param-list>`__

.. _raw-api-integrations-state-changed:

Integrations.StateChanged
~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever a state of a thing changes.

Params
^^^^^^

.. code-block:: json

   {
     "maxValue": "Variant",
     "minValue": "Variant",
     "possibleValues": [
       "Variant"
     ],
     "stateTypeId": "Uuid",
     "thingId": "Uuid",
     "value": "Variant"
   }

.. _raw-api-integrations-thing-added:

Integrations.ThingAdded
~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever a thing was added.

Params
^^^^^^

.. code-block:: json

   {
     "thing": "$ref:Thing"
   }

See also: `Thing <#raw-api-thing>`__

.. _raw-api-integrations-thing-changed:

Integrations.ThingChanged
~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever the params or name of a thing are changed (by EditThing or ReconfigureThing).

Params
^^^^^^

.. code-block:: json

   {
     "thing": "$ref:Thing"
   }

See also: `Thing <#raw-api-thing>`__

.. _raw-api-integrations-thing-removed:

Integrations.ThingRemoved
~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever a thing was removed.

Params
^^^^^^

.. code-block:: json

   {
     "thingId": "Uuid"
   }

.. _raw-api-integrations-thing-setting-changed:

Integrations.ThingSettingChanged
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever the setting of a thing is changed.

Params
^^^^^^

.. code-block:: json

   {
     "paramTypeId": "Uuid",
     "thingId": "Uuid",
     "value": "Variant"
   }

.. _raw-api-j-s-o-n-r-p-c-push-button-auth-finished:

JSONRPC.PushButtonAuthFinished
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted when a push button authentication reaches final state. NOTE: This notification is special. It will only be emitted to connections that did actively request a push button authentication, but also it will be emitted regardless of the notification settings. 

Params
^^^^^^

.. code-block:: json

   {
     "o:token": "String",
     "success": "Bool",
     "transactionId": "Int"
   }

.. _raw-api-logging-log-entry-added:

Logging.LogEntryAdded
~~~~~~~~~~~~~~~~~~~~~

Emitted when a log entry is added. This will only be emitted for discrete series, not for resampled entries

Params
^^^^^^

.. code-block:: json

   {
     "logEntry": "$ref:LogEntry"
   }

See also: `LogEntry <#raw-api-log-entry>`__

.. _raw-api-modbus-rtu-modbus-rtu-master-added:

ModbusRtu.ModbusRtuMasterAdded
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever a new modbus RTU master has been added to the system.

Params
^^^^^^

.. code-block:: json

   {
     "modbusRtuMaster": "$ref:ModbusRtuMaster"
   }

See also: `ModbusRtuMaster <#raw-api-modbus-rtu-master>`__

.. _raw-api-modbus-rtu-modbus-rtu-master-changed:

ModbusRtu.ModbusRtuMasterChanged
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever a modbus RTU master has been changed in the system.

Params
^^^^^^

.. code-block:: json

   {
     "modbusRtuMaster": "$ref:ModbusRtuMaster"
   }

See also: `ModbusRtuMaster <#raw-api-modbus-rtu-master>`__

.. _raw-api-modbus-rtu-modbus-rtu-master-removed:

ModbusRtu.ModbusRtuMasterRemoved
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever a modbus RTU master has been removed from the system.

Params
^^^^^^

.. code-block:: json

   {
     "modbusUuid": "Uuid"
   }

.. _raw-api-modbus-rtu-serial-port-added:

ModbusRtu.SerialPortAdded
~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever a serial port has been added to the system.

Params
^^^^^^

.. code-block:: json

   {
     "serialPort": "$ref:SerialPort"
   }

See also: `SerialPort <#raw-api-serial-port>`__

.. _raw-api-modbus-rtu-serial-port-removed:

ModbusRtu.SerialPortRemoved
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever a serial port has been removed from the system.

Params
^^^^^^

.. code-block:: json

   {
     "serialPort": "$ref:SerialPort"
   }

See also: `SerialPort <#raw-api-serial-port>`__

.. _raw-api-network-manager-network-status-changed:

NetworkManager.NetworkStatusChanged
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever a status of a NetworkManager changes.

Params
^^^^^^

.. code-block:: json

   {
     "status": {
       "networkingEnabled": "Bool",
       "state": "$ref:NetworkManagerState",
       "wirelessNetworkingEnabled": "Bool"
     }
   }

See also: `NetworkManagerState <#raw-api-network-manager-state>`__

.. _raw-api-network-manager-wired-network-device-added:

NetworkManager.WiredNetworkDeviceAdded
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever a new WiredNetworkDevice was added.

Params
^^^^^^

.. code-block:: json

   {
     "wiredNetworkDevice": "$ref:WiredNetworkDevice"
   }

See also: `WiredNetworkDevice <#raw-api-wired-network-device>`__

.. _raw-api-network-manager-wired-network-device-changed:

NetworkManager.WiredNetworkDeviceChanged
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever the given WiredNetworkDevice has changed.

Params
^^^^^^

.. code-block:: json

   {
     "wiredNetworkDevice": "$ref:WiredNetworkDevice"
   }

See also: `WiredNetworkDevice <#raw-api-wired-network-device>`__

.. _raw-api-network-manager-wired-network-device-removed:

NetworkManager.WiredNetworkDeviceRemoved
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever a WiredNetworkDevice was removed.

Params
^^^^^^

.. code-block:: json

   {
     "interface": "String"
   }

.. _raw-api-network-manager-wireless-network-device-added:

NetworkManager.WirelessNetworkDeviceAdded
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever a new WirelessNetworkDevice was added.

Params
^^^^^^

.. code-block:: json

   {
     "wirelessNetworkDevice": "$ref:WirelessNetworkDevice"
   }

See also: `WirelessNetworkDevice <#raw-api-wireless-network-device>`__

.. _raw-api-network-manager-wireless-network-device-changed:

NetworkManager.WirelessNetworkDeviceChanged
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever the given WirelessNetworkDevice has changed.

Params
^^^^^^

.. code-block:: json

   {
     "wirelessNetworkDevice": "$ref:WirelessNetworkDevice"
   }

See also: `WirelessNetworkDevice <#raw-api-wireless-network-device>`__

.. _raw-api-network-manager-wireless-network-device-removed:

NetworkManager.WirelessNetworkDeviceRemoved
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever a WirelessNetworkDevice was removed.

Params
^^^^^^

.. code-block:: json

   {
     "interface": "String"
   }

.. _raw-api-rules-rule-active-changed:

Rules.RuleActiveChanged
~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever the active state of a Rule changed.

Params
^^^^^^

.. code-block:: json

   {
     "active": "Bool",
     "ruleId": "Uuid"
   }

.. _raw-api-rules-rule-added:

Rules.RuleAdded
~~~~~~~~~~~~~~~

Emitted whenever a Rule was added.

Params
^^^^^^

.. code-block:: json

   {
     "rule": "$ref:Rule"
   }

See also: `Rule <#raw-api-rule>`__

.. _raw-api-rules-rule-configuration-changed:

Rules.RuleConfigurationChanged
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever the configuration of a Rule changed.

Params
^^^^^^

.. code-block:: json

   {
     "rule": "$ref:Rule"
   }

See also: `Rule <#raw-api-rule>`__

.. _raw-api-rules-rule-removed:

Rules.RuleRemoved
~~~~~~~~~~~~~~~~~

Emitted whenever a Rule was removed.

Params
^^^^^^

.. code-block:: json

   {
     "ruleId": "Uuid"
   }

.. _raw-api-scripts-script-added:

Scripts.ScriptAdded
~~~~~~~~~~~~~~~~~~~

Emitted when a script has been added to the system.

Params
^^^^^^

.. code-block:: json

   {
     "script": "$ref:Script"
   }

See also: `Script <#raw-api-script>`__

.. _raw-api-scripts-script-changed:

Scripts.ScriptChanged
~~~~~~~~~~~~~~~~~~~~~

Emitted when a script has been changed in the system (e.g. renamed).

Params
^^^^^^

.. code-block:: json

   {
     "name": "String",
     "scriptId": "Uuid"
   }

.. _raw-api-scripts-script-content-changed:

Scripts.ScriptContentChanged
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted when a script's content has been changed in the system.

Params
^^^^^^

.. code-block:: json

   {
     "scriptId": "Uuid"
   }

.. _raw-api-scripts-script-log-message:

Scripts.ScriptLogMessage
~~~~~~~~~~~~~~~~~~~~~~~~

Emitted when a script produces a console message.

Params
^^^^^^

.. code-block:: json

   {
     "message": "String",
     "scriptId": "Uuid",
     "type": "$ref:ScriptMessageType"
   }

See also: `ScriptMessageType <#raw-api-script-message-type>`__

.. _raw-api-scripts-script-removed:

Scripts.ScriptRemoved
~~~~~~~~~~~~~~~~~~~~~

Emitted when a script has been removed from the system.

Params
^^^^^^

.. code-block:: json

   {
     "id": "Uuid"
   }

.. _raw-api-system-capabilities-changed:

System.CapabilitiesChanged
~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever the system capabilities change.

Params
^^^^^^

.. code-block:: json

   {
     "powerManagement": "Bool",
     "updateManagement": "Bool",
     "updateManagementType": "$ref:UpdateType"
   }

See also: `UpdateType <#raw-api-update-type>`__

.. _raw-api-system-package-added:

System.PackageAdded
~~~~~~~~~~~~~~~~~~~

Emitted whenever a package is added to the list of packages.

Params
^^^^^^

.. code-block:: json

   {
     "package": "$ref:Package"
   }

See also: `Package <#raw-api-package>`__

.. _raw-api-system-package-changed:

System.PackageChanged
~~~~~~~~~~~~~~~~~~~~~

Emitted whenever a package in the list of packages changes.

Params
^^^^^^

.. code-block:: json

   {
     "package": "$ref:Package"
   }

See also: `Package <#raw-api-package>`__

.. _raw-api-system-package-removed:

System.PackageRemoved
~~~~~~~~~~~~~~~~~~~~~

Emitted whenever a package is removed from the list of packages.

Params
^^^^^^

.. code-block:: json

   {
     "packageId": "String"
   }

.. _raw-api-system-repository-added:

System.RepositoryAdded
~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever a repository is added to the list of repositories.

Params
^^^^^^

.. code-block:: json

   {
     "repository": "$ref:Repository"
   }

See also: `Repository <#raw-api-repository>`__

.. _raw-api-system-repository-changed:

System.RepositoryChanged
~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever a repository in the list of repositories changes.

Params
^^^^^^

.. code-block:: json

   {
     "repository": "$ref:Repository"
   }

See also: `Repository <#raw-api-repository>`__

.. _raw-api-system-repository-removed:

System.RepositoryRemoved
~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever a repository is removed from the list of repositories.

Params
^^^^^^

.. code-block:: json

   {
     "repositoryId": "String"
   }

.. _raw-api-system-time-configuration-changed:

System.TimeConfigurationChanged
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever the time configuration is changed

Params
^^^^^^

.. code-block:: json

   {
     "automaticTime": "Bool",
     "automaticTimeAvailable": "Bool",
     "time": "Uint",
     "timeZone": "String"
   }

.. _raw-api-system-update-status-changed:

System.UpdateStatusChanged
~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted whenever the update status changes.

Params
^^^^^^

.. code-block:: json

   {
     "busy": "Bool",
     "o:updateProgress": "Int",
     "updateRunning": "Bool"
   }

.. _raw-api-tags-tag-added:

Tags.TagAdded
~~~~~~~~~~~~~

Emitted whenever a tag is added to the system. 

Params
^^^^^^

.. code-block:: json

   {
     "tag": "$ref:Tag"
   }

See also: `Tag <#raw-api-tag>`__

.. _raw-api-tags-tag-removed:

Tags.TagRemoved
~~~~~~~~~~~~~~~

Emitted whenever a tag is removed from the system. 

Params
^^^^^^

.. code-block:: json

   {
     "tag": "$ref:Tag"
   }

See also: `Tag <#raw-api-tag>`__

.. _raw-api-tags-tag-value-changed:

Tags.TagValueChanged
~~~~~~~~~~~~~~~~~~~~

Emitted whenever a tag's value is changed in the system. 

Params
^^^^^^

.. code-block:: json

   {
     "tag": "$ref:Tag"
   }

See also: `Tag <#raw-api-tag>`__

.. _raw-api-transfers-download-available:

Transfers.DownloadAvailable
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted when a completed upload can be downloaded on the dedicated transfer connection.

Params
^^^^^^

.. code-block:: json

   {
     "downloadId": "String",
     "fileName": "String",
     "size": "Int"
   }

.. _raw-api-users-push-button-auth-finished:

Users.PushButtonAuthFinished
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emitted when a push button authentication reaches final state. NOTE: This notification is special. It will only be emitted to connections that did actively request a push button authentication, but also it will be emitted regardless of the notification settings.

Params
^^^^^^

.. code-block:: json

   {
     "o:token": "String",
     "success": "Bool",
     "transactionId": "Int"
   }

.. _raw-api-users-user-added:

Users.UserAdded
~~~~~~~~~~~~~~~

Emitted when a user is added to the system.

Params
^^^^^^

.. code-block:: json

   {
     "userInfo": "$ref:UserInfo"
   }

See also: `UserInfo <#raw-api-user-info>`__

.. _raw-api-users-user-changed:

Users.UserChanged
~~~~~~~~~~~~~~~~~

Emitted whenever a user is changed.

Params
^^^^^^

.. code-block:: json

   {
     "userInfo": "$ref:UserInfo"
   }

See also: `UserInfo <#raw-api-user-info>`__

.. _raw-api-users-user-removed:

Users.UserRemoved
~~~~~~~~~~~~~~~~~

Emitted when a user is removed from the system.

Params
^^^^^^

.. code-block:: json

   {
     "username": "String"
   }

.. _raw-api-z-wave-network-added:

ZWave.NetworkAdded
~~~~~~~~~~~~~~~~~~

Emitted whenever a new Z-Wave network has been added to the system.

Params
^^^^^^

.. code-block:: json

   {
     "network": "$ref:ZWaveNetwork"
   }

See also: `ZWaveNetwork <#raw-api-z-wave-network>`__

.. _raw-api-z-wave-network-changed:

ZWave.NetworkChanged
~~~~~~~~~~~~~~~~~~~~

Emitted whenever a Z-Wave network changes.

Params
^^^^^^

.. code-block:: json

   {
     "network": "$ref:ZWaveNetwork"
   }

See also: `ZWaveNetwork <#raw-api-z-wave-network>`__

.. _raw-api-z-wave-network-removed:

ZWave.NetworkRemoved
~~~~~~~~~~~~~~~~~~~~

Emitted whenever a Z-Wave network has been removed from the system.

Params
^^^^^^

.. code-block:: json

   {
     "networkUuid": "Uuid"
   }

.. _raw-api-z-wave-node-added:

ZWave.NodeAdded
~~~~~~~~~~~~~~~

Emitted whenever a Z-Wave node is added.

Params
^^^^^^

.. code-block:: json

   {
     "networkUuid": "Uuid",
     "node": "$ref:ZWaveNode"
   }

See also: `ZWaveNode <#raw-api-z-wave-node>`__

.. _raw-api-z-wave-node-changed:

ZWave.NodeChanged
~~~~~~~~~~~~~~~~~

Emitted whenever a Z-Wave node has changed.

Params
^^^^^^

.. code-block:: json

   {
     "networkUuid": "Uuid",
     "node": "$ref:ZWaveNode"
   }

See also: `ZWaveNode <#raw-api-z-wave-node>`__

.. _raw-api-z-wave-node-removed:

ZWave.NodeRemoved
~~~~~~~~~~~~~~~~~

Emitted whenever a Z-Wave node is removed.

Params
^^^^^^

.. code-block:: json

   {
     "networkUuid": "Uuid",
     "nodeId": "Uint"
   }

.. _raw-api-zigbee-adapter-added:

Zigbee.AdapterAdded
~~~~~~~~~~~~~~~~~~~

Emitted whenever a new ZigBee adapter or serial port has been detected in the system.

Params
^^^^^^

.. code-block:: json

   {
     "adapter": "$ref:ZigbeeAdapter"
   }

See also: `ZigbeeAdapter <#raw-api-zigbee-adapter>`__

.. _raw-api-zigbee-adapter-removed:

Zigbee.AdapterRemoved
~~~~~~~~~~~~~~~~~~~~~

Emitted whenever a ZigBee adapter or serial port has been removed from the system (i.e. unplugged).

Params
^^^^^^

.. code-block:: json

   {
     "adapter": "$ref:ZigbeeAdapter"
   }

See also: `ZigbeeAdapter <#raw-api-zigbee-adapter>`__

.. _raw-api-zigbee-network-added:

Zigbee.NetworkAdded
~~~~~~~~~~~~~~~~~~~

Emitted whenever a new ZigBee network has been added.

Params
^^^^^^

.. code-block:: json

   {
     "zigbeeNetwork": "$ref:ZigbeeNetwork"
   }

See also: `ZigbeeNetwork <#raw-api-zigbee-network>`__

.. _raw-api-zigbee-network-changed:

Zigbee.NetworkChanged
~~~~~~~~~~~~~~~~~~~~~

Emitted whenever a new ZigBee network has changed.

Params
^^^^^^

.. code-block:: json

   {
     "zigbeeNetwork": "$ref:ZigbeeNetwork"
   }

See also: `ZigbeeNetwork <#raw-api-zigbee-network>`__

.. _raw-api-zigbee-network-removed:

Zigbee.NetworkRemoved
~~~~~~~~~~~~~~~~~~~~~

Emitted whenever a new ZigBee network has been removed.

Params
^^^^^^

.. code-block:: json

   {
     "networkUuid": "Uuid"
   }

.. _raw-api-zigbee-node-added:

Zigbee.NodeAdded
~~~~~~~~~~~~~~~~

Emitted whenever a new ZigBee node has joined the network with the given 'networkUuid'.

Params
^^^^^^

.. code-block:: json

   {
     "networkUuid": "Uuid",
     "zigbeeNode": "$ref:ZigbeeNode"
   }

See also: `ZigbeeNode <#raw-api-zigbee-node>`__

.. _raw-api-zigbee-node-changed:

Zigbee.NodeChanged
~~~~~~~~~~~~~~~~~~

Emitted whenever a ZigBee node has changed.

Params
^^^^^^

.. code-block:: json

   {
     "networkUuid": "Uuid",
     "zigbeeNode": "$ref:ZigbeeNode"
   }

See also: `ZigbeeNode <#raw-api-zigbee-node>`__

.. _raw-api-zigbee-node-removed:

Zigbee.NodeRemoved
~~~~~~~~~~~~~~~~~~

Emitted whenever a ZigBee node has removed from the network with the given 'networkUuid'.

Params
^^^^^^

.. code-block:: json

   {
     "networkUuid": "Uuid",
     "zigbeeNode": "$ref:ZigbeeNode"
   }

See also: `ZigbeeNode <#raw-api-zigbee-node>`__

