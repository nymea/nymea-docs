---
id: plugin-wizard
title: Plugin Wizard
---

The plug-in wizard is a tool for the QtCreator to generate the required file structure for a plug-in.



First you need to setup the [build envionment](/docs/plugins/plugin-build-environment).
Afterwards install the wizard:

```bash
 $ sudo apt update
 $ sudo apt install nymea-qtcreator-wizards
```
After the sucessfull installation start the  Qt Creator

```bash
 $ qtcreator
```

Start the wizard inside the Qt Creator by: File -> New File or Project ... 

![wizard plugin template](/img/wizard1.png)

## Project location

Choose the project name and the path where the project should be located. As in this example the name is template and will be used within the source code as refference. A good practice is to pick a general describing name like a vendor or product/project name.

![wizard plugin template](/img/wizard2.png)

## Plugin details

In this section, the plugin details can be defined.

**Class name:** Enter the name of the main class for this device plugin. The naming should be DevicePluginName in camel case.

**Vendor name:** Enter the name of the Vendor.

**Device name:** Enter the name for the default device which will be created as template. You can change this any time in the json file.

**Setup method:** Pick the desired setup method for the default device which will be created as template. You can change this any time in the json file. You can find more information in the CreateMethods and SetupMethods section.

**Create method:** Pick the desired create method for the default device which will be created as template. You can change this any time in the json file.

![wizard plugin template](/img/wizard3.png)

## Developer information

Enter the developers name and email. These information will be used in the copyright sections of the plugin. The copyright information are placed in the debian/copyright file and in each source code license header.

![wizard plugin template](/img/wizard4.png)

## Kit selection

Pick the build kit for this project. The kit must match the version of the nymead and libnymea1 built.

> **Note:** You have to make sure you are using the same kit as the nymea daemon and libraries use. If you have installed the nymea library and Qt libraries from you default system package manager, you should probably go with the default kit of your distribution.

![wizard plugin template](/img/wizard5.png)

## Project Management

Here you can select your preferred project management tool. If you choose git, the default .gitignore file will be added to the project.

![wizard plugin template](/img/wizard6.png)

## Project tree

Once you've finished the plugin wizard, you can start with the development of your plugin.

![wizard plugin template](/img/wizard_7.png)

## File structure

Starting with the new created project you can find following files in you project:

* template.pro
* deviceplugintemplate.json
* deviceplugintemplate.h
* deviceplugintemplate.cpp

### File _template.pro_

This is the Qt project file of your plugin. If you need additional Qt modules or external libraries in your project you can include them normaly using i.e. QT += network or INCLUDEPATH += /path/to/includes and LIBS += -lfoo like in any other Qt project.

### File _deviceplugintemplate.json_

Here you can find the device plugin interface describing the vendors, devices and plugin information. A detailed description of each section can be found in the The plugin [JSON File](/docs/plugins/plugin-json) section.

In the first section you can find the plugin specific properties. The id will be set to zero and must be changed with an actual UUID. The UUID with all zeros is creaed by the plugin wizard in order to indicate that this field has to be updated.


### File _deviceplugintemplate.h_

The main header file shows you the basic structure of your DevicePlugin template. The header file start with the license header containing the copyright information passed during the wizard.
```cpp
/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 *                                                                   
 *  Copyright (C) 2020 Developer Name <developer.name@example.com> 
 *                                                                        
 *  This file is part of nymea.                                          
 *                                                                        
 *  This library is free software; you can redistribute it and/or         
 *  modify it under the terms of the GNU Lesser General Public            
 *  License as published by the Free Software Foundation; either          
 *  version 2.1 of the License, or (at your option) any later version.    
 *                                                                        
 *  This library is distributed in the hope that it will be useful,       
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of        
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU     
 *  Lesser General Public License for more details.                       
 *                                                                        
 *  You should have received a copy of the GNU Lesser General Public      
 *  License along with this library; If not, see                          
 *  <http://www.gnu.org/licenses/>.                                       
 *                                                                      
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
```

The main class has the name DevicePluginExample. The device plugin class inherts from the DevicePlugin class and must implement the pure virtual methods in order build correctly.

```cpp
class DevicePluginTemplate: public DevicePlugin
{
    Q_OBJECT

    Q_PLUGIN_METADATA(IID "io.nymea.DevicePlugin" FILE "deviceplugintemplate.json")
    Q_INTERFACES(DevicePlugin)


public:
    explicit DevicePluginTemplate();

    void init() override;
    void startMonitoringAutoDevices() override;
    void postSetupDevice(Device *device) override;
    void deviceRemoved(Device *device) override;

    void setupDevice(DeviceSetupInfo *info) override;
    void executeAction(DeviceActionInfo *info) override;

private:

private slots:

};
```

### File _deviceplugintemplate.cpp_

The implementation of each method can be found in the corresponding cpp file.

As you can see, the plugin includes in the _.cpp_ file the plugininfo.h file, which will be generated during build time from the nymea-plugininfocompiler tool. This tool translates the deviceplugintemplate.json into a C++ header file containing all UUID definitions, translations strings and the debug catergory definition.
```cpp
#include "plugininfo.h"
```
The main entry point of the plugin is the **init()** method. This method will be called from the DeviceManager once all plugins are loaded and the initialization phase starts for you all plugins. Here you can start creating your objects in initialize whatever you need. This method can be seen like a constructor.

```cpp
void DevicePluginExample::init()
{
    // Initialize/create objects
}
```
The **startMonitoringAutoDevices** method will be called from the DeviceManager once all devices are set up and the plugin can start for searching device which appear automatically if your plugin supports such device types.
```cpp
void DevicePluginExample::startMonitoringAutoDevices()
{
    // Start seaching for devices which can be discovered and added automatically
}
```
The **postSetupDevice** method will be called from the DeviceManager once the setup of a device has finished successfully. Here is a good point to initialize the states of the device.
```cpp
void DevicePluginExample::postSetupDevice(Device *device)
{
    qCDebug(dcTemplate()) << "Post setup device" << device->name() << device->params();

    // This method will be called once the setup for device is finished
}
```
The **deviceRemoved** method will be called from the DeviceManager once a device is about to be removed from the system. Here is a good place to clean up everything related to the device which will be removed.

```cpp
void DevicePluginExample::deviceRemoved(Device *device)
{
    qCDebug(dcTemplate()) << "Remove device" << device->name() << device->params();

    // Clean up all data related to this device
}
```

When the user wants to add a new device from this plugin, the **setupDevice** method will be called. Here you can initialize Objects and set up everything you need for your device.

```cpp
void DevicePluginTemplate::setupDevice(DeviceSetupInfo *info)
{
    qCDebug(dcTemplate()) << "Setup device" << info->device();

    info->finish(Device::DeviceErrorNoError);
}
```

When the user wants to execute an Action of a Device from this DevicePlugin, the **executeAction** method will be called. Here you can perform the actual execution of the custom call for your Device.

```cpp
void DevicePluginTemplate::executeAction(DeviceActionInfo *info)
{
    qCDebug(dcTemplate()) << "Executing action for device" << info->device() << info->action().actionTypeId().toString() << info->action().params();

    info->finish(Device::DeviceErrorNoError);
}
```
