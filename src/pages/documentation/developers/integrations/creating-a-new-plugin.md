---
id: creating-a-new-plugin
title: Creating a new plugin
---

<script>
    import Code from '../../../../_components/Code.svelte';
</script>

## QtCreator wizard (C++/Qt only)

The recommended way to create a new C++/Qt plugin is to use QtCreator and get started by creating a new project using the project wizard for nymea plugins.

Go to `File` -> `New File or Project`. Select `nymea` in the projects list and then `Integration plugin for nymea`.

![Wizard](/img/wizard1.png)

Follow the steps in the wizard to complete the setup.

See the [integration plugin tutorial](tutorial-integration) for a more complete walkthrough of the wizard.

## Manual project creation

The shortest path to create new plugin without using the QtCreator wizard is to clone the examples repository.

```bash
git clone https://github.com/nymea/nymea-plugin-examples.git
```
    
The repository contains a folder named template with subdirectories for the supported programming languages. Copy the entire folder contents of the language of your choice and start by renaming the files to the desired name. The terms "template" and "example" should be renamed to the plugins name.


<Code>

```C++
cp -r nymea-plugin-examples/templates/cpp my-plugin
cd my-plugin
mv template.pro myplugin.pro
mv integrationplugintemplate.cpp integrationpluginmyplugin.cpp
mv integrationplugintemplate.h integrationpluginmyplugin.h
mv integrationplugintemplate.json integrationpluginmyplugin.json
```

```Python
cp -r nymea-plugin-examples/templates/python my-plugin
cd my-plugin
mv integrationplugintemplate.py integrationpluginmyplugin.py
mv integrationplugintemplate.json integrationpluginmyplugin.json
```

```JavaScript
cp -r nymea-plugin-examples/templates/js my-plugin
cd my-plugin
mv integrationplugintemplate.js integrationpluginmyplugin.js
mv integrationplugintemplate.json integrationpluginmyplugin.json
```

</Code>

If there is a project file in the directory, edit it and adjust the file names in there accordingly.
