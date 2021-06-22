import os
import time
from sense_hat import SenseHat

# Get CPU temp
def get_cpu_temp():
    res = os.popen("vcgencmd measure_temp").readline()
    t = float(res.replace("temp=","").replace("'C\n",""))

    return t

# Average
def get_smooth(x):
    if not hasattr(get_smooth, "t"):
        get_smooth.t = [x,x,x]
    get_smooth.t[2] = get_smooth.t[1]
    get_smooth.t[1] = get_smooth.t[0]
    get_smooth.t[0] = x
    xs = (get_smooth.t[0] + get_smooth.t[1] + get_smooth.t[2]) / 3
    return xs

sense = SenseHat()

while True:
    t1 = sense.get_temperature_from_humidity()
    t2 = sense.get_temperature_from_pressure()
    cpu_temperature = get_cpu_temp()

    t = (t1+t2) / 2
    cor_t = t - ((cpu_temperature) / 1.5)
    cor_t = get_smooth(cor_t)

    time.sleep(5)

    print(cor_t)