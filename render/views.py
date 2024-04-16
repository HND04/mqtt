from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'render/index.html', {})
# views.py
from django.shortcuts import render
import paho.mqtt.client as mqtt

def mqtt_callback(client, userdata, msg):
    # Handle incoming MQTT message
    temperature = msg.payload.decode("utf-8")
    # Update temperature data in Django model or context
    context = {'temperature': temperature}

def mqtt_connect():
    client = mqtt.Client()
    client.on_message = mqtt_callback
    client.connect("public.mqtthq.com", 1883, 60)  # Connect to MQTT broker
    client.subscribe("sensors/temperature")        # Subscribe to MQTT topic
    client.loop_start()                            # Start MQTT client loop

def indexs(request):
    mqtt_connect()  # Connect to MQTT broker
    # Render Django template with temperature data
    return render(request, 'render/indexs.html', context)
