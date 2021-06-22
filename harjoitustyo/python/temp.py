from gpiozero import CPUTemperature

def measure_cpu_temp():
    temp = CPUTemperature()
    return temp.temperature

print(measure_cpu_temp())
