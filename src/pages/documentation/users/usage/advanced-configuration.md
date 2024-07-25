---
id: advanced-configuration
title: Advanced configuration
---

Besides the normal configuration, there are some more advanced configuration options that should not be required to be changed for most users. However, in some rare circumstances, editing those options too might be desirable.

For a standard nymea:core installation, which will run nymead as root, the configuration file can be found in `/etc/nymea/nymead.conf`. If nymead is started as a user, the configuration file can be found in `~/.nymea/nymea.conf`.

Most of this sections can and should be configured through nymea:app, however, if needed all options can also be edited in this configuration file. Alongside to those options, some more advanced configuration options are available in this configuration file.

A restart of nymead is required in order to reload the configuration file.


### Section [BluetoothServer]

```bash
[BluetoothServer]
enabled=false
```

Offers the nymea API through a Bluetooth RFCOMM service. Requires Bluetooth hardware and Bluez installed. Enabling this option will expose the nymea API over Bluetooth. This way a nymea setup can be used without TCP/IP networking at all.

### Section [SSL]

```bash
[SSL]
certificate=
certificate-key=
```

The SSL section allows to provide an SSL certificate which will be used for all serverfaces, such as API interfaces, the web server and the MQTT server. If nymea is started for the first time without any SSL certification configured, a new self-signed certificate will be generated.

### Section [LoggingRules]

This section allows to configure debug output of nymead. It can be used to filter debug output in a more customized way.

```bash
[Rules]
*.debug=false
```

This example would disable all debug output and only keep warnings and errors. Individual debug categories can be enabled by adding e.g.

```bash
Bluetooth.debug=true
```
