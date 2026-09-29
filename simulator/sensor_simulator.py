import random
import time
from datetime import datetime


def generate_sensor_data():
    return {
        "timestamp": datetime.now().isoformat(),
        "temperature": round(random.uniform(18.0, 30.0), 2),
        "humidity": round(random.uniform(35.0, 75.0), 2),
        "light": random.randint(0, 1000),
        "air_quality": random.randint(0, 500)
    }


while True:
    data = generate_sensor_data()

    print(data)

    time.sleep(2)
