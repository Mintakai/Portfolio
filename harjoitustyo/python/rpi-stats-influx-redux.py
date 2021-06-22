# -*- coding: utf-8 -*-
import argparse
import time
import datetime
import sys
from influxdb import InfluxDBClient
from sense_hat import SenseHat
from gpiozero import CPUTemperature
from temp_disp_use import GetTemp

sense=SenseHat()
 
# Set required InfluxDB parameters.
# (this could be added to the program args instead of beeing hard coded...)
host = "192.168.100.150" #Could also set local ip address
port = 8086
user = "pascal"
password = "pascalinkolmio"
 
# Sample period (s).
# How frequently we will write sensor data from SenseHat to the database.
sampling_period = 5

def get_args():
    '''This function parses and returns arguments passed in'''
    # Assign description to the help doc
    parser = argparse.ArgumentParser(description='Program writes measurements data from SenseHat to specified influx db.')
    # Add arguments
    parser.add_argument(
        '-db','--database', type=str, help='Database name', required=True)
    parser.add_argument(
        '-sn','--session', type=str, help='Session', required=True)
    now = datetime.datetime.now()
    parser.add_argument(
        '-rn','--run', type=str, help='Run number', required=False,default=now.strftime("%Y%m%d"))
    
    # Array of all arguments passed to script
    args=parser.parse_args()
    # Assign args to variables
    dbname=args.database
    runNo=args.run
    session=args.session
    return dbname, session,runNo
    
def measure_cpu_temp():
        temp = CPUTemperature()
        return temp.temperature

def get_data_points():
    # Get the three measurement values from the SenseHat sensors
    temperature = sense.get_temperature()
    pressure = sense.get_pressure()
    humidity = sense.get_humidity()
    cpu_temp = measure_cpu_temp()
    # Get a local timestamp
    timestamp=datetime.datetime.utcnow().isoformat()
    print ("{0} {1} Temperature: {2}{3}C Pressure: {4}mb Humidity: {5}% CPU Temp: {6}C".format(session,runNo,
    round(temperature,1),u'u00b0'.encode('utf8'),
    round(pressure,3),round(humidity,1),round(cpu_temp,1)))
    
    # Create Influxdb datapoints (using lineprotocol as of Influxdb >1.1)
    datapoints = [
            {
                "measurement": session,
                "tags": {"runNum": runNo,
                },
                "time": timestamp,
                "fields": {
                    "temperaturevalue":temperature,"pressurevalue":pressure,"humidityvalue":humidity,"cputempvalue":cpu_temp
                    }
                }
            ]
    return datapoints

# Match return values from get_arguments()
# and assign to their respective variables
dbname, session, runNo =get_args()   
print("Session: ", session)
print("Run No: ", runNo)
print("DB name: ", dbname)

# Initialize the Influxdb client
client = InfluxDBClient(host, port, user, password, dbname)
        
try:
     while True:
        # Write datapoints to InfluxDB
        datapoints=get_data_points()
        bResult=client.write_points(datapoints)
        print("Write points {0} Bresult:{1}".format(datapoints,bResult))
        
        # sense.show_message("OK")
            
        # Wait for next sample
        time.sleep(sampling_period)

        # Show temperature value on Sense Hat screen
        GetTemp()
        
        # Run until keyboard ctrl-c
except KeyboardInterrupt:
    print ("Program stopped by keyboard interrupt [CTRL_C] by user. ")