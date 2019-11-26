---
id: configuration-file
title: Configuration file
---

## nymea Configuration file

!!! Note
    Usually you don't need to edit the configration file. Almost all options can be set within the nymea clients. 
    The config file will be created by nymea during start if there is no file present. Stop nymead before you make 
    changes on the file.

### nymea.conf
```
[BluetoothServer]
enabled=false

[Logs]
logDBDriver=QSQLITE
logDBHost=127.0.0.1
logDBMaxEntries=200000
logDBName=/var/log/nymead.sqlite
logDBPassword=
logDBUser=

[MqttServer]
default\address=0.0.0.0
default\authenticationEnabled=true
default\port=1883
default\sslEnabled=false

[SSL]
certificate=
certificate-key=

[TcpServer]
default\address=0.0.0.0
default\authenticationEnabled=true
default\port=2222
default\sslEnabled=true

[WebServer]
insecure\address=0.0.0.0
insecure\authenticationEnabled=false
insecure\port=80
insecure\publicFolder=/usr/share/nymea-webinterface/public/
insecure\restServerEnabled=false
insecure\sslEnabled=false
secure\address=0.0.0.0
secure\authenticationEnabled=false
secure\port=443
secure\publicFolder=/usr/share/nymea-webinterface/public/
secure\restServerEnabled=false
secure\sslEnabled=true

[WebSocketServer]
default\address=0.0.0.0
default\authenticationEnabled=true
default\port=4444
default\sslEnabled=true

[nymead]
debugServerEnabled=false
language=en_US
name=nymea
timeZone=@ByteArray(Europe/Vienna)
uuid=@Variant(\0\0\0\x1e-\xb2?tRPL\x2c\xb3\x31\v\x3b\x61\x36\xe2\x9b)
```

## Filesystem location

The location changes if you start nymea as root or as user.

* Root: /etc/nymea/nymea.conf
* User: ~/.nymea/nymea.conf

## Section [BluetoothServer]

#### enabled 

Offers the nymea API through a Bluetooth classic service. Requires Bluetooth classic hardware and Bluez installed.

* Required: `true` 
* Type: `bool`
* Default value: `false`
* Example: `enabled=false`

## Section [Logs]

nymea will start also without a log-database configured.

Example configuration for a mySQL database named nymea. Name, user and password must be changed according to your databases settings.

```text
[Logs]
logDBDriver=QMYSQL
logDBHost=127.0.0.1
logDBMaxEntries=200000
logDBName=nymea
logDBPassword=nymea
logDBUser=nymea
```

### logDBDriver

Configure which kind of database is going to be used.

* Required: `false`
* Type: `enum`
* Default value: `QSQLITE`
* Possible values:
    ```
    QSQLITE
    QMYSQL
    ```
* Example: `logDBDriver=QSQLITE`

### logDBHost

Specfies the IP address of the database. Use 127.0.0.1 if the log database is running on the same machine, otherwise enter the IP address of the database.

* Required: `false`
* Type: `int`
* Default value: `127.0.0.1`
* Example:
    `logDBHost=127.0.0.1`

### logDBMaxEntries

The maximum amount of database entries. If the database reaches the limit older entries will be deleted.

* Required: `false`
* Type: `int`
* Default value: `200000`
* Example: `logDBMaxEntries=200000`

### logDBName

In case of sqLite this is the path to the database, otherwise it's the actual name.

* Required: `false`
* Type: `String`
* Default value: `/var/log/nymead.sqlite`
* Example: `logDBName=/var/log/nymead.sqlite`

### logDBPassword

Password for the log database. The default database has no password set. 
Change it to the according password for the given database user.

* Required: `false`
* Type: `String`
* Default value: ""
* Example: `logDBPassword=nymea`

### logDBUser

The log database username. This is not the username of nymea.

* Required: `false`
* Type: `String`
* Default value: ` `
* Example: `logDBUser=nymea`

## Section [SSL]

### certificate

### certificate-key

## Section [TcpServer]

This section defines the TCP interface for the JSON-RPC. You can specify more than one TCP interface.
The value before the backslash "\" is the name of the interface. Each interface needs it's unique name.

## Section [WebSocketServer]

Option are the same as for the TCP server, see section [TcpServer]

## Section [MqttServer]

Option are the same as for the TCP server, see section [TcpServer]

## Section [WebServer]

### address

