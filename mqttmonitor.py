# MQTT Client demo
# Continuously monitor two different MQTT topics for data,
# check if the received data matches two predefined 'commands'

import paho.mqtt.client as mqtt
import sqlite3 as sqlite3
from datetime import datetime


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):


    print("Connected with result code "+str(rc))
        # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("myoware/results")
#    client.subscribe("myoware/results2")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    msg.payload = msg.payload.decode("utf-8")
    #    print(msg.topic+" "+str(msg.payload))
    print("Received from "+ msg.topic+" "+ str(msg.payload))
    msg.payload=int(msg.payload)
    reading = msg.payload
    #csvoperation(reading)
    #print(msg.payload)
    # if msg.payload >= 1000:
    #     sendsms()
    #     print("Received message #2, do something else")

    #dbinsert(reading)


    # if msg.payload == "13":
    #     print("Received message #1, do something")

        # Do something



        # Do something else

# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#desktop
#client.connect("192.168.1.3", 1883, 60)
#hall
client.connect("192.168.0.196", 1883, 60)
#hotspot
#client.connect("192.168.126.151", 1883, 60)

# Process network traffic and dispatch callbacks. This will also handle
# reconnecting. Check the documentation at
# https://github.com/eclipse/paho.mqtt.python
# for information on how to use other loop*() functions
client.loop_forever()
