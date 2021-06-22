import paho.mqtt.client as mqtt

mqtt_server = "192.168.100.150"
port = 1883
temperature_topic = "sensorpi/temperature"
mqtt_username = "pascal"
mqtt_password = "pascalinmqttkolmio"

def on_connect(client, userdata, flags, rc):
    print('Connection successful!')
    client.subscribe(temperature_topic)

def on_message(client, userdata, msg):
    print(msg.topic + ' ' + str(msg.payload))

def main():
    Client = mqtt.Client()
    Client.username_pw_set(mqtt_username, mqtt_password)
    Client.on_connect = on_connect
    Client.on_message = on_message

    Client.connect(mqtt_server)
    try:
        Client.loop_forever()
    except KeyboardInterrupt:
        print("Interrupted by user!")

if __name__ == '__main__':
    print('MQTT to InfluxDB bridge')
    main()