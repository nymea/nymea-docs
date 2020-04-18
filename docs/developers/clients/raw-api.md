---
id: rawapi
title: The nymea JSON-RPC API
---

## Introduction

nymea offers a JSON-RPC based API to build client applications. This API is exposed in different ways on the nymea:core instance. The available options are plain TCP sockets or WebSocket based communication, both either plaintext or SSL encrypted. In the default configuration, nymea will expose the API via a SSL enabled TCP socket on port 2222 and an SSL enabled WebSocket on port 4444. However, a nymea:core instance can be configured with any combination of these. The interfaces can be described using URLs:

### Plaintext nymea TCP sockets
Plaintext nymea TCP sockets are described in nymea via the URL schema `nymea://`. For instance `telnet` or `ncat` can be used to communicatte with those. Establishing a standdard TCP connection to such a service is enough to communicate with the server. An example URL would be

    nymea://192.168.0.10:2222

### SSL encrypted nymea TCP sockets
SSL encrypted nymea TCP sockets are described in nymea via the URL schema `nymeas://`. In principle they behave the same as `nymea://` sockets, but require a valid SSL handshake to be performed before any communication can happen. For testing purposes, `ncat --ssl` can be used to talk to the server. An example URL would be

    nymeas://192.168.0.10:2222

### Plaintext websockets
Plaintext websockets follow the registered URL schema for websockets of `ws://`. A valid websockets handshake is required on those interfaces before any communication can happen. An example URL would be

    ws://192.168.0.10:4444

### SSL encrypted websockets
Like plaintext websockets they follow the registered URL schema for secure websockets of `wss://`. Both, a valid SSL handshake as well as a valid websocket handshake need to be performed before communicating with the server. An example URL would be

    wss://192.168.0.10:4444

### SSL Certificates
Given the typical installation of a nymea setup is in a local network, most nymea instances will use a self signed SSL certificate. A client implementation can not expect a publicly signed SSL certificate from the server. Because of this, it is highly recommended to use certificate pinning when implementing nymea clients to keep the security level up to expectations. That means, the first time the user connects to a new instance, an informational message should be displayed to the user. Once the user accepts this certificate, the fingerprint should be stored and in *all* subsequent connection attempts, the certificate provided by nymea should be checked against the locally storedd fingerprint and made sure it did not change. If it did change, the user shall be warned about that.

## Discovering nymea API interfaces in the network

nymea can be discovered in the local network by using either **UPnP 1.1** ([Universal Plug and Play](https://en.wikipedia.org/wiki/Universal_Plug_and_Play)) network discovery or **Zeroconf** (mDNS/DNS-SD).

### UPnP

The server will present itself as [UPnP Basic 1.0](http://upnp.org/specs/basic/basic1/) device according to the following specifications:

http://upnp.org/specs/basic/UPnP-basic-Basic-v1-Device.pdf

A detailed documentation of the UPnP device architecture can be found here:

http://upnp.org/specs/arch/UPnP-arch-DeviceArchitecture-v1.1.pdf

#### Network Discovery with UPnP

Once nymea is started, it can be discovered over the [Simple Service Discovery Protocol](https://en.wikipedia.org/wiki/Simple_Service_Discovery_Protocol) (SSDP). A client can perform a discovery by binding to the UDP multicast address `239.255.255.250` on port `1900`.

In order to search for UPnP devices in the network a client can send following message to the UPD multicast socket:

    M-SEARCH * HTTP/1.1
    HOST:239.255.255.250:1900
    MAN:"ssdp:discover"
    MX:4
    ST: ssdp:all

> **Note:** use `\r\n` at the end of each line and twice at the end of the message.

Each UPnP device in the network will respond to the SSDP search message with a *HTTP/1.1* message. The nymead server response will look like this:

    HTTP/1.1 200 OK
    Cache-Control: max-age=1900
    DATE: Mon, 12 Oct 2015 09:39:36 GMT
    EXT:
    CONTENT-LENGTH:0
    Location: http://10.10.10.50:80/server.xml
    Server: nymea/0.9.0 UPnP/1.1
    ST:upnp:rootdevice
    USN:uuid:81d520cd-90cd-422d-9cbb-a0287e467e79::urn:schemas-upnp-org:device:Basic:1
    
From this message, the `Location` header can be used to get information about the remote system. Fetching the URL using a HTTP GET command will deliver an XML document as specified by UPnP which can be examined to determine if the remote system is a nymea:core instance. For instance

    GET http://10.10.10.50:80/server.xml

on a nymea:core instance will return this XML document:

    <?xml version="1.0" encoding="UTF-8"?>
    <root xmlns="urn:schemas-upnp-org:device-1-0">
        <specVersion>
            <major>1</major>
            <minor>1</minor>
        </specVersion>
        <device>
            <presentationURL>http://10.10.10.45:80</presentationURL>
            <deviceType>urn:schemas-upnp-org:device:Basic:1</deviceType>
            <friendlyName>nymea Pi4</friendlyName>
            <manufacturer>nymea GmbH</manufacturer>
            <manufacturerURL>http://nymea.io</manufacturerURL>
            <modelDescription>IoT server</modelDescription>
            <modelName>nymead</modelName>
            <modelNumber>0.18.1+202001232205~buster+rpi1</modelNumber>
            <modelURL>http://nymea.io</modelURL>
            <UDN>uuid:8c566f13-d231-420e-b6cf-e3e810d0cc42</UDN>
            <iconList>
                <icon>
                    <mimetype>image/png</mimetype>
                    <width>8</width>
                    <height>8</height>
                    <depth>8</depth>
                    <url>/icons/nymea-logo-8x8.png</url>
                </icon>
            </iconList>
            <serviceList>
                <service>
                    <serviceType>urn:nymea.io:service:wss:1</serviceType>
                    <serviceId>urn:nymea.io:serviceId:wss:1</serviceId>
                    <SCPDURL>wss://10.10.10.45:4444</SCPDURL>
                </service>
                <service>
                    <serviceType>urn:nymea.io:service:wss:1</serviceType>
                    <serviceId>urn:nymea.io:serviceId:wss:1</serviceId>
                    <SCPDURL>ws://10.10.10.45:4445</SCPDURL>
                </service>
                <service>
                    <serviceType>urn:nymea.io:service:nymeas:1</serviceType>
                    <serviceId>urn:nymea.io:serviceId:nymeas:1</serviceId>
                    <SCPDURL>nymeas://10.10.10.45:2223</SCPDURL>
                </service>
                <service>
                    <serviceType>urn:nymea.io:service:nymea:1</serviceType>
                    <serviceId>urn:nymea.io:serviceId:nymea:1</serviceId>
                    <SCPDURL>nymea://10.10.10.45:2222</SCPDURL>
                </service>
            </serviceList>
        </device>
    </root>

   
The `modelName` value of the device description can be used to determin if the remote system is actually a nymea:core instance by comparing it to the value `nymead`. Once the service is known to be a nymea:core instance, the `serviceList` can be examined to find all the exposed API interfaces of this nymea:core instance. In the above example, the nymea:core offers its API on 4 interfaces:

* A plaintext web socket on port 4445
* A plaintext nymea TCP socket on port 2222
* An SSL encrypted web socket on port 4444
* An SSL encrypted nymea TCP socket on port 2223


### Zeroconf

nymea advertises its services via [Zeroconf](https://en.wikipedia.org/wiki/Zero-configuration_networking) and can be discovered using mDNS discovery. The used service types are 

* `_jsonrpc._tcp`: For nymea TCP socket based interfaces
* `_ws._tcp`: For websocket based interfaces

The field `sslEnabled` in the `txt` record should be examined to determine whether the interface is using SSL encryption or not. The `port` and `address` records provide information on the connection parameters.


#### Network discovery with Avahi

[Avahi](https://www.avahi.org) is an open source Zeroconf implementation. Assuming you have `avahi-discover` and `avahi-utils` installed, you can run following command in order to search for nymea systems in your network:

    $ avahi-browse -arl | grep -P '^=' -A 4 | grep "IPv4 nymea-" -A 4

    
    =  wlan0 IPv4 nymea-tcp-default                             _jsonrpc._tcp        local
       hostname = [nymea.local]
       address = [10.10.10.121]
       port = [2222]
       txt = ["uuid={c82f7b33-d283-44f0-85df-6e7992dcf9e6}" "name=nymea" "sslEnabled=false" "jsonrpcVersion=1.4" "manufacturer=nymea GmbH" "serverVersion=0.9.0"]
    
    =  wlan0 IPv4 nymea-ws-default                              _ws._tcp             local
       hostname = [nymea.local]
       address = [10.10.10.121]
       port = [4444]
       txt = ["uuid={c82f7b33-d283-44f0-85df-6e7992dcf9e6}" "name=nymea" "sslEnabled=false" "jsonrpcVersion=1.4" "manufacturer=nymea GmbH" "serverVersion=0.9.0"]

## Communicating with the API

Once a conection to nymea:core has been established using one of the above transports, the message exchange format is the same for all transports, using JSON based messages. With the exception of notifications all messages follow a request/reply pattern. The client sends a command to nymea:core and receives a reply containing the response. Please note that every message must be followed by a newline (`\n`) character.

### Requests

The basic message format of a request sent from the client to nymea:core follows this format:

    {
        "id": integer,
        "method": "Namespace.Method",
        "token": "string",
        "params": {...}
    }

Every request *must* provide at least `id` and `method`. The `id` should be unique for every call. The `method` entry determines the actual method to be called from nymea's API. Depending on the actual method, `params` might or might not be required. The documentation for each method provides information regarding the params content.


In addition, depending on whether authentication is enabled on a particular interface, a `token` might be required in order for nymea:core to accept the request.

### Responses
If nymea:core accepts a request, it will reply with a response following this format:

    {
        "id": integer,
        "status": "string",
        "params": {...},
        "error": "string",
    }

Whenever replying to a request, nymea:core will fill in the same `id` as the request contained. A client may use this `id` to match a given response to the request it had sent to nymea:core earlier. The `status` field always contains either `success`, `error` or `unauthorized`. If the request passed validation, this will be set to `success`, otherwise, for instance if the used method has not been found, this will contain `error` or `unauthorized` if a client is not allowed to call a certain method. In case of success, the response will contain an additional field `params` conaining the response params. The actual content again depends on the acutal called method in the request. In case of failure, instead of params, the response will contain an `error` field with a message that might help the client developer to determine the source of the problem. This error message will always indicate a program error and should not be presented to the user.

### The initial handshake

Every new connection is required to send the initial handshake message to nymea. The handshake message looks like this:

    {
        "id": 0,
        "method": "JSONRPC.Hello",
        "params": {
            "locale": "de_DE"
        }
    }
    
As any other message, also the handshake message is required to have an `id`. The method for the handshake is `JSONRPC.Hello`. Additionally, `params` might be included to configure the connection parameters for this connection. At this point, only the `locale` parameter is supported which will cause nymea:core to translate strings to be displayed to the user into the given langauge.


nymea:core will reply with this message:

    {
        "id":0,
        "params": {
            "authenticationRequired":false,
            "initialSetupRequired":false,
            "locale":"de_DE",
            "name":"nymea Pi4",
            "protocol version":"4.1",
            "pushButtonAuthAvailable":false,
            "server":"nymea",
            "uuid":"{8c566f13-d231-420e-b6cf-e3e810d0cc42}",
            "version":"0.18.1+202001232205~buster+rpi1"
        },
        "status":"success"
    }

As specified in the basic message protocol, the response will contain the same `id` as the `Hello` request. Given a valid request, the `status` parameter contains `success` and the `Hello` method response contains the following parameters:
 * `authenticationRequired` indicates whether or not authentication is required for all further communication. If this field is set to true, any subsequent call must include a valid `token` in any call.
 * `initialSetupRequired` indicates whether this nymea:core instance is being set up initially. If this field is set to true, the initial setup procedure by creating a new user needs to be performed.
 * `locale` indicates the locale for this connections. If the Hello command requested a certain locale, this will reflect that request if possible. In case the request did not specify a locale, this will indicate what the default on the nymea:core system is set to.
 * `name` indicates the user displayable name of this nymea:core instance.
 * `protocol version` indicates the nymea JSON-RPC version of this nymea:core instance.
 * `pushButtonAuthAvailable`indicates whether or not a push button flow is available for user authentication.
 * `server` will always be set to `nymea` unless product branding dictates anything different.
 * `uuid` contains the UUID of this nymea:core instance.
 * `version` contains the build version of this instance.
    
### Introspecting the API

The nymea:core JSON-RPC API is introspectable. That means, the API documentation for the API can be obtained through the API itself. For that, the `JSONRPC.Introspect` method is used. The introspection method does not take any parameters. Hence the request looks like this:

    {
        "id": 1,
        "method": "JSONRPC.Introspect`
    }
    
nymea will reply with the entire API documentation. The structure of the introsection response is of the following format:

    {
        "id":1,
        "params":{
            "enums":{ ... },
            "flags": { ... },
            "objects": { ... },
            "methods": { ... },
            "notificattions": { ... }
        },
        "status": "success"
    }

    
#### enums
The enums map contains a list of enumeration types and their possible values. For example
    
    "CreateMethod": [
        "CreateMethodUser",
        "CreateMethodAuto",
        "CreateMethodDiscovery"
    ]

This defines an enumeration type of name `CreateMethod`. Wherever the API description indicates the presence of an entry of this type by stating `$ref:CreateMethod`, an actual call would contain *one of* the possible values in that place. For example, if the introspection describes this entry:

    "createMethod": "$ref:CreateMethod"
    
the actual entry in method call would look something like this:

    "createMethod": "CreateMethodUser"

#### flags
The flags map contains a list of flag types and their possible values. For example

    "CreateMethods":[
        "$ref:CreateMethod"
    ]

This defines a flag of type `CreateMethods`. Whenever the API description indicates the presence of an entry of this type by stating `$ref:CreateMethods`, an actual call would contain *multiple* pf the possible values. For example, if the introspection describes this entry:

    "createMethods": "$ref:CreateMethods"
    
the actual entry in the method call would look something like this:

    "createMethods": ["CreateMethodUser", "CreateMethodDiscovery" ]

    
#### objects
The objects map contains a list of object tpyes to be used in the API. For example

    "Vendor": {
        "id":"Uuid",
        "name":"String",
        "displayName":"String"
    }
    
This defines an object of type `Vendor`. Whenever the API description indicates the presence of an entry of this type by stating `$ref:Venddor`, an actual call would contain the full object of this type. For example, if the introspection describes this entry:

    "vendor": "$ref:Vendor"
    
the actual entry in the method call would look something like this:

    "vendor": {
        "id": "8c566f13-d231-420e-b6cf-e3e810d0cc42",
        "name": "nymea",
        "displayName": "nymea GmbH"
    }
    
#### methods
This object map contains the list of available methods to call on the API. For example

    "JSONRPC.Introspect": {
        "description": "Introspect this API.",
        "params": {},
        "returns": {
            "methods": "Object",
            "notifications": "Object",
            "enums": "Object",
            "flags": "Object",
            "objects": "Object"
        }
    }

This defines the method `JSONRPC.Introspect` on the API. It describes the required `params` (in this case none) as well as the return value in it's `returns` property.

#### notifications

This defines the available notifications on this interface. A client can subscribe to notifications of a given namespace using the `JSONRPC.SetNotificationsEnabled` call. Once notifications have been enabled, nymea:core will send such messages to the client without the need of the client actively polling. For example:

    "Devices.DeviceAdded": {
        "description": "Emitted whenever a Device was added.",
        "params": {
            "device": "$ref:Device"
        }
    }
    
Using `JSONRPC.SetNotificationsEnabled` to enable notifications for the `Devices` namespace would cause nymea:core to send this notification to the client whenever a new device is added to the system. The actual notification will look something like this:

    {
        "id":13666,
        "notification":"Devices.DeviceAdded",
        "params":{ ... }
    }

#### read-only, optional and deprecated entries

Every entry in the API can have modifiers attached. Those modifiers can be `r:` for "read-only", `o:` for "optional" and `d:` for "deprecated". For example:

    "SomeObject": {
        "property1": "bool",
        "r:property2": "bool",
        "o:property3": "bool",
        "d:property4": "bool",
        "o:d:property5": "bool"
        
    }
    
In this example `property1` has no modifiers. When a method returns an entry of this type, it will include `property1`. When a method takes an entry of this type in its params, the client must include `propertty1` in its request params.

`property2` is marked as read-only. That means, when a method returns an entry of this type, it will contain `property2`, however, when a method takes an entry of this type in its params, the client must not include this property in the request params. Read-only properties can only obtained from nymea:core, but never written to them.

`property3` is marked as optional. This means, when a method returns an entry of this type, it may or may not contain `property3`. When a method takes an entry of this object in its params, the client may or may not include this property in the request params.

`property4` is marked as deprecated. This means, when a method returns an entry of this type, it will include `property4`, however, developers are strongly adviced to not rely on it any more because it may disappear in the next major version of the API. When a method takes an entry of this object in its params, the client must still include it in the request parameters, but be prepared that a future update of the API will not support this any more and reject the call. The `protocol version` field in the initial handshake message may be used to determine if a property is to be included in a call or not.

Properties may have multiple modifiers at the same time, as `property5` shows.


## Authentication

Nymea can be configured to require authentication on the API (by default, authentication is enabled). The initial handshake will inform the client whether authentication is required or not through the `authenticationRequired` field. If authentication is required, each call, except `JSONRPC.Hello`, `JSONRPC.Introspect`, `Users.Authenticate` and `Users.RequestPushButtonAuth` are required to contain a valid authentication token. The token is added to the method parameters on the topmost level. A method call package follows this format:

    {
        "id": "Int",
        "method": "String",
        "o:token": "String",
        "o:params": "Object"
    }

`token` is marked as optional because it is might not be required for servers configured to not require authentication. However, if the token is not included on a server that does require quthentication, the response will indicate a failure like this:

    {
        "id": "...",
        "status": "unauthorized"
    }
    
### Creating users

Currently, nymea only supports a single user. When a fresh nymea system is started up, there will be no user. This is indicated in the initial handshake through the `initialSetupRequired` property. In this case, a client cannot authenticate to the API yet. Instead a one-time setup needs to be performed by calling `Users.CreateUser`. A user can be created by providing a valid email address to the `username` field, a valid password in the `password` field. A password is valid if it fulfills the minimum password requirements which are enforce a minimum length of 8 characters, the use of uppercase and lowercase characters, as well as numbers.

    {
        "id": 1,
        "method": "Users.CreateUser",
        "params": {
            "username": "a.valid@email.org",
            "password": "Upper,lower and a 1"
        }
    }

Once `Users.CreateUser` succeeded, the `initialSetupRequired` property in the handshake will turn to false. As of this point, `Users.CreateUser` can not be called any more as long as multi-user is not supported in nymea.

### Obtaining a token

A token is obtained by calling `Users.Authenticate` using username/password authentication or `Users.RequestPushButtonAuth` if the push button authentication is available.

#### Username and password

Authenticating via user and password requires the presence of a user in the system. The authenticate call requires the client to provide `username` and `password` in the call parameters as well as a `deviceName` parameter which is used to present this login to the user. Hence, the device name should be a user displayable indicating the user as clear as possible who logged it. A good example for this would be "nymea:app on Steve's iPhone". A bad example for this would be "device-1342".

    {
        "id": 1,
        "method": "Users.Authenticate`,
        "params": {
            "username": "a.valid@email.org",
            "password": "...",
            "deviceName": "my client device"
        }
    }
    
If authentication succeeds, the call will return a token that can be used to all subsequent calls. For instance:

    {
        "id": 1,
        "status": "success",
        "params": {
            "success": "true",
            "token": "NGE4ZTRjOWQtMjdiNi00ZDk0LTljOTYtOWRmNjkwYzY1MDNlCg=="
        }
    }
    
In the case of authentication failure, the response would look like this:

    {
        "id": 1,
        "status": "success",
        "params": {
            "success": "false"
        }
    }

Note, the top level `status` property indicates success because the server did understand and process the request. However, the `success` property in the return value `params` object indicates the authentication failure and the token is missing. The `Authenticate` method is scarse on details by design. There is only a boolean flag for "success" because a potential attacker should not get more than the absolute minimum required about the failure.

#### Push button

If push button authentication is available, in addition to the username and password authentication, `Users.RequestPushButtonAuth` is available.

Note: It requires hardware support for push button authentication. For development purposes a fake push button module is provided in the nymea source repository in the tests/tools/simplepushbuttonhandler/ directory. Starting that utility will simulate the presence of a push button and allow "pressing the button" pressing the space bar on the keyboard.

The request looks like this:

    {
        "id": 1,
        "method": "Users.RequestPushButtonAuth",
        "deviceName": "my cool device"
    }
    
The `deviceName` property serves the same purpose as in the user/password authentication case.

When requesting push button authentication, nymea:core will immediately reply with with the status message and - in case everything is fine - a transaction id.

    {
        "id": 1,
        "status": "success",
        "params": {
            "transactionId": "627f091d-06f0-4d17-b316-def225ddae25"
        }
    }


Then it will start listening for button presses. If the button is pressed within the timeout (30 seconds), the API will emit a notification to the client requesting the authentication containing the transaction id and an access token.

    {
        "id": 2,
        "notification": "Users.PushButtonAuthFinished",
        "params": {
            "success": true,
            "transactionId": "627f091d-06f0-4d17-b316-def225ddae25",
            "token": "NGE4ZTRjOWQtMjdiNi00ZDk0LTljOTYtOWRmNjkwYzY1MDNlCg=="
        }
    }
    
Note: If a client requests push button authentication while another client has already started it, or the same client requests a new push button transaction before a previous one is finished. All previous attempts will be cancelled by a `PushButtonAuthFinished` notification with a non-successful status.

If the user does not press the push button on within the timeout, the `PushButtonAuthFinished` notification with a non-successful status.


## The complete API


In the following section you can find a detailed description of the current API version **4.2**.

 * [Enums](#enums)
 * [Flags](#flags)
 * [Types](#types)
 * [Methods](#methods)
 * [Notifications](#notifications)


------------------------------
### Enums

 * [BasicType](#basictype)
 * [BrowserIcon](#browsericon)
 * [CloudConnectionState](#cloudconnectionstate)
 * [ConfigurationError](#configurationerror)
 * [CreateMethod](#createmethod)
 * [DeviceError](#deviceerror)
 * [DeviceSetupStatus](#devicesetupstatus)
 * [InputType](#inputtype)
 * [LoggingError](#loggingerror)
 * [LoggingEventType](#loggingeventtype)
 * [LoggingLevel](#logginglevel)
 * [LoggingSource](#loggingsource)
 * [MediaBrowserIcon](#mediabrowsericon)
 * [NetworkDeviceState](#networkdevicestate)
 * [NetworkManagerError](#networkmanagererror)
 * [NetworkManagerState](#networkmanagerstate)
 * [RemovePolicy](#removepolicy)
 * [RepeatingMode](#repeatingmode)
 * [RuleError](#ruleerror)
 * [ScriptError](#scripterror)
 * [ScriptMessageType](#scriptmessagetype)
 * [SetupMethod](#setupmethod)
 * [StateOperator](#stateoperator)
 * [TagError](#tagerror)
 * [Unit](#unit)
 * [UserError](#usererror)
 * [ValueOperator](#valueoperator)
------------------------------
#### BasicType

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



------------------------------
#### BrowserIcon

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



------------------------------
#### CloudConnectionState

      [
          "CloudConnectionStateDisabled", 
          "CloudConnectionStateUnconfigured", 
          "CloudConnectionStateConnecting", 
          "CloudConnectionStateConnected"
      ]



------------------------------
#### ConfigurationError

      [
          "ConfigurationErrorNoError", 
          "ConfigurationErrorInvalidTimeZone", 
          "ConfigurationErrorInvalidStationName", 
          "ConfigurationErrorInvalidId", 
          "ConfigurationErrorInvalidPort", 
          "ConfigurationErrorInvalidHostAddress", 
          "ConfigurationErrorBluetoothHardwareNotAvailable", 
          "ConfigurationErrorInvalidCertificate"
      ]



------------------------------
#### CreateMethod

      [
          "CreateMethodUser", 
          "CreateMethodAuto", 
          "CreateMethodDiscovery"
      ]



------------------------------
#### DeviceError

      [
          "DeviceErrorNoError", 
          "DeviceErrorPluginNotFound", 
          "DeviceErrorVendorNotFound", 
          "DeviceErrorDeviceNotFound", 
          "DeviceErrorDeviceClassNotFound", 
          "DeviceErrorActionTypeNotFound", 
          "DeviceErrorStateTypeNotFound", 
          "DeviceErrorEventTypeNotFound", 
          "DeviceErrorDeviceDescriptorNotFound", 
          "DeviceErrorMissingParameter", 
          "DeviceErrorInvalidParameter", 
          "DeviceErrorSetupFailed", 
          "DeviceErrorDuplicateUuid", 
          "DeviceErrorCreationMethodNotSupported", 
          "DeviceErrorSetupMethodNotSupported", 
          "DeviceErrorHardwareNotAvailable", 
          "DeviceErrorHardwareFailure", 
          "DeviceErrorAuthenticationFailure", 
          "DeviceErrorDeviceInUse", 
          "DeviceErrorDeviceInRule", 
          "DeviceErrorDeviceIsChild", 
          "DeviceErrorPairingTransactionIdNotFound", 
          "DeviceErrorParameterNotWritable", 
          "DeviceErrorItemNotFound", 
          "DeviceErrorItemNotExecutable", 
          "DeviceErrorUnsupportedFeature", 
          "DeviceErrorTimeout"
      ]



------------------------------
#### DeviceSetupStatus

      [
          "DeviceSetupStatusNone", 
          "DeviceSetupStatusInProgress", 
          "DeviceSetupStatusComplete", 
          "DeviceSetupStatusFailed"
      ]



------------------------------
#### InputType

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



------------------------------
#### LoggingError

      [
          "LoggingErrorNoError", 
          "LoggingErrorLogEntryNotFound", 
          "LoggingErrorInvalidFilterParameter"
      ]



------------------------------
#### LoggingEventType

      [
          "LoggingEventTypeTrigger", 
          "LoggingEventTypeActiveChange", 
          "LoggingEventTypeEnabledChange", 
          "LoggingEventTypeActionsExecuted", 
          "LoggingEventTypeExitActionsExecuted"
      ]



------------------------------
#### LoggingLevel

      [
          "LoggingLevelInfo", 
          "LoggingLevelAlert"
      ]



------------------------------
#### LoggingSource

      [
          "LoggingSourceSystem", 
          "LoggingSourceEvents", 
          "LoggingSourceActions", 
          "LoggingSourceStates", 
          "LoggingSourceRules", 
          "LoggingSourceBrowserActions"
      ]



------------------------------
#### MediaBrowserIcon

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
          "MediaBrowserIconSoundCloud"
      ]



------------------------------
#### NetworkDeviceState

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



------------------------------
#### NetworkManagerError

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
          "NetworkManagerErrorNetworkManagerNotAvailable"
      ]



------------------------------
#### NetworkManagerState

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



------------------------------
#### RemovePolicy

      [
          "RemovePolicyCascade", 
          "RemovePolicyUpdate"
      ]



------------------------------
#### RepeatingMode

      [
          "RepeatingModeNone", 
          "RepeatingModeHourly", 
          "RepeatingModeDaily", 
          "RepeatingModeWeekly", 
          "RepeatingModeMonthly", 
          "RepeatingModeYearly"
      ]



------------------------------
#### RuleError

      [
          "RuleErrorNoError", 
          "RuleErrorInvalidRuleId", 
          "RuleErrorRuleNotFound", 
          "RuleErrorDeviceNotFound", 
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



------------------------------
#### ScriptError

      [
          "ScriptErrorNoError", 
          "ScriptErrorScriptNotFound", 
          "ScriptErrorInvalidScript", 
          "ScriptErrorHardwareFailure"
      ]



------------------------------
#### ScriptMessageType

      [
          "ScriptMessageTypeLog", 
          "ScriptMessageTypeWarning"
      ]



------------------------------
#### SetupMethod

      [
          "SetupMethodJustAdd", 
          "SetupMethodDisplayPin", 
          "SetupMethodEnterPin", 
          "SetupMethodPushButton", 
          "SetupMethodUserAndPassword", 
          "SetupMethodOAuth"
      ]



------------------------------
#### StateOperator

      [
          "StateOperatorAnd", 
          "StateOperatorOr"
      ]



------------------------------
#### TagError

      [
          "TagErrorNoError", 
          "TagErrorDeviceNotFound", 
          "TagErrorRuleNotFound", 
          "TagErrorTagNotFound"
      ]



------------------------------
#### Unit

      [
          "UnitNone", 
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
          "UnitMicroSiemensPerCentimeter", 
          "UnitDuration"
      ]



------------------------------
#### UserError

      [
          "UserErrorNoError", 
          "UserErrorBackendError", 
          "UserErrorInvalidUserId", 
          "UserErrorDuplicateUserId", 
          "UserErrorBadPassword", 
          "UserErrorTokenNotFound", 
          "UserErrorPermissionDenied"
      ]



------------------------------
#### ValueOperator

      [
          "ValueOperatorEquals", 
          "ValueOperatorNotEquals", 
          "ValueOperatorLess", 
          "ValueOperatorGreater", 
          "ValueOperatorLessOrEqual", 
          "ValueOperatorGreaterOrEqual"
      ]



------------------------------
### Flags

 * [CreateMethods](#createmethods)
------------------------------
##### CreateMethods


      [
          "$ref:CreateMethod"
      ]


See also: [CreateMethod](#createmethod)

------------------------------
### Types

 * [Action](#action)
 * [ActionType](#actiontype)
 * [ActionTypes](#actiontypes)
 * [BrowserItem](#browseritem)
 * [CalendarItem](#calendaritem)
 * [CalendarItems](#calendaritems)
 * [Device](#device)
 * [DeviceClass](#deviceclass)
 * [DeviceClasses](#deviceclasses)
 * [DeviceDescriptor](#devicedescriptor)
 * [DeviceDescriptors](#devicedescriptors)
 * [DevicePlugin](#deviceplugin)
 * [DevicePlugins](#deviceplugins)
 * [Devices](#devices)
 * [Event](#event)
 * [EventDescriptor](#eventdescriptor)
 * [EventDescriptors](#eventdescriptors)
 * [EventType](#eventtype)
 * [EventTypes](#eventtypes)
 * [Experience](#experience)
 * [LogEntries](#logentries)
 * [LogEntry](#logentry)
 * [MqttPolicy](#mqttpolicy)
 * [Package](#package)
 * [Packages](#packages)
 * [Param](#param)
 * [ParamDescriptor](#paramdescriptor)
 * [ParamDescriptors](#paramdescriptors)
 * [ParamList](#paramlist)
 * [ParamType](#paramtype)
 * [ParamTypes](#paramtypes)
 * [RepeatingOption](#repeatingoption)
 * [Repositories](#repositories)
 * [Repository](#repository)
 * [Rule](#rule)
 * [RuleAction](#ruleaction)
 * [RuleActionParam](#ruleactionparam)
 * [RuleActionParams](#ruleactionparams)
 * [RuleActions](#ruleactions)
 * [RuleDescription](#ruledescription)
 * [Rules](#rules)
 * [Script](#script)
 * [Scripts](#scripts)
 * [ServerConfiguration](#serverconfiguration)
 * [State](#state)
 * [StateDescriptor](#statedescriptor)
 * [StateEvaluator](#stateevaluator)
 * [StateEvaluators](#stateevaluators)
 * [StateType](#statetype)
 * [StateTypes](#statetypes)
 * [States](#states)
 * [Tag](#tag)
 * [Tags](#tags)
 * [TimeDescriptor](#timedescriptor)
 * [TimeEventItem](#timeeventitem)
 * [TimeEventItems](#timeeventitems)
 * [TokenInfo](#tokeninfo)
 * [TokenInfoList](#tokeninfolist)
 * [UserInfo](#userinfo)
 * [Vendor](#vendor)
 * [Vendors](#vendors)
 * [WebServerConfiguration](#webserverconfiguration)
 * [WiredNetworkDevice](#wirednetworkdevice)
 * [WirelessAccessPoint](#wirelessaccesspoint)
 * [WirelessNetworkDevice](#wirelessnetworkdevice)
------------------------------
##### Action

      {
          "actionTypeId": "Uuid", 
          "deviceId": "Uuid", 
          "o:params": "$ref:ParamList"
      }

See also: [ParamList](#paramlist)

------------------------------
##### ActionType

      {
          "displayName": "String", 
          "index": "Int", 
          "name": "String", 
          "paramTypes": "$ref:ParamTypes", 
          "r:id": "Uuid"
      }

See also: [ParamTypes](#paramtypes)

------------------------------
##### ActionTypes

      [
          "$ref:ActionType"
      ]

See also: [ActionType](#actiontype)

------------------------------
##### BrowserItem

      {
          "actionTypeIds": [
              "Uuid"
          ], 
          "browsable": "Bool", 
          "description": "String", 
          "disabled": "Bool", 
          "displayName": "String", 
          "executable": "Bool", 
          "icon": "$ref:BrowserIcon", 
          "id": "String", 
          "o:mediaIcon": "$ref:MediaBrowserIcon", 
          "thumbnail": "String"
      }

See also: [MediaBrowserIcon](#mediabrowsericon), [BrowserIcon](#browsericon)

------------------------------
##### CalendarItem

      {
          "duration": "Uint", 
          "o:datetime": "Uint", 
          "o:repeating": "$ref:RepeatingOption", 
          "o:startTime": "Time"
      }

See also: [RepeatingOption](#repeatingoption)

------------------------------
##### CalendarItems

      [
          "$ref:CalendarItem"
      ]

See also: [CalendarItem](#calendaritem)

------------------------------
##### Device

      {
          "d:r:setupComplete": "Bool", 
          "o:name": "String", 
          "o:settings": "$ref:ParamList", 
          "r:deviceClassId": "Uuid", 
          "r:id": "Uuid", 
          "r:o:parentId": "Uuid", 
          "r:o:setupDisplayMessage": "String", 
          "r:params": "$ref:ParamList", 
          "r:setupError": "$ref:DeviceError", 
          "r:setupStatus": "$ref:DeviceSetupStatus", 
          "r:states": "$ref:States"
      }

> **Warning**: following values are deprecated and will be removed with the next major API version: `r:setupComplete`

See also: [States](#states), [ParamList](#paramlist), [ParamList](#paramlist), [DeviceError](#deviceerror), [DeviceSetupStatus](#devicesetupstatus)

------------------------------
##### DeviceClass

      {
          "r:actionTypes": "$ref:ActionTypes", 
          "r:browsable": "Bool", 
          "r:browserItemActionTypes": "$ref:ActionTypes", 
          "r:createMethods": "$ref:CreateMethods", 
          "r:discoveryParamTypes": "$ref:ParamTypes", 
          "r:displayName": "String", 
          "r:eventTypes": "$ref:EventTypes", 
          "r:id": "Uuid", 
          "r:interfaces": "StringList", 
          "r:name": "String", 
          "r:paramTypes": "$ref:ParamTypes", 
          "r:pluginId": "Uuid", 
          "r:settingsTypes": "$ref:ParamTypes", 
          "r:setupMethod": "$ref:SetupMethod", 
          "r:stateTypes": "$ref:StateTypes", 
          "r:vendorId": "Uuid"
      }

See also: [ActionTypes](#actiontypes), [ActionTypes](#actiontypes), [EventTypes](#eventtypes), [SetupMethod](#setupmethod), [ParamTypes](#paramtypes), [ParamTypes](#paramtypes), [ParamTypes](#paramtypes), [CreateMethods](#createmethods), [StateTypes](#statetypes)

------------------------------
##### DeviceClasses

      [
          "$ref:DeviceClass"
      ]

See also: [DeviceClass](#deviceclass)

------------------------------
##### DeviceDescriptor

      {
          "r:description": "String", 
          "r:deviceParams": "$ref:ParamList", 
          "r:id": "Uuid", 
          "r:o:deviceId": "Uuid", 
          "r:title": "String"
      }

See also: [ParamList](#paramlist)

------------------------------
##### DeviceDescriptors

      [
          "$ref:DeviceDescriptor"
      ]

See also: [DeviceDescriptor](#devicedescriptor)

------------------------------
##### DevicePlugin

      {
          "r:displayName": "String", 
          "r:id": "Uuid", 
          "r:name": "String", 
          "r:paramTypes": "$ref:ParamTypes"
      }

See also: [ParamTypes](#paramtypes)

------------------------------
##### DevicePlugins

      [
          "$ref:DevicePlugin"
      ]

See also: [DevicePlugin](#deviceplugin)

------------------------------
##### Devices

      [
          "$ref:Device"
      ]

See also: [Device](#device)

------------------------------
##### Event

      {
          "r:deviceId": "Uuid", 
          "r:eventTypeId": "Uuid", 
          "r:params": "$ref:ParamList"
      }

See also: [ParamList](#paramlist)

------------------------------
##### EventDescriptor

      {
          "o:deviceId": "Uuid", 
          "o:eventTypeId": "Uuid", 
          "o:interface": "String", 
          "o:interfaceEvent": "String", 
          "o:paramDescriptors": "$ref:ParamDescriptors"
      }

See also: [ParamDescriptors](#paramdescriptors)

------------------------------
##### EventDescriptors

      [
          "$ref:EventDescriptor"
      ]

See also: [EventDescriptor](#eventdescriptor)

------------------------------
##### EventType

      {
          "displayName": "String", 
          "name": "String", 
          "paramTypes": "$ref:ParamTypes", 
          "r:id": "Uuid", 
          "r:index": "Int"
      }

See also: [ParamTypes](#paramtypes)

------------------------------
##### EventTypes

      [
          "$ref:EventType"
      ]

See also: [EventType](#eventtype)

------------------------------
##### Experience

      {
          "name": "String", 
          "version": "String"
      }



------------------------------
##### LogEntries

      [
          "$ref:LogEntry"
      ]

See also: [LogEntry](#logentry)

------------------------------
##### LogEntry

      {
          "r:loggingLevel": "$ref:LoggingLevel", 
          "r:o:active": "Bool", 
          "r:o:deviceId": "Uuid", 
          "r:o:errorCode": "String", 
          "r:o:eventType": "$ref:LoggingEventType", 
          "r:o:typeId": "Uuid", 
          "r:o:value": "Variant", 
          "r:source": "$ref:LoggingSource", 
          "r:timestamp": "Uint"
      }

See also: [LoggingLevel](#logginglevel), [LoggingEventType](#loggingeventtype), [LoggingSource](#loggingsource)

------------------------------
##### MqttPolicy

      {
          "allowedPublishTopicFilters": "StringList", 
          "allowedSubscribeTopicFilters": "StringList", 
          "clientId": "String", 
          "password": "String", 
          "username": "String"
      }



------------------------------
##### Package

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



------------------------------
##### Packages

      [
          "$ref:Package"
      ]

See also: [Package](#package)

------------------------------
##### Param

      {
          "o:paramTypeId": "Uuid", 
          "value": "Variant"
      }



------------------------------
##### ParamDescriptor

      {
          "o:paramName": "String", 
          "o:paramTypeId": "Uuid", 
          "operator": "$ref:ValueOperator", 
          "value": "Variant"
      }

See also: [ValueOperator](#valueoperator)

------------------------------
##### ParamDescriptors

      [
          "$ref:ParamDescriptor"
      ]

See also: [ParamDescriptor](#paramdescriptor)

------------------------------
##### ParamList

      [
          "$ref:Param"
      ]

See also: [Param](#param)

------------------------------
##### ParamType

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
          "o:unit": "$ref:Unit", 
          "r:id": "Uuid", 
          "type": "$ref:BasicType"
      }

See also: [Unit](#unit), [InputType](#inputtype), [BasicType](#basictype)

------------------------------
##### ParamTypes

      [
          "$ref:ParamType"
      ]

See also: [ParamType](#paramtype)

------------------------------
##### RepeatingOption

      {
          "mode": "$ref:RepeatingMode", 
          "o:monthDays": [
              "Int"
          ], 
          "o:weekDays": [
              "Int"
          ]
      }

See also: [RepeatingMode](#repeatingmode)

------------------------------
##### Repositories

      [
          "$ref:Repository"
      ]

See also: [Repository](#repository)

------------------------------
##### Repository

      {
          "enabled": "Bool", 
          "r:displayName": "String", 
          "r:id": "String"
      }



------------------------------
##### Rule

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

See also: [RuleActions](#ruleactions), [TimeDescriptor](#timedescriptor), [RuleActions](#ruleactions), [EventDescriptors](#eventdescriptors), [StateEvaluator](#stateevaluator)

------------------------------
##### RuleAction

      {
          "o:actionTypeId": "Uuid", 
          "o:browserItemId": "String", 
          "o:deviceId": "Uuid", 
          "o:interface": "String", 
          "o:interfaceAction": "String", 
          "o:ruleActionParams": "$ref:RuleActionParams"
      }

See also: [RuleActionParams](#ruleactionparams)

------------------------------
##### RuleActionParam

      {
          "o:eventParamTypeId": "Uuid", 
          "o:eventTypeId": "Uuid", 
          "o:paramName": "String", 
          "o:paramTypeId": "Uuid", 
          "o:stateDeviceId": "Uuid", 
          "o:stateTypeId": "Uuid", 
          "o:value": "Variant"
      }



------------------------------
##### RuleActionParams

      [
          "$ref:RuleActionParam"
      ]

See also: [RuleActionParam](#ruleactionparam)

------------------------------
##### RuleActions

      [
          "$ref:RuleAction"
      ]

See also: [RuleAction](#ruleaction)

------------------------------
##### RuleDescription

      {
          "active": "Bool", 
          "enabled": "Bool", 
          "executable": "Bool", 
          "id": "Uuid", 
          "name": "String"
      }



------------------------------
##### Rules

      [
          "$ref:Rule"
      ]

See also: [Rule](#rule)

------------------------------
##### Script

      {
          "name": "String", 
          "r:id": "Uuid"
      }



------------------------------
##### Scripts

      [
          "$ref:Script"
      ]

See also: [Script](#script)

------------------------------
##### ServerConfiguration

      {
          "address": "String", 
          "authenticationEnabled": "Bool", 
          "id": "String", 
          "port": "Uint", 
          "sslEnabled": "Bool"
      }



------------------------------
##### State

      {
          "r:stateTypeId": "Uuid", 
          "r:value": "Variant"
      }



------------------------------
##### StateDescriptor

      {
          "o:deviceId": "Uuid", 
          "o:interface": "String", 
          "o:interfaceState": "String", 
          "o:stateTypeId": "Uuid", 
          "operator": "$ref:ValueOperator", 
          "value": "Variant"
      }

See also: [ValueOperator](#valueoperator)

------------------------------
##### StateEvaluator

      {
          "o:childEvaluators": "$ref:StateEvaluators", 
          "o:operator": "$ref:StateOperator", 
          "o:stateDescriptor": "$ref:StateDescriptor"
      }

See also: [StateEvaluators](#stateevaluators), [StateDescriptor](#statedescriptor), [StateOperator](#stateoperator)

------------------------------
##### StateEvaluators

      [
          "$ref:StateEvaluator"
      ]

See also: [StateEvaluator](#stateevaluator)

------------------------------
##### StateType

      {
          "defaultValue": "Variant", 
          "displayName": "String", 
          "index": "Int", 
          "name": "String", 
          "o:maxValue": "Variant", 
          "o:minValue": "Variant", 
          "o:possibleValues": [
              "Variant"
          ], 
          "o:unit": "$ref:Unit", 
          "r:id": "Uuid", 
          "type": "$ref:BasicType"
      }

See also: [Unit](#unit), [BasicType](#basictype)

------------------------------
##### StateTypes

      [
          "$ref:StateType"
      ]

See also: [StateType](#statetype)

------------------------------
##### States

      [
          "$ref:State"
      ]

See also: [State](#state)

------------------------------
##### Tag

      {
          "appId": "String", 
          "o:deviceId": "Uuid", 
          "o:ruleId": "Uuid", 
          "o:value": "String", 
          "tagId": "String"
      }



------------------------------
##### Tags

      [
          "$ref:Tag"
      ]

See also: [Tag](#tag)

------------------------------
##### TimeDescriptor

      {
          "o:calendarItems": "$ref:CalendarItems", 
          "o:timeEventItems": "$ref:TimeEventItems"
      }

See also: [TimeEventItems](#timeeventitems), [CalendarItems](#calendaritems)

------------------------------
##### TimeEventItem

      {
          "o:datetime": "Uint", 
          "o:repeating": "$ref:RepeatingOption", 
          "o:time": "Time"
      }

See also: [RepeatingOption](#repeatingoption)

------------------------------
##### TimeEventItems

      [
          "$ref:TimeEventItem"
      ]

See also: [TimeEventItem](#timeeventitem)

------------------------------
##### TokenInfo

      {
          "r:creationTime": "Uint", 
          "r:deviceName": "String", 
          "r:id": "Uuid", 
          "r:username": "String"
      }



------------------------------
##### TokenInfoList

      [
          "$ref:TokenInfo"
      ]

See also: [TokenInfo](#tokeninfo)

------------------------------
##### UserInfo

      {
          "r:username": "String"
      }



------------------------------
##### Vendor

      {
          "displayName": "String", 
          "id": "Uuid", 
          "name": "String"
      }



------------------------------
##### Vendors

      [
          "$ref:Vendor"
      ]

See also: [Vendor](#vendor)

------------------------------
##### WebServerConfiguration

      {
          "address": "String", 
          "authenticationEnabled": "Bool", 
          "id": "String", 
          "port": "Uint", 
          "publicFolder": "String", 
          "sslEnabled": "Bool"
      }



------------------------------
##### WiredNetworkDevice

      {
          "r:bitRate": "String", 
          "r:interface": "String", 
          "r:macAddress": "String", 
          "r:pluggedIn": "Bool", 
          "r:state": "$ref:NetworkDeviceState"
      }

See also: [NetworkDeviceState](#networkdevicestate)

------------------------------
##### WirelessAccessPoint

      {
          "r:frequency": "Double", 
          "r:macAddress": "String", 
          "r:protected": "Bool", 
          "r:signalStrength": "Int", 
          "r:ssid": "String"
      }



------------------------------
##### WirelessNetworkDevice

      {
          "bitRate": "String", 
          "interface": "String", 
          "macAddress": "String", 
          "o:currentAccessPoint": "$ref:WirelessAccessPoint", 
          "state": "$ref:NetworkDeviceState"
      }

See also: [WirelessAccessPoint](#wirelessaccesspoint), [NetworkDeviceState](#networkdevicestate)

------------------------------
### Methods

 * [Actions.ExecuteAction](#actionsexecuteaction)
 * [Actions.ExecuteBrowserItem](#actionsexecutebrowseritem)
 * [Actions.ExecuteBrowserItemAction](#actionsexecutebrowseritemaction)
 * [Actions.GetActionType](#actionsgetactiontype)
 * [Configuration.DeleteMqttPolicy](#configurationdeletemqttpolicy)
 * [Configuration.DeleteMqttServerConfiguration](#configurationdeletemqttserverconfiguration)
 * [Configuration.DeleteTcpServerConfiguration](#configurationdeletetcpserverconfiguration)
 * [Configuration.DeleteWebServerConfiguration](#configurationdeletewebserverconfiguration)
 * [Configuration.DeleteWebSocketServerConfiguration](#configurationdeletewebsocketserverconfiguration)
 * [Configuration.GetAvailableLanguages](#configurationgetavailablelanguages)
 * [Configuration.GetConfigurations](#configurationgetconfigurations)
 * [Configuration.GetMqttPolicies](#configurationgetmqttpolicies)
 * [Configuration.GetMqttServerConfigurations](#configurationgetmqttserverconfigurations)
 * [Configuration.GetTimeZones](#configurationgettimezones)
 * [Configuration.SetCloudEnabled](#configurationsetcloudenabled)
 * [Configuration.SetDebugServerEnabled](#configurationsetdebugserverenabled)
 * [Configuration.SetLanguage](#configurationsetlanguage)
 * [Configuration.SetMqttPolicy](#configurationsetmqttpolicy)
 * [Configuration.SetMqttServerConfiguration](#configurationsetmqttserverconfiguration)
 * [Configuration.SetServerName](#configurationsetservername)
 * [Configuration.SetTcpServerConfiguration](#configurationsettcpserverconfiguration)
 * [Configuration.SetTimeZone](#configurationsettimezone)
 * [Configuration.SetWebServerConfiguration](#configurationsetwebserverconfiguration)
 * [Configuration.SetWebSocketServerConfiguration](#configurationsetwebsocketserverconfiguration)
 * [Devices.AddConfiguredDevice](#devicesaddconfigureddevice)
 * [Devices.BrowseDevice](#devicesbrowsedevice)
 * [Devices.ConfirmPairing](#devicesconfirmpairing)
 * [Devices.EditDevice](#deviceseditdevice)
 * [Devices.ExecuteAction](#devicesexecuteaction)
 * [Devices.ExecuteBrowserItem](#devicesexecutebrowseritem)
 * [Devices.ExecuteBrowserItemAction](#devicesexecutebrowseritemaction)
 * [Devices.GetActionTypes](#devicesgetactiontypes)
 * [Devices.GetBrowserItem](#devicesgetbrowseritem)
 * [Devices.GetConfiguredDevices](#devicesgetconfigureddevices)
 * [Devices.GetDiscoveredDevices](#devicesgetdiscovereddevices)
 * [Devices.GetEventTypes](#devicesgeteventtypes)
 * [Devices.GetPluginConfiguration](#devicesgetpluginconfiguration)
 * [Devices.GetPlugins](#devicesgetplugins)
 * [Devices.GetStateTypes](#devicesgetstatetypes)
 * [Devices.GetStateValue](#devicesgetstatevalue)
 * [Devices.GetStateValues](#devicesgetstatevalues)
 * [Devices.GetSupportedDevices](#devicesgetsupporteddevices)
 * [Devices.GetSupportedVendors](#devicesgetsupportedvendors)
 * [Devices.PairDevice](#devicespairdevice)
 * [Devices.ReconfigureDevice](#devicesreconfiguredevice)
 * [Devices.RemoveConfiguredDevice](#devicesremoveconfigureddevice)
 * [Devices.SetDeviceSettings](#devicessetdevicesettings)
 * [Devices.SetPluginConfiguration](#devicessetpluginconfiguration)
 * [Events.GetEventType](#eventsgeteventtype)
 * [JSONRPC.Authenticate](#jsonrpcauthenticate)
 * [JSONRPC.CreateUser](#jsonrpccreateuser)
 * [JSONRPC.Hello](#jsonrpchello)
 * [JSONRPC.Introspect](#jsonrpcintrospect)
 * [JSONRPC.IsCloudConnected](#jsonrpciscloudconnected)
 * [JSONRPC.KeepAlive](#jsonrpckeepalive)
 * [JSONRPC.RemoveToken](#jsonrpcremovetoken)
 * [JSONRPC.RequestPushButtonAuth](#jsonrpcrequestpushbuttonauth)
 * [JSONRPC.SetNotificationStatus](#jsonrpcsetnotificationstatus)
 * [JSONRPC.SetupCloudConnection](#jsonrpcsetupcloudconnection)
 * [JSONRPC.SetupRemoteAccess](#jsonrpcsetupremoteaccess)
 * [JSONRPC.Tokens](#jsonrpctokens)
 * [JSONRPC.Version](#jsonrpcversion)
 * [Logging.GetLogEntries](#logginggetlogentries)
 * [NetworkManager.ConnectWifiNetwork](#networkmanagerconnectwifinetwork)
 * [NetworkManager.DisconnectInterface](#networkmanagerdisconnectinterface)
 * [NetworkManager.EnableNetworking](#networkmanagerenablenetworking)
 * [NetworkManager.EnableWirelessNetworking](#networkmanagerenablewirelessnetworking)
 * [NetworkManager.GetNetworkDevices](#networkmanagergetnetworkdevices)
 * [NetworkManager.GetNetworkStatus](#networkmanagergetnetworkstatus)
 * [NetworkManager.GetWirelessAccessPoints](#networkmanagergetwirelessaccesspoints)
 * [NetworkManager.ScanWifiNetworks](#networkmanagerscanwifinetworks)
 * [Rules.AddRule](#rulesaddrule)
 * [Rules.DisableRule](#rulesdisablerule)
 * [Rules.EditRule](#ruleseditrule)
 * [Rules.EnableRule](#rulesenablerule)
 * [Rules.ExecuteActions](#rulesexecuteactions)
 * [Rules.ExecuteExitActions](#rulesexecuteexitactions)
 * [Rules.FindRules](#rulesfindrules)
 * [Rules.GetRuleDetails](#rulesgetruledetails)
 * [Rules.GetRules](#rulesgetrules)
 * [Rules.RemoveRule](#rulesremoverule)
 * [Scripts.AddScript](#scriptsaddscript)
 * [Scripts.EditScript](#scriptseditscript)
 * [Scripts.GetScriptContent](#scriptsgetscriptcontent)
 * [Scripts.GetScripts](#scriptsgetscripts)
 * [Scripts.RemoveScript](#scriptsremovescript)
 * [States.GetStateType](#statesgetstatetype)
 * [System.CheckForUpdates](#systemcheckforupdates)
 * [System.EnableRepository](#systemenablerepository)
 * [System.GetCapabilities](#systemgetcapabilities)
 * [System.GetPackages](#systemgetpackages)
 * [System.GetRepositories](#systemgetrepositories)
 * [System.GetTime](#systemgettime)
 * [System.GetTimeZones](#systemgettimezones)
 * [System.GetUpdateStatus](#systemgetupdatestatus)
 * [System.Reboot](#systemreboot)
 * [System.RemovePackages](#systemremovepackages)
 * [System.RollbackPackages](#systemrollbackpackages)
 * [System.SetTime](#systemsettime)
 * [System.Shutdown](#systemshutdown)
 * [System.UpdatePackages](#systemupdatepackages)
 * [Tags.AddTag](#tagsaddtag)
 * [Tags.GetTags](#tagsgettags)
 * [Tags.RemoveTag](#tagsremovetag)
 * [Users.Authenticate](#usersauthenticate)
 * [Users.ChangePassword](#userschangepassword)
 * [Users.CreateUser](#userscreateuser)
 * [Users.GetTokens](#usersgettokens)
 * [Users.GetUserInfo](#usersgetuserinfo)
 * [Users.RemoveToken](#usersremovetoken)
 * [Users.RequestPushButtonAuth](#usersrequestpushbuttonauth)
------------------------------
##### **Actions.ExecuteAction**

Execute a single action.

> **Warning**: this method is deprecated. Please use Devices.ExecuteAction instead.

*Params*


      {
          "actionTypeId": "Uuid", 
          "deviceId": "Uuid", 
          "o:params": "$ref:ParamList"
      }


*Returns*


      {
          "deviceError": "$ref:DeviceError", 
          "o:displayMessage": "String"
      }


See also: [DeviceError](#deviceerror), [ParamList](#paramlist)

------------------------------
##### **Actions.ExecuteBrowserItem**

Execute the item identified by itemId on the given device.

> **Warning**: this method is deprecated. Please use Devices.ExecuteBrowserItem instead.

*Params*


      {
          "deviceId": "Uuid", 
          "itemId": "String"
      }


*Returns*


      {
          "deviceError": "$ref:DeviceError"
      }


See also: [DeviceError](#deviceerror)

------------------------------
##### **Actions.ExecuteBrowserItemAction**

Execute the action for the browser item identified by actionTypeId and the itemId on the given device.

> **Warning**: this method is deprecated. Please use Devices.ExecuteBrowserItem instead.

*Params*


      {
          "actionTypeId": "Uuid", 
          "deviceId": "Uuid", 
          "itemId": "String", 
          "o:params": "$ref:ParamList"
      }


*Returns*


      {
          "deviceError": "$ref:DeviceError"
      }


See also: [DeviceError](#deviceerror), [ParamList](#paramlist)

------------------------------
##### **Actions.GetActionType**

Get the ActionType for the given ActionTypeId.

> **Warning**: this method is deprecated. Please use the Devices namespace instead.

*Params*


      {
          "actionTypeId": "Uuid"
      }


*Returns*


      {
          "deviceError": "$ref:DeviceError", 
          "o:actionType": "$ref:ActionType"
      }


See also: [ActionType](#actiontype), [DeviceError](#deviceerror)

------------------------------
##### **Configuration.DeleteMqttPolicy**

Delete a MQTT policy from the broker.


*Params*


      {
          "clientId": "String"
      }


*Returns*


      {
          "configurationError": "$ref:ConfigurationError"
      }


See also: [ConfigurationError](#configurationerror)

------------------------------
##### **Configuration.DeleteMqttServerConfiguration**

Delete a MQTT Server interface of the server.


*Params*


      {
          "id": "String"
      }


*Returns*


      {
          "configurationError": "$ref:ConfigurationError"
      }


See also: [ConfigurationError](#configurationerror)

------------------------------
##### **Configuration.DeleteTcpServerConfiguration**

Delete a TCP interface of the server. Note: if you are deleting the configuration for the interface you are currently connected to, the connection will be dropped.


*Params*


      {
          "id": "String"
      }


*Returns*


      {
          "configurationError": "$ref:ConfigurationError"
      }


See also: [ConfigurationError](#configurationerror)

------------------------------
##### **Configuration.DeleteWebServerConfiguration**

Delete a WebServer interface of the server.


*Params*


      {
          "id": "String"
      }


*Returns*


      {
          "configurationError": "$ref:ConfigurationError"
      }


See also: [ConfigurationError](#configurationerror)

------------------------------
##### **Configuration.DeleteWebSocketServerConfiguration**

Delete a WebSocket Server interface of the server. Note: if you are deleting the configuration for the interface you are currently connected to, the connection will be dropped.


*Params*


      {
          "id": "String"
      }


*Returns*


      {
          "configurationError": "$ref:ConfigurationError"
      }


See also: [ConfigurationError](#configurationerror)

------------------------------
##### **Configuration.GetAvailableLanguages**

Returns a list of locale codes available for the server. i.e. en_US, de_AT

> **Warning**: this method is deprecated. Use the locale property in the Handshake message instead.

*Params*


      {}


*Returns*


      {
          "languages": [
              "String"
          ]
      }




------------------------------
##### **Configuration.GetConfigurations**

Get all configuration parameters of the server.


*Params*


      {}


*Returns*


      {
          "basicConfiguration": {
              "d:language": "String", 
              "d:serverTime": "Uint", 
              "d:timeZone": "String", 
              "debugServerEnabled": "Bool", 
              "serverName": "String", 
              "serverUuid": "Uuid"
          }, 
          "cloud": {
              "enabled": "Bool"
          }, 
          "tcpServerConfigurations": [
              "$ref:ServerConfiguration"
          ], 
          "webServerConfigurations": [
              "$ref:WebServerConfiguration"
          ], 
          "webSocketServerConfigurations": [
              "$ref:ServerConfiguration"
          ]
      }


> **Warning**: following values are deprecated and will be removed with the next major API version: `serverTime`, `timeZone`, `language`

See also: [ServerConfiguration](#serverconfiguration), [WebServerConfiguration](#webserverconfiguration), [ServerConfiguration](#serverconfiguration)

------------------------------
##### **Configuration.GetMqttPolicies**

Get all MQTT broker policies.


*Params*


      {}


*Returns*


      {
          "mqttPolicies": [
              "$ref:MqttPolicy"
          ]
      }


See also: [MqttPolicy](#mqttpolicy)

------------------------------
##### **Configuration.GetMqttServerConfigurations**

Get all MQTT Server configurations.


*Params*


      {}


*Returns*


      {
          "mqttServerConfigurations": [
              "$ref:ServerConfiguration"
          ]
      }


See also: [ServerConfiguration](#serverconfiguration)

------------------------------
##### **Configuration.GetTimeZones**

Get the list of available timezones.

> **Warning**: this method is deprecated. Use System.GetTimeZones instead.

*Params*


      {}


*Returns*


      {
          "timeZones": [
              "String"
          ]
      }




------------------------------
##### **Configuration.SetCloudEnabled**

Sets whether the cloud connection is enabled or disabled in the settings.


*Params*


      {
          "enabled": "Bool"
      }


*Returns*


      {
          "configurationError": "$ref:ConfigurationError"
      }


See also: [ConfigurationError](#configurationerror)

------------------------------
##### **Configuration.SetDebugServerEnabled**

Enable or disable the debug server.


*Params*


      {
          "enabled": "String"
      }


*Returns*


      {
          "configurationError": "$ref:ConfigurationError"
      }


See also: [ConfigurationError](#configurationerror)

------------------------------
##### **Configuration.SetLanguage**

Sets the server language to the given language. See also: "GetAvailableLanguages"

> **Warning**: this method is deprecated. Use the locale property in the Handshake message instead.

*Params*


      {
          "language": "String"
      }


*Returns*


      {
          "configurationError": "$ref:ConfigurationError"
      }


See also: [ConfigurationError](#configurationerror)

------------------------------
##### **Configuration.SetMqttPolicy**

Configure a MQTT broker policy. If the ID is an existing one, the existing policy will be modified, otherwise a new one will be added.


*Params*


      {
          "policy": "$ref:MqttPolicy"
      }


*Returns*


      {
          "configurationError": "$ref:ConfigurationError"
      }


See also: [ConfigurationError](#configurationerror), [MqttPolicy](#mqttpolicy)

------------------------------
##### **Configuration.SetMqttServerConfiguration**

Configure a MQTT Server interface on the MQTT broker. If the ID is an existing one, the existing config will be modified, otherwise a new one will be added. Setting authenticationEnabled to true will require MQTT clients to use credentials set in the MQTT broker policies.


*Params*


      {
          "configuration": "$ref:ServerConfiguration"
      }


*Returns*


      {
          "configurationError": "$ref:ConfigurationError"
      }


See also: [ConfigurationError](#configurationerror), [ServerConfiguration](#serverconfiguration)

------------------------------
##### **Configuration.SetServerName**

Set the name of the server. Default is nymea.


*Params*


      {
          "serverName": "String"
      }


*Returns*


      {
          "configurationError": "$ref:ConfigurationError"
      }


See also: [ConfigurationError](#configurationerror)

------------------------------
##### **Configuration.SetTcpServerConfiguration**

Configure a TCP interface of the server. If the ID is an existing one, the existing config will be modified, otherwise a new one will be added. Note: if you are changing the configuration for the interface you are currently connected to, the connection will be dropped.


*Params*


      {
          "configuration": "$ref:ServerConfiguration"
      }


*Returns*


      {
          "configurationError": "$ref:ConfigurationError"
      }


See also: [ConfigurationError](#configurationerror), [ServerConfiguration](#serverconfiguration)

------------------------------
##### **Configuration.SetTimeZone**

Set the time zone of the server. See also: "GetTimeZones"

> **Warning**: this method is deprecated. Use System.SetTimeZone instead.

*Params*


      {
          "timeZone": "String"
      }


*Returns*


      {
          "configurationError": "$ref:ConfigurationError"
      }


See also: [ConfigurationError](#configurationerror)

------------------------------
##### **Configuration.SetWebServerConfiguration**

Configure a WebServer interface of the server. If the ID is an existing one, the existing config will be modified, otherwise a new one will be added.


*Params*


      {
          "configuration": "$ref:WebServerConfiguration"
      }


*Returns*


      {
          "configurationError": "$ref:ConfigurationError"
      }


See also: [ConfigurationError](#configurationerror), [WebServerConfiguration](#webserverconfiguration)

------------------------------
##### **Configuration.SetWebSocketServerConfiguration**

Configure a WebSocket Server interface of the server. If the ID is an existing one, the existing config will be modified, otherwise a new one will be added. Note: if you are changing the configuration for the interface you are currently connected to, the connection will be dropped.


*Params*


      {
          "configuration": "$ref:ServerConfiguration"
      }


*Returns*


      {
          "configurationError": "$ref:ConfigurationError"
      }


See also: [ConfigurationError](#configurationerror), [ServerConfiguration](#serverconfiguration)

------------------------------
##### **Devices.AddConfiguredDevice**

Add a configured device with a setupMethod of SetupMethodJustAdd. For devices with a setupMethod different than SetupMethodJustAdd, use PairDevice. Devices with CreateMethodJustAdd require all parameters to be supplied here. Devices with CreateMethodDiscovery require the use of a deviceDescriptorId. For discovered devices params are not required and will be taken from the DeviceDescriptor, however, they may be overridden by supplying deviceParams.


*Params*


      {
          "deviceClassId": "Uuid", 
          "name": "String", 
          "o:deviceDescriptorId": "Uuid", 
          "o:deviceParams": "$ref:ParamList"
      }


*Returns*


      {
          "deviceError": "$ref:DeviceError", 
          "o:deviceId": "Uuid", 
          "o:displayMessage": "String"
      }


See also: [DeviceError](#deviceerror), [ParamList](#paramlist)

------------------------------
##### **Devices.BrowseDevice**

Browse a device. If a DeviceClass indicates a device is browsable, this method will return the BrowserItems. If no parameter besides the deviceId is used, the root node of this device will be returned. Any returned item which is browsable can be passed as node. Results will be children of the given node.


*Params*


      {
          "deviceId": "Uuid", 
          "o:itemId": "String"
      }


*Returns*


      {
          "deviceError": "$ref:DeviceError", 
          "items": [
              "$ref:BrowserItem"
          ]
      }


See also: [BrowserItem](#browseritem), [DeviceError](#deviceerror)

------------------------------
##### **Devices.ConfirmPairing**

Confirm an ongoing pairing. For SetupMethodUserAndPassword, provide the username in the "username" field and the password in the "secret" field. For SetupMethodEnterPin and provide the PIN in the "secret" field. In case of SetupMethodOAuth, the previously opened web view will eventually be redirected to http://128.0.0.1:8888 and the OAuth code as query parameters to this url. Provide the entire unmodified URL in the secret field.


*Params*


      {
          "o:secret": "String", 
          "o:username": "String", 
          "pairingTransactionId": "Uuid"
      }


*Returns*


      {
          "deviceError": "$ref:DeviceError", 
          "o:deviceId": "Uuid", 
          "o:displayMessage": "String"
      }


See also: [DeviceError](#deviceerror)

------------------------------
##### **Devices.EditDevice**

Edit the name of a device. This method does not change the configuration of the device.


*Params*


      {
          "deviceId": "Uuid", 
          "name": "String"
      }


*Returns*


      {
          "deviceError": "$ref:DeviceError"
      }


See also: [DeviceError](#deviceerror)

------------------------------
##### **Devices.ExecuteAction**

Execute a single action.


*Params*


      {
          "actionTypeId": "Uuid", 
          "deviceId": "Uuid", 
          "o:params": "$ref:ParamList"
      }


*Returns*


      {
          "deviceError": "$ref:DeviceError", 
          "o:displayMessage": "String"
      }


See also: [DeviceError](#deviceerror), [ParamList](#paramlist)

------------------------------
##### **Devices.ExecuteBrowserItem**

Execute the item identified by itemId on the given device.


*Params*


      {
          "deviceId": "Uuid", 
          "itemId": "String"
      }


*Returns*


      {
          "deviceError": "$ref:DeviceError"
      }


See also: [DeviceError](#deviceerror)

------------------------------
##### **Devices.ExecuteBrowserItemAction**

Execute the action for the browser item identified by actionTypeId and the itemId on the given device.


*Params*


      {
          "actionTypeId": "Uuid", 
          "deviceId": "Uuid", 
          "itemId": "String", 
          "o:params": "$ref:ParamList"
      }


*Returns*


      {
          "deviceError": "$ref:DeviceError"
      }


See also: [DeviceError](#deviceerror), [ParamList](#paramlist)

------------------------------
##### **Devices.GetActionTypes**

Get action types for a specified deviceClassId.


*Params*


      {
          "deviceClassId": "Uuid"
      }


*Returns*


      {
          "actionTypes": "$ref:ActionTypes"
      }


See also: [ActionTypes](#actiontypes)

------------------------------
##### **Devices.GetBrowserItem**

Get a single item from the browser. This won't give any more info on an item than a regular browseDevice call, but it allows to fetch details of an item if only the ID is known.


*Params*


      {
          "deviceId": "Uuid", 
          "o:itemId": "String"
      }


*Returns*


      {
          "deviceError": "$ref:DeviceError", 
          "o:item": "$ref:BrowserItem"
      }


See also: [BrowserItem](#browseritem), [DeviceError](#deviceerror)

------------------------------
##### **Devices.GetConfiguredDevices**

Returns a list of configured devices, optionally filtered by deviceId.


*Params*


      {
          "o:deviceId": "Uuid"
      }


*Returns*


      {
          "devices": "$ref:Devices"
      }


See also: [Devices](#devices)

------------------------------
##### **Devices.GetDiscoveredDevices**

Performs a device discovery and returns the results. This function may take a while to return. Note that this method will include all the found devices, that is, including devices that may already have been added. Those devices will have deviceId set to the device id of the already added device. Such results may be used to reconfigure existing devices and might be filtered in cases where only unknown devices are of interest.


*Params*


      {
          "deviceClassId": "Uuid", 
          "o:discoveryParams": "$ref:ParamList"
      }


*Returns*


      {
          "deviceError": "$ref:DeviceError", 
          "o:deviceDescriptors": "$ref:DeviceDescriptors", 
          "o:displayMessage": "String"
      }


See also: [DeviceDescriptors](#devicedescriptors), [DeviceError](#deviceerror), [ParamList](#paramlist)

------------------------------
##### **Devices.GetEventTypes**

Get event types for a specified deviceClassId.


*Params*


      {
          "deviceClassId": "Uuid"
      }


*Returns*


      {
          "eventTypes": "$ref:EventTypes"
      }


See also: [EventTypes](#eventtypes)

------------------------------
##### **Devices.GetPluginConfiguration**

Get a plugin's params.


*Params*


      {
          "pluginId": "Uuid"
      }


*Returns*


      {
          "deviceError": "$ref:DeviceError", 
          "o:configuration": "$ref:ParamList"
      }


See also: [ParamList](#paramlist), [DeviceError](#deviceerror)

------------------------------
##### **Devices.GetPlugins**

Returns a list of loaded plugins.


*Params*


      {}


*Returns*


      {
          "plugins": "$ref:DevicePlugins"
      }


See also: [DevicePlugins](#deviceplugins)

------------------------------
##### **Devices.GetStateTypes**

Get state types for a specified deviceClassId.


*Params*


      {
          "deviceClassId": "Uuid"
      }


*Returns*


      {
          "stateTypes": "$ref:StateTypes"
      }


See also: [StateTypes](#statetypes)

------------------------------
##### **Devices.GetStateValue**

Get the value of the given device and the given stateType


*Params*


      {
          "deviceId": "Uuid", 
          "stateTypeId": "Uuid"
      }


*Returns*


      {
          "deviceError": "$ref:DeviceError", 
          "o:value": "Variant"
      }


See also: [DeviceError](#deviceerror)

------------------------------
##### **Devices.GetStateValues**

Get all the state values of the given device.


*Params*


      {
          "deviceId": "Uuid"
      }


*Returns*


      {
          "deviceError": "$ref:DeviceError", 
          "o:values": "$ref:States"
      }


See also: [States](#states), [DeviceError](#deviceerror)

------------------------------
##### **Devices.GetSupportedDevices**

Returns a list of supported Device classes, optionally filtered by vendorId.


*Params*


      {
          "o:vendorId": "Uuid"
      }


*Returns*


      {
          "deviceClasses": "$ref:DeviceClasses"
      }


See also: [DeviceClasses](#deviceclasses)

------------------------------
##### **Devices.GetSupportedVendors**

Returns a list of supported Vendors.


*Params*


      {}


*Returns*


      {
          "vendors": "$ref:Vendors"
      }


See also: [Vendors](#vendors)

------------------------------
##### **Devices.PairDevice**

Pair a device. Use this to set up or reconfigure devices for DeviceClasses with a setupMethod different than SetupMethodJustAdd. Depending on the CreateMethod and whether a new devices is set up or an existing one is reconfigured, different parameters are required:
CreateMethodJustAdd takes the deviceClassId and the parameters you want to have with that device.
CreateMethodDiscovery requires the use of a deviceDescriptorId, previously obtained with DiscoverDevices. Optionally, parameters can be overridden with the give deviceParams.
If an existing device should be reconfigured, the deviceId of said device should be given additionally.
If success is true, the return values will contain a pairingTransactionId, a displayMessage and the setupMethod. Depending on the setupMethod, the application should present the use an appropriate login mask, that is, For SetupMethodDisplayPin the user should enter a pin that is displayed on the device, for SetupMethodEnterPin the application should present the given PIN so the user can enter it on the device. For SetupMethodPushButton, the displayMessage shall be presented to the user as informational hints to press a button on the device. For SetupMethodUserAndPassword a login mask for a user and password login should be presented to the user. In case of SetupMethodOAuth, an OAuth URL will be returned which shall be opened in a web view to allow the user logging in.
Once the login procedure has completed, the application shall proceed with ConfirmPairing, providing the results of the pairing procedure.


*Params*


      {
          "o:deviceClassId": "Uuid", 
          "o:deviceDescriptorId": "Uuid", 
          "o:deviceId": "Uuid", 
          "o:deviceParams": "$ref:ParamList", 
          "o:name": "String"
      }


*Returns*


      {
          "deviceError": "$ref:DeviceError", 
          "o:displayMessage": "String", 
          "o:oAuthUrl": "String", 
          "o:pairingTransactionId": "Uuid", 
          "o:pin": "String", 
          "o:setupMethod": "$ref:SetupMethod"
      }


See also: [DeviceError](#deviceerror), [SetupMethod](#setupmethod), [ParamList](#paramlist)

------------------------------
##### **Devices.ReconfigureDevice**

Reconfigure a device. This comes down to removing and recreating a device with new parameters but keeping its device id the same (and with that keeping rules, tags etc). For devices with create method CreateMethodDiscovery, a discovery (GetDiscoveredDevices) shall be performed first and this method is to be called with a deviceDescriptorId of the re-discovered device instead of the deviceId directly. Device parameters will be taken from the discovery, but can be overridden individually here by providing them in the deviceParams parameter. Only writable parameters can be changed.


*Params*


      {
          "o:deviceDescriptorId": "Uuid", 
          "o:deviceId": "Uuid", 
          "o:deviceParams": "$ref:ParamList"
      }


*Returns*


      {
          "deviceError": "$ref:DeviceError", 
          "o:displayMessage": "String"
      }


See also: [DeviceError](#deviceerror), [ParamList](#paramlist)

------------------------------
##### **Devices.RemoveConfiguredDevice**

Remove a device from the system.


*Params*


      {
          "deviceId": "Uuid", 
          "o:removePolicy": "$ref:RemovePolicy", 
          "o:removePolicyList": [
              {
                  "policy": "$ref:RemovePolicy", 
                  "ruleId": "Uuid"
              }
          ]
      }


*Returns*


      {
          "deviceError": "$ref:DeviceError", 
          "o:ruleIds": [
              "Uuid"
          ]
      }


See also: [DeviceError](#deviceerror), [RemovePolicy](#removepolicy), [RemovePolicy](#removepolicy)

------------------------------
##### **Devices.SetDeviceSettings**

Change the settings of a device.


*Params*


      {
          "deviceId": "Uuid", 
          "settings": "$ref:ParamList"
      }


*Returns*


      {
          "deviceError": "$ref:DeviceError"
      }


See also: [DeviceError](#deviceerror), [ParamList](#paramlist)

------------------------------
##### **Devices.SetPluginConfiguration**

Set a plugin's params.


*Params*


      {
          "configuration": "$ref:ParamList", 
          "pluginId": "Uuid"
      }


*Returns*


      {
          "deviceError": "$ref:DeviceError"
      }


See also: [DeviceError](#deviceerror), [ParamList](#paramlist)

------------------------------
##### **Events.GetEventType**

Get the EventType for the given eventTypeId.

> **Warning**: this method is deprecated. Please use the Devices namespace instead.

*Params*


      {
          "eventTypeId": "Uuid"
      }


*Returns*


      {
          "deviceError": "$ref:DeviceError", 
          "o:eventType": "$ref:EventType"
      }


See also: [EventType](#eventtype), [DeviceError](#deviceerror)

------------------------------
##### **JSONRPC.Authenticate**

Authenticate a client to the api via user & password challenge. Provide a device name which allows the user to identify the client and revoke the token in case the device is lost or stolen. This will return a new token to be used to authorize a client at the API.

> **Warning**: this method is deprecated. Use Users.Authenticate instead.

*Params*


      {
          "deviceName": "String", 
          "password": "String", 
          "username": "String"
      }


*Returns*


      {
          "o:token": "String", 
          "success": "Bool"
      }




------------------------------
##### **JSONRPC.CreateUser**

Create a new user in the API. Currently this is only allowed to be called once when a new nymea instance is set up. Call Authenticate after this to obtain a device token for this user.

> **Warning**: this method is deprecated. Use Users.CreateUser instead.

*Params*


      {
          "password": "String", 
          "username": "String"
      }


*Returns*


      {
          "error": "$ref:UserError"
      }


See also: [UserError](#usererror)

------------------------------
##### **JSONRPC.Hello**

Initiates a connection. Use this method to perform an initial handshake of the connection. Optionally, a parameter "locale" is can be passed to set up the used locale for this connection. Strings such as DeviceClass displayNames etc will be localized to this locale. If this parameter is omitted, the default system locale (depending on the configuration) is used. The reply of this method contains information about this core instance such as version information, uuid and its name. The locale valueindicates the locale used for this connection. Note: This method can be called multiple times. The locale used in the last call for this connection will be used. Other values, like initialSetupRequired might change if the setup has been performed in the meantime.


*Params*


      {
          "o:locale": "String"
      }


*Returns*


      {
          "authenticationRequired": "Bool", 
          "initialSetupRequired": "Bool", 
          "language": "String", 
          "locale": "String", 
          "name": "String", 
          "o:experiences": [
              "$ref:Experience"
          ], 
          "protocol version": "String", 
          "pushButtonAuthAvailable": "Bool", 
          "server": "String", 
          "uuid": "Uuid", 
          "version": "String"
      }


See also: [Experience](#experience)

------------------------------
##### **JSONRPC.Introspect**

Introspect this API.


*Params*


      {}


*Returns*


      {
          "methods": "Object", 
          "notifications": "Object", 
          "types": "Object"
      }




------------------------------
##### **JSONRPC.IsCloudConnected**

Check whether the cloud is currently connected. "connected" will be true whenever connectionState equals CloudConnectionStateConnected and is deprecated. Please use the connectionState value instead.


*Params*


      {}


*Returns*


      {
          "connected": "Bool", 
          "connectionState": "$ref:CloudConnectionState"
      }


See also: [CloudConnectionState](#cloudconnectionstate)

------------------------------
##### **JSONRPC.KeepAlive**

This is basically a Ping/Pong mechanism a client app may use to check server connectivity. Currently, the server does not actually do anything with this information and will return the call providing the given sessionId back to the caller. It is up to the client whether to use this or not and not required by the server to keep the connection alive.


*Params*


      {
          "sessionId": "String"
      }


*Returns*


      {
          "sessionId": "String", 
          "success": "Bool"
      }




------------------------------
##### **JSONRPC.RemoveToken**

Revoke access for a given token.

> **Warning**: this method is deprecated. Use Users.RemoveToken instead.

*Params*


      {
          "tokenId": "Uuid"
      }


*Returns*


      {
          "error": "$ref:UserError"
      }


See also: [UserError](#usererror)

------------------------------
##### **JSONRPC.RequestPushButtonAuth**

Authenticate a client to the api via Push Button method. Provide a device name which allows the user to identify the client and revoke the token in case the device is lost or stolen. If push button hardware is available, this will return with success and start listening for push button presses. When the push button is pressed, the PushButtonAuthFinished notification will be sent to the requesting client. The procedure will be cancelled when the connection is interrupted. If another client requests push button authentication while a procedure is still going on, the second call will take over and the first one will be notified by the PushButtonAuthFinished signal about the error. The application should make it clear to the user to not press the button when the procedure fails as this can happen for 2 reasons: a) a second user is trying to auth at the same time and only the currently active user should press the button or b) it might indicate an attacker trying to take over and snooping in for tokens.

> **Warning**: this method is deprecated. Use Users.RequestPushButtonAuth instead.

*Params*


      {
          "deviceName": "String"
      }


*Returns*


      {
          "success": "Bool", 
          "transactionId": "Int"
      }




------------------------------
##### **JSONRPC.SetNotificationStatus**

Enable/Disable notifications for this connections. Either "enabled" or "namespaces" needs to be given but not both of them. The boolean based "enabled" parameter will enable/disable all notifications at once. If instead the list-based "namespaces" parameter is provided, all given namespaceswill be enabled, the others will be disabled. The return value of "success" will indicate success of the operation. The "enabled" property in the return value is deprecated and used for legacy compatibilty only. It will be set to true if at least one namespace has been enabled.


*Params*


      {
          "o:enabled": "Bool", 
          "o:namespaces": "StringList"
      }


*Returns*


      {
          "enabled": "Bool", 
          "namespaces": "StringList"
      }




------------------------------
##### **JSONRPC.SetupCloudConnection**

Sets up the cloud connection by deploying a certificate and its configuration.


*Params*


      {
          "certificatePEM": "String", 
          "endpoint": "String", 
          "privateKey": "String", 
          "publicKey": "String", 
          "rootCA": "String"
      }


*Returns*


      {
          "success": "Bool"
      }




------------------------------
##### **JSONRPC.SetupRemoteAccess**

Setup the remote connection by providing AWS token information. This requires the cloud to be connected.


*Params*


      {
          "idToken": "String", 
          "userId": "String"
      }


*Returns*


      {
          "message": "String", 
          "status": "Int"
      }




------------------------------
##### **JSONRPC.Tokens**

Return a list of TokenInfo objects of all the tokens for the current user.

> **Warning**: this method is deprecated. Use Users.GetTokens instead.

*Params*


      {}


*Returns*


      {
          "tokenInfoList": [
              "$ref:TokenInfo"
          ]
      }


See also: [TokenInfo](#tokeninfo)

------------------------------
##### **JSONRPC.Version**

Version of this nymea/JSONRPC interface.


*Params*


      {}


*Returns*


      {
          "protocol version": "String", 
          "qtBuildVersion": "String", 
          "qtVersion": "String", 
          "version": "String"
      }




------------------------------
##### **Logging.GetLogEntries**

Get the LogEntries matching the given filter. The result set will contain entries matching all filter rules combined. If multiple options are given for a single filter type, the result set will contain entries matching any of those. The offset starts at the newest entry in the result set. By default all items are returned. Example: If the specified filter returns a total amount of 100 entries:
- a offset value of 10 would include the oldest 90 entries
- a offset value of 0 would return all 100 entries

The offset is particularly useful in combination with the maxCount property and can be used for pagination. E.g. A result set of 10000 entries can be fetched in  batches of 1000 entries by fetching
1) offset 0, maxCount 1000: Entries 0 to 9999
2) offset 10000, maxCount 1000: Entries 10000 - 19999
3) offset 20000, maxCount 1000: Entries 20000 - 29999
...


*Params*


      {
          "o:deviceIds": [
              "Uuid"
          ], 
          "o:eventTypes": [
              "$ref:LoggingEventType"
          ], 
          "o:limit": "Int", 
          "o:loggingLevels": [
              "$ref:LoggingLevel"
          ], 
          "o:loggingSources": [
              "$ref:LoggingSource"
          ], 
          "o:offset": "Int", 
          "o:timeFilters": [
              {
                  "o:endDate": "Int", 
                  "o:startDate": "Int"
              }
          ], 
          "o:typeIds": [
              "Uuid"
          ], 
          "o:values": [
              "Variant"
          ]
      }


*Returns*


      {
          "count": "Int", 
          "loggingError": "$ref:LoggingError", 
          "o:logEntries": "$ref:LogEntries", 
          "offset": "Int"
      }


See also: [LogEntries](#logentries), [LoggingError](#loggingerror), [LoggingLevel](#logginglevel), [LoggingEventType](#loggingeventtype), [LoggingSource](#loggingsource)

------------------------------
##### **NetworkManager.ConnectWifiNetwork**

Connect to the wifi network with the given ssid and password.


*Params*


      {
          "interface": "String", 
          "o:password": "String", 
          "ssid": "String"
      }


*Returns*


      {
          "networkManagerError": "$ref:NetworkManagerError"
      }


See also: [NetworkManagerError](#networkmanagererror)

------------------------------
##### **NetworkManager.DisconnectInterface**

Disconnect the given network interface. The interface will remain disconnected until the user connect it again.


*Params*


      {
          "interface": "String"
      }


*Returns*


      {
          "networkManagerError": "$ref:NetworkManagerError"
      }


See also: [NetworkManagerError](#networkmanagererror)

------------------------------
##### **NetworkManager.EnableNetworking**

Enable or disable networking in the NetworkManager.


*Params*


      {
          "enable": "Bool"
      }


*Returns*


      {
          "networkManagerError": "$ref:NetworkManagerError"
      }


See also: [NetworkManagerError](#networkmanagererror)

------------------------------
##### **NetworkManager.EnableWirelessNetworking**

Enable or disable wireless networking in the NetworkManager.


*Params*


      {
          "enable": "Bool"
      }


*Returns*


      {
          "networkManagerError": "$ref:NetworkManagerError"
      }


See also: [NetworkManagerError](#networkmanagererror)

------------------------------
##### **NetworkManager.GetNetworkDevices**

Get the list of current network devices.


*Params*


      {}


*Returns*


      {
          "networkManagerError": "$ref:NetworkManagerError", 
          "wiredNetworkDevices": [
              "$ref:WiredNetworkDevice"
          ], 
          "wirelessNetworkDevices": [
              "$ref:WirelessNetworkDevice"
          ]
      }


See also: [NetworkManagerError](#networkmanagererror), [WiredNetworkDevice](#wirednetworkdevice), [WirelessNetworkDevice](#wirelessnetworkdevice)

------------------------------
##### **NetworkManager.GetNetworkStatus**

Get the current network manager status.


*Params*


      {}


*Returns*


      {
          "networkManagerError": "$ref:NetworkManagerError", 
          "o:status": {
              "networkingEnabled": "Bool", 
              "state": "$ref:NetworkManagerState", 
              "wirelessNetworkingEnabled": "Bool"
          }
      }


See also: [NetworkManagerError](#networkmanagererror), [NetworkManagerState](#networkmanagerstate)

------------------------------
##### **NetworkManager.GetWirelessAccessPoints**

Get the current list of wireless network access points for the given interface. The interface has to be a WirelessNetworkDevice.


*Params*


      {
          "interface": "String"
      }


*Returns*


      {
          "networkManagerError": "$ref:NetworkManagerError", 
          "o:wirelessAccessPoints": [
              "$ref:WirelessAccessPoint"
          ]
      }


See also: [NetworkManagerError](#networkmanagererror), [WirelessAccessPoint](#wirelessaccesspoint)

------------------------------
##### **NetworkManager.ScanWifiNetworks**

Start a wifi scan for searching new networks.


*Params*


      {
          "interface": "String"
      }


*Returns*


      {
          "networkManagerError": "$ref:NetworkManagerError"
      }


See also: [NetworkManagerError](#networkmanagererror)

------------------------------
##### **Rules.AddRule**

Add a rule. You can describe rules by one or many EventDesciptors and a StateEvaluator. Note that only one of either eventDescriptor or eventDescriptorList may be passed at a time. A rule can be created but left disabled, meaning it won't actually be executed until set to enabled. If not given, enabled defaults to true. A rule can have a list of actions and exitActions. It must have at least one Action. For state based rules, actions will be executed when the system enters a state matching the stateDescriptor. The exitActions will be executed when the system leaves the described state again. For event based rules, actions will be executed when a matching event happens and if the stateEvaluator matches the system's state. ExitActions for such rules will be executed when a matching event happens and the stateEvaluator is not matching the system's state. A rule marked as executable can be executed via the API using Rules.ExecuteRule, that means, its actions will be executed regardless of the eventDescriptor and stateEvaluators.


*Params*


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


*Returns*


      {
          "o:ruleId": "Uuid", 
          "ruleError": "$ref:RuleError"
      }


See also: [RuleError](#ruleerror), [RuleAction](#ruleaction), [TimeDescriptor](#timedescriptor), [RuleAction](#ruleaction), [EventDescriptor](#eventdescriptor), [StateEvaluator](#stateevaluator)

------------------------------
##### **Rules.DisableRule**

Disable a rule. The rule won't be triggered by it's events or state changes while it is disabled. If successful, the notification "Rule.RuleConfigurationChanged" will be emitted.


*Params*


      {
          "ruleId": "Uuid"
      }


*Returns*


      {
          "ruleError": "$ref:RuleError"
      }


See also: [RuleError](#ruleerror)

------------------------------
##### **Rules.EditRule**

Edit the parameters of a rule. The configuration of the rule with the given ruleId will be replaced with the new given configuration. In ordert to enable or disable a Rule, please use the methods "Rules.EnableRule" and "Rules.DisableRule". If successful, the notification "Rule.RuleConfigurationChanged" will be emitted.


*Params*


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


*Returns*


      {
          "o:rule": "$ref:Rule", 
          "ruleError": "$ref:RuleError"
      }


See also: [RuleError](#ruleerror), [Rule](#rule), [RuleAction](#ruleaction), [TimeDescriptor](#timedescriptor), [RuleAction](#ruleaction), [EventDescriptor](#eventdescriptor), [StateEvaluator](#stateevaluator)

------------------------------
##### **Rules.EnableRule**

Enabled a rule that has previously been disabled.If successful, the notification "Rule.RuleConfigurationChanged" will be emitted.


*Params*


      {
          "ruleId": "Uuid"
      }


*Returns*


      {
          "ruleError": "$ref:RuleError"
      }


See also: [RuleError](#ruleerror)

------------------------------
##### **Rules.ExecuteActions**

Execute the action list of the rule with the given ruleId.


*Params*


      {
          "ruleId": "Uuid"
      }


*Returns*


      {
          "ruleError": "$ref:RuleError"
      }


See also: [RuleError](#ruleerror)

------------------------------
##### **Rules.ExecuteExitActions**

Execute the exit action list of the rule with the given ruleId.


*Params*


      {
          "ruleId": "Uuid"
      }


*Returns*


      {
          "ruleError": "$ref:RuleError"
      }


See also: [RuleError](#ruleerror)

------------------------------
##### **Rules.FindRules**

Find a list of rules containing any of the given parameters.


*Params*


      {
          "deviceId": "Uuid"
      }


*Returns*


      {
          "ruleIds": [
              "Uuid"
          ]
      }




------------------------------
##### **Rules.GetRuleDetails**

Get details for the rule identified by ruleId


*Params*


      {
          "ruleId": "Uuid"
      }


*Returns*


      {
          "o:rule": "$ref:Rule", 
          "ruleError": "$ref:RuleError"
      }


See also: [RuleError](#ruleerror), [Rule](#rule)

------------------------------
##### **Rules.GetRules**

Get the descriptions of all configured rules. If you need more information about a specific rule use the method Rules.GetRuleDetails.


*Params*


      {}


*Returns*


      {
          "ruleDescriptions": [
              "$ref:RuleDescription"
          ]
      }


See also: [RuleDescription](#ruledescription)

------------------------------
##### **Rules.RemoveRule**

Remove a rule


*Params*


      {
          "ruleId": "Uuid"
      }


*Returns*


      {
          "ruleError": "$ref:RuleError"
      }


See also: [RuleError](#ruleerror)

------------------------------
##### **Scripts.AddScript**

Add a script


*Params*


      {
          "content": "String", 
          "name": "String"
      }


*Returns*


      {
          "o:errors": "StringList", 
          "o:script": "$ref:Script", 
          "scriptError": "$ref:ScriptError"
      }


See also: [ScriptError](#scripterror), [Script](#script)

------------------------------
##### **Scripts.EditScript**

Edit a script


*Params*


      {
          "id": "Uuid", 
          "o:content": "String", 
          "o:name": "String"
      }


*Returns*


      {
          "o:errors": "StringList", 
          "scriptError": "$ref:ScriptError"
      }


See also: [ScriptError](#scripterror)

------------------------------
##### **Scripts.GetScriptContent**

Get a scripts content.


*Params*


      {
          "id": "Uuid"
      }


*Returns*


      {
          "o:content": "String", 
          "scriptError": "$ref:ScriptError"
      }


See also: [ScriptError](#scripterror)

------------------------------
##### **Scripts.GetScripts**

Get all script, that is, their names and properties, but no content.


*Params*


      {}


*Returns*


      {
          "scripts": "$ref:Scripts"
      }


See also: [Scripts](#scripts)

------------------------------
##### **Scripts.RemoveScript**

remove a script


*Params*


      {
          "id": "Uuid"
      }


*Returns*


      {
          "scriptError": "$ref:ScriptError"
      }


See also: [ScriptError](#scripterror)

------------------------------
##### **States.GetStateType**

Get the StateType for the given stateTypeId.

> **Warning**: this method is deprecated. Please use the Devices namespace instead.

*Params*


      {
          "stateTypeId": "Uuid"
      }


*Returns*


      {
          "deviceError": "$ref:DeviceError", 
          "o:stateType": "$ref:StateType"
      }


See also: [StateType](#statetype), [DeviceError](#deviceerror)

------------------------------
##### **System.CheckForUpdates**

Instruct the system to poll the server for updates. Normally the system should automatically do this in regular intervals, however, if the client wants to allow the user to manually check for new updates now, this can be called. Returns true if the operation has been started successfully and the update manager will become busy. In order to know whether there are updates available, clients should walk through the list of packages retrieved from GetPackages and check whether there are packages with the updateAvailable flag set to true.


*Params*


      {}


*Returns*


      {
          "success": "Bool"
      }




------------------------------
##### **System.EnableRepository**

Enable or disable a repository.


*Params*


      {
          "enabled": "Bool", 
          "repositoryId": "String"
      }


*Returns*


      {
          "success": "Bool"
      }




------------------------------
##### **System.GetCapabilities**

Get the list of capabilites on this system. The property "powerManagement" indicates whether rebooting or shutting down is supported on this system. The property "updateManagement indicates whether system update features are available in this system. The property "timeManagement" indicates whether the system time can be configured on this system. Note that GetTime will be available in any case.


*Params*


      {}


*Returns*


      {
          "powerManagement": "Bool", 
          "timeManagement": "Bool", 
          "updateManagement": "Bool"
      }




------------------------------
##### **System.GetPackages**

Get the list of packages currently available to the system. This might include installed available but not installed packages. Installed packages will have the installedVersion set to a non-empty value.


*Params*


      {}


*Returns*


      {
          "packages": "$ref:Packages"
      }


See also: [Packages](#packages)

------------------------------
##### **System.GetRepositories**

Get the list of repositories currently available to the system.


*Params*


      {}


*Returns*


      {
          "repositories": "$ref:Repositories"
      }


See also: [Repositories](#repositories)

------------------------------
##### **System.GetTime**

Get the system time and configuraton. The "time" and "timeZone" properties give the current server time and time zone. "automaticTimeAvailable" indicates whether this system supports automatically setting the clock (e.g. using NTP). "automaticTime" will be true if the system is configured to automatically update the clock.


*Params*


      {}


*Returns*


      {
          "automaticTime": "Bool", 
          "automaticTimeAvailable": "Bool", 
          "time": "Uint", 
          "timeZone": "String"
      }




------------------------------
##### **System.GetTimeZones**

Returns the list of IANA specified time zone IDs which can be used to select a time zone. It is not required to use this method if the client toolkit already provides means to obtain a list of IANA time zone ids.


*Params*


      {}


*Returns*


      {
          "timeZones": "StringList"
      }




------------------------------
##### **System.GetUpdateStatus**

Get the current status of the update system. "busy" indicates that the system is current busy with an operation regarding updates. This does not necessarily mean an actual update is running. When this is true, update related functions on the client should be marked as busy and no interaction with update components shall be allowed. An example for such a state is when the system queries the server if there are updates available, typically after a call to CheckForUpdates. "updateRunning" on the other hand indicates an actual update process is ongoing. The user should be informed about it, the system also might restart at any point while an update is running.


*Params*


      {}


*Returns*


      {
          "busy": "Bool", 
          "updateRunning": "Bool"
      }




------------------------------
##### **System.Reboot**

Initiate a reboot of the system. The return value will indicate whether the procedure has been initiated successfully.


*Params*


      {}


*Returns*


      {
          "success": "Bool"
      }




------------------------------
##### **System.RemovePackages**

Starts removing a package. Returns true if the removal has been started successfully. Before calling this method, clients should check whether the package can be removed (canRemove set to true).


*Params*


      {
          "packageIds": [
              "String"
          ]
      }


*Returns*


      {
          "success": "Bool"
      }




------------------------------
##### **System.RollbackPackages**

Starts a rollback. Returns true if the rollback has been started successfully. Before calling this method, clients should check whether the package can be rolled back (canRollback set to true).


*Params*


      {
          "packageIds": [
              "String"
          ]
      }


*Returns*


      {
          "success": "Bool"
      }




------------------------------
##### **System.SetTime**

Set the system time configuraton. The system can be configured to update the time automatically by setting "automaticTime" to true. This will only work if the "timeManagement" capability is available on this system and "GetTime" indicates the availability of automatic time settings. If any of those requirements are not met, this method will return "false" in the "success" property. In order to manually configure the time, "automaticTime" should be set to false and "time" should be set. Note that if "automaticTime" is set to true and a manual "time" is still passed, the system will attempt to configure automatic time updates and only set the manual time if automatic mode fails. A time zone can always be passed optionally to change the system time zone and should be a IANA time zone id.


*Params*


      {
          "o:automaticTime": "Bool", 
          "o:time": "Uint", 
          "o:timeZone": "String"
      }


*Returns*


      {
          "success": "Bool"
      }




------------------------------
##### **System.Shutdown**

Initiate a shutdown of the system. The return value will indicate whether the procedure has been initiated successfully.


*Params*


      {}


*Returns*


      {
          "success": "Bool"
      }




------------------------------
##### **System.UpdatePackages**

Starts updating/installing packages with the given ids. Returns true if the upgrade has been started successfully. Note that it might still fail later. Before calling this method, clients should check the packages whether they are in a state where they can either be installed (no installedVersion set) or upgraded (updateAvailable set to true).


*Params*


      {
          "o:packageIds": [
              "String"
          ]
      }


*Returns*


      {
          "success": "Bool"
      }




------------------------------
##### **Tags.AddTag**

Add a Tag. A Tag must have a deviceId OR a ruleId (call this method twice if you want to attach the same tag to a device and a rule), an appId (Use the appId of your app), a tagId (e.g. "favorites") and a value. Upon success, a TagAdded notification will be emitted. Calling this method twice for the same ids (device/rule, appId and tagId) but with a different value will update the tag's value and the TagValueChanged notification will be emitted.


*Params*


      {
          "tag": "$ref:Tag"
      }


*Returns*


      {
          "tagError": "$ref:TagError"
      }


See also: [TagError](#tagerror), [Tag](#tag)

------------------------------
##### **Tags.GetTags**

Get the Tags matching the given filter. Tags can be filtered by a deviceID, a ruleId, an appId, a tagId or a combination of any (however, combining deviceId and ruleId will return an empty result set).


*Params*


      {
          "o:appId": "String", 
          "o:deviceId": "Uuid", 
          "o:ruleId": "Uuid", 
          "o:tagId": "String"
      }


*Returns*


      {
          "o:tags": "$ref:Tags", 
          "tagError": "$ref:TagError"
      }


See also: [TagError](#tagerror), [Tags](#tags)

------------------------------
##### **Tags.RemoveTag**

Remove a Tag. Tag value is optional and will be disregarded. If the ids match, the tag will be deleted and a TagRemoved notification will be emitted.


*Params*


      {
          "tag": "$ref:Tag"
      }


*Returns*


      {
          "tagError": "$ref:TagError"
      }


See also: [TagError](#tagerror), [Tag](#tag)

------------------------------
##### **Users.Authenticate**

Authenticate a client to the api via user & password challenge. Provide a device name which allows the user to identify the client and revoke the token in case the device is lost or stolen. This will return a new token to be used to authorize a client at the API.


*Params*


      {
          "deviceName": "String", 
          "password": "String", 
          "username": "String"
      }


*Returns*


      {
          "o:token": "String", 
          "success": "Bool"
      }




------------------------------
##### **Users.ChangePassword**

Change the password for the currently logged in user.


*Params*


      {
          "newPassword": "String"
      }


*Returns*


      {
          "error": "$ref:UserError"
      }


See also: [UserError](#usererror)

------------------------------
##### **Users.CreateUser**

Create a new user in the API. Currently this is only allowed to be called once when a new nymea instance is set up. Call Authenticate after this to obtain a device token for this user.


*Params*


      {
          "password": "String", 
          "username": "String"
      }


*Returns*


      {
          "error": "$ref:UserError"
      }


See also: [UserError](#usererror)

------------------------------
##### **Users.GetTokens**

Get all the tokens for the current user.


*Params*


      {}


*Returns*


      {
          "error": "$ref:UserError", 
          "o:tokenInfoList": "$ref:TokenInfoList"
      }


See also: [TokenInfoList](#tokeninfolist), [UserError](#usererror)

------------------------------
##### **Users.GetUserInfo**

Get info about the current token (the currently logged in user).


*Params*


      {}


*Returns*


      {
          "error": "$ref:UserError", 
          "o:userInfo": "$ref:UserInfo"
      }


See also: [UserInfo](#userinfo), [UserError](#usererror)

------------------------------
##### **Users.RemoveToken**

Revoke access for a given token.


*Params*


      {
          "tokenId": "Uuid"
      }


*Returns*


      {
          "error": "$ref:UserError"
      }


See also: [UserError](#usererror)

------------------------------
##### **Users.RequestPushButtonAuth**

Authenticate a client to the api via Push Button method. Provide a device name which allows the user to identify the client and revoke the token in case the device is lost or stolen. If push button hardware is available, this will return with success and start listening for push button presses. When the push button is pressed, the PushButtonAuthFinished notification will be sent to the requesting client. The procedure will be cancelled when the connection is interrupted. If another client requests push button authentication while a procedure is still going on, the second call will take over and the first one will be notified by the PushButtonAuthFinished signal about the error. The application should make it clear to the user to not press the button when the procedure fails as this can happen for 2 reasons: a) a second user is trying to auth at the same time and only the currently active user should press the button or b) it might indicate an attacker trying to take over and snooping in for tokens.


*Params*


      {
          "deviceName": "String"
      }


*Returns*


      {
          "success": "Bool", 
          "transactionId": "Int"
      }




------------------------------
### Notifications
 * [Configuration.BasicConfigurationChanged](#configurationbasicconfigurationchanged)
 * [Configuration.CloudConfigurationChanged](#configurationcloudconfigurationchanged)
 * [Configuration.LanguageChanged](#configurationlanguagechanged)
 * [Configuration.MqttPolicyChanged](#configurationmqttpolicychanged)
 * [Configuration.MqttPolicyRemoved](#configurationmqttpolicyremoved)
 * [Configuration.MqttServerConfigurationChanged](#configurationmqttserverconfigurationchanged)
 * [Configuration.MqttServerConfigurationRemoved](#configurationmqttserverconfigurationremoved)
 * [Configuration.TcpServerConfigurationChanged](#configurationtcpserverconfigurationchanged)
 * [Configuration.TcpServerConfigurationRemoved](#configurationtcpserverconfigurationremoved)
 * [Configuration.WebServerConfigurationChanged](#configurationwebserverconfigurationchanged)
 * [Configuration.WebServerConfigurationRemoved](#configurationwebserverconfigurationremoved)
 * [Configuration.WebSocketServerConfigurationChanged](#configurationwebsocketserverconfigurationchanged)
 * [Configuration.WebSocketServerConfigurationRemoved](#configurationwebsocketserverconfigurationremoved)
 * [Devices.DeviceAdded](#devicesdeviceadded)
 * [Devices.DeviceChanged](#devicesdevicechanged)
 * [Devices.DeviceRemoved](#devicesdeviceremoved)
 * [Devices.DeviceSettingChanged](#devicesdevicesettingchanged)
 * [Devices.EventTriggered](#deviceseventtriggered)
 * [Devices.PluginConfigurationChanged](#devicespluginconfigurationchanged)
 * [Devices.StateChanged](#devicesstatechanged)
 * [Events.EventTriggered](#eventseventtriggered)
 * [JSONRPC.CloudConnectedChanged](#jsonrpccloudconnectedchanged)
 * [JSONRPC.PushButtonAuthFinished](#jsonrpcpushbuttonauthfinished)
 * [Logging.LogDatabaseUpdated](#logginglogdatabaseupdated)
 * [Logging.LogEntryAdded](#logginglogentryadded)
 * [NetworkManager.NetworkStatusChanged](#networkmanagernetworkstatuschanged)
 * [NetworkManager.WiredNetworkDeviceAdded](#networkmanagerwirednetworkdeviceadded)
 * [NetworkManager.WiredNetworkDeviceChanged](#networkmanagerwirednetworkdevicechanged)
 * [NetworkManager.WiredNetworkDeviceRemoved](#networkmanagerwirednetworkdeviceremoved)
 * [NetworkManager.WirelessNetworkDeviceAdded](#networkmanagerwirelessnetworkdeviceadded)
 * [NetworkManager.WirelessNetworkDeviceChanged](#networkmanagerwirelessnetworkdevicechanged)
 * [NetworkManager.WirelessNetworkDeviceRemoved](#networkmanagerwirelessnetworkdeviceremoved)
 * [Rules.RuleActiveChanged](#rulesruleactivechanged)
 * [Rules.RuleAdded](#rulesruleadded)
 * [Rules.RuleConfigurationChanged](#rulesruleconfigurationchanged)
 * [Rules.RuleRemoved](#rulesruleremoved)
 * [Scripts.ScriptAdded](#scriptsscriptadded)
 * [Scripts.ScriptChanged](#scriptsscriptchanged)
 * [Scripts.ScriptContentChanged](#scriptsscriptcontentchanged)
 * [Scripts.ScriptLogMessage](#scriptsscriptlogmessage)
 * [Scripts.ScriptRemoved](#scriptsscriptremoved)
 * [System.CapabilitiesChanged](#systemcapabilitieschanged)
 * [System.PackageAdded](#systempackageadded)
 * [System.PackageChanged](#systempackagechanged)
 * [System.PackageRemoved](#systempackageremoved)
 * [System.RepositoryAdded](#systemrepositoryadded)
 * [System.RepositoryChanged](#systemrepositorychanged)
 * [System.RepositoryRemoved](#systemrepositoryremoved)
 * [System.TimeConfigurationChanged](#systemtimeconfigurationchanged)
 * [System.UpdateStatusChanged](#systemupdatestatuschanged)
 * [Tags.TagAdded](#tagstagadded)
 * [Tags.TagRemoved](#tagstagremoved)
 * [Tags.TagValueChanged](#tagstagvaluechanged)
 * [Users.PushButtonAuthFinished](#userspushbuttonauthfinished)
------------------------------
##### Configuration.BasicConfigurationChanged

Emitted whenever the basic configuration of this server changes.


*Params*


      {
          "basicConfiguration": {
              "d:language": "String", 
              "d:serverTime": "Uint", 
              "d:timeZone": "String", 
              "debugServerEnabled": "Bool", 
              "serverName": "String", 
              "serverUuid": "Uuid"
          }
      }

> **Warning**: following values are deprecated and will be removed with the next major API version: `serverTime`, `timeZone`, `language`



------------------------------
##### Configuration.CloudConfigurationChanged

Emitted whenever the cloud configuration is changed.


*Params*


      {
          "cloudConfiguration": {
              "enabled": "Bool"
          }
      }



------------------------------
##### Configuration.LanguageChanged

Emitted whenever the language of the server changed. The Plugins, Vendors and DeviceClasses have to be reloaded to get the translated data.


*Params*


      {
          "language": "String"
      }



------------------------------
##### Configuration.MqttPolicyChanged

Emitted whenever a MQTT broker policy is changed.


*Params*


      {
          "policy": "$ref:MqttPolicy"
      }

See also: [MqttPolicy](#mqttpolicy)

------------------------------
##### Configuration.MqttPolicyRemoved

Emitted whenever a MQTT broker policy is removed.


*Params*


      {
          "clientId": "String"
      }



------------------------------
##### Configuration.MqttServerConfigurationChanged

Emitted whenever the MQTT broker configuration is changed.


*Params*


      {
          "mqttServerConfiguration": "$ref:ServerConfiguration"
      }

See also: [ServerConfiguration](#serverconfiguration)

------------------------------
##### Configuration.MqttServerConfigurationRemoved

Emitted whenever a MQTT server configuration is removed.


*Params*


      {
          "id": "String"
      }



------------------------------
##### Configuration.TcpServerConfigurationChanged

Emitted whenever the TCP server configuration changes.


*Params*


      {
          "tcpServerConfiguration": "$ref:ServerConfiguration"
      }

See also: [ServerConfiguration](#serverconfiguration)

------------------------------
##### Configuration.TcpServerConfigurationRemoved

Emitted whenever a TCP server configuration is removed.


*Params*


      {
          "id": "String"
      }



------------------------------
##### Configuration.WebServerConfigurationChanged

Emitted whenever the web server configuration changes.


*Params*


      {
          "webServerConfiguration": "$ref:WebServerConfiguration"
      }

See also: [WebServerConfiguration](#webserverconfiguration)

------------------------------
##### Configuration.WebServerConfigurationRemoved

Emitted whenever a Web server configuration is removed.


*Params*


      {
          "id": "String"
      }



------------------------------
##### Configuration.WebSocketServerConfigurationChanged

Emitted whenever the web socket server configuration changes.


*Params*


      {
          "webSocketServerConfiguration": "$ref:ServerConfiguration"
      }

See also: [ServerConfiguration](#serverconfiguration)

------------------------------
##### Configuration.WebSocketServerConfigurationRemoved

Emitted whenever a WebSocket server configuration is removed.


*Params*


      {
          "id": "String"
      }



------------------------------
##### Devices.DeviceAdded

Emitted whenever a Device was added.


*Params*


      {
          "device": "$ref:Device"
      }

See also: [Device](#device)

------------------------------
##### Devices.DeviceChanged

Emitted whenever the params, name or setupStatus of a Device changes.


*Params*


      {
          "device": "$ref:Device"
      }

See also: [Device](#device)

------------------------------
##### Devices.DeviceRemoved

Emitted whenever a Device was removed.


*Params*


      {
          "deviceId": "Uuid"
      }



------------------------------
##### Devices.DeviceSettingChanged

Emitted whenever the setting of a Device is changed.


*Params*


      {
          "deviceId": "Uuid", 
          "paramTypeId": "Uuid", 
          "value": "Variant"
      }



------------------------------
##### Devices.EventTriggered

Emitted whenever an Event is triggered.


*Params*


      {
          "event": "$ref:Event"
      }

See also: [Event](#event)

------------------------------
##### Devices.PluginConfigurationChanged

Emitted whenever a plugin's configuration is changed.


*Params*


      {
          "configuration": "$ref:ParamList", 
          "pluginId": "Uuid"
      }

See also: [ParamList](#paramlist)

------------------------------
##### Devices.StateChanged

Emitted whenever a State of a device changes.


*Params*


      {
          "deviceId": "Uuid", 
          "stateTypeId": "Uuid", 
          "value": "Variant"
      }



------------------------------
##### Events.EventTriggered

Emitted whenever an Event is triggered.

> **Warning**: this notification is deprecated. Please use Devices.EventTriggered instead.

*Params*


      {
          "event": "$ref:Event"
      }

See also: [Event](#event)

------------------------------
##### JSONRPC.CloudConnectedChanged

Emitted whenever the cloud connection status changes.


*Params*


      {
          "connected": "Bool", 
          "connectionState": "$ref:CloudConnectionState"
      }

See also: [CloudConnectionState](#cloudconnectionstate)

------------------------------
##### JSONRPC.PushButtonAuthFinished

Emitted when a push button authentication reaches final state. NOTE: This notification is special. It will only be emitted to connections that did actively request a push button authentication, but also it will be emitted regardless of the notification settings. 

> **Warning**: this notification is deprecated. Use Users.PushButtonAuthFinished instead.

*Params*


      {
          "o:token": "String", 
          "success": "Bool", 
          "transactionId": "Int"
      }



------------------------------
##### Logging.LogDatabaseUpdated

Emitted whenever the database was updated. The database will be updated when a log entry was deleted. A log entry will be deleted when the corresponding device or a rule will be removed, or when the oldest entry of the database was deleted to keep to database in the size limits.


*Params*


      {}



------------------------------
##### Logging.LogEntryAdded

Emitted whenever an entry is appended to the logging system. 


*Params*


      {
          "logEntry": "$ref:LogEntry"
      }

See also: [LogEntry](#logentry)

------------------------------
##### NetworkManager.NetworkStatusChanged

Emitted whenever a status of a NetworkManager changes.


*Params*


      {
          "status": {
              "networkingEnabled": "Bool", 
              "state": "$ref:NetworkManagerState", 
              "wirelessNetworkingEnabled": "Bool"
          }
      }

See also: [NetworkManagerState](#networkmanagerstate)

------------------------------
##### NetworkManager.WiredNetworkDeviceAdded

Emitted whenever a new WiredNetworkDevice was added.


*Params*


      {
          "wiredNetworkDevice": "$ref:WiredNetworkDevice"
      }

See also: [WiredNetworkDevice](#wirednetworkdevice)

------------------------------
##### NetworkManager.WiredNetworkDeviceChanged

Emitted whenever the given WiredNetworkDevice has changed.


*Params*


      {
          "wiredNetworkDevice": "$ref:WiredNetworkDevice"
      }

See also: [WiredNetworkDevice](#wirednetworkdevice)

------------------------------
##### NetworkManager.WiredNetworkDeviceRemoved

Emitted whenever a WiredNetworkDevice was removed.


*Params*


      {
          "interface": "String"
      }



------------------------------
##### NetworkManager.WirelessNetworkDeviceAdded

Emitted whenever a new WirelessNetworkDevice was added.


*Params*


      {
          "wirelessNetworkDevice": "$ref:WirelessNetworkDevice"
      }

See also: [WirelessNetworkDevice](#wirelessnetworkdevice)

------------------------------
##### NetworkManager.WirelessNetworkDeviceChanged

Emitted whenever the given WirelessNetworkDevice has changed.


*Params*


      {
          "wirelessNetworkDevice": "$ref:WirelessNetworkDevice"
      }

See also: [WirelessNetworkDevice](#wirelessnetworkdevice)

------------------------------
##### NetworkManager.WirelessNetworkDeviceRemoved

Emitted whenever a WirelessNetworkDevice was removed.


*Params*


      {
          "interface": "String"
      }



------------------------------
##### Rules.RuleActiveChanged

Emitted whenever the active state of a Rule changed.


*Params*


      {
          "active": "Bool", 
          "ruleId": "Uuid"
      }



------------------------------
##### Rules.RuleAdded

Emitted whenever a Rule was added.


*Params*


      {
          "rule": "$ref:Rule"
      }

See also: [Rule](#rule)

------------------------------
##### Rules.RuleConfigurationChanged

Emitted whenever the configuration of a Rule changed.


*Params*


      {
          "rule": "$ref:Rule"
      }

See also: [Rule](#rule)

------------------------------
##### Rules.RuleRemoved

Emitted whenever a Rule was removed.


*Params*


      {
          "ruleId": "Uuid"
      }



------------------------------
##### Scripts.ScriptAdded

Emitted when a script has been added to the system.


*Params*


      {
          "script": "$ref:Script"
      }

See also: [Script](#script)

------------------------------
##### Scripts.ScriptChanged

Emitted when a script has been changed in the system (e.g. renamed).


*Params*


      {
          "name": "String", 
          "scriptId": "Uuid"
      }



------------------------------
##### Scripts.ScriptContentChanged

Emitted when a script's content has been changed in the system.


*Params*


      {
          "scriptId": "Uuid"
      }



------------------------------
##### Scripts.ScriptLogMessage

Emitted when a script produces a console message.


*Params*


      {
          "message": "String", 
          "scriptId": "Uuid", 
          "type": "$ref:ScriptMessageType"
      }

See also: [ScriptMessageType](#scriptmessagetype)

------------------------------
##### Scripts.ScriptRemoved

Emitted when a script has been removed from the system.


*Params*


      {
          "id": "Uuid"
      }



------------------------------
##### System.CapabilitiesChanged

Emitted whenever the system capabilities change.


*Params*


      {
          "powerManagement": "Bool", 
          "updateManagement": "Bool"
      }



------------------------------
##### System.PackageAdded

Emitted whenever a package is added to the list of packages.


*Params*


      {
          "package": "$ref:Package"
      }

See also: [Package](#package)

------------------------------
##### System.PackageChanged

Emitted whenever a package in the list of packages changes.


*Params*


      {
          "package": "$ref:Package"
      }

See also: [Package](#package)

------------------------------
##### System.PackageRemoved

Emitted whenever a package is removed from the list of packages.


*Params*


      {
          "packageId": "String"
      }



------------------------------
##### System.RepositoryAdded

Emitted whenever a repository is added to the list of repositories.


*Params*


      {
          "repository": "$ref:Repository"
      }

See also: [Repository](#repository)

------------------------------
##### System.RepositoryChanged

Emitted whenever a repository in the list of repositories changes.


*Params*


      {
          "repository": "$ref:Repository"
      }

See also: [Repository](#repository)

------------------------------
##### System.RepositoryRemoved

Emitted whenever a repository is removed from the list of repositories.


*Params*


      {
          "repositoryId": "String"
      }



------------------------------
##### System.TimeConfigurationChanged

Emitted whenever the time configuration is changed


*Params*


      {
          "automaticTime": "Bool", 
          "automaticTimeAvailable": "Bool", 
          "time": "Uint", 
          "timeZone": "String"
      }



------------------------------
##### System.UpdateStatusChanged

Emitted whenever the update status changes.


*Params*


      {
          "busy": "Bool", 
          "updateRunning": "Bool"
      }



------------------------------
##### Tags.TagAdded

Emitted whenever a tag is added to the system. 


*Params*


      {
          "tag": "$ref:Tag"
      }

See also: [Tag](#tag)

------------------------------
##### Tags.TagRemoved

Emitted whenever a tag is removed from the system. 


*Params*


      {
          "tag": "$ref:Tag"
      }

See also: [Tag](#tag)

------------------------------
##### Tags.TagValueChanged

Emitted whenever a tag's value is changed in the system. 


*Params*


      {
          "tag": "$ref:Tag"
      }

See also: [Tag](#tag)

------------------------------
##### Users.PushButtonAuthFinished

Emitted when a push button authentication reaches final state. NOTE: This notification is special. It will only be emitted to connections that did actively request a push button authentication, but also it will be emitted regardless of the notification settings.


*Params*


      {
          "o:token": "String", 
          "success": "Bool", 
          "transactionId": "Int"
      }




## Full introspect


      {
          "enums": {
              "BasicType": [
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
              ], 
              "BrowserIcon": [
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
              ], 
              "CloudConnectionState": [
                  "CloudConnectionStateDisabled", 
                  "CloudConnectionStateUnconfigured", 
                  "CloudConnectionStateConnecting", 
                  "CloudConnectionStateConnected"
              ], 
              "ConfigurationError": [
                  "ConfigurationErrorNoError", 
                  "ConfigurationErrorInvalidTimeZone", 
                  "ConfigurationErrorInvalidStationName", 
                  "ConfigurationErrorInvalidId", 
                  "ConfigurationErrorInvalidPort", 
                  "ConfigurationErrorInvalidHostAddress", 
                  "ConfigurationErrorBluetoothHardwareNotAvailable", 
                  "ConfigurationErrorInvalidCertificate"
              ], 
              "CreateMethod": [
                  "CreateMethodUser", 
                  "CreateMethodAuto", 
                  "CreateMethodDiscovery"
              ], 
              "DeviceError": [
                  "DeviceErrorNoError", 
                  "DeviceErrorPluginNotFound", 
                  "DeviceErrorVendorNotFound", 
                  "DeviceErrorDeviceNotFound", 
                  "DeviceErrorDeviceClassNotFound", 
                  "DeviceErrorActionTypeNotFound", 
                  "DeviceErrorStateTypeNotFound", 
                  "DeviceErrorEventTypeNotFound", 
                  "DeviceErrorDeviceDescriptorNotFound", 
                  "DeviceErrorMissingParameter", 
                  "DeviceErrorInvalidParameter", 
                  "DeviceErrorSetupFailed", 
                  "DeviceErrorDuplicateUuid", 
                  "DeviceErrorCreationMethodNotSupported", 
                  "DeviceErrorSetupMethodNotSupported", 
                  "DeviceErrorHardwareNotAvailable", 
                  "DeviceErrorHardwareFailure", 
                  "DeviceErrorAuthenticationFailure", 
                  "DeviceErrorDeviceInUse", 
                  "DeviceErrorDeviceInRule", 
                  "DeviceErrorDeviceIsChild", 
                  "DeviceErrorPairingTransactionIdNotFound", 
                  "DeviceErrorParameterNotWritable", 
                  "DeviceErrorItemNotFound", 
                  "DeviceErrorItemNotExecutable", 
                  "DeviceErrorUnsupportedFeature", 
                  "DeviceErrorTimeout"
              ], 
              "DeviceSetupStatus": [
                  "DeviceSetupStatusNone", 
                  "DeviceSetupStatusInProgress", 
                  "DeviceSetupStatusComplete", 
                  "DeviceSetupStatusFailed"
              ], 
              "InputType": [
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
              ], 
              "LoggingError": [
                  "LoggingErrorNoError", 
                  "LoggingErrorLogEntryNotFound", 
                  "LoggingErrorInvalidFilterParameter"
              ], 
              "LoggingEventType": [
                  "LoggingEventTypeTrigger", 
                  "LoggingEventTypeActiveChange", 
                  "LoggingEventTypeEnabledChange", 
                  "LoggingEventTypeActionsExecuted", 
                  "LoggingEventTypeExitActionsExecuted"
              ], 
              "LoggingLevel": [
                  "LoggingLevelInfo", 
                  "LoggingLevelAlert"
              ], 
              "LoggingSource": [
                  "LoggingSourceSystem", 
                  "LoggingSourceEvents", 
                  "LoggingSourceActions", 
                  "LoggingSourceStates", 
                  "LoggingSourceRules", 
                  "LoggingSourceBrowserActions"
              ], 
              "MediaBrowserIcon": [
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
                  "MediaBrowserIconSoundCloud"
              ], 
              "NetworkDeviceState": [
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
              ], 
              "NetworkManagerError": [
                  "NetworkManagerErrorNoError", 
                  "NetworkManagerErrorUnknownError", 
                  "NetworkManagerErrorWirelessNotAvailable", 
                  "NetworkManagerErrorAccessPointNotFound", 
                  "NetworkManagerErrorNetworkInterfaceNotFound", 
                  "NetworkManagerErrorInvalidNetworkDeviceType", 
                  "NetworkManagerErrorWirelessNetworkingDisabled", 
                  "NetworkManagerErrorWirelessConnectionFailed", 
                  "NetworkManagerErrorNetworkingDisabled", 
                  "NetworkManagerErrorNetworkManagerNotAvailable"
              ], 
              "NetworkManagerState": [
                  "NetworkManagerStateUnknown", 
                  "NetworkManagerStateAsleep", 
                  "NetworkManagerStateDisconnected", 
                  "NetworkManagerStateDisconnecting", 
                  "NetworkManagerStateConnecting", 
                  "NetworkManagerStateConnectedLocal", 
                  "NetworkManagerStateConnectedSite", 
                  "NetworkManagerStateConnectedGlobal"
              ], 
              "RemovePolicy": [
                  "RemovePolicyCascade", 
                  "RemovePolicyUpdate"
              ], 
              "RepeatingMode": [
                  "RepeatingModeNone", 
                  "RepeatingModeHourly", 
                  "RepeatingModeDaily", 
                  "RepeatingModeWeekly", 
                  "RepeatingModeMonthly", 
                  "RepeatingModeYearly"
              ], 
              "RuleError": [
                  "RuleErrorNoError", 
                  "RuleErrorInvalidRuleId", 
                  "RuleErrorRuleNotFound", 
                  "RuleErrorDeviceNotFound", 
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
              ], 
              "ScriptError": [
                  "ScriptErrorNoError", 
                  "ScriptErrorScriptNotFound", 
                  "ScriptErrorInvalidScript", 
                  "ScriptErrorHardwareFailure"
              ], 
              "ScriptMessageType": [
                  "ScriptMessageTypeLog", 
                  "ScriptMessageTypeWarning"
              ], 
              "SetupMethod": [
                  "SetupMethodJustAdd", 
                  "SetupMethodDisplayPin", 
                  "SetupMethodEnterPin", 
                  "SetupMethodPushButton", 
                  "SetupMethodUserAndPassword", 
                  "SetupMethodOAuth"
              ], 
              "StateOperator": [
                  "StateOperatorAnd", 
                  "StateOperatorOr"
              ], 
              "TagError": [
                  "TagErrorNoError", 
                  "TagErrorDeviceNotFound", 
                  "TagErrorRuleNotFound", 
                  "TagErrorTagNotFound"
              ], 
              "Unit": [
                  "UnitNone", 
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
                  "UnitMicroSiemensPerCentimeter", 
                  "UnitDuration"
              ], 
              "UserError": [
                  "UserErrorNoError", 
                  "UserErrorBackendError", 
                  "UserErrorInvalidUserId", 
                  "UserErrorDuplicateUserId", 
                  "UserErrorBadPassword", 
                  "UserErrorTokenNotFound", 
                  "UserErrorPermissionDenied"
              ], 
              "ValueOperator": [
                  "ValueOperatorEquals", 
                  "ValueOperatorNotEquals", 
                  "ValueOperatorLess", 
                  "ValueOperatorGreater", 
                  "ValueOperatorLessOrEqual", 
                  "ValueOperatorGreaterOrEqual"
              ]
          }, 
          "flags": {
              "CreateMethods": [
                  "$ref:CreateMethod"
              ]
          }, 
          "methods": {
              "Actions.ExecuteAction": {
                  "deprecated": "Please use Devices.ExecuteAction instead.", 
                  "description": "Execute a single action.", 
                  "params": {
                      "actionTypeId": "Uuid", 
                      "deviceId": "Uuid", 
                      "o:params": "$ref:ParamList"
                  }, 
                  "returns": {
                      "deviceError": "$ref:DeviceError", 
                      "o:displayMessage": "String"
                  }
              }, 
              "Actions.ExecuteBrowserItem": {
                  "deprecated": "Please use Devices.ExecuteBrowserItem instead.", 
                  "description": "Execute the item identified by itemId on the given device.", 
                  "params": {
                      "deviceId": "Uuid", 
                      "itemId": "String"
                  }, 
                  "returns": {
                      "deviceError": "$ref:DeviceError"
                  }
              }, 
              "Actions.ExecuteBrowserItemAction": {
                  "deprecated": "Please use Devices.ExecuteBrowserItem instead.", 
                  "description": "Execute the action for the browser item identified by actionTypeId and the itemId on the given device.", 
                  "params": {
                      "actionTypeId": "Uuid", 
                      "deviceId": "Uuid", 
                      "itemId": "String", 
                      "o:params": "$ref:ParamList"
                  }, 
                  "returns": {
                      "deviceError": "$ref:DeviceError"
                  }
              }, 
              "Actions.GetActionType": {
                  "deprecated": "Please use the Devices namespace instead.", 
                  "description": "Get the ActionType for the given ActionTypeId.", 
                  "params": {
                      "actionTypeId": "Uuid"
                  }, 
                  "returns": {
                      "deviceError": "$ref:DeviceError", 
                      "o:actionType": "$ref:ActionType"
                  }
              }, 
              "Configuration.DeleteMqttPolicy": {
                  "description": "Delete a MQTT policy from the broker.", 
                  "params": {
                      "clientId": "String"
                  }, 
                  "returns": {
                      "configurationError": "$ref:ConfigurationError"
                  }
              }, 
              "Configuration.DeleteMqttServerConfiguration": {
                  "description": "Delete a MQTT Server interface of the server.", 
                  "params": {
                      "id": "String"
                  }, 
                  "returns": {
                      "configurationError": "$ref:ConfigurationError"
                  }
              }, 
              "Configuration.DeleteTcpServerConfiguration": {
                  "description": "Delete a TCP interface of the server. Note: if you are deleting the configuration for the interface you are currently connected to, the connection will be dropped.", 
                  "params": {
                      "id": "String"
                  }, 
                  "returns": {
                      "configurationError": "$ref:ConfigurationError"
                  }
              }, 
              "Configuration.DeleteWebServerConfiguration": {
                  "description": "Delete a WebServer interface of the server.", 
                  "params": {
                      "id": "String"
                  }, 
                  "returns": {
                      "configurationError": "$ref:ConfigurationError"
                  }
              }, 
              "Configuration.DeleteWebSocketServerConfiguration": {
                  "description": "Delete a WebSocket Server interface of the server. Note: if you are deleting the configuration for the interface you are currently connected to, the connection will be dropped.", 
                  "params": {
                      "id": "String"
                  }, 
                  "returns": {
                      "configurationError": "$ref:ConfigurationError"
                  }
              }, 
              "Configuration.GetAvailableLanguages": {
                  "deprecated": "Use the locale property in the Handshake message instead.", 
                  "description": "Returns a list of locale codes available for the server. i.e. en_US, de_AT", 
                  "params": {}, 
                  "returns": {
                      "languages": [
                          "String"
                      ]
                  }
              }, 
              "Configuration.GetConfigurations": {
                  "description": "Get all configuration parameters of the server.", 
                  "params": {}, 
                  "returns": {
                      "basicConfiguration": {
                          "d:language": "String", 
                          "d:serverTime": "Uint", 
                          "d:timeZone": "String", 
                          "debugServerEnabled": "Bool", 
                          "serverName": "String", 
                          "serverUuid": "Uuid"
                      }, 
                      "cloud": {
                          "enabled": "Bool"
                      }, 
                      "tcpServerConfigurations": [
                          "$ref:ServerConfiguration"
                      ], 
                      "webServerConfigurations": [
                          "$ref:WebServerConfiguration"
                      ], 
                      "webSocketServerConfigurations": [
                          "$ref:ServerConfiguration"
                      ]
                  }
              }, 
              "Configuration.GetMqttPolicies": {
                  "description": "Get all MQTT broker policies.", 
                  "params": {}, 
                  "returns": {
                      "mqttPolicies": [
                          "$ref:MqttPolicy"
                      ]
                  }
              }, 
              "Configuration.GetMqttServerConfigurations": {
                  "description": "Get all MQTT Server configurations.", 
                  "params": {}, 
                  "returns": {
                      "mqttServerConfigurations": [
                          "$ref:ServerConfiguration"
                      ]
                  }
              }, 
              "Configuration.GetTimeZones": {
                  "deprecated": "Use System.GetTimeZones instead.", 
                  "description": "Get the list of available timezones.", 
                  "params": {}, 
                  "returns": {
                      "timeZones": [
                          "String"
                      ]
                  }
              }, 
              "Configuration.SetCloudEnabled": {
                  "description": "Sets whether the cloud connection is enabled or disabled in the settings.", 
                  "params": {
                      "enabled": "Bool"
                  }, 
                  "returns": {
                      "configurationError": "$ref:ConfigurationError"
                  }
              }, 
              "Configuration.SetDebugServerEnabled": {
                  "description": "Enable or disable the debug server.", 
                  "params": {
                      "enabled": "String"
                  }, 
                  "returns": {
                      "configurationError": "$ref:ConfigurationError"
                  }
              }, 
              "Configuration.SetLanguage": {
                  "deprecated": "Use the locale property in the Handshake message instead.", 
                  "description": "Sets the server language to the given language. See also: \"GetAvailableLanguages\"", 
                  "params": {
                      "language": "String"
                  }, 
                  "returns": {
                      "configurationError": "$ref:ConfigurationError"
                  }
              }, 
              "Configuration.SetMqttPolicy": {
                  "description": "Configure a MQTT broker policy. If the ID is an existing one, the existing policy will be modified, otherwise a new one will be added.", 
                  "params": {
                      "policy": "$ref:MqttPolicy"
                  }, 
                  "returns": {
                      "configurationError": "$ref:ConfigurationError"
                  }
              }, 
              "Configuration.SetMqttServerConfiguration": {
                  "description": "Configure a MQTT Server interface on the MQTT broker. If the ID is an existing one, the existing config will be modified, otherwise a new one will be added. Setting authenticationEnabled to true will require MQTT clients to use credentials set in the MQTT broker policies.", 
                  "params": {
                      "configuration": "$ref:ServerConfiguration"
                  }, 
                  "returns": {
                      "configurationError": "$ref:ConfigurationError"
                  }
              }, 
              "Configuration.SetServerName": {
                  "description": "Set the name of the server. Default is nymea.", 
                  "params": {
                      "serverName": "String"
                  }, 
                  "returns": {
                      "configurationError": "$ref:ConfigurationError"
                  }
              }, 
              "Configuration.SetTcpServerConfiguration": {
                  "description": "Configure a TCP interface of the server. If the ID is an existing one, the existing config will be modified, otherwise a new one will be added. Note: if you are changing the configuration for the interface you are currently connected to, the connection will be dropped.", 
                  "params": {
                      "configuration": "$ref:ServerConfiguration"
                  }, 
                  "returns": {
                      "configurationError": "$ref:ConfigurationError"
                  }
              }, 
              "Configuration.SetTimeZone": {
                  "deprecated": "Use System.SetTimeZone instead.", 
                  "description": "Set the time zone of the server. See also: \"GetTimeZones\"", 
                  "params": {
                      "timeZone": "String"
                  }, 
                  "returns": {
                      "configurationError": "$ref:ConfigurationError"
                  }
              }, 
              "Configuration.SetWebServerConfiguration": {
                  "description": "Configure a WebServer interface of the server. If the ID is an existing one, the existing config will be modified, otherwise a new one will be added.", 
                  "params": {
                      "configuration": "$ref:WebServerConfiguration"
                  }, 
                  "returns": {
                      "configurationError": "$ref:ConfigurationError"
                  }
              }, 
              "Configuration.SetWebSocketServerConfiguration": {
                  "description": "Configure a WebSocket Server interface of the server. If the ID is an existing one, the existing config will be modified, otherwise a new one will be added. Note: if you are changing the configuration for the interface you are currently connected to, the connection will be dropped.", 
                  "params": {
                      "configuration": "$ref:ServerConfiguration"
                  }, 
                  "returns": {
                      "configurationError": "$ref:ConfigurationError"
                  }
              }, 
              "Devices.AddConfiguredDevice": {
                  "description": "Add a configured device with a setupMethod of SetupMethodJustAdd. For devices with a setupMethod different than SetupMethodJustAdd, use PairDevice. Devices with CreateMethodJustAdd require all parameters to be supplied here. Devices with CreateMethodDiscovery require the use of a deviceDescriptorId. For discovered devices params are not required and will be taken from the DeviceDescriptor, however, they may be overridden by supplying deviceParams.", 
                  "params": {
                      "deviceClassId": "Uuid", 
                      "name": "String", 
                      "o:deviceDescriptorId": "Uuid", 
                      "o:deviceParams": "$ref:ParamList"
                  }, 
                  "returns": {
                      "deviceError": "$ref:DeviceError", 
                      "o:deviceId": "Uuid", 
                      "o:displayMessage": "String"
                  }
              }, 
              "Devices.BrowseDevice": {
                  "description": "Browse a device. If a DeviceClass indicates a device is browsable, this method will return the BrowserItems. If no parameter besides the deviceId is used, the root node of this device will be returned. Any returned item which is browsable can be passed as node. Results will be children of the given node.", 
                  "params": {
                      "deviceId": "Uuid", 
                      "o:itemId": "String"
                  }, 
                  "returns": {
                      "deviceError": "$ref:DeviceError", 
                      "items": [
                          "$ref:BrowserItem"
                      ]
                  }
              }, 
              "Devices.ConfirmPairing": {
                  "description": "Confirm an ongoing pairing. For SetupMethodUserAndPassword, provide the username in the \"username\" field and the password in the \"secret\" field. For SetupMethodEnterPin and provide the PIN in the \"secret\" field. In case of SetupMethodOAuth, the previously opened web view will eventually be redirected to http://128.0.0.1:8888 and the OAuth code as query parameters to this url. Provide the entire unmodified URL in the secret field.", 
                  "params": {
                      "o:secret": "String", 
                      "o:username": "String", 
                      "pairingTransactionId": "Uuid"
                  }, 
                  "returns": {
                      "deviceError": "$ref:DeviceError", 
                      "o:deviceId": "Uuid", 
                      "o:displayMessage": "String"
                  }
              }, 
              "Devices.EditDevice": {
                  "description": "Edit the name of a device. This method does not change the configuration of the device.", 
                  "params": {
                      "deviceId": "Uuid", 
                      "name": "String"
                  }, 
                  "returns": {
                      "deviceError": "$ref:DeviceError"
                  }
              }, 
              "Devices.ExecuteAction": {
                  "description": "Execute a single action.", 
                  "params": {
                      "actionTypeId": "Uuid", 
                      "deviceId": "Uuid", 
                      "o:params": "$ref:ParamList"
                  }, 
                  "returns": {
                      "deviceError": "$ref:DeviceError", 
                      "o:displayMessage": "String"
                  }
              }, 
              "Devices.ExecuteBrowserItem": {
                  "description": "Execute the item identified by itemId on the given device.", 
                  "params": {
                      "deviceId": "Uuid", 
                      "itemId": "String"
                  }, 
                  "returns": {
                      "deviceError": "$ref:DeviceError"
                  }
              }, 
              "Devices.ExecuteBrowserItemAction": {
                  "description": "Execute the action for the browser item identified by actionTypeId and the itemId on the given device.", 
                  "params": {
                      "actionTypeId": "Uuid", 
                      "deviceId": "Uuid", 
                      "itemId": "String", 
                      "o:params": "$ref:ParamList"
                  }, 
                  "returns": {
                      "deviceError": "$ref:DeviceError"
                  }
              }, 
              "Devices.GetActionTypes": {
                  "description": "Get action types for a specified deviceClassId.", 
                  "params": {
                      "deviceClassId": "Uuid"
                  }, 
                  "returns": {
                      "actionTypes": "$ref:ActionTypes"
                  }
              }, 
              "Devices.GetBrowserItem": {
                  "description": "Get a single item from the browser. This won't give any more info on an item than a regular browseDevice call, but it allows to fetch details of an item if only the ID is known.", 
                  "params": {
                      "deviceId": "Uuid", 
                      "o:itemId": "String"
                  }, 
                  "returns": {
                      "deviceError": "$ref:DeviceError", 
                      "o:item": "$ref:BrowserItem"
                  }
              }, 
              "Devices.GetConfiguredDevices": {
                  "description": "Returns a list of configured devices, optionally filtered by deviceId.", 
                  "params": {
                      "o:deviceId": "Uuid"
                  }, 
                  "returns": {
                      "devices": "$ref:Devices"
                  }
              }, 
              "Devices.GetDiscoveredDevices": {
                  "description": "Performs a device discovery and returns the results. This function may take a while to return. Note that this method will include all the found devices, that is, including devices that may already have been added. Those devices will have deviceId set to the device id of the already added device. Such results may be used to reconfigure existing devices and might be filtered in cases where only unknown devices are of interest.", 
                  "params": {
                      "deviceClassId": "Uuid", 
                      "o:discoveryParams": "$ref:ParamList"
                  }, 
                  "returns": {
                      "deviceError": "$ref:DeviceError", 
                      "o:deviceDescriptors": "$ref:DeviceDescriptors", 
                      "o:displayMessage": "String"
                  }
              }, 
              "Devices.GetEventTypes": {
                  "description": "Get event types for a specified deviceClassId.", 
                  "params": {
                      "deviceClassId": "Uuid"
                  }, 
                  "returns": {
                      "eventTypes": "$ref:EventTypes"
                  }
              }, 
              "Devices.GetPluginConfiguration": {
                  "description": "Get a plugin's params.", 
                  "params": {
                      "pluginId": "Uuid"
                  }, 
                  "returns": {
                      "deviceError": "$ref:DeviceError", 
                      "o:configuration": "$ref:ParamList"
                  }
              }, 
              "Devices.GetPlugins": {
                  "description": "Returns a list of loaded plugins.", 
                  "params": {}, 
                  "returns": {
                      "plugins": "$ref:DevicePlugins"
                  }
              }, 
              "Devices.GetStateTypes": {
                  "description": "Get state types for a specified deviceClassId.", 
                  "params": {
                      "deviceClassId": "Uuid"
                  }, 
                  "returns": {
                      "stateTypes": "$ref:StateTypes"
                  }
              }, 
              "Devices.GetStateValue": {
                  "description": "Get the value of the given device and the given stateType", 
                  "params": {
                      "deviceId": "Uuid", 
                      "stateTypeId": "Uuid"
                  }, 
                  "returns": {
                      "deviceError": "$ref:DeviceError", 
                      "o:value": "Variant"
                  }
              }, 
              "Devices.GetStateValues": {
                  "description": "Get all the state values of the given device.", 
                  "params": {
                      "deviceId": "Uuid"
                  }, 
                  "returns": {
                      "deviceError": "$ref:DeviceError", 
                      "o:values": "$ref:States"
                  }
              }, 
              "Devices.GetSupportedDevices": {
                  "description": "Returns a list of supported Device classes, optionally filtered by vendorId.", 
                  "params": {
                      "o:vendorId": "Uuid"
                  }, 
                  "returns": {
                      "deviceClasses": "$ref:DeviceClasses"
                  }
              }, 
              "Devices.GetSupportedVendors": {
                  "description": "Returns a list of supported Vendors.", 
                  "params": {}, 
                  "returns": {
                      "vendors": "$ref:Vendors"
                  }
              }, 
              "Devices.PairDevice": {
                  "description": "Pair a device. Use this to set up or reconfigure devices for DeviceClasses with a setupMethod different than SetupMethodJustAdd. Depending on the CreateMethod and whether a new devices is set up or an existing one is reconfigured, different parameters are required:\nCreateMethodJustAdd takes the deviceClassId and the parameters you want to have with that device.\nCreateMethodDiscovery requires the use of a deviceDescriptorId, previously obtained with DiscoverDevices. Optionally, parameters can be overridden with the give deviceParams.\nIf an existing device should be reconfigured, the deviceId of said device should be given additionally.\nIf success is true, the return values will contain a pairingTransactionId, a displayMessage and the setupMethod. Depending on the setupMethod, the application should present the use an appropriate login mask, that is, For SetupMethodDisplayPin the user should enter a pin that is displayed on the device, for SetupMethodEnterPin the application should present the given PIN so the user can enter it on the device. For SetupMethodPushButton, the displayMessage shall be presented to the user as informational hints to press a button on the device. For SetupMethodUserAndPassword a login mask for a user and password login should be presented to the user. In case of SetupMethodOAuth, an OAuth URL will be returned which shall be opened in a web view to allow the user logging in.\nOnce the login procedure has completed, the application shall proceed with ConfirmPairing, providing the results of the pairing procedure.", 
                  "params": {
                      "o:deviceClassId": "Uuid", 
                      "o:deviceDescriptorId": "Uuid", 
                      "o:deviceId": "Uuid", 
                      "o:deviceParams": "$ref:ParamList", 
                      "o:name": "String"
                  }, 
                  "returns": {
                      "deviceError": "$ref:DeviceError", 
                      "o:displayMessage": "String", 
                      "o:oAuthUrl": "String", 
                      "o:pairingTransactionId": "Uuid", 
                      "o:pin": "String", 
                      "o:setupMethod": "$ref:SetupMethod"
                  }
              }, 
              "Devices.ReconfigureDevice": {
                  "description": "Reconfigure a device. This comes down to removing and recreating a device with new parameters but keeping its device id the same (and with that keeping rules, tags etc). For devices with create method CreateMethodDiscovery, a discovery (GetDiscoveredDevices) shall be performed first and this method is to be called with a deviceDescriptorId of the re-discovered device instead of the deviceId directly. Device parameters will be taken from the discovery, but can be overridden individually here by providing them in the deviceParams parameter. Only writable parameters can be changed.", 
                  "params": {
                      "o:deviceDescriptorId": "Uuid", 
                      "o:deviceId": "Uuid", 
                      "o:deviceParams": "$ref:ParamList"
                  }, 
                  "returns": {
                      "deviceError": "$ref:DeviceError", 
                      "o:displayMessage": "String"
                  }
              }, 
              "Devices.RemoveConfiguredDevice": {
                  "description": "Remove a device from the system.", 
                  "params": {
                      "deviceId": "Uuid", 
                      "o:removePolicy": "$ref:RemovePolicy", 
                      "o:removePolicyList": [
                          {
                              "policy": "$ref:RemovePolicy", 
                              "ruleId": "Uuid"
                          }
                      ]
                  }, 
                  "returns": {
                      "deviceError": "$ref:DeviceError", 
                      "o:ruleIds": [
                          "Uuid"
                      ]
                  }
              }, 
              "Devices.SetDeviceSettings": {
                  "description": "Change the settings of a device.", 
                  "params": {
                      "deviceId": "Uuid", 
                      "settings": "$ref:ParamList"
                  }, 
                  "returns": {
                      "deviceError": "$ref:DeviceError"
                  }
              }, 
              "Devices.SetPluginConfiguration": {
                  "description": "Set a plugin's params.", 
                  "params": {
                      "configuration": "$ref:ParamList", 
                      "pluginId": "Uuid"
                  }, 
                  "returns": {
                      "deviceError": "$ref:DeviceError"
                  }
              }, 
              "Events.GetEventType": {
                  "deprecated": "Please use the Devices namespace instead.", 
                  "description": "Get the EventType for the given eventTypeId.", 
                  "params": {
                      "eventTypeId": "Uuid"
                  }, 
                  "returns": {
                      "deviceError": "$ref:DeviceError", 
                      "o:eventType": "$ref:EventType"
                  }
              }, 
              "JSONRPC.Authenticate": {
                  "deprecated": "Use Users.Authenticate instead.", 
                  "description": "Authenticate a client to the api via user & password challenge. Provide a device name which allows the user to identify the client and revoke the token in case the device is lost or stolen. This will return a new token to be used to authorize a client at the API.", 
                  "params": {
                      "deviceName": "String", 
                      "password": "String", 
                      "username": "String"
                  }, 
                  "returns": {
                      "o:token": "String", 
                      "success": "Bool"
                  }
              }, 
              "JSONRPC.CreateUser": {
                  "deprecated": "Use Users.CreateUser instead.", 
                  "description": "Create a new user in the API. Currently this is only allowed to be called once when a new nymea instance is set up. Call Authenticate after this to obtain a device token for this user.", 
                  "params": {
                      "password": "String", 
                      "username": "String"
                  }, 
                  "returns": {
                      "error": "$ref:UserError"
                  }
              }, 
              "JSONRPC.Hello": {
                  "description": "Initiates a connection. Use this method to perform an initial handshake of the connection. Optionally, a parameter \"locale\" is can be passed to set up the used locale for this connection. Strings such as DeviceClass displayNames etc will be localized to this locale. If this parameter is omitted, the default system locale (depending on the configuration) is used. The reply of this method contains information about this core instance such as version information, uuid and its name. The locale valueindicates the locale used for this connection. Note: This method can be called multiple times. The locale used in the last call for this connection will be used. Other values, like initialSetupRequired might change if the setup has been performed in the meantime.", 
                  "params": {
                      "o:locale": "String"
                  }, 
                  "returns": {
                      "authenticationRequired": "Bool", 
                      "initialSetupRequired": "Bool", 
                      "language": "String", 
                      "locale": "String", 
                      "name": "String", 
                      "o:experiences": [
                          "$ref:Experience"
                      ], 
                      "protocol version": "String", 
                      "pushButtonAuthAvailable": "Bool", 
                      "server": "String", 
                      "uuid": "Uuid", 
                      "version": "String"
                  }
              }, 
              "JSONRPC.Introspect": {
                  "description": "Introspect this API.", 
                  "params": {}, 
                  "returns": {
                      "methods": "Object", 
                      "notifications": "Object", 
                      "types": "Object"
                  }
              }, 
              "JSONRPC.IsCloudConnected": {
                  "description": "Check whether the cloud is currently connected. \"connected\" will be true whenever connectionState equals CloudConnectionStateConnected and is deprecated. Please use the connectionState value instead.", 
                  "params": {}, 
                  "returns": {
                      "connected": "Bool", 
                      "connectionState": "$ref:CloudConnectionState"
                  }
              }, 
              "JSONRPC.KeepAlive": {
                  "description": "This is basically a Ping/Pong mechanism a client app may use to check server connectivity. Currently, the server does not actually do anything with this information and will return the call providing the given sessionId back to the caller. It is up to the client whether to use this or not and not required by the server to keep the connection alive.", 
                  "params": {
                      "sessionId": "String"
                  }, 
                  "returns": {
                      "sessionId": "String", 
                      "success": "Bool"
                  }
              }, 
              "JSONRPC.RemoveToken": {
                  "deprecated": "Use Users.RemoveToken instead.", 
                  "description": "Revoke access for a given token.", 
                  "params": {
                      "tokenId": "Uuid"
                  }, 
                  "returns": {
                      "error": "$ref:UserError"
                  }
              }, 
              "JSONRPC.RequestPushButtonAuth": {
                  "deprecated": "Use Users.RequestPushButtonAuth instead.", 
                  "description": "Authenticate a client to the api via Push Button method. Provide a device name which allows the user to identify the client and revoke the token in case the device is lost or stolen. If push button hardware is available, this will return with success and start listening for push button presses. When the push button is pressed, the PushButtonAuthFinished notification will be sent to the requesting client. The procedure will be cancelled when the connection is interrupted. If another client requests push button authentication while a procedure is still going on, the second call will take over and the first one will be notified by the PushButtonAuthFinished signal about the error. The application should make it clear to the user to not press the button when the procedure fails as this can happen for 2 reasons: a) a second user is trying to auth at the same time and only the currently active user should press the button or b) it might indicate an attacker trying to take over and snooping in for tokens.", 
                  "params": {
                      "deviceName": "String"
                  }, 
                  "returns": {
                      "success": "Bool", 
                      "transactionId": "Int"
                  }
              }, 
              "JSONRPC.SetNotificationStatus": {
                  "description": "Enable/Disable notifications for this connections. Either \"enabled\" or \"namespaces\" needs to be given but not both of them. The boolean based \"enabled\" parameter will enable/disable all notifications at once. If instead the list-based \"namespaces\" parameter is provided, all given namespaceswill be enabled, the others will be disabled. The return value of \"success\" will indicate success of the operation. The \"enabled\" property in the return value is deprecated and used for legacy compatibilty only. It will be set to true if at least one namespace has been enabled.", 
                  "params": {
                      "o:enabled": "Bool", 
                      "o:namespaces": "StringList"
                  }, 
                  "returns": {
                      "enabled": "Bool", 
                      "namespaces": "StringList"
                  }
              }, 
              "JSONRPC.SetupCloudConnection": {
                  "description": "Sets up the cloud connection by deploying a certificate and its configuration.", 
                  "params": {
                      "certificatePEM": "String", 
                      "endpoint": "String", 
                      "privateKey": "String", 
                      "publicKey": "String", 
                      "rootCA": "String"
                  }, 
                  "returns": {
                      "success": "Bool"
                  }
              }, 
              "JSONRPC.SetupRemoteAccess": {
                  "description": "Setup the remote connection by providing AWS token information. This requires the cloud to be connected.", 
                  "params": {
                      "idToken": "String", 
                      "userId": "String"
                  }, 
                  "returns": {
                      "message": "String", 
                      "status": "Int"
                  }
              }, 
              "JSONRPC.Tokens": {
                  "deprecated": "Use Users.GetTokens instead.", 
                  "description": "Return a list of TokenInfo objects of all the tokens for the current user.", 
                  "params": {}, 
                  "returns": {
                      "tokenInfoList": [
                          "$ref:TokenInfo"
                      ]
                  }
              }, 
              "JSONRPC.Version": {
                  "description": "Version of this nymea/JSONRPC interface.", 
                  "params": {}, 
                  "returns": {
                      "protocol version": "String", 
                      "qtBuildVersion": "String", 
                      "qtVersion": "String", 
                      "version": "String"
                  }
              }, 
              "Logging.GetLogEntries": {
                  "description": "Get the LogEntries matching the given filter. The result set will contain entries matching all filter rules combined. If multiple options are given for a single filter type, the result set will contain entries matching any of those. The offset starts at the newest entry in the result set. By default all items are returned. Example: If the specified filter returns a total amount of 100 entries:\n- a offset value of 10 would include the oldest 90 entries\n- a offset value of 0 would return all 100 entries\n\nThe offset is particularly useful in combination with the maxCount property and can be used for pagination. E.g. A result set of 10000 entries can be fetched in  batches of 1000 entries by fetching\n1) offset 0, maxCount 1000: Entries 0 to 9999\n2) offset 10000, maxCount 1000: Entries 10000 - 19999\n3) offset 20000, maxCount 1000: Entries 20000 - 29999\n...", 
                  "params": {
                      "o:deviceIds": [
                          "Uuid"
                      ], 
                      "o:eventTypes": [
                          "$ref:LoggingEventType"
                      ], 
                      "o:limit": "Int", 
                      "o:loggingLevels": [
                          "$ref:LoggingLevel"
                      ], 
                      "o:loggingSources": [
                          "$ref:LoggingSource"
                      ], 
                      "o:offset": "Int", 
                      "o:timeFilters": [
                          {
                              "o:endDate": "Int", 
                              "o:startDate": "Int"
                          }
                      ], 
                      "o:typeIds": [
                          "Uuid"
                      ], 
                      "o:values": [
                          "Variant"
                      ]
                  }, 
                  "returns": {
                      "count": "Int", 
                      "loggingError": "$ref:LoggingError", 
                      "o:logEntries": "$ref:LogEntries", 
                      "offset": "Int"
                  }
              }, 
              "NetworkManager.ConnectWifiNetwork": {
                  "description": "Connect to the wifi network with the given ssid and password.", 
                  "params": {
                      "interface": "String", 
                      "o:password": "String", 
                      "ssid": "String"
                  }, 
                  "returns": {
                      "networkManagerError": "$ref:NetworkManagerError"
                  }
              }, 
              "NetworkManager.DisconnectInterface": {
                  "description": "Disconnect the given network interface. The interface will remain disconnected until the user connect it again.", 
                  "params": {
                      "interface": "String"
                  }, 
                  "returns": {
                      "networkManagerError": "$ref:NetworkManagerError"
                  }
              }, 
              "NetworkManager.EnableNetworking": {
                  "description": "Enable or disable networking in the NetworkManager.", 
                  "params": {
                      "enable": "Bool"
                  }, 
                  "returns": {
                      "networkManagerError": "$ref:NetworkManagerError"
                  }
              }, 
              "NetworkManager.EnableWirelessNetworking": {
                  "description": "Enable or disable wireless networking in the NetworkManager.", 
                  "params": {
                      "enable": "Bool"
                  }, 
                  "returns": {
                      "networkManagerError": "$ref:NetworkManagerError"
                  }
              }, 
              "NetworkManager.GetNetworkDevices": {
                  "description": "Get the list of current network devices.", 
                  "params": {}, 
                  "returns": {
                      "networkManagerError": "$ref:NetworkManagerError", 
                      "wiredNetworkDevices": [
                          "$ref:WiredNetworkDevice"
                      ], 
                      "wirelessNetworkDevices": [
                          "$ref:WirelessNetworkDevice"
                      ]
                  }
              }, 
              "NetworkManager.GetNetworkStatus": {
                  "description": "Get the current network manager status.", 
                  "params": {}, 
                  "returns": {
                      "networkManagerError": "$ref:NetworkManagerError", 
                      "o:status": {
                          "networkingEnabled": "Bool", 
                          "state": "$ref:NetworkManagerState", 
                          "wirelessNetworkingEnabled": "Bool"
                      }
                  }
              }, 
              "NetworkManager.GetWirelessAccessPoints": {
                  "description": "Get the current list of wireless network access points for the given interface. The interface has to be a WirelessNetworkDevice.", 
                  "params": {
                      "interface": "String"
                  }, 
                  "returns": {
                      "networkManagerError": "$ref:NetworkManagerError", 
                      "o:wirelessAccessPoints": [
                          "$ref:WirelessAccessPoint"
                      ]
                  }
              }, 
              "NetworkManager.ScanWifiNetworks": {
                  "description": "Start a wifi scan for searching new networks.", 
                  "params": {
                      "interface": "String"
                  }, 
                  "returns": {
                      "networkManagerError": "$ref:NetworkManagerError"
                  }
              }, 
              "Rules.AddRule": {
                  "description": "Add a rule. You can describe rules by one or many EventDesciptors and a StateEvaluator. Note that only one of either eventDescriptor or eventDescriptorList may be passed at a time. A rule can be created but left disabled, meaning it won't actually be executed until set to enabled. If not given, enabled defaults to true. A rule can have a list of actions and exitActions. It must have at least one Action. For state based rules, actions will be executed when the system enters a state matching the stateDescriptor. The exitActions will be executed when the system leaves the described state again. For event based rules, actions will be executed when a matching event happens and if the stateEvaluator matches the system's state. ExitActions for such rules will be executed when a matching event happens and the stateEvaluator is not matching the system's state. A rule marked as executable can be executed via the API using Rules.ExecuteRule, that means, its actions will be executed regardless of the eventDescriptor and stateEvaluators.", 
                  "params": {
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
                  }, 
                  "returns": {
                      "o:ruleId": "Uuid", 
                      "ruleError": "$ref:RuleError"
                  }
              }, 
              "Rules.DisableRule": {
                  "description": "Disable a rule. The rule won't be triggered by it's events or state changes while it is disabled. If successful, the notification \"Rule.RuleConfigurationChanged\" will be emitted.", 
                  "params": {
                      "ruleId": "Uuid"
                  }, 
                  "returns": {
                      "ruleError": "$ref:RuleError"
                  }
              }, 
              "Rules.EditRule": {
                  "description": "Edit the parameters of a rule. The configuration of the rule with the given ruleId will be replaced with the new given configuration. In ordert to enable or disable a Rule, please use the methods \"Rules.EnableRule\" and \"Rules.DisableRule\". If successful, the notification \"Rule.RuleConfigurationChanged\" will be emitted.", 
                  "params": {
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
                  }, 
                  "returns": {
                      "o:rule": "$ref:Rule", 
                      "ruleError": "$ref:RuleError"
                  }
              }, 
              "Rules.EnableRule": {
                  "description": "Enabled a rule that has previously been disabled.If successful, the notification \"Rule.RuleConfigurationChanged\" will be emitted.", 
                  "params": {
                      "ruleId": "Uuid"
                  }, 
                  "returns": {
                      "ruleError": "$ref:RuleError"
                  }
              }, 
              "Rules.ExecuteActions": {
                  "description": "Execute the action list of the rule with the given ruleId.", 
                  "params": {
                      "ruleId": "Uuid"
                  }, 
                  "returns": {
                      "ruleError": "$ref:RuleError"
                  }
              }, 
              "Rules.ExecuteExitActions": {
                  "description": "Execute the exit action list of the rule with the given ruleId.", 
                  "params": {
                      "ruleId": "Uuid"
                  }, 
                  "returns": {
                      "ruleError": "$ref:RuleError"
                  }
              }, 
              "Rules.FindRules": {
                  "description": "Find a list of rules containing any of the given parameters.", 
                  "params": {
                      "deviceId": "Uuid"
                  }, 
                  "returns": {
                      "ruleIds": [
                          "Uuid"
                      ]
                  }
              }, 
              "Rules.GetRuleDetails": {
                  "description": "Get details for the rule identified by ruleId", 
                  "params": {
                      "ruleId": "Uuid"
                  }, 
                  "returns": {
                      "o:rule": "$ref:Rule", 
                      "ruleError": "$ref:RuleError"
                  }
              }, 
              "Rules.GetRules": {
                  "description": "Get the descriptions of all configured rules. If you need more information about a specific rule use the method Rules.GetRuleDetails.", 
                  "params": {}, 
                  "returns": {
                      "ruleDescriptions": [
                          "$ref:RuleDescription"
                      ]
                  }
              }, 
              "Rules.RemoveRule": {
                  "description": "Remove a rule", 
                  "params": {
                      "ruleId": "Uuid"
                  }, 
                  "returns": {
                      "ruleError": "$ref:RuleError"
                  }
              }, 
              "Scripts.AddScript": {
                  "description": "Add a script", 
                  "params": {
                      "content": "String", 
                      "name": "String"
                  }, 
                  "returns": {
                      "o:errors": "StringList", 
                      "o:script": "$ref:Script", 
                      "scriptError": "$ref:ScriptError"
                  }
              }, 
              "Scripts.EditScript": {
                  "description": "Edit a script", 
                  "params": {
                      "id": "Uuid", 
                      "o:content": "String", 
                      "o:name": "String"
                  }, 
                  "returns": {
                      "o:errors": "StringList", 
                      "scriptError": "$ref:ScriptError"
                  }
              }, 
              "Scripts.GetScriptContent": {
                  "description": "Get a scripts content.", 
                  "params": {
                      "id": "Uuid"
                  }, 
                  "returns": {
                      "o:content": "String", 
                      "scriptError": "$ref:ScriptError"
                  }
              }, 
              "Scripts.GetScripts": {
                  "description": "Get all script, that is, their names and properties, but no content.", 
                  "params": {}, 
                  "returns": {
                      "scripts": "$ref:Scripts"
                  }
              }, 
              "Scripts.RemoveScript": {
                  "description": "remove a script", 
                  "params": {
                      "id": "Uuid"
                  }, 
                  "returns": {
                      "scriptError": "$ref:ScriptError"
                  }
              }, 
              "States.GetStateType": {
                  "deprecated": "Please use the Devices namespace instead.", 
                  "description": "Get the StateType for the given stateTypeId.", 
                  "params": {
                      "stateTypeId": "Uuid"
                  }, 
                  "returns": {
                      "deviceError": "$ref:DeviceError", 
                      "o:stateType": "$ref:StateType"
                  }
              }, 
              "System.CheckForUpdates": {
                  "description": "Instruct the system to poll the server for updates. Normally the system should automatically do this in regular intervals, however, if the client wants to allow the user to manually check for new updates now, this can be called. Returns true if the operation has been started successfully and the update manager will become busy. In order to know whether there are updates available, clients should walk through the list of packages retrieved from GetPackages and check whether there are packages with the updateAvailable flag set to true.", 
                  "params": {}, 
                  "returns": {
                      "success": "Bool"
                  }
              }, 
              "System.EnableRepository": {
                  "description": "Enable or disable a repository.", 
                  "params": {
                      "enabled": "Bool", 
                      "repositoryId": "String"
                  }, 
                  "returns": {
                      "success": "Bool"
                  }
              }, 
              "System.GetCapabilities": {
                  "description": "Get the list of capabilites on this system. The property \"powerManagement\" indicates whether rebooting or shutting down is supported on this system. The property \"updateManagement indicates whether system update features are available in this system. The property \"timeManagement\" indicates whether the system time can be configured on this system. Note that GetTime will be available in any case.", 
                  "params": {}, 
                  "returns": {
                      "powerManagement": "Bool", 
                      "timeManagement": "Bool", 
                      "updateManagement": "Bool"
                  }
              }, 
              "System.GetPackages": {
                  "description": "Get the list of packages currently available to the system. This might include installed available but not installed packages. Installed packages will have the installedVersion set to a non-empty value.", 
                  "params": {}, 
                  "returns": {
                      "packages": "$ref:Packages"
                  }
              }, 
              "System.GetRepositories": {
                  "description": "Get the list of repositories currently available to the system.", 
                  "params": {}, 
                  "returns": {
                      "repositories": "$ref:Repositories"
                  }
              }, 
              "System.GetTime": {
                  "description": "Get the system time and configuraton. The \"time\" and \"timeZone\" properties give the current server time and time zone. \"automaticTimeAvailable\" indicates whether this system supports automatically setting the clock (e.g. using NTP). \"automaticTime\" will be true if the system is configured to automatically update the clock.", 
                  "params": {}, 
                  "returns": {
                      "automaticTime": "Bool", 
                      "automaticTimeAvailable": "Bool", 
                      "time": "Uint", 
                      "timeZone": "String"
                  }
              }, 
              "System.GetTimeZones": {
                  "description": "Returns the list of IANA specified time zone IDs which can be used to select a time zone. It is not required to use this method if the client toolkit already provides means to obtain a list of IANA time zone ids.", 
                  "params": {}, 
                  "returns": {
                      "timeZones": "StringList"
                  }
              }, 
              "System.GetUpdateStatus": {
                  "description": "Get the current status of the update system. \"busy\" indicates that the system is current busy with an operation regarding updates. This does not necessarily mean an actual update is running. When this is true, update related functions on the client should be marked as busy and no interaction with update components shall be allowed. An example for such a state is when the system queries the server if there are updates available, typically after a call to CheckForUpdates. \"updateRunning\" on the other hand indicates an actual update process is ongoing. The user should be informed about it, the system also might restart at any point while an update is running.", 
                  "params": {}, 
                  "returns": {
                      "busy": "Bool", 
                      "updateRunning": "Bool"
                  }
              }, 
              "System.Reboot": {
                  "description": "Initiate a reboot of the system. The return value will indicate whether the procedure has been initiated successfully.", 
                  "params": {}, 
                  "returns": {
                      "success": "Bool"
                  }
              }, 
              "System.RemovePackages": {
                  "description": "Starts removing a package. Returns true if the removal has been started successfully. Before calling this method, clients should check whether the package can be removed (canRemove set to true).", 
                  "params": {
                      "packageIds": [
                          "String"
                      ]
                  }, 
                  "returns": {
                      "success": "Bool"
                  }
              }, 
              "System.RollbackPackages": {
                  "description": "Starts a rollback. Returns true if the rollback has been started successfully. Before calling this method, clients should check whether the package can be rolled back (canRollback set to true).", 
                  "params": {
                      "packageIds": [
                          "String"
                      ]
                  }, 
                  "returns": {
                      "success": "Bool"
                  }
              }, 
              "System.SetTime": {
                  "description": "Set the system time configuraton. The system can be configured to update the time automatically by setting \"automaticTime\" to true. This will only work if the \"timeManagement\" capability is available on this system and \"GetTime\" indicates the availability of automatic time settings. If any of those requirements are not met, this method will return \"false\" in the \"success\" property. In order to manually configure the time, \"automaticTime\" should be set to false and \"time\" should be set. Note that if \"automaticTime\" is set to true and a manual \"time\" is still passed, the system will attempt to configure automatic time updates and only set the manual time if automatic mode fails. A time zone can always be passed optionally to change the system time zone and should be a IANA time zone id.", 
                  "params": {
                      "o:automaticTime": "Bool", 
                      "o:time": "Uint", 
                      "o:timeZone": "String"
                  }, 
                  "returns": {
                      "success": "Bool"
                  }
              }, 
              "System.Shutdown": {
                  "description": "Initiate a shutdown of the system. The return value will indicate whether the procedure has been initiated successfully.", 
                  "params": {}, 
                  "returns": {
                      "success": "Bool"
                  }
              }, 
              "System.UpdatePackages": {
                  "description": "Starts updating/installing packages with the given ids. Returns true if the upgrade has been started successfully. Note that it might still fail later. Before calling this method, clients should check the packages whether they are in a state where they can either be installed (no installedVersion set) or upgraded (updateAvailable set to true).", 
                  "params": {
                      "o:packageIds": [
                          "String"
                      ]
                  }, 
                  "returns": {
                      "success": "Bool"
                  }
              }, 
              "Tags.AddTag": {
                  "description": "Add a Tag. A Tag must have a deviceId OR a ruleId (call this method twice if you want to attach the same tag to a device and a rule), an appId (Use the appId of your app), a tagId (e.g. \"favorites\") and a value. Upon success, a TagAdded notification will be emitted. Calling this method twice for the same ids (device/rule, appId and tagId) but with a different value will update the tag's value and the TagValueChanged notification will be emitted.", 
                  "params": {
                      "tag": "$ref:Tag"
                  }, 
                  "returns": {
                      "tagError": "$ref:TagError"
                  }
              }, 
              "Tags.GetTags": {
                  "description": "Get the Tags matching the given filter. Tags can be filtered by a deviceID, a ruleId, an appId, a tagId or a combination of any (however, combining deviceId and ruleId will return an empty result set).", 
                  "params": {
                      "o:appId": "String", 
                      "o:deviceId": "Uuid", 
                      "o:ruleId": "Uuid", 
                      "o:tagId": "String"
                  }, 
                  "returns": {
                      "o:tags": "$ref:Tags", 
                      "tagError": "$ref:TagError"
                  }
              }, 
              "Tags.RemoveTag": {
                  "description": "Remove a Tag. Tag value is optional and will be disregarded. If the ids match, the tag will be deleted and a TagRemoved notification will be emitted.", 
                  "params": {
                      "tag": "$ref:Tag"
                  }, 
                  "returns": {
                      "tagError": "$ref:TagError"
                  }
              }, 
              "Users.Authenticate": {
                  "description": "Authenticate a client to the api via user & password challenge. Provide a device name which allows the user to identify the client and revoke the token in case the device is lost or stolen. This will return a new token to be used to authorize a client at the API.", 
                  "params": {
                      "deviceName": "String", 
                      "password": "String", 
                      "username": "String"
                  }, 
                  "returns": {
                      "o:token": "String", 
                      "success": "Bool"
                  }
              }, 
              "Users.ChangePassword": {
                  "description": "Change the password for the currently logged in user.", 
                  "params": {
                      "newPassword": "String"
                  }, 
                  "returns": {
                      "error": "$ref:UserError"
                  }
              }, 
              "Users.CreateUser": {
                  "description": "Create a new user in the API. Currently this is only allowed to be called once when a new nymea instance is set up. Call Authenticate after this to obtain a device token for this user.", 
                  "params": {
                      "password": "String", 
                      "username": "String"
                  }, 
                  "returns": {
                      "error": "$ref:UserError"
                  }
              }, 
              "Users.GetTokens": {
                  "description": "Get all the tokens for the current user.", 
                  "params": {}, 
                  "returns": {
                      "error": "$ref:UserError", 
                      "o:tokenInfoList": "$ref:TokenInfoList"
                  }
              }, 
              "Users.GetUserInfo": {
                  "description": "Get info about the current token (the currently logged in user).", 
                  "params": {}, 
                  "returns": {
                      "error": "$ref:UserError", 
                      "o:userInfo": "$ref:UserInfo"
                  }
              }, 
              "Users.RemoveToken": {
                  "description": "Revoke access for a given token.", 
                  "params": {
                      "tokenId": "Uuid"
                  }, 
                  "returns": {
                      "error": "$ref:UserError"
                  }
              }, 
              "Users.RequestPushButtonAuth": {
                  "description": "Authenticate a client to the api via Push Button method. Provide a device name which allows the user to identify the client and revoke the token in case the device is lost or stolen. If push button hardware is available, this will return with success and start listening for push button presses. When the push button is pressed, the PushButtonAuthFinished notification will be sent to the requesting client. The procedure will be cancelled when the connection is interrupted. If another client requests push button authentication while a procedure is still going on, the second call will take over and the first one will be notified by the PushButtonAuthFinished signal about the error. The application should make it clear to the user to not press the button when the procedure fails as this can happen for 2 reasons: a) a second user is trying to auth at the same time and only the currently active user should press the button or b) it might indicate an attacker trying to take over and snooping in for tokens.", 
                  "params": {
                      "deviceName": "String"
                  }, 
                  "returns": {
                      "success": "Bool", 
                      "transactionId": "Int"
                  }
              }
          }, 
          "notifications": {
              "Configuration.BasicConfigurationChanged": {
                  "description": "Emitted whenever the basic configuration of this server changes.", 
                  "params": {
                      "basicConfiguration": {
                          "d:language": "String", 
                          "d:serverTime": "Uint", 
                          "d:timeZone": "String", 
                          "debugServerEnabled": "Bool", 
                          "serverName": "String", 
                          "serverUuid": "Uuid"
                      }
                  }
              }, 
              "Configuration.CloudConfigurationChanged": {
                  "description": "Emitted whenever the cloud configuration is changed.", 
                  "params": {
                      "cloudConfiguration": {
                          "enabled": "Bool"
                      }
                  }
              }, 
              "Configuration.LanguageChanged": {
                  "description": "Emitted whenever the language of the server changed. The Plugins, Vendors and DeviceClasses have to be reloaded to get the translated data.", 
                  "params": {
                      "language": "String"
                  }
              }, 
              "Configuration.MqttPolicyChanged": {
                  "description": "Emitted whenever a MQTT broker policy is changed.", 
                  "params": {
                      "policy": "$ref:MqttPolicy"
                  }
              }, 
              "Configuration.MqttPolicyRemoved": {
                  "description": "Emitted whenever a MQTT broker policy is removed.", 
                  "params": {
                      "clientId": "String"
                  }
              }, 
              "Configuration.MqttServerConfigurationChanged": {
                  "description": "Emitted whenever the MQTT broker configuration is changed.", 
                  "params": {
                      "mqttServerConfiguration": "$ref:ServerConfiguration"
                  }
              }, 
              "Configuration.MqttServerConfigurationRemoved": {
                  "description": "Emitted whenever a MQTT server configuration is removed.", 
                  "params": {
                      "id": "String"
                  }
              }, 
              "Configuration.TcpServerConfigurationChanged": {
                  "description": "Emitted whenever the TCP server configuration changes.", 
                  "params": {
                      "tcpServerConfiguration": "$ref:ServerConfiguration"
                  }
              }, 
              "Configuration.TcpServerConfigurationRemoved": {
                  "description": "Emitted whenever a TCP server configuration is removed.", 
                  "params": {
                      "id": "String"
                  }
              }, 
              "Configuration.WebServerConfigurationChanged": {
                  "description": "Emitted whenever the web server configuration changes.", 
                  "params": {
                      "webServerConfiguration": "$ref:WebServerConfiguration"
                  }
              }, 
              "Configuration.WebServerConfigurationRemoved": {
                  "description": "Emitted whenever a Web server configuration is removed.", 
                  "params": {
                      "id": "String"
                  }
              }, 
              "Configuration.WebSocketServerConfigurationChanged": {
                  "description": "Emitted whenever the web socket server configuration changes.", 
                  "params": {
                      "webSocketServerConfiguration": "$ref:ServerConfiguration"
                  }
              }, 
              "Configuration.WebSocketServerConfigurationRemoved": {
                  "description": "Emitted whenever a WebSocket server configuration is removed.", 
                  "params": {
                      "id": "String"
                  }
              }, 
              "Devices.DeviceAdded": {
                  "description": "Emitted whenever a Device was added.", 
                  "params": {
                      "device": "$ref:Device"
                  }
              }, 
              "Devices.DeviceChanged": {
                  "description": "Emitted whenever the params, name or setupStatus of a Device changes.", 
                  "params": {
                      "device": "$ref:Device"
                  }
              }, 
              "Devices.DeviceRemoved": {
                  "description": "Emitted whenever a Device was removed.", 
                  "params": {
                      "deviceId": "Uuid"
                  }
              }, 
              "Devices.DeviceSettingChanged": {
                  "description": "Emitted whenever the setting of a Device is changed.", 
                  "params": {
                      "deviceId": "Uuid", 
                      "paramTypeId": "Uuid", 
                      "value": "Variant"
                  }
              }, 
              "Devices.EventTriggered": {
                  "description": "Emitted whenever an Event is triggered.", 
                  "params": {
                      "event": "$ref:Event"
                  }
              }, 
              "Devices.PluginConfigurationChanged": {
                  "description": "Emitted whenever a plugin's configuration is changed.", 
                  "params": {
                      "configuration": "$ref:ParamList", 
                      "pluginId": "Uuid"
                  }
              }, 
              "Devices.StateChanged": {
                  "description": "Emitted whenever a State of a device changes.", 
                  "params": {
                      "deviceId": "Uuid", 
                      "stateTypeId": "Uuid", 
                      "value": "Variant"
                  }
              }, 
              "Events.EventTriggered": {
                  "deprecated": "Please use Devices.EventTriggered instead.", 
                  "description": "Emitted whenever an Event is triggered.", 
                  "params": {
                      "event": "$ref:Event"
                  }
              }, 
              "JSONRPC.CloudConnectedChanged": {
                  "description": "Emitted whenever the cloud connection status changes.", 
                  "params": {
                      "connected": "Bool", 
                      "connectionState": "$ref:CloudConnectionState"
                  }
              }, 
              "JSONRPC.PushButtonAuthFinished": {
                  "deprecated": "Use Users.PushButtonAuthFinished instead.", 
                  "description": "Emitted when a push button authentication reaches final state. NOTE: This notification is special. It will only be emitted to connections that did actively request a push button authentication, but also it will be emitted regardless of the notification settings. ", 
                  "params": {
                      "o:token": "String", 
                      "success": "Bool", 
                      "transactionId": "Int"
                  }
              }, 
              "Logging.LogDatabaseUpdated": {
                  "description": "Emitted whenever the database was updated. The database will be updated when a log entry was deleted. A log entry will be deleted when the corresponding device or a rule will be removed, or when the oldest entry of the database was deleted to keep to database in the size limits.", 
                  "params": {}
              }, 
              "Logging.LogEntryAdded": {
                  "description": "Emitted whenever an entry is appended to the logging system. ", 
                  "params": {
                      "logEntry": "$ref:LogEntry"
                  }
              }, 
              "NetworkManager.NetworkStatusChanged": {
                  "description": "Emitted whenever a status of a NetworkManager changes.", 
                  "params": {
                      "status": {
                          "networkingEnabled": "Bool", 
                          "state": "$ref:NetworkManagerState", 
                          "wirelessNetworkingEnabled": "Bool"
                      }
                  }
              }, 
              "NetworkManager.WiredNetworkDeviceAdded": {
                  "description": "Emitted whenever a new WiredNetworkDevice was added.", 
                  "params": {
                      "wiredNetworkDevice": "$ref:WiredNetworkDevice"
                  }
              }, 
              "NetworkManager.WiredNetworkDeviceChanged": {
                  "description": "Emitted whenever the given WiredNetworkDevice has changed.", 
                  "params": {
                      "wiredNetworkDevice": "$ref:WiredNetworkDevice"
                  }
              }, 
              "NetworkManager.WiredNetworkDeviceRemoved": {
                  "description": "Emitted whenever a WiredNetworkDevice was removed.", 
                  "params": {
                      "interface": "String"
                  }
              }, 
              "NetworkManager.WirelessNetworkDeviceAdded": {
                  "description": "Emitted whenever a new WirelessNetworkDevice was added.", 
                  "params": {
                      "wirelessNetworkDevice": "$ref:WirelessNetworkDevice"
                  }
              }, 
              "NetworkManager.WirelessNetworkDeviceChanged": {
                  "description": "Emitted whenever the given WirelessNetworkDevice has changed.", 
                  "params": {
                      "wirelessNetworkDevice": "$ref:WirelessNetworkDevice"
                  }
              }, 
              "NetworkManager.WirelessNetworkDeviceRemoved": {
                  "description": "Emitted whenever a WirelessNetworkDevice was removed.", 
                  "params": {
                      "interface": "String"
                  }
              }, 
              "Rules.RuleActiveChanged": {
                  "description": "Emitted whenever the active state of a Rule changed.", 
                  "params": {
                      "active": "Bool", 
                      "ruleId": "Uuid"
                  }
              }, 
              "Rules.RuleAdded": {
                  "description": "Emitted whenever a Rule was added.", 
                  "params": {
                      "rule": "$ref:Rule"
                  }
              }, 
              "Rules.RuleConfigurationChanged": {
                  "description": "Emitted whenever the configuration of a Rule changed.", 
                  "params": {
                      "rule": "$ref:Rule"
                  }
              }, 
              "Rules.RuleRemoved": {
                  "description": "Emitted whenever a Rule was removed.", 
                  "params": {
                      "ruleId": "Uuid"
                  }
              }, 
              "Scripts.ScriptAdded": {
                  "description": "Emitted when a script has been added to the system.", 
                  "params": {
                      "script": "$ref:Script"
                  }
              }, 
              "Scripts.ScriptChanged": {
                  "description": "Emitted when a script has been changed in the system (e.g. renamed).", 
                  "params": {
                      "name": "String", 
                      "scriptId": "Uuid"
                  }
              }, 
              "Scripts.ScriptContentChanged": {
                  "description": "Emitted when a script's content has been changed in the system.", 
                  "params": {
                      "scriptId": "Uuid"
                  }
              }, 
              "Scripts.ScriptLogMessage": {
                  "description": "Emitted when a script produces a console message.", 
                  "params": {
                      "message": "String", 
                      "scriptId": "Uuid", 
                      "type": "$ref:ScriptMessageType"
                  }
              }, 
              "Scripts.ScriptRemoved": {
                  "description": "Emitted when a script has been removed from the system.", 
                  "params": {
                      "id": "Uuid"
                  }
              }, 
              "System.CapabilitiesChanged": {
                  "description": "Emitted whenever the system capabilities change.", 
                  "params": {
                      "powerManagement": "Bool", 
                      "updateManagement": "Bool"
                  }
              }, 
              "System.PackageAdded": {
                  "description": "Emitted whenever a package is added to the list of packages.", 
                  "params": {
                      "package": "$ref:Package"
                  }
              }, 
              "System.PackageChanged": {
                  "description": "Emitted whenever a package in the list of packages changes.", 
                  "params": {
                      "package": "$ref:Package"
                  }
              }, 
              "System.PackageRemoved": {
                  "description": "Emitted whenever a package is removed from the list of packages.", 
                  "params": {
                      "packageId": "String"
                  }
              }, 
              "System.RepositoryAdded": {
                  "description": "Emitted whenever a repository is added to the list of repositories.", 
                  "params": {
                      "repository": "$ref:Repository"
                  }
              }, 
              "System.RepositoryChanged": {
                  "description": "Emitted whenever a repository in the list of repositories changes.", 
                  "params": {
                      "repository": "$ref:Repository"
                  }
              }, 
              "System.RepositoryRemoved": {
                  "description": "Emitted whenever a repository is removed from the list of repositories.", 
                  "params": {
                      "repositoryId": "String"
                  }
              }, 
              "System.TimeConfigurationChanged": {
                  "description": "Emitted whenever the time configuration is changed", 
                  "params": {
                      "automaticTime": "Bool", 
                      "automaticTimeAvailable": "Bool", 
                      "time": "Uint", 
                      "timeZone": "String"
                  }
              }, 
              "System.UpdateStatusChanged": {
                  "description": "Emitted whenever the update status changes.", 
                  "params": {
                      "busy": "Bool", 
                      "updateRunning": "Bool"
                  }
              }, 
              "Tags.TagAdded": {
                  "description": "Emitted whenever a tag is added to the system. ", 
                  "params": {
                      "tag": "$ref:Tag"
                  }
              }, 
              "Tags.TagRemoved": {
                  "description": "Emitted whenever a tag is removed from the system. ", 
                  "params": {
                      "tag": "$ref:Tag"
                  }
              }, 
              "Tags.TagValueChanged": {
                  "description": "Emitted whenever a tag's value is changed in the system. ", 
                  "params": {
                      "tag": "$ref:Tag"
                  }
              }, 
              "Users.PushButtonAuthFinished": {
                  "description": "Emitted when a push button authentication reaches final state. NOTE: This notification is special. It will only be emitted to connections that did actively request a push button authentication, but also it will be emitted regardless of the notification settings.", 
                  "params": {
                      "o:token": "String", 
                      "success": "Bool", 
                      "transactionId": "Int"
                  }
              }
          }, 
          "types": {
              "Action": {
                  "actionTypeId": "Uuid", 
                  "deviceId": "Uuid", 
                  "o:params": "$ref:ParamList"
              }, 
              "ActionType": {
                  "displayName": "String", 
                  "index": "Int", 
                  "name": "String", 
                  "paramTypes": "$ref:ParamTypes", 
                  "r:id": "Uuid"
              }, 
              "ActionTypes": [
                  "$ref:ActionType"
              ], 
              "BrowserItem": {
                  "actionTypeIds": [
                      "Uuid"
                  ], 
                  "browsable": "Bool", 
                  "description": "String", 
                  "disabled": "Bool", 
                  "displayName": "String", 
                  "executable": "Bool", 
                  "icon": "$ref:BrowserIcon", 
                  "id": "String", 
                  "o:mediaIcon": "$ref:MediaBrowserIcon", 
                  "thumbnail": "String"
              }, 
              "CalendarItem": {
                  "duration": "Uint", 
                  "o:datetime": "Uint", 
                  "o:repeating": "$ref:RepeatingOption", 
                  "o:startTime": "Time"
              }, 
              "CalendarItems": [
                  "$ref:CalendarItem"
              ], 
              "Device": {
                  "d:r:setupComplete": "Bool", 
                  "o:name": "String", 
                  "o:settings": "$ref:ParamList", 
                  "r:deviceClassId": "Uuid", 
                  "r:id": "Uuid", 
                  "r:o:parentId": "Uuid", 
                  "r:o:setupDisplayMessage": "String", 
                  "r:params": "$ref:ParamList", 
                  "r:setupError": "$ref:DeviceError", 
                  "r:setupStatus": "$ref:DeviceSetupStatus", 
                  "r:states": "$ref:States"
              }, 
              "DeviceClass": {
                  "r:actionTypes": "$ref:ActionTypes", 
                  "r:browsable": "Bool", 
                  "r:browserItemActionTypes": "$ref:ActionTypes", 
                  "r:createMethods": "$ref:CreateMethods", 
                  "r:discoveryParamTypes": "$ref:ParamTypes", 
                  "r:displayName": "String", 
                  "r:eventTypes": "$ref:EventTypes", 
                  "r:id": "Uuid", 
                  "r:interfaces": "StringList", 
                  "r:name": "String", 
                  "r:paramTypes": "$ref:ParamTypes", 
                  "r:pluginId": "Uuid", 
                  "r:settingsTypes": "$ref:ParamTypes", 
                  "r:setupMethod": "$ref:SetupMethod", 
                  "r:stateTypes": "$ref:StateTypes", 
                  "r:vendorId": "Uuid"
              }, 
              "DeviceClasses": [
                  "$ref:DeviceClass"
              ], 
              "DeviceDescriptor": {
                  "r:description": "String", 
                  "r:deviceParams": "$ref:ParamList", 
                  "r:id": "Uuid", 
                  "r:o:deviceId": "Uuid", 
                  "r:title": "String"
              }, 
              "DeviceDescriptors": [
                  "$ref:DeviceDescriptor"
              ], 
              "DevicePlugin": {
                  "r:displayName": "String", 
                  "r:id": "Uuid", 
                  "r:name": "String", 
                  "r:paramTypes": "$ref:ParamTypes"
              }, 
              "DevicePlugins": [
                  "$ref:DevicePlugin"
              ], 
              "Devices": [
                  "$ref:Device"
              ], 
              "Event": {
                  "r:deviceId": "Uuid", 
                  "r:eventTypeId": "Uuid", 
                  "r:params": "$ref:ParamList"
              }, 
              "EventDescriptor": {
                  "o:deviceId": "Uuid", 
                  "o:eventTypeId": "Uuid", 
                  "o:interface": "String", 
                  "o:interfaceEvent": "String", 
                  "o:paramDescriptors": "$ref:ParamDescriptors"
              }, 
              "EventDescriptors": [
                  "$ref:EventDescriptor"
              ], 
              "EventType": {
                  "displayName": "String", 
                  "name": "String", 
                  "paramTypes": "$ref:ParamTypes", 
                  "r:id": "Uuid", 
                  "r:index": "Int"
              }, 
              "EventTypes": [
                  "$ref:EventType"
              ], 
              "Experience": {
                  "name": "String", 
                  "version": "String"
              }, 
              "LogEntries": [
                  "$ref:LogEntry"
              ], 
              "LogEntry": {
                  "r:loggingLevel": "$ref:LoggingLevel", 
                  "r:o:active": "Bool", 
                  "r:o:deviceId": "Uuid", 
                  "r:o:errorCode": "String", 
                  "r:o:eventType": "$ref:LoggingEventType", 
                  "r:o:typeId": "Uuid", 
                  "r:o:value": "Variant", 
                  "r:source": "$ref:LoggingSource", 
                  "r:timestamp": "Uint"
              }, 
              "MqttPolicy": {
                  "allowedPublishTopicFilters": "StringList", 
                  "allowedSubscribeTopicFilters": "StringList", 
                  "clientId": "String", 
                  "password": "String", 
                  "username": "String"
              }, 
              "Package": {
                  "r:canRemove": "Bool", 
                  "r:candidateVersion": "String", 
                  "r:changelog": "String", 
                  "r:displayName": "String", 
                  "r:id": "String", 
                  "r:installedVersion": "String", 
                  "r:rollbackAvailable": "Bool", 
                  "r:summary": "String", 
                  "r:updateAvailable": "Bool"
              }, 
              "Packages": [
                  "$ref:Package"
              ], 
              "Param": {
                  "o:paramTypeId": "Uuid", 
                  "value": "Variant"
              }, 
              "ParamDescriptor": {
                  "o:paramName": "String", 
                  "o:paramTypeId": "Uuid", 
                  "operator": "$ref:ValueOperator", 
                  "value": "Variant"
              }, 
              "ParamDescriptors": [
                  "$ref:ParamDescriptor"
              ], 
              "ParamList": [
                  "$ref:Param"
              ], 
              "ParamType": {
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
                  "o:unit": "$ref:Unit", 
                  "r:id": "Uuid", 
                  "type": "$ref:BasicType"
              }, 
              "ParamTypes": [
                  "$ref:ParamType"
              ], 
              "RepeatingOption": {
                  "mode": "$ref:RepeatingMode", 
                  "o:monthDays": [
                      "Int"
                  ], 
                  "o:weekDays": [
                      "Int"
                  ]
              }, 
              "Repositories": [
                  "$ref:Repository"
              ], 
              "Repository": {
                  "enabled": "Bool", 
                  "r:displayName": "String", 
                  "r:id": "String"
              }, 
              "Rule": {
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
              }, 
              "RuleAction": {
                  "o:actionTypeId": "Uuid", 
                  "o:browserItemId": "String", 
                  "o:deviceId": "Uuid", 
                  "o:interface": "String", 
                  "o:interfaceAction": "String", 
                  "o:ruleActionParams": "$ref:RuleActionParams"
              }, 
              "RuleActionParam": {
                  "o:eventParamTypeId": "Uuid", 
                  "o:eventTypeId": "Uuid", 
                  "o:paramName": "String", 
                  "o:paramTypeId": "Uuid", 
                  "o:stateDeviceId": "Uuid", 
                  "o:stateTypeId": "Uuid", 
                  "o:value": "Variant"
              }, 
              "RuleActionParams": [
                  "$ref:RuleActionParam"
              ], 
              "RuleActions": [
                  "$ref:RuleAction"
              ], 
              "RuleDescription": {
                  "active": "Bool", 
                  "enabled": "Bool", 
                  "executable": "Bool", 
                  "id": "Uuid", 
                  "name": "String"
              }, 
              "Rules": [
                  "$ref:Rule"
              ], 
              "Script": {
                  "name": "String", 
                  "r:id": "Uuid"
              }, 
              "Scripts": [
                  "$ref:Script"
              ], 
              "ServerConfiguration": {
                  "address": "String", 
                  "authenticationEnabled": "Bool", 
                  "id": "String", 
                  "port": "Uint", 
                  "sslEnabled": "Bool"
              }, 
              "State": {
                  "r:stateTypeId": "Uuid", 
                  "r:value": "Variant"
              }, 
              "StateDescriptor": {
                  "o:deviceId": "Uuid", 
                  "o:interface": "String", 
                  "o:interfaceState": "String", 
                  "o:stateTypeId": "Uuid", 
                  "operator": "$ref:ValueOperator", 
                  "value": "Variant"
              }, 
              "StateEvaluator": {
                  "o:childEvaluators": "$ref:StateEvaluators", 
                  "o:operator": "$ref:StateOperator", 
                  "o:stateDescriptor": "$ref:StateDescriptor"
              }, 
              "StateEvaluators": [
                  "$ref:StateEvaluator"
              ], 
              "StateType": {
                  "defaultValue": "Variant", 
                  "displayName": "String", 
                  "index": "Int", 
                  "name": "String", 
                  "o:maxValue": "Variant", 
                  "o:minValue": "Variant", 
                  "o:possibleValues": [
                      "Variant"
                  ], 
                  "o:unit": "$ref:Unit", 
                  "r:id": "Uuid", 
                  "type": "$ref:BasicType"
              }, 
              "StateTypes": [
                  "$ref:StateType"
              ], 
              "States": [
                  "$ref:State"
              ], 
              "Tag": {
                  "appId": "String", 
                  "o:deviceId": "Uuid", 
                  "o:ruleId": "Uuid", 
                  "o:value": "String", 
                  "tagId": "String"
              }, 
              "Tags": [
                  "$ref:Tag"
              ], 
              "TimeDescriptor": {
                  "o:calendarItems": "$ref:CalendarItems", 
                  "o:timeEventItems": "$ref:TimeEventItems"
              }, 
              "TimeEventItem": {
                  "o:datetime": "Uint", 
                  "o:repeating": "$ref:RepeatingOption", 
                  "o:time": "Time"
              }, 
              "TimeEventItems": [
                  "$ref:TimeEventItem"
              ], 
              "TokenInfo": {
                  "r:creationTime": "Uint", 
                  "r:deviceName": "String", 
                  "r:id": "Uuid", 
                  "r:username": "String"
              }, 
              "TokenInfoList": [
                  "$ref:TokenInfo"
              ], 
              "UserInfo": {
                  "r:username": "String"
              }, 
              "Vendor": {
                  "displayName": "String", 
                  "id": "Uuid", 
                  "name": "String"
              }, 
              "Vendors": [
                  "$ref:Vendor"
              ], 
              "WebServerConfiguration": {
                  "address": "String", 
                  "authenticationEnabled": "Bool", 
                  "id": "String", 
                  "port": "Uint", 
                  "publicFolder": "String", 
                  "sslEnabled": "Bool"
              }, 
              "WiredNetworkDevice": {
                  "r:bitRate": "String", 
                  "r:interface": "String", 
                  "r:macAddress": "String", 
                  "r:pluggedIn": "Bool", 
                  "r:state": "$ref:NetworkDeviceState"
              }, 
              "WirelessAccessPoint": {
                  "r:frequency": "Double", 
                  "r:macAddress": "String", 
                  "r:protected": "Bool", 
                  "r:signalStrength": "Int", 
                  "r:ssid": "String"
              }, 
              "WirelessNetworkDevice": {
                  "bitRate": "String", 
                  "interface": "String", 
                  "macAddress": "String", 
                  "o:currentAccessPoint": "$ref:WirelessAccessPoint", 
                  "state": "$ref:NetworkDeviceState"
              }
          }
      }


