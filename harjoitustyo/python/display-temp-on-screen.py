# -*- coding: utf-8 -*-
import time
from sense_hat import SenseHat
from temp_disp_use import GetTemp

sense=SenseHat()
sense.low_light = True

def main():
    try:
        while True:
            GetTemp()
            time.sleep(900)
    except KeyboardInterrupt:
        print("Interrupted by user!")

if __name__ == '__main__':
    print('Temperature display on Sense Hat screen...')
    main()