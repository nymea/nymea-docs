API Namespaces
==============

The API is organised into the following namespaces.

.. _api-namespace-appdata:

AppData
-------

**Methods:** :ref:`AppData.Load <api-app-data-load>`, :ref:`AppData.Store <api-app-data-store>`

**Notifications:** :ref:`AppData.Changed <api-app-data-changed>`

.. _api-namespace-configuration:

Configuration
-------------

**Methods:** :ref:`Configuration.CreateAndDownloadBackup <api-configuration-create-and-download-backup>`, :ref:`Configuration.CreateBackup <api-configuration-create-backup>`, :ref:`Configuration.DeleteBackupFile <api-configuration-delete-backup-file>`, :ref:`Configuration.DeleteMqttPolicy <api-configuration-delete-mqtt-policy>`, :ref:`Configuration.DeleteMqttServerConfiguration <api-configuration-delete-mqtt-server-configuration>`, :ref:`Configuration.DeleteTcpServerConfiguration <api-configuration-delete-tcp-server-configuration>`, :ref:`Configuration.DeleteTunnelProxyServerConfiguration <api-configuration-delete-tunnel-proxy-server-configuration>`, :ref:`Configuration.DeleteWebServerConfiguration <api-configuration-delete-web-server-configuration>`, :ref:`Configuration.DeleteWebSocketServerConfiguration <api-configuration-delete-web-socket-server-configuration>`, :ref:`Configuration.DownloadBackupFile <api-configuration-download-backup-file>`, :ref:`Configuration.GetAvailableLanguages <api-configuration-get-available-languages>`, :ref:`Configuration.GetBackupFiles <api-configuration-get-backup-files>`, :ref:`Configuration.GetConfigurations <api-configuration-get-configurations>`, :ref:`Configuration.GetMqttPolicies <api-configuration-get-mqtt-policies>`, :ref:`Configuration.GetMqttServerConfigurations <api-configuration-get-mqtt-server-configurations>`, :ref:`Configuration.GetTimeZones <api-configuration-get-time-zones>`, :ref:`Configuration.RestoreBackupFile <api-configuration-restore-backup-file>`, :ref:`Configuration.SetBackupConfiguration <api-configuration-set-backup-configuration>`, :ref:`Configuration.SetDebugServerEnabled <api-configuration-set-debug-server-enabled>`, :ref:`Configuration.SetLanguage <api-configuration-set-language>`, :ref:`Configuration.SetLocation <api-configuration-set-location>`, :ref:`Configuration.SetMqttPolicy <api-configuration-set-mqtt-policy>`, :ref:`Configuration.SetMqttServerConfiguration <api-configuration-set-mqtt-server-configuration>`, :ref:`Configuration.SetServerName <api-configuration-set-server-name>`, :ref:`Configuration.SetTcpServerConfiguration <api-configuration-set-tcp-server-configuration>`, :ref:`Configuration.SetTimeZone <api-configuration-set-time-zone>`, :ref:`Configuration.SetTunnelProxyServerConfiguration <api-configuration-set-tunnel-proxy-server-configuration>`, :ref:`Configuration.SetWebServerConfiguration <api-configuration-set-web-server-configuration>`, :ref:`Configuration.SetWebSocketServerConfiguration <api-configuration-set-web-socket-server-configuration>`, :ref:`Configuration.UploadAndRestoreBackup <api-configuration-upload-and-restore-backup>`

**Notifications:** :ref:`Configuration.BackupConfigurationChanged <api-configuration-backup-configuration-changed>`, :ref:`Configuration.BackupFilesChanged <api-configuration-backup-files-changed>`, :ref:`Configuration.BasicConfigurationChanged <api-configuration-basic-configuration-changed>`, :ref:`Configuration.MqttPolicyChanged <api-configuration-mqtt-policy-changed>`, :ref:`Configuration.MqttPolicyRemoved <api-configuration-mqtt-policy-removed>`, :ref:`Configuration.MqttServerConfigurationChanged <api-configuration-mqtt-server-configuration-changed>`, :ref:`Configuration.MqttServerConfigurationRemoved <api-configuration-mqtt-server-configuration-removed>`, :ref:`Configuration.TcpServerConfigurationChanged <api-configuration-tcp-server-configuration-changed>`, :ref:`Configuration.TcpServerConfigurationRemoved <api-configuration-tcp-server-configuration-removed>`, :ref:`Configuration.TunnelProxyServerConfigurationChanged <api-configuration-tunnel-proxy-server-configuration-changed>`, :ref:`Configuration.TunnelProxyServerConfigurationRemoved <api-configuration-tunnel-proxy-server-configuration-removed>`, :ref:`Configuration.WebServerConfigurationChanged <api-configuration-web-server-configuration-changed>`, :ref:`Configuration.WebServerConfigurationRemoved <api-configuration-web-server-configuration-removed>`, :ref:`Configuration.WebSocketServerConfigurationChanged <api-configuration-web-socket-server-configuration-changed>`, :ref:`Configuration.WebSocketServerConfigurationRemoved <api-configuration-web-socket-server-configuration-removed>`

