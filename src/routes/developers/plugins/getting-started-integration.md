---
id: getting-started-integration
title: Getting started
---

Integration plugins in nymea provide support for additional integrations with hardware devices and online services, commonly referred to as "things". A single plugin can provide support for multiple things.

A plugin is responsible for translating the nymea internal things api into the device or service specific protocol. This mainly consists of handling setup and connecting to a given thing and then monitoring it for state changes and forwarding actions triggered by nymea to it.


Integration plugins can be written either using [C++/Qt](#cqt) or using [JavaScript](#javascript). However, either way a [plugin JSON](plugin-json) file is required to define all the supported integrations by this plugin.


## C++/Qt

### QtCreator

For C++/Qt plugins it is recommended to use QtCreator and get started by creating a new project using the project wizard for nymea plugins.

Go to `File` -> `New File or Project`. Select `nymea` in the projects list and then `Integration plugin for nymea`.

![Wizard](/img/wizard1.png)

Follow the steps in the wizard to complete the setup.

See the [integration plugin tutorial](tutorial-integration) for a more complete walkthrough of the wizard.

### Manual project creation

The shortest path to create new C++/Qt plugin without using QtCreator is to clone the examples repository.

    git clone https://github.com/nymea/nymea-plugin-examples.git
    
The repository contains a folder named template with a subdirectory named cpp. Copy the entire folder contents and start by renaming the files to the desired name. The terms "template" and "example" should be renamed to the plugins name.

## JavaScript

The shortest path to create new JavaScript plugin is to clone the examples repository.

    git clone https://github.com/nymea/nymea-plugin-examples.git
    
The repository contains a folder named template with a subdirectory named js. Copy the entire folder contents and start by renaming the files to the desired name. The terms "template" and "example" should be renamed to the plugins name.


