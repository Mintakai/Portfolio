import argparse
import time
import datetime
import sys
import os
import paho.mqtt.client as mqtt
from sense_hat import SenseHat
from gpiozero import CPUTemperature
from temp_disp_use import GetTemp

sense=SenseHat()

mqtt_server = "192.168.100.150"
port = 1883
temperature_topic = "sensorpi/outside/temperature"
mqtt_username = "pascal"
mqtt_password = "pascalinmqttkolmio"

flag_connected = 0

def get_args():
    # Assign description to the help doc
    parser = argparse.ArgumentParser(description='Program writes measurements data from SenseHat to MQTT Broker.')
    # Add arguments
    parser.add_argument(
        '-id','--client_id', type=str, help='Client ID', required=False, default='client_sensorpi')
    # parser.add_argument(
    #    '-cs','--clean_session', type=str, help='Clean Session', required=False)
    # parser.add_argument(
    #    '-ud','--userdata', type=str, help='User Data', required=False)
    # parser.add_argument(
    #    '-pc','--protocol', type=str, help='Protocol', required=False)
    # parser.add_argument(
    #    '-tp','--transport', type=str, help='Transport', required=False)
    
    # Array of all arguments passed to script
    args=parser.parse_args()
    # Assign args to variables
    clientid=args.client_id
    # cleansession=args.clean_session
    # userdata=args.userdata
    # protocol=args.protocol
    # transport=args.transport

    return clientid

def get_temp():
    temperature = sense.get_temperature()
    print("Temperature: {0}".format(temperature))

    return temperature

def connect_to_broker():
    Client.username_pw_set(username=mqtt_username,password=mqtt_password)
    try:
        print("Connecting to broker...")
        Client.connect(mqtt_server)
    except:
        print("Connection failed!")

# def on_connect(client, userdata, rc):
    # global flag_connected
    # flag_connected = 1
    # print("Connection established")

# def on_disconnect(client, userdata, rc):
    # global flag_connected
    # flag_connected = 0
    # print("Connection interrupted")

# Match return values from get_arguments()
# and assign to their respective variables
clientid = get_args()   
print("Client ID: {0}".format(clientid))

Client = mqtt.Client(clientid)
# Client.on_connect = on_connect
# Client.on_disconnect = on_disconnect

connect_to_broker()

try:
    while True:
        Client.publish(temperature_topic, get_temp())
        time.sleep(60)
        
except KeyboardInterrupt:
    print("Interrupted by user!")