.. _api-namespace-debug:

Debug
-----

**Methods:** :ref:`Debug.GetLoggingCategories <api-debug-get-logging-categories>`, :ref:`Debug.SetLoggingCategoryLevel <api-debug-set-logging-category-level>`

**Notifications:** :ref:`Debug.LoggingCategoryLevelChanged <api-debug-logging-category-level-changed>`

.. _api-namespace-integrations:

Integrations
------------

**Methods:** :ref:`Integrations.AddThing <api-integrations-add-thing>`, :ref:`Integrations.BrowseThing <api-integrations-browse-thing>`, :ref:`Integrations.ConfirmPairing <api-integrations-confirm-pairing>`, :ref:`Integrations.ConnectIO <api-integrations-connect-i-o>`, :ref:`Integrations.DisconnectIO <api-integrations-disconnect-i-o>`, :ref:`Integrations.DiscoverThings <api-integrations-discover-things>`, :ref:`Integrations.EditThing <api-integrations-edit-thing>`, :ref:`Integrations.ExecuteAction <api-integrations-execute-action>`, :ref:`Integrations.ExecuteBrowserItem <api-integrations-execute-browser-item>`, :ref:`Integrations.ExecuteBrowserItemAction <api-integrations-execute-browser-item-action>`, :ref:`Integrations.GetActionTypes <api-integrations-get-action-types>`, :ref:`Integrations.GetBrowserItem <api-integrations-get-browser-item>`, :ref:`Integrations.GetEventTypes <api-integrations-get-event-types>`, :ref:`Integrations.GetIOConnections <api-integrations-get-i-o-connections>`, :ref:`Integrations.GetPluginConfiguration <api-integrations-get-plugin-configuration>`, :ref:`Integrations.GetPlugins <api-integrations-get-plugins>`, :ref:`Integrations.GetStateTypes <api-integrations-get-state-types>`, :ref:`Integrations.GetStateValue <api-integrations-get-state-value>`, :ref:`Integrations.GetStateValues <api-integrations-get-state-values>`, :ref:`Integrations.GetThingClasses <api-integrations-get-thing-classes>`, :ref:`Integrations.GetThings <api-integrations-get-things>`, :ref:`Integrations.GetVendors <api-integrations-get-vendors>`, :ref:`Integrations.PairThing <api-integrations-pair-thing>`, :ref:`Integrations.ReconfigureThing <api-integrations-reconfigure-thing>`, :ref:`Integrations.RemoveThing <api-integrations-remove-thing>`, :ref:`Integrations.SetActionLogging <api-integrations-set-action-logging>`, :ref:`Integrations.SetEventLogging <api-integrations-set-event-logging>`, :ref:`Integrations.SetPluginConfiguration <api-integrations-set-plugin-configuration>`, :ref:`Integrations.SetStateFilter <api-integrations-set-state-filter>`, :ref:`Integrations.SetStateLogging <api-integrations-set-state-logging>`, :ref:`Integrations.SetThingSettings <api-integrations-set-thing-settings>`

**Notifications:** :ref:`Integrations.EventTriggered <api-integrations-event-triggered>`, :ref:`Integrations.IOConnectionAdded <api-integrations-i-o-connection-added>`, :ref:`Integrations.IOConnectionRemoved <api-integrations-i-o-connection-removed>`, :ref:`Integrations.PluginConfigurationChanged <api-integrations-plugin-configuration-changed>`, :ref:`Integrations.StateChanged <api-integrations-state-changed>`, :ref:`Integrations.ThingAdded <api-integrations-thing-added>`, :ref:`Integrations.ThingChanged <api-integrations-thing-changed>`, :ref:`Integrations.ThingRemoved <api-integrations-thing-removed>`, :ref:`Integrations.ThingSettingChanged <api-integrations-thing-setting-changed>`

.. _api-namespace-jsonrpc:

JSONRPC
-------

