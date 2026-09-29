import json

import paho.mqtt.client as mqtt


BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "eleni-iot-project/environment"


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Connected to MQTT broker!")
        print(f"Listening for sensor data on: {TOPIC}")
        client.subscribe(TOPIC)
    else:
        print(f"Connection failed with code: {reason_code}")


def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8")
    data = json.loads(payload)

    print("\nNew sensor data received:")
    print(f"Temperature: {data['temperature']} °C")
    print(f"Humidity: {data['humidity']} %")
    print(f"Light: {data['light']}")
    print(f"Air Quality: {data['air_quality']}")
    print(f"Timestamp: {data['timestamp']}")


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_connect = on_connect
client.on_message = on_message

print("Connecting to MQTT broker...")

client.connect(BROKER, PORT, 60)

try:
    client.loop_forever()

except KeyboardInterrupt:
    print("\nMQTT receiver stopped.")

finally:
    client.disconnect()