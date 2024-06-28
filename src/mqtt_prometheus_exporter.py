import os
from flask import Flask, Response
from prometheus_client import Gauge, generate_latest
import paho.mqtt.client as mqtt

# Create Flask application
app = Flask(__name__)

# Define Prometheus metrics
mqtt_messages = Gauge('mqtt_messages', 'MQTT Messages', ['topic'])

# MQTT message callback
def on_message(client, userdata, message):
    # Try to convert the payload to a float and update the Prometheus gauge
    try:
        mqtt_messages.labels(message.topic).set(float(message.payload))
    except ValueError:
        print(f"Could not convert payload to float: {message.payload}")

# Get connection info from environment variables
mqtt_broker_address = os.getenv("MQTT_BROKER_URL")
mqtt_username = os.getenv("MQTT_USERNAME")
mqtt_password = os.getenv("MQTT_PASSWORD")

# Connect to MQTT broker
client = mqtt.Client()
client.username_pw_set(mqtt_username, mqtt_password)
client.on_message = on_message
client.connect(mqtt_broker_address, 1883, 60)
client.subscribe("#") # Subscribe to all topics
client.subscribe("$SYS/#")  # Subscribe to all topics
client.loop_start()

# Expose Prometheus metrics
@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

# if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000)