**Methods:** :ref:`JSONRPC.Authenticate <api-j-s-o-n-r-p-c-authenticate>`, :ref:`JSONRPC.CreateUser <api-j-s-o-n-r-p-c-create-user>`, :ref:`JSONRPC.Hello <api-j-s-o-n-r-p-c-hello>`, :ref:`JSONRPC.Introspect <api-j-s-o-n-r-p-c-introspect>`, :ref:`JSONRPC.KeepAlive <api-j-s-o-n-r-p-c-keep-alive>`, :ref:`JSONRPC.RequestPushButtonAuth <api-j-s-o-n-r-p-c-request-push-button-auth>`, :ref:`JSONRPC.SetNotificationStatus <api-j-s-o-n-r-p-c-set-notification-status>`, :ref:`JSONRPC.Version <api-j-s-o-n-r-p-c-version>`

**Notifications:** :ref:`JSONRPC.PushButtonAuthFinished <api-j-s-o-n-r-p-c-push-button-auth-finished>`

.. _api-namespace-logging:

Logging
-------

**Methods:** :ref:`Logging.GetLogEntries <api-logging-get-log-entries>`

**Notifications:** :ref:`Logging.LogEntryAdded <api-logging-log-entry-added>`

.. _api-namespace-modbusrtu:

ModbusRtu
---------

**Methods:** :ref:`ModbusRtu.AddModbusRtuMaster <api-modbus-rtu-add-modbus-rtu-master>`, :ref:`ModbusRtu.GetModbusRtuMasters <api-modbus-rtu-get-modbus-rtu-masters>`, :ref:`ModbusRtu.GetSerialPorts <api-modbus-rtu-get-serial-ports>`, :ref:`ModbusRtu.ReconfigureModbusRtuMaster <api-modbus-rtu-reconfigure-modbus-rtu-master>`, :ref:`ModbusRtu.RemoveModbusRtuMaster <api-modbus-rtu-remove-modbus-rtu-master>`

**Notifications:** :ref:`ModbusRtu.ModbusRtuMasterAdded <api-modbus-rtu-modbus-rtu-master-added>`, :ref:`ModbusRtu.ModbusRtuMasterChanged <api-modbus-rtu-modbus-rtu-master-changed>`, :ref:`ModbusRtu.ModbusRtuMasterRemoved <api-modbus-rtu-modbus-rtu-master-removed>`, :ref:`ModbusRtu.SerialPortAdded <api-modbus-rtu-serial-port-added>`, :ref:`ModbusRtu.SerialPortRemoved <api-modbus-rtu-serial-port-removed>`

.. _api-namespace-networkmanager:

NetworkManager
--------------

**Methods:** :ref:`NetworkManager.ConnectWifiNetwork <api-network-manager-connect-wifi-network>`, :ref:`NetworkManager.CreateWiredConnection <api-network-manager-create-wired-connection>`, :ref:`NetworkManager.DisconnectInterface <api-network-manager-disconnect-interface>`, :ref:`NetworkManager.EnableNetworking <api-network-manager-enable-networking>`, :ref:`NetworkManager.EnableWirelessNetworking <api-network-manager-enable-wireless-networking>`, :ref:`NetworkManager.GetNetworkDevices <api-network-manager-get-network-devices>`, :ref:`NetworkManager.GetNetworkStatus <api-network-manager-get-network-status>`, :ref:`NetworkManager.GetWirelessAccessPoints <api-network-manager-get-wireless-access-points>`, :ref:`NetworkManager.ScanWifiNetworks <api-network-manager-scan-wifi-networks>`, :ref:`NetworkManager.StartAccessPoint <api-network-manager-start-access-point>`

**Notifications:** :ref:`NetworkManager.NetworkStatusChanged <api-network-manager-network-status-changed>`, :ref:`NetworkManager.WiredNetworkDeviceAdded <api-network-manager-wired-network-device-added>`, :ref:`NetworkManager.WiredNetworkDeviceChanged <api-network-manager-wired-network-device-changed>`, :ref:`NetworkManager.WiredNetworkDeviceRemoved <api-network-manager-wired-network-device-removed>`, :ref:`NetworkManager.WirelessNetworkDeviceAdded <api-network-manager-wireless-network-device-added>`, :ref:`NetworkManager.WirelessNetworkDeviceChanged <api-network-manager-wireless-network-device-changed>`, :ref:`NetworkManager.WirelessNetworkDeviceRemoved <api-network-manager-wireless-network-device-removed>`

.. _api-namespace-rules:

Rules
-----

