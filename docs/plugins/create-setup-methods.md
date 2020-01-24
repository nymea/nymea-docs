---
id: create-setup-methods
title: Create and Setup Methods
---

This page describes how the setup and creation of a device is working in a plugin. Since the device manager handles all the plugins and devices there are certain steps during the device setup which have to be considered.

The CreateMethod describes how the device will be created (by the user, by discovery or automatically). The SetupMethod describes how the device will be set up. A Device can have multiple CreateMethods, but only one SetupMethod.

![test](/img/setup-sync-resized.png)

    CreateMethods
        User → DeviceClass::CreateMethodUser
        Discovery → DeviceClass::CreateMethodDiscovery
        Auto → DeviceClass::CreateMethodAuto
    SetupMethods
        JustAdd → DeviceClass::SetupMethodJustAdd
        DisplayPin → DeviceClass::SetupMethodDisplayPin
        EnterPin
        PushButton

## CreateMethod "User" - SetupMethod "JustAdd - synchronous"

This is the simplest setup what a device can have.

    CreateMethod "User": the user has to fill out the Params of the device by hand
    SetupMethod "JustAdd": there is nothing special to do during the setup with the device.

Once the is adding the device the DeviceManager is calling following methods in the device plugin:


## CreateMethod "User" - SetupMethod "JustAdd" - asynchronous

    Setup
        1. | The main setup of the device in the plugin.
        2. | If the status can not be determined immediately, we have to tell the DeviceManager that the status will be communicated later.
        3. | Once the setup status is determined, the plugin can emit the signal DevicePlugin::deviceSetupFinished to inform the DeviceManager about the result.
        4. | If the device setup succeeded and the device is in the system, the DeviceManager will call the postSetupDevice() method.

## CreateMethod "auto" - SetupMethod "justAdd"

    Monitor
        1. | The method startMonitoringAutoDevices() will be called once the DeviceManager has loaded all Plugins and the discovery for auto devices can be started.
        2. | Once the plugin has discovered one or more devices, the plugin can emit the signal DevicePlugin::autoDevicesAppeared() to inform the DeviceManager that new devices where found (without user interaction).
    Setup
        3. | The plugin will be set up with the params of the auto discovered DeviceDescriptor.
        4. | If something goes wrong during the setup return DeviceManager::DeviceSetupStatusFailure, otherwise DeviceManager::DeviceSetupStatusSuccess.
        5. | If the device setup succeeded and the device is in the system, the DeviceManager will call the postSetupDevice() method.

## CreateMethod "Discovery" - SetupMethod "JustAdd"


    Discovery
        1. | The user started to discover devices. The method discoverDevices() will be called in the plugin.
        2. | Return DeviceErrorAsync and start the discovery in the source code.
        3. | Once the discovery is finished, the plugin can emit the signal DevicePlugin::devicesDiscovered to inform the DeviceManager about the result.
    Setup
        4. | The plugin will be set up with the params of the discovered DeviceDescriptor.
        5. | If something goes wrong during the setup return DeviceManager::DeviceSetupStatusFailure, otherwise DeviceManager::DeviceSetupStatusSuccess.
        6. | If the device setup succeeded and the device is in the system, the DeviceManager will call the postSetupDevice() method.


## CreateMethod "Discovery" - SetupMethod "PushButton"


    Discovery
        1. | The user started to discover devices. The method discoverDevices() will be called in the plugin.
        2. | Return DeviceErrorAsync and start the discovery in the source code.
        3. | Once the discovery is finished, the plugin can emit the signal DevicePlugin::devicesDiscovered to inform the DeviceManager about the result.
    Pairing
        4. | The user has already seen the pairing info with the push button instructions and should also already have pushed the button. The method DevicePlugin::confirmPairing() will be called. Here can be verified if the push button has been pressed and if the pairing succeeded.
        5. | Returns the DeviceManager::DeviceSetupStatus to inform about the result (sync or async).
        6. | Once the pairing has been verified (check if the button has been pushed) the plugin can emit the signal DevicePlugin::pairingFinished() to inform the DeviceManager about the result.
    Setup
        7. | The plugin will be set up with the params of the paired Device.
        8. | If something goes wrong during the setup return DeviceManager::DeviceSetupStatusFailure, otherwise DeviceManager::DeviceSetupStatusSuccess.
        9. | If the device setup succeeded and the device is in the system, the DeviceManager will call the postSetupDevice() method.


## CreateMethod "Discovery" - SetupMethod "EnterPin"


    Discovery
        1. | The user started to discover devices. The method discoverDevices() will be called in the plugin.
        2. | Return DeviceErrorAsync and start the discovery in the source code.
        3. | Once the discovery is finished, the plugin can emit the signal DevicePlugin::devicesDiscovered to inform the DeviceManager about the result.
    Pairing
        4. | The user has already seen the pairing info with the instructions which pin should be entered. The method DevicePlugin::confirmPairing() will be called. Here can be verified if the entered pin is valid and if the pairing succeeded.
        5. | Returns the DeviceManager::DeviceSetupStatus to inform about the result (sync or async).
        6. | Once the pairing has been verified (check if the button has been pushed) the plugin can emit the signal DevicePlugin::pairingFinished() to inform the DeviceManager about the result.
    Setup
        7. | The plugin will be set up with the params of the paired Device.
        8. | If something goes wrong during the setup return DeviceManager::DeviceSetupStatusFailure, otherwise DeviceManager::DeviceSetupStatusSuccess.
        9. | If the device setup succeeded and the device is in the system, the DeviceManager will call the postSetupDevice() method.


## CreateMethod "Discovery" - SetupMethod "DisplayPin"


    Discovery
        1. | The user started to discover devices. The method discoverDevices() will be called in the plugin.
        2. | Return DeviceErrorAsync and start the discovery in the source code.
        3. | Once the discovery is finished, the plugin can emit the signal DevicePlugin::devicesDiscovered to inform the DeviceManager about the result.
    Display pin
        4. | Once the user selected one of the discovered devices the device manager will call the method DevicePlugin::displayPin() in the plugin. Here can be sent the command to display the pin on the device. The pin which will be displayed on the device will be passed as secret in the DevicePlugin::confirmPairing() method.
        5. | Returns the Device::DeviceError to inform about the result (sync or async).
    Pairing
        6. | The user should see now the pin on the display and the pairing info. The method DevicePlugin::confirmPairing() will be called once he entered the pin. Here can be verified if the pin is authorized by the device and if the pairing succeeded.
        7. | Returns the DeviceManager::DeviceSetupStatus to inform about the result (sync or async).
        8. | Once the pairing has been verified (check if the button has been pushed) the plugin can emit the signal DevicePlugin::pairingFinished() to inform the DeviceManager about the result.
    Setup
        9. | The plugin will be set up with the params (i.e. containing a pin param) of the paired Device.
        10. | If something goes wrong during the setup return DeviceManager::DeviceSetupStatusFailure, otherwise DeviceManager::DeviceSetupStatusSuccess.
        11. | If the device setup succeeded and the device is in the system, the DeviceManager will call the postSetupDevice() method.
