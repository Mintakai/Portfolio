import time
from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()
sense.low_light = True

try:
    while True:
        time.sleep(0.5)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        temp = sense.get_temperature()
        tempFromHum = sense.get_temperature_from_humidity()
        tempFromPress = sense.get_temperature_from_pressure()
        press = sense.get_pressure()
        hum = sense.get_humidity()
        
        if (temp < 0):
            sense.show_letter("E",[255,0,0])
        else:
            sense.show_letter("K",[0,255,0])

        if (temp < 0) or (tempFromHum < 0) or (tempFromPress < 0):
            print("Date & time\n")
            print(dt_string + "\n")
            print("Data \n")
            print("--------")
            print("Temperature: \t{0}").format(temp)
            print("TempH: \t\t{0}").format(tempFromHum)
            print("TempP: \t\t{0}").format(tempFromPress)
            print("Pressure: \t{0}").format(press)
            print("Humidity: \t{0}").format(hum)
            print("--------")
            print("INTERRUPTED!")
            break
        else:
            print("Date & time\n")
            print(dt_string + "\n")
            print("Data \n")
            print("--------")
            print("Temperature: \t{0}").format(temp)
            print("TempH: \t\t{0}").format(tempFromHum)
            print("TempP: \t\t{0}").format(tempFromPress)
            print("Pressure: \t{0}").format(press)
            print("Humidity: \t{0}").format(hum)
            print("--------\n\n")

except KeyboardInterrupt:
    print ("Program stopped by keyboard interrupt [CTRL_C] by user. ")