**Methods:** :ref:`Rules.AddRule <api-rules-add-rule>`, :ref:`Rules.DisableRule <api-rules-disable-rule>`, :ref:`Rules.EditRule <api-rules-edit-rule>`, :ref:`Rules.EnableRule <api-rules-enable-rule>`, :ref:`Rules.ExecuteActions <api-rules-execute-actions>`, :ref:`Rules.ExecuteExitActions <api-rules-execute-exit-actions>`, :ref:`Rules.FindRules <api-rules-find-rules>`, :ref:`Rules.GetRuleDetails <api-rules-get-rule-details>`, :ref:`Rules.GetRules <api-rules-get-rules>`, :ref:`Rules.RemoveRule <api-rules-remove-rule>`

**Notifications:** :ref:`Rules.RuleActiveChanged <api-rules-rule-active-changed>`, :ref:`Rules.RuleAdded <api-rules-rule-added>`, :ref:`Rules.RuleConfigurationChanged <api-rules-rule-configuration-changed>`, :ref:`Rules.RuleRemoved <api-rules-rule-removed>`

.. _api-namespace-scripts:

Scripts
-------

**Methods:** :ref:`Scripts.AddScript <api-scripts-add-script>`, :ref:`Scripts.EditScript <api-scripts-edit-script>`, :ref:`Scripts.GetScriptContent <api-scripts-get-script-content>`, :ref:`Scripts.GetScripts <api-scripts-get-scripts>`, :ref:`Scripts.RemoveScript <api-scripts-remove-script>`

**Notifications:** :ref:`Scripts.ScriptAdded <api-scripts-script-added>`, :ref:`Scripts.ScriptChanged <api-scripts-script-changed>`, :ref:`Scripts.ScriptContentChanged <api-scripts-script-content-changed>`, :ref:`Scripts.ScriptLogMessage <api-scripts-script-log-message>`, :ref:`Scripts.ScriptRemoved <api-scripts-script-removed>`

.. _api-namespace-system:

System
------

**Methods:** :ref:`System.CheckForUpdates <api-system-check-for-updates>`, :ref:`System.EnableRepository <api-system-enable-repository>`, :ref:`System.FactoryReset <api-system-factory-reset>`, :ref:`System.GetCapabilities <api-system-get-capabilities>`, :ref:`System.GetPackages <api-system-get-packages>`, :ref:`System.GetRepositories <api-system-get-repositories>`, :ref:`System.GetSystemInfo <api-system-get-system-info>`, :ref:`System.GetTime <api-system-get-time>`, :ref:`System.GetTimeZones <api-system-get-time-zones>`, :ref:`System.GetUpdateStatus <api-system-get-update-status>`, :ref:`System.Reboot <api-system-reboot>`, :ref:`System.RemovePackages <api-system-remove-packages>`, :ref:`System.Restart <api-system-restart>`, :ref:`System.RollbackPackages <api-system-rollback-packages>`, :ref:`System.SetTime <api-system-set-time>`, :ref:`System.Shutdown <api-system-shutdown>`, :ref:`System.UpdatePackages <api-system-update-packages>`

**Notifications:** :ref:`System.CapabilitiesChanged <api-system-capabilities-changed>`, :ref:`System.PackageAdded <api-system-package-added>`, :ref:`System.PackageChanged <api-system-package-changed>`, :ref:`System.PackageRemoved <api-system-package-removed>`, :ref:`System.RepositoryAdded <api-system-repository-added>`, :ref:`System.RepositoryChanged <api-system-repository-changed>`, :ref:`System.RepositoryRemoved <api-system-repository-removed>`, :ref:`System.TimeConfigurationChanged <api-system-time-configuration-changed>`, :ref:`System.UpdateStatusChanged <api-system-update-status-changed>`

.. _api-namespace-tags:

Tags
----

**Methods:** :ref:`Tags.AddTag <api-tags-add-tag>`, :ref:`Tags.GetTags <api-tags-get-tags>`, :ref:`Tags.RemoveTag <api-tags-remove-tag>`

**Notifications:** :ref:`Tags.TagAdded <api-tags-tag-added>`, :ref:`Tags.TagRemoved <api-tags-tag-removed>`, :ref:`Tags.TagValueChanged <api-tags-tag-value-changed>`

.. _api-namespace-transfers:

Transfers
---------

**Methods:** :ref:`Transfers.CreateUpload <api-transfers-create-upload>`, :ref:`Transfers.StartDownload <api-transfers-start-download>`

**Notifications:** :ref:`Transfers.DownloadAvailable <api-transfers-download-available>`

