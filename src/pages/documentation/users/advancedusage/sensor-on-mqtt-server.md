---
id: sensor-on-mqtt-server
title: Publishing sensor values to nymea via MQTT
---

In this example we're going to publish sensor values via MQTT to nymea and attach them to a virtual sensor thing for a nice graph.

Assume you have a home-brew weather station which can read temperature sensor values and publish them to a MQTT server. We will establish a MQTT connection to nymea and post those values to a topic named `/example/temp1/`

### Enabling the MQTT broker
First, make sure the MQTT broker is enabled in nymea. For that, open System Settings and go the MQTT broker section. In there, make sure there is at lase one MQTT server interface enabled. If not, click the "Add" button to add one. Pick the desired interface (Leave to "Any" if unsure) and a port. Normally MQTT uses port 1883. Make sure there aren't any other services blocking the port you choose. Enable SSL encryption and/or login if desired. In this example we'll enable authentication but won't enable SSL encryption.

![](/img/documentation/users/mqtt-server.png)


### Create a policy for the client
Because we've enabled authentication with the "login required" option before, we need to create a policy to allow the client to log in. This may can be skipped if the MQTT server interface has been configured without login required.

In the MQTT permissions section, click the "Add" button and fill in the details in the next page. The Client ID cannot be blank. You can pick a random string there. We'll name it `tempsensor1` and enter a username and password of `test` and `test`. The next step is to set up permissions of the client on the MQTT broker. We want it to publish to the `/example/temp1` topic but don't want it to subscribe to anything on the server. For that we remove the default entry of `#` in the "Allowed publish topics" by longpressing/swiping it and add a new one pointing to `/example/temp1`. We can delete the default of `#` in the "Allowed subscribe topcis" section and don't need to add anything. For more details on how MQTT topic filters work, please refer to the MQTT documentation.
    
![](/img/documentation/users/mqtt-policy.png)


### Connect the client

Now it's time to test the connection of the client to nymea. In this example we'll be using `mosquitto_pub` to publish the values to nymea from another machine:

We'll be using `-h <ip-of-nymea>` and `-p <port>` to provide the IP address and port of the nymea instance. In our example, nymea would be running on the machine with the IP address 192.168.0.200 and we've configured the MQTT server interface to listen on port 1883.

As we've enabled authentication we need to provide the client ID using `-i`, the username with `-u` and the password with `-P`. In addition to that, we'll be using the topic (`-t`) "/example/temp1" and post the message (`-b`) "10" to simulate a sensor value of 10 degrees.

```Bash
$ mosquitto_pub -h 192.168.0.200 -p 1883 -i tempsensor1 -u test -P test -t /example/temp1 -m 10
```

If this fails with an error, something has gone wrong. For example, if clientId, the password or the username are incorrect, it would fail with this error:
```Bash
Connection error: Connection Refused: identifier rejected.
```

However, if this command ends without any output, all seems good for now.

### Getting logs if things don't work

If things don't work as expected, we can use the debug interface to check nymeas logs. For that, make sure the debug interface is enabled in System Settings -> Developer tools and open the debug interface using the web browser by navigating to the url http://192.168.0.200:80/debug. As before, replace the IP with the actual IP of the nymea server.

> Note: If you've changed the Webserver port in System Settings -> Webserver, you also need to adjust the port in the URL.

In the debug interface, navigate to the logs tab, enable the MQTT logs and click on "Start logs". Every time you publish something to the MQTT server, this log should appear:

```
 I | Mqtt: Accepting client "tempsensor1" . Login successful.
 I | Mqtt: Client "tempsensor1" connected with username "test" from "192.168.0.201"
 I | Mqtt: Client "tempsensor1" disconnected
```

### Processing the MQTT messages

Now that we're publishing MQTT messages to nymea, we also need to subscribe to the topic in order to receive the values. For that, we'll be using the MQTT client plugin.

Go to Configure Things and press the `+` button to add a new thing. Select the "Internal MQTT client" thing. In the next page, enter the desired topic to subscribe to. In this example that will be again `/example/temp1`. Once done, click OK. 

![](/img/documentation/users/internal-mqtt-client.png)

Returning to the main view of the app, we'll find a new category named "Incoming events" having appeared. Enter there and you'll find the incoming events on the MQTT server in the topic `/example/temp1`.

Now send a MQTT message again with mosquitto_pub and you'll find the message appearing in this log.

![](/img/documentation/users/incoming-mqtt-messages.png)

Congratulations, you've now captured an MQTT sensor event in nymea. This, however, is still not as useful as we'd like it to be, right? We want it to look like a pretty temperature sensor, don't we?

### Presenting the data as a temperature sensor

For this, we add another thing to the system using "Configure Things -> `+`". This time we'll pick a "Generic Temperature Sensor". The sensor will appear right there in the app, however, it's value is not updated yet. One last piece is missing. We need to process the MQTT message to extract the sensor value and feed it into the generic sensor.

Enter the "Magic" section in the app and navigate to the scripting toolbox with the icon on the upper right. Create a new script using the `+` button.

In the script we first need to fetch the events from the MQTT client by adding this snippet:

```QML
ThingEvent {
    thingId: "..." // Internal MQTT client
    eventName: "triggered"
    onTriggered: {
        console.log("MQTT event reveived:", JSON.stringify(params));
    }
}
```

Now deploy the script to nymea but don't exit the script editor yet. If you now use mosquitto_pub to send the event again, the script console will pop up printing this message:

```
MQTT event received {"27ec8baf-0c13-4d0a-aaee-313582592695":"/example/temp1","8af98566-79d9-4e65-b1dc-9067e4f93af1":"18","data":"18","topic":"/example/temp1"}
```

Now we can see the payload of the MQTT message in the `data` field of the params. We can access it using `params["value"]`.

Next thing is to feed that value into the Generic Temperature Sensor thing using such a script snippet:

```QML
ThingState {
    thingId: "..." // Generic Temperature Sensor
    stateName: "input"
}
```

All generic things have an input state which takes floating point values from 0 to 1. The generic temperature sensor will calculate the temperature using this input value by mapping it to the minimum/maximum range defined in its settings. By default this will be from -20°C to +50°C. This means, we'll need to generate an input value ranging from 0 to 1, which represents temperature sensor values from -20 to +50. We can do this with the simple formula `(params["data"] + 20) / 70`. So let's extend the first snipped to transform the value and write it to the generic sensor thing:

```QML
ThingEvent {
    thingId: "..." // Internal MQTT client
    eventName: "triggered"
    onTriggered: {
        console.log("MQTT event reveived:", JSON.stringify(params));
        temp1.value = (1.0 * params["data"] + 20) / 70
    }
}
```

The final script would look something like this:

![](/img/documentation/users/mqtt-to-temp-script.png)

And we're done. Now, whenever you send something to nymea with mosquitto_pub, it will update the temperature sensor. 

![](/img/documentation/users/temp-via-mqtt.png)

You can adjust the formula above according to your liking. For instance if your MQTT client can only send JSON, you will get the entire JSON message in the `data` parameter and can unpack and extract relevant information using JSON.parse(). Or if your input sensor is using a different mapping, for example it sends values from 1 to 10, it can be taken into account and map values accordingly.
