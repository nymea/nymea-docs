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

### Section [Logs]

```bash
[Logs]
logDBDriver=QSQLITE
logDBHost=
logDBMaxEntries=200000
logDBName=/var/log/nymead.sqlite
logDBPassword=
logDBUser=
```

This section configures where the log database is stored. By default, this is SQLite but it can also be configured to log to other databases such as MySQL/MariaDB, PostgreSQL, OracleDB etc.

Note that this requires the according Qt database backend plugin to be installed and the according database server must be set up prior to enabling it.

An example to configure nymea to log into MySQL instead of SQLite:

```bash
[Logs]
logDBDriver=QMYSQL
logDBHost=127.0.0.1
logDBMaxEntries=200000
logDBName=nymea
logDBPassword=nymea
logDBUser=nymea
```

#### logDBDriver

See the [Qt SQL Database Drivers documentation](https://doc.qt.io/qt-5/sql-driver.html) for a list of supported database drivers.

#### logDBHost

Specifies the host of the database server. For SQLite, this value is not used. For client/server based databases this normally is the IP address and port combination.

#### logDBMaxEntries

The maximum amount of database entries. If the database reaches the limit older entries will be deleted.

#### logDBName

The database name of the database to log to. For SQLite, this is a path to a local file. For client/server base databases this normally is the name of the database on the server which has to be created manually before attempting to start nymea with this configuration.

#### logDBUser

Username for the log database. For SQLite, this is a path to a local file. 

#### logDBPassword

Password for the log database. For SQLite, this value is not used.

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