.. _api-namespace-users:

Users
-----

**Methods:** :ref:`Users.ChangePassword <api-users-change-password>`, :ref:`Users.ChangeUserPassword <api-users-change-user-password>`, :ref:`Users.CreateUser <api-users-create-user>`, :ref:`Users.GetTokens <api-users-get-tokens>`, :ref:`Users.GetUserInfo <api-users-get-user-info>`, :ref:`Users.GetUserTokens <api-users-get-user-tokens>`, :ref:`Users.GetUsers <api-users-get-users>`, :ref:`Users.RemoveToken <api-users-remove-token>`, :ref:`Users.RemoveUser <api-users-remove-user>`, :ref:`Users.SetUserInfo <api-users-set-user-info>`, :ref:`Users.SetUserScopes <api-users-set-user-scopes>`

**Notifications:** :ref:`Users.PushButtonAuthFinished <api-users-push-button-auth-finished>`, :ref:`Users.UserAdded <api-users-user-added>`, :ref:`Users.UserChanged <api-users-user-changed>`, :ref:`Users.UserRemoved <api-users-user-removed>`

.. _api-namespace-zwave:

ZWave
-----

**Methods:** :ref:`ZWave.AddNetwork <api-z-wave-add-network>`, :ref:`ZWave.AddNode <api-z-wave-add-node>`, :ref:`ZWave.CancelPendingOperation <api-z-wave-cancel-pending-operation>`, :ref:`ZWave.FactoryResetNetwork <api-z-wave-factory-reset-network>`, :ref:`ZWave.GetNetworks <api-z-wave-get-networks>`, :ref:`ZWave.GetNodes <api-z-wave-get-nodes>`, :ref:`ZWave.GetSerialPorts <api-z-wave-get-serial-ports>`, :ref:`ZWave.IsZWaveAvailable <api-z-wave-is-z-wave-available>`, :ref:`ZWave.RemoveFailedNode <api-z-wave-remove-failed-node>`, :ref:`ZWave.RemoveNetwork <api-z-wave-remove-network>`, :ref:`ZWave.RemoveNode <api-z-wave-remove-node>`

**Notifications:** :ref:`ZWave.NetworkAdded <api-z-wave-network-added>`, :ref:`ZWave.NetworkChanged <api-z-wave-network-changed>`, :ref:`ZWave.NetworkRemoved <api-z-wave-network-removed>`, :ref:`ZWave.NodeAdded <api-z-wave-node-added>`, :ref:`ZWave.NodeChanged <api-z-wave-node-changed>`, :ref:`ZWave.NodeRemoved <api-z-wave-node-removed>`

.. _api-namespace-zigbee:

Zigbee
------

**Methods:** :ref:`Zigbee.AddNetwork <api-zigbee-add-network>`, :ref:`Zigbee.CreateBinding <api-zigbee-create-binding>`, :ref:`Zigbee.FactoryResetNetwork <api-zigbee-factory-reset-network>`, :ref:`Zigbee.GetAdapters <api-zigbee-get-adapters>`, :ref:`Zigbee.GetAvailableBackends <api-zigbee-get-available-backends>`, :ref:`Zigbee.GetNetworks <api-zigbee-get-networks>`, :ref:`Zigbee.GetNodes <api-zigbee-get-nodes>`, :ref:`Zigbee.RefreshBindings <api-zigbee-refresh-bindings>`, :ref:`Zigbee.RefreshNeighborTables <api-zigbee-refresh-neighbor-tables>`, :ref:`Zigbee.RemoveBinding <api-zigbee-remove-binding>`, :ref:`Zigbee.RemoveNetwork <api-zigbee-remove-network>`, :ref:`Zigbee.RemoveNode <api-zigbee-remove-node>`, :ref:`Zigbee.SetPermitJoin <api-zigbee-set-permit-join>`

**Notifications:** :ref:`Zigbee.AdapterAdded <api-zigbee-adapter-added>`, :ref:`Zigbee.AdapterRemoved <api-zigbee-adapter-removed>`, :ref:`Zigbee.NetworkAdded <api-zigbee-network-added>`, :ref:`Zigbee.NetworkChanged <api-zigbee-network-changed>`, :ref:`Zigbee.NetworkRemoved <api-zigbee-network-removed>`, :ref:`Zigbee.NodeAdded <api-zigbee-node-added>`, :ref:`Zigbee.NodeChanged <api-zigbee-node-changed>`, :ref:`Zigbee.NodeRemoved <api-zigbee-node-removed>`

