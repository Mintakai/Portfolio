import time
import paho.mqtt.publish as publish
from sense_hat import SenseHat
from get_real_weather import get_real_temp

mqtt_server = "192.168.100.150"
mqtt_clientid = "SensorPi_Redux"
port = 1883
temperature_topic = "sensorpi/outside/temperature"
real_temperature_topic = "openweather/vantaa/realtemp"
mqtt_username = "pascal"
mqtt_password = "pascalinmqttkolmio"

sense = SenseHat()

def get_temp():
    temperature = "{temp:.2f}".format(temp=sense.get_temperature())

    return temperature

msgs = [{'topic':temperature_topic, 'payload':get_temp()},
        {'topic':real_temperature_topic, 'payload':get_real_temp()}]

# publish.single(temperature_topic, payload=get_temp(), hostname=mqtt_server, port=1883, client_id=mqtt_clientid, auth={'username':mqtt_username, 'password':mqtt_password})
publish.multiple(msgs, hostname=mqtt_server, port=1883, client_id=mqtt_clientid, auth={'username':mqtt_username, 'password':mqtt_password})