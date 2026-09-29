import json
import random
import time
from datetime import datetime

import paho.mqtt.client as mqtt


BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "eleni-iot-project/environment"


def generate_sensor_data():
    return {
        "timestamp": datetime.now().isoformat(),
        "temperature": round(random.uniform(18.0, 30.0), 2),
        "humidity": round(random.uniform(35.0, 75.0), 2),
        "light": random.randint(0, 1000),
        "air_quality": random.randint(0, 500)
    }


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

print("Connecting to MQTT broker...")
client.connect(BROKER, PORT, 60)
client.loop_start()

print("Connected!")
print(f"Publishing sensor data to: {TOPIC}")


try:
    while True:
        data = generate_sensor_data()

        message = json.dumps(data)

        client.publish(TOPIC, message)

        print(f"Published: {message}")

        time.sleep(2)

except KeyboardInterrupt:
    print("\nSensor simulator stopped.")

finally:
    client.loop_stop()
    client.disconnect()