#!/usr/bin/python3
import paho.mqtt.client as mqtt
import os
import time
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

mqttc = mqtt.Client()
mqttc.on_connect = on_connect

mqttc.connect(os.environ.get('MQTT_HOST', 'mosquitto'), os.environ.get('MQTT_PORT', 1883), 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
mqttc.loop_start()

while True:
    mqttc.publish("mdm/temperature", "{device: 'xya', x: '42.15', y: '12.11'}")
    time.sleep(1)