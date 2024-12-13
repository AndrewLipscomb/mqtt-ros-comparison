#!/usr/bin/python3

import time
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

# Callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(f"Received message on {msg.topic}: {msg.payload}")

# Create a FlatBuffer builder
builder = flatbuffers.Builder(1024)

# Serialize a Monster
name = builder.CreateString("Goblin")

Monster.MonsterStart(builder)
Monster.MonsterAddName(builder, name)
Monster.MonsterAddHp(builder, 300)
monster = Monster.MonsterEnd(builder)

builder.Finish(monster)

# Get the serialized byte array
buf = builder.Output()

# Set up MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Start the loop
client.loop_start()

while True:
    # Publish the serialized FlatBuffers message to the "monster" topic
    client.publish(MQTT_TOPIC, buf)

    time.sleep(1.0)

# Stop the loop after sending the message
client.loop_stop()
client.disconnect()

print("Message sent to topic:", MQTT_TOPIC)