#!/usr/bin/python3

import flatbuffers
import paho.mqtt.client as mqtt
import Messages.Monster as Monster

# MQTT Configuration
MQTT_BROKER = "localhost"  # Use a public broker for testing, or your local broker
MQTT_PORT = 1883
MQTT_TOPIC = "monster"

# Callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribe to the "monster" topic
    client.subscribe(MQTT_TOPIC)

# Callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(f"Message received on topic {msg.topic}")

    # Deserialize the Monster from the message payload
    buf = msg.payload
    monster = Monster.Monster.GetRootAsMonster(buf, 0)

    # Access and print the Monster's fields
    print("Monster Name:", monster.Name().decode('utf-8'))
    print("Monster HP:", monster.Hp())

# Set up the MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Start the loop to process network events
client.loop_forever()