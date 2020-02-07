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

Whenever replying to a request, nymea:core will fill in the same `id` as the request contained. A client may use this `id` to match a given response to the request it had sent to nymea:core earlier. The `status` field always contains one of the two values of `success` or `error`. If the request passed validation, this will be set to `success`, otherwise, for instance if the used method has not been found, this will contain `error`. In case of success, the response will contain an additional field `params` conaining the response params. The actual content again depends on the acutal called method in the request. In case of failure, instead of params, the response will contain an `error` field with a message that might help the client developer to determine the source of the problem. This error message will always indicate a program error and should not be presented to the user.

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


## The complete API

@@GENERATED@@
