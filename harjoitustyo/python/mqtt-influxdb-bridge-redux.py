import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient
from typing import NamedTuple

# Influx parameters
INFLUXDB_ADDRESS = '192.168.100.150'
INFLUXDB_USER = 'mqtt'
INFLUXDB_PASSWORD = 'pascalinmqttkolmio'
INFLUXDB_DATABASE = 'mqtt-measurements-final'

influxdb_client = InfluxDBClient(INFLUXDB_ADDRESS, 8086, INFLUXDB_USER, INFLUXDB_PASSWORD, None)

MQTT_ADDRESS = '192.168.100.150'
MQTT_USER = 'pascal'
MQTT_PASSWORD = 'pascalinmqttkolmio'
MQTT_TOPIC_VANTAA = 'sensorpi/+/+'
MQTT_TOPIC_SAVIA = 'savia/+/+/+'
MQTT_TOPIC_REAL = 'openweather/+/+'
MQTT_CLIENT_ID = 'MQTTInfluxDBBridge'
MQTT_TOPICS = {MQTT_TOPIC_VANTAA, MQTT_TOPIC_SAVIA, MQTT_TOPIC_REAL}

# CONST FOR FAULT TOLERANCE
PREV_PAYLOAD = float(0)

class SensorData(NamedTuple):
    measurement: str
    location: str
    value: float

def on_connect(client, userdata, flags, rc):
    print('Connected with result code ' + str(rc))
    for topic in MQTT_TOPICS:
        client.subscribe(topic)

def _parse_mqtt_message(topic, payload):
    global PREV_PAYLOAD
    topic_data = topic.split("/", 1)
    measurement = topic_data[0]
    location = topic_data[1]
    try:
        payload = float(payload)
    except ValueError:
        payload = PREV_PAYLOAD
    
    if payload != 0:
        PREV_PAYLOAD = payload
    else:
        pass

    return SensorData(measurement, location, payload) 

def on_message(client, userdata, msg):
    """The callback for when a PUBLISH message is received from the server."""
    sensor_data = None
    print(str(msg.topic) + ' ' + str(msg.payload.decode('utf-8')))
    if msg.payload is not "unavailable":
        sensor_data = _parse_mqtt_message(msg.topic, msg.payload.decode('utf-8'))
        try:
            if sensor_data is not None:
                _send_sensor_data_to_influxdb(sensor_data)
            else:
                print("Data was None")
        except ValueError:
            pass

    else:
        print("Payload was unavailable!")

def on_log(client, userdata, level, buf):
    print(buf)

def _send_sensor_data_to_influxdb(sensor_data):
    json_body = [
        {
            'measurement': sensor_data.measurement,
            'tags': {
                'location': sensor_data.location
            },
            'fields': {
                'value': sensor_data.value
            }
        }
    ]
    influxdb_client.write_points(json_body)

def _init_influxdb_database():
    databases = influxdb_client.get_list_database()
    if len(list(filter(lambda x: x['name'] == INFLUXDB_DATABASE, databases))) == 0:
        influxdb_client.create_database(INFLUXDB_DATABASE)
    influxdb_client.switch_database(INFLUXDB_DATABASE)

def main():
    _init_influxdb_database()

    mqtt_client = mqtt.Client(MQTT_CLIENT_ID)
    
    mqtt_client.enable_logger()
    mqtt_client.on_log = on_log

    mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    mqtt_client.connect(MQTT_ADDRESS, 1883)
    mqtt_client.loop_forever()

if __name__ == '__main__':
    print('MQTT to InfluxDB bridge')
    main()