Defines from where the WebServer  can be reached. Use 127.0.0.1 to make it accessible only from the same maching,
0.0.0.0 makes it accessible from any network interface.

* Required: `true`
* Type: `String`
* Default: `address=0.0.0.0`
* Example: `insecure\address=0.0.0.0`

### authenticationEnabled

Requires the client to use an encrypted connection

* Required: `true`
* Type: `Bool`
* Default: `false`
* Example: `insecure\authenticationEnabled=false`

### port

Defines the port of the WebServer. Port 80 is the default port for browsers.

* Required: `true`
* Type: `int`
* Default: `80`
* Example: `insecure\port=80`

### publicFolder

Defines the where the web page is located.

* Required: `true`
* Type: `String`
* Default: `/usr/share/nymea-webinterface/public/`
* Example: `insecure\publicFolder=/usr/share/nymea-webinterface/public/`

### restServerEnabled

Enables the WebServer.

* Required: `true`
* Type: `bool`
* Default: `false`
* Example: `insecure\restServerEnabled=false`

### sslEnabled

Enable SSL for an encrypted connection (https)

* Required: `true`
* Type: `bool`
* Default: `false`
* Example: `insecure\sslEnabled=false`

## Section [WebSocketServer]

Option are the same as for the TCP server, see section [TcpServer]

## Section [nymead]

### debugServerEnabled

Enables the debug server, this should not be enabled by default as it states a security risk.
Needs to have the webserver enabled.

* Required: `true`
* Type: `Bool`
* Default value: `false`
* Example: 
    `debugServerEnabled=false`
* Description:

### language

The language is obtained by the host system language.

* Required: `true`
* Type: `Strin/locale`
* Default value: `en_US`
* Example: `language=en_US`

### name

The name of your nymea.

* Required: `true`
* Type: `String`
* Default value: `nymea`

### timeZone

The timezone is required for time based rules.

* Required: true
* Type: `ByteArray`
* Default: `Europe/Vienna`
* Example: `timeZone=@ByteArray(Europe/Vienna)`

### uuid

An unique value to identify the nymea instance, is required by nymea:cloud.
Altering this value might compsomise the access to nymea:cloud.

* Required: `true`
* Type: Encoded string
* Default value: unique value
* Example:
    `uuid=@Variant(\0\0\0\x1e-\xb2?tRPL\x8c\xb3\x81\v\xcb\x61\x36\xe2\x9b)`

## Logging configuration file

This file helps to filter the debug output.
This file is not necessary and is not created by default

Example logging.conf file:

```text
[Rules]
*.debug=false
Application.debug=false
Avahi.debug=false
Bluetooth.debug=true
Cloud.debug=false
Connection.debug=false
DebugServer.debug=false
DeviceManager.debug=false
Hardware.debug=false
JsonRpc.debug=false
JsonRpcTraffic.debug=false
LogEngine.debug=false
RuleEngine.debug=false
TcpServer.debug=false
TimeManager.debug=false
UserManager.debug=false
WebServer.debug=false
WebServer.warning=false
WebSocketServer.debug=false
UPnP.debug=false
​
Platform.debug=false
PlatformUpdate.debug=false
​
Bluez.debug=false
```

## Devices configuration file

This file is created and modified by the devicemanager. In generally this file should not be modified manually.
If you need to change it manually make sure nymea is shut down before.


Example devices.conf file:

```text
[DeviceConfig]
%7B25fbd68c-1136-462b-9c0c-18797c11660f%7D\Params\%7B866e8d6a-953f-4bdc-8d85-8d92e51e8592%7D\type=10
%7B25fbd68c-1136-462b-9c0c-18797c11660f%7D\Params\%7B866e8d6a-953f-4bdc-8d85-8d92e51e8592%7D\value=
%7B25fbd68c-1136-462b-9c0c-18797c11660f%7D\Params\%7B89629008-6ad8-4e92-863d-b86e0e012d0b%7D\type=2
%7B25fbd68c-1136-462b-9c0c-18797c11660f%7D\Params\%7B89629008-6ad8-4e92-863d-b86e0e012d0b%7D\value=-1964425326
%7B25fbd68c-1136-462b-9c0c-18797c11660f%7D\Params\%7Baa1158f7-b451-456a-840f-4f0c63b2b7f0%7D\type=10
%7B25fbd68c-1136-462b-9c0c-18797c11660f%7D\Params\%7Baa1158f7-b451-456a-840f-4f0c63b2b7f0%7D\value=
%7B25fbd68c-1136-462b-9c0c-18797c11660f%7D\Params\%7Be760f92b-8fca-4f20-aead-a52045505b81%7D\type=10
%7B25fbd68c-1136-462b-9c0c-18797c11660f%7D\Params\%7Be760f92b-8fca-4f20-aead-a52045505b81%7D\value=
%7B25fbd68c-1136-462b-9c0c-18797c11660f%7D\autoCreated=true
%7B25fbd68c-1136-462b-9c0c-18797c11660f%7D\deviceClassId={fce5247f-4c6d-408f-ac62-e5973dc6adfa}
%7B25fbd68c-1136-462b-9c0c-18797c11660f%7D\devicename=Bedroom
%7B25fbd68c-1136-462b-9c0c-18797c11660f%7D\parentid={6d15a39c-95c6-4af2-9036-3ecbedbc7c8c}
%7B25fbd68c-1136-462b-9c0c-18797c11660f%7D\pluginid={cd758269-dbbb-4ef0-80ab-48bd9a8a2765}
%7B6d15a39c-95c6-4af2-9036-3ecbedbc7c8c%7D\Params\%7Ba54b98b4-b78f-41dd-a257-14425c6cf9ab%7D\type=10
%7B6d15a39c-95c6-4af2-9036-3ecbedbc7c8c%7D\Params\%7Ba54b98b4-b78f-41dd-a257-14425c6cf9ab%7D\value=10.0.0.8
%7B6d15a39c-95c6-4af2-9036-3ecbedbc7c8c%7D\Params\%7Bab1a0be8-e3a5-4f95-b9b7-893de1ca4cf7%7D\type=10
%7B6d15a39c-95c6-4af2-9036-3ecbedbc7c8c%7D\Params\%7Bab1a0be8-e3a5-4f95-b9b7-893de1ca4cf7%7D\value=HEOS Drive
%7B6d15a39c-95c6-4af2-9036-3ecbedbc7c8c%7D\Params\%7Bf796664d-6cb7-4f29-9d05-771968d82a32%7D\type=10
%7B6d15a39c-95c6-4af2-9036-3ecbedbc7c8c%7D\Params\%7Bf796664d-6cb7-4f29-9d05-771968d82a32%7D\value=apt12171001894
%7B6d15a39c-95c6-4af2-9036-3ecbedbc7c8c%7D\autoCreated=false
%7B6d15a39c-95c6-4af2-9036-3ecbedbc7c8c%7D\deviceClassId={28bbf4c6-dfd8-4d9d-aa27-5daf2c25d63c}
%7B6d15a39c-95c6-4af2-9036-3ecbedbc7c8c%7D\devicename=HEOS Drive
%7B6d15a39c-95c6-4af2-9036-3ecbedbc7c8c%7D\pluginid={cd758269-dbbb-4ef0-80ab-48bd9a8a2765}
```

UUIDS are limited by %7B for "{" and %7D for "}", the first UUID is the device UUID that is unique for that particular device.
The example files has 2 devices _6d15a39c-95c6-4af2-9036-3ecbedbc7c8c_ and _25fbd68c-1136-462b-9c0c-18797c11660f_. The first device is the parent of the second one.

!!! Note
    A device UUID is not a device class id, it is create during the device setup.

### deviceName

The device name is defined during device setup and can be altered any time.

### deviceClassId

The deviceClassId is defined in the plug-in JSON file, and is an unique identifier of the device class/type.

### pluginId

The plug-in id is defined in the plug-in JSON file.

### autoCreated

An auto created device cannot be deleted manually

### parentId

If a parentId is set, the device will be deleted when the parent is deleted.
Example a gateway might be the parent of a light bulb. Or an account might be the parent of a device

### Params

Params and params ids are definded in the plug-in JSON file.

## Rules configuration file

Each rule beginns with a rule uuid, like [%7Bc7f72b5c-15e0-4519-9fbd-bbf2882f1631%7D].

### name

The rule display name.

### executable

Defines if the rule can be triggered manually. Rules that can be triggered manually are called scenes.

### enabled

Enables or disables the rule.

### events

Events that trigger the rule.

### stateEvaluator

States that get evaluated.

### timeDescriptor

.

### ruleAction

Action that will be triggered if the rule gets activated.
