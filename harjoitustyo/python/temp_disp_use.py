import time
from sense_hat import SenseHat

def GetTemp():
    sense = SenseHat()
    temp = sense.get_temperature()
    temp = temp / 1.6 - 5
    temp = round(temp,0)

    o = (0,0,0)
    if temp <= 10:
        r = (0,0,255)
    elif temp <= 29:
        r = (0,255,0)
    elif temp >= 30:
        r = (255,0,0)

    minus = [
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,r,r,r,r,r,r,o,
        o,r,r,r,r,r,r,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        ]
    
    zero = [
        o,o,o,o,o,o,o,o,
        o,o,o,r,o,o,o,o,
        o,o,r,o,r,o,o,o,
        o,o,r,o,r,o,o,o,
        o,o,r,o,r,o,o,o,
        o,o,r,o,r,o,o,o,
        o,o,o,r,o,o,o,o,
        o,o,o,o,o,o,o,o,
        ]
    
    one = [
        o,o,o,o,o,o,o,o,
        o,o,o,r,o,o,o,o,
        o,o,o,r,o,o,o,o,
        o,o,o,r,o,o,o,o,
        o,o,o,r,o,o,o,o,
        o,o,o,r,o,o,o,o,
        o,o,o,r,o,o,o,o,
        o,o,o,o,o,o,o,o,
        ]
    
    two = [
        o,o,o,o,o,o,o,o,
        o,o,r,r,r,o,o,o,
        o,o,o,o,r,o,o,o,
        o,o,r,r,r,o,o,o,
        o,o,r,o,o,o,o,o,
        o,o,r,o,o,o,o,o,
        o,o,r,r,r,o,o,o,
        o,o,o,o,o,o,o,o,
        ]
        
    three = [
        o,o,o,o,o,o,o,o,
        o,o,r,r,r,o,o,o,
        o,o,o,o,r,o,o,o,
        o,o,r,r,r,o,o,o,
        o,o,o,o,r,o,o,o,
        o,o,o,o,r,o,o,o,
        o,o,r,r,r,o,o,o,
        o,o,o,o,o,o,o,o,
        ]
    
    four = [
        o,o,o,o,o,o,o,o,
        o,o,r,o,r,o,o,o,
        o,o,r,o,r,o,o,o,
        o,o,r,r,r,o,o,o,
        o,o,o,o,r,o,o,o,
        o,o,o,o,r,o,o,o,
        o,o,o,o,r,o,o,o,
        o,o,o,o,o,o,o,o,
        ]
    
    five = [
        o,o,o,o,o,o,o,o,
        o,o,r,r,r,o,o,o,
        o,o,r,o,o,o,o,o,
        o,o,r,r,r,o,o,o,
        o,o,o,o,r,o,o,o,
        o,o,o,o,r,o,o,o,
        o,o,r,r,r,o,o,o,
        o,o,o,o,o,o,o,o,
        ]
    
    six = [
        o,o,o,o,o,o,o,o,
        o,o,r,r,r,o,o,o,
        o,o,r,o,o,o,o,o,
        o,o,r,r,r,o,o,o,
        o,o,r,o,r,o,o,o,
        o,o,r,o,r,o,o,o,
        o,o,r,r,r,o,o,o,
        o,o,o,o,o,o,o,o,
        ]
    
    seven = [
        o,o,o,o,o,o,o,o,
        o,o,r,r,r,o,o,o,
        o,o,o,o,r,o,o,o,
        o,o,o,o,r,o,o,o,
        o,o,o,o,r,o,o,o,
        o,o,o,o,r,o,o,o,
        o,o,o,o,r,o,o,o,
        o,o,o,o,o,o,o,o,
        ]
    
    eight = [
        o,o,o,o,o,o,o,o,
        o,o,r,r,r,o,o,o,
        o,o,r,o,r,o,o,o,
        o,o,r,r,r,o,o,o,
        o,o,r,o,r,o,o,o,
        o,o,r,o,r,o,o,o,
        o,o,r,r,r,o,o,o,
        o,o,o,o,o,o,o,o,
        ]
    
    nine = [
        o,o,o,o,o,o,o,o,
        o,o,r,r,r,o,o,o,
        o,o,r,o,r,o,o,o,
        o,o,r,r,r,o,o,o,
        o,o,o,o,r,o,o,o,
        o,o,o,o,r,o,o,o,
        o,o,r,r,r,o,o,o,
        o,o,o,o,o,o,o,o,
        ]
    
    ten = [
        o,o,o,o,o,o,o,o,
        o,r,o,o,o,r,o,o,
        o,r,o,o,r,o,r,o,
        o,r,o,o,r,o,r,o,
        o,r,o,o,r,o,r,o,
        o,r,o,o,r,o,r,o,
        o,r,o,o,o,r,o,o,
        o,o,o,o,o,o,o,o,
        ]
    
    eleven = [
        o,o,o,o,o,o,o,o,
        o,r,o,o,r,o,o,o,
        o,r,o,o,r,o,o,o,
        o,r,o,o,r,o,o,o,
        o,r,o,o,r,o,o,o,
        o,r,o,o,r,o,o,o,
        o,r,o,o,r,o,o,o,
        o,o,o,o,o,o,o,o,
        ]
    
    twelve = [
        o,o,o,o,o,o,o,o,
        o,r,o,o,r,r,r,o,
        o,r,o,o,o,o,r,o,
        o,r,o,o,r,r,r,o,
        o,r,o,o,r,o,o,o,
        o,r,o,o,r,o,o,o,
        o,r,o,o,r,r,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    thirteen = [
        o,o,o,o,o,o,o,o,
        o,r,o,o,r,r,r,o,
        o,r,o,o,o,o,r,o,
        o,r,o,o,r,r,r,o,
        o,r,o,o,o,o,r,o,
        o,r,o,o,o,o,r,o,
        o,r,o,o,r,r,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    fourteen = [
        o,o,o,o,o,o,o,o,
        o,r,o,o,r,o,r,o,
        o,r,o,o,r,o,r,o,
        o,r,o,o,r,r,r,o,
        o,r,o,o,o,o,r,o,
        o,r,o,o,o,o,r,o,
        o,r,o,o,o,o,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    fifteen = [
        o,o,o,o,o,o,o,o,
        o,r,o,o,r,r,r,o,
        o,r,o,o,r,o,o,o,
        o,r,o,o,r,r,r,o,
        o,r,o,o,o,o,r,o,
        o,r,o,o,o,o,r,o,
        o,r,o,o,r,r,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    sixteen = [
        o,o,o,o,o,o,o,o,
        o,r,o,o,r,r,r,o,
        o,r,o,o,r,o,o,o,
        o,r,o,o,r,r,r,o,
        o,r,o,o,r,o,r,o,
        o,r,o,o,r,o,r,o,
        o,r,o,o,r,r,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    seventeen = [
        o,o,o,o,o,o,o,o,
        o,r,o,o,r,r,r,o,
        o,r,o,o,o,o,r,o,
        o,r,o,o,o,o,r,o,
        o,r,o,o,o,o,r,o,
        o,r,o,o,o,o,r,o,
        o,r,o,o,o,o,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    eighteen = [
        o,o,o,o,o,o,o,o,
        o,r,o,o,r,r,r,o,
        o,r,o,o,r,o,r,o,
        o,r,o,o,r,r,r,o,
        o,r,o,o,r,o,r,o,
        o,r,o,o,r,o,r,o,
        o,r,o,o,r,r,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    nineteen = [
        o,o,o,o,o,o,o,o,
        o,r,o,o,r,r,r,o,
        o,r,o,o,r,o,r,o,
        o,r,o,o,r,r,r,o,
        o,r,o,o,o,o,r,o,
        o,r,o,o,o,o,r,o,
        o,r,o,o,r,r,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    twenty = [
        o,o,o,o,o,o,o,o,
        r,r,r,o,o,r,o,o,
        o,o,r,o,r,o,r,o,
        r,r,r,o,r,o,r,o,
        r,o,o,o,r,o,r,o,
        r,o,o,o,r,o,r,o,
        r,r,r,o,o,r,o,o,
        o,o,o,o,o,o,o,o,
        ]
    
    twentyone = [
        o,o,o,o,o,o,o,o,
        r,r,r,o,o,r,o,o,
        o,o,r,o,o,r,o,o,
        r,r,r,o,o,r,o,o,
        r,o,o,o,o,r,o,o,
        r,o,o,o,o,r,o,o,
        r,r,r,o,o,r,o,o,
        o,o,o,o,o,o,o,o,
        ]
    
    twentytwo = [
        o,o,o,o,o,o,o,o,
        r,r,r,o,r,r,r,o,
        o,o,r,o,o,o,r,o,
        r,r,r,o,r,r,r,o,
        r,o,o,o,r,o,o,o,
        r,o,o,o,r,o,o,o,
        r,r,r,o,r,r,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    twentythree = [
        o,o,o,o,o,o,o,o,
        r,r,r,o,r,r,r,o,
        o,o,r,o,o,o,r,o,
        r,r,r,o,r,r,r,o,
        r,o,o,o,o,o,r,o,
        r,o,o,o,o,o,r,o,
        r,r,r,o,r,r,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    twentyfour = [
        o,o,o,o,o,o,o,o,
        r,r,r,o,r,o,r,o,
        o,o,r,o,r,o,r,o,
        r,r,r,o,r,r,r,o,
        r,o,o,o,o,o,r,o,
        r,o,o,o,o,o,r,o,
        r,r,r,o,o,o,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    twentyfive = [
        o,o,o,o,o,o,o,o,
        r,r,r,o,r,r,r,o,
        o,o,r,o,r,o,o,o,
        r,r,r,o,r,r,r,o,
        r,o,o,o,o,o,r,o,
        r,o,o,o,o,o,r,o,
        r,r,r,o,r,r,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    twentysix = [
        o,o,o,o,o,o,o,o,
        r,r,r,o,r,r,r,o,
        o,o,r,o,r,o,o,o,
        r,r,r,o,r,r,r,o,
        r,o,o,o,r,o,r,o,
        r,o,o,o,r,o,r,o,
        r,r,r,o,r,r,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    twentyseven = [
        o,o,o,o,o,o,o,o,
        r,r,r,o,r,r,r,o,
        o,o,r,o,o,o,r,o,
        r,r,r,o,o,o,r,o,
        r,o,o,o,o,o,r,o,
        r,o,o,o,o,o,r,o,
        r,r,r,o,o,o,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    twentyeight = [
        o,o,o,o,o,o,o,o,
        r,r,r,o,r,r,r,o,
        o,o,r,o,r,o,r,o,
        r,r,r,o,r,r,r,o,
        r,o,o,o,r,o,r,o,
        r,o,o,o,r,o,r,o,
        r,r,r,o,r,r,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    twentynine = [
        o,o,o,o,o,o,o,o,
        r,r,r,o,r,r,r,o,
        o,o,r,o,r,o,r,o,
        r,r,r,o,r,r,r,o,
        r,o,o,o,o,o,r,o,
        r,o,o,o,o,o,r,o,
        r,r,r,o,r,r,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    thirty = [
        o,o,o,o,o,o,o,o,
        r,r,r,o,o,r,o,o,
        o,o,r,o,r,o,r,o,
        r,r,r,o,r,o,r,o,
        o,o,r,o,r,o,r,o,
        o,o,r,o,r,o,r,o,
        r,r,r,o,o,r,o,o,
        o,o,o,o,o,o,o,o,
        ]
    
    thirtyone = [
        o,o,o,o,o,o,o,o,
        r,r,r,o,o,r,o,o,
        o,o,r,o,o,r,o,o,
        r,r,r,o,o,r,o,o,
        o,o,r,o,o,r,o,o,
        o,o,r,o,o,r,o,o,
        r,r,r,o,o,r,o,o,
        o,o,o,o,o,o,o,o,
        ]
    
    thirtytwo = [
        o,o,o,o,o,o,o,o,
        r,r,r,o,r,r,r,o,
        o,o,r,o,o,o,r,o,
        r,r,r,o,r,r,r,o,
        o,o,r,o,r,o,o,o,
        o,o,r,o,r,o,o,o,
        r,r,r,o,r,r,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    thirtythree = [
        o,o,o,o,o,o,o,o,
        r,r,r,o,r,r,r,o,
        o,o,r,o,o,o,r,o,
        r,r,r,o,r,r,r,o,
        o,o,r,o,o,o,r,o,
        o,o,r,o,o,o,r,o,
        r,r,r,o,r,r,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    thirtyfour = [
        o,o,o,o,o,o,o,o,
        r,r,r,o,r,o,r,o,
        o,o,r,o,r,o,r,o,
        r,r,r,o,r,r,r,o,
        o,o,r,o,o,o,r,o,
        o,o,r,o,o,o,r,o,
        r,r,r,o,o,o,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    thirtyfive = [
        o,o,o,o,o,o,o,o,
        r,r,r,o,r,r,r,o,
        o,o,r,o,r,o,o,o,
        r,r,r,o,r,r,r,o,
        o,o,r,o,o,o,r,o,
        o,o,r,o,o,o,r,o,
        r,r,r,o,r,r,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    thirtysix = [
        o,o,o,o,o,o,o,o,
        r,r,r,o,r,r,r,o,
        o,o,r,o,r,o,o,o,
        r,r,r,o,r,r,r,o,
        o,o,r,o,r,o,r,o,
        o,o,r,o,r,o,r,o,
        r,r,r,o,r,r,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    thirtyseven = [
        o,o,o,o,o,o,o,o,
        r,r,r,o,r,r,r,o,
        o,o,r,o,o,o,r,o,
        r,r,r,o,o,o,r,o,
        o,o,r,o,o,o,r,o,
        o,o,r,o,o,o,r,o,
        r,r,r,o,o,o,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    thirtyeight = [
        o,o,o,o,o,o,o,o,
        r,r,r,o,r,r,r,o,
        o,o,r,o,r,o,r,o,
        r,r,r,o,r,r,r,o,
        o,o,r,o,r,o,r,o,
        o,o,r,o,r,o,r,o,
        r,r,r,o,r,r,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    thirtynine = [
        o,o,o,o,o,o,o,o,
        r,r,r,o,r,r,r,o,
        o,o,r,o,r,o,r,o,
        r,r,r,o,r,r,r,o,
        o,o,r,o,o,o,r,o,
        o,o,r,o,o,o,r,o,
        r,r,r,o,r,r,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    forty = [
        o,o,o,o,o,o,o,o,
        r,o,r,o,o,r,o,o,
        r,o,r,o,r,o,r,o,
        r,r,r,o,r,o,r,o,
        o,o,r,o,r,o,r,o,
        o,o,r,o,r,o,r,o,
        o,o,r,o,o,r,o,o,
        o,o,o,o,o,o,o,o,
        ]
    
    fortyone = [
        o,o,o,o,o,o,o,o,
        r,o,r,o,o,r,o,o,
        r,o,r,o,o,r,o,o,
        r,r,r,o,o,r,o,o,
        o,o,r,o,o,r,o,o,
        o,o,r,o,o,r,o,o,
        o,o,r,o,o,r,o,o,
        o,o,o,o,o,o,o,o,
        ]
    
    fortytwo = [
        o,o,o,o,o,o,o,o,
        r,o,r,o,r,r,r,o,
        r,o,r,o,o,o,r,o,
        r,r,r,o,r,r,r,o,
        o,o,r,o,r,o,o,o,
        o,o,r,o,r,o,o,o,
        o,o,r,o,r,r,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    fortythree = [
        o,o,o,o,o,o,o,o,
        r,o,r,o,r,r,r,o,
        r,o,r,o,o,o,r,o,
        r,r,r,o,r,r,r,o,
        o,o,r,o,o,o,r,o,
        o,o,r,o,o,o,r,o,
        o,o,r,o,r,r,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    fortyfour = [
        o,o,o,o,o,o,o,o,
        r,o,r,o,r,o,r,o,
        r,o,r,o,r,o,r,o,
        r,r,r,o,r,r,r,o,
        o,o,r,o,o,o,r,o,
        o,o,r,o,o,o,r,o,
        o,o,r,o,o,o,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    fortyfive = [
        o,o,o,o,o,o,o,o,
        r,o,r,o,r,r,r,o,
        r,o,r,o,r,o,o,o,
        r,r,r,o,r,r,r,o,
        o,o,r,o,o,o,r,o,
        o,o,r,o,o,o,r,o,
        o,o,r,o,r,r,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    fortysix = [
        o,o,o,o,o,o,o,o,
        r,o,r,o,r,r,r,o,
        r,o,r,o,r,o,o,o,
        r,r,r,o,r,r,r,o,
        o,o,r,o,r,o,r,o,
        o,o,r,o,r,o,r,o,
        o,o,r,o,r,r,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    fortyseven = [
        o,o,o,o,o,o,o,o,
        r,o,r,o,r,r,r,o,
        r,o,r,o,o,o,r,o,
        r,r,r,o,o,o,r,o,
        o,o,r,o,o,o,r,o,
        o,o,r,o,o,o,r,o,
        o,o,r,o,o,o,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    fortyeight = [
        o,o,o,o,o,o,o,o,
        r,o,r,o,r,r,r,o,
        r,o,r,o,r,o,r,o,
        r,r,r,o,r,r,r,o,
        o,o,r,o,r,o,r,o,
        o,o,r,o,r,o,r,o,
        o,o,r,o,r,r,r,o,
        o,o,o,o,o,o,o,o,
        ]
    
    fortynine = [
        o,o,o,o,o,o,o,o,
        r,o,r,o,r,r,r,o,
        r,o,r,o,r,o,r,o,
        r,r,r,o,r,r,r,o,
        o,o,r,o,o,o,r,o,
        o,o,r,o,o,o,r,o,
        o,o,r,o,r,r,r,o,
        o,o,o,o,o,o,o,o,
        ]
        
    toocoldorhot = [
        r,r,r,r,r,r,r,r,
        r,r,r,o,o,r,r,r,
        r,r,r,o,o,r,r,r,
        r,r,r,o,o,r,r,r,
        r,r,r,o,o,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,o,o,r,r,r,
        r,r,r,r,r,r,r,r,
        ]
    
    if temp <= -40:
        sense.set_pixels(toocoldorhot)
    elif temp == -39:
        sense.set_pixels(thirtynine)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -38:
        sense.set_pixels(thirtyeight)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -37:
        sense.set_pixels(thirtyseven)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -36:
        sense.set_pixels(thirtysix)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -35:
        sense.set_pixels(thirtyfive)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -34:
        sense.set_pixels(thirtyfour)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -33:
        sense.set_pixels(thirtythree)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -32:
        sense.set_pixels(thirtytwo)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -31:
        sense.set_pixels(thirtyone)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -30:
        sense.set_pixels(thirty)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -29:
        sense.set_pixels(twentynine)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -28:
        sense.set_pixels(twentyeight)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -27:
        sense.set_pixels(twentyseven)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -26:
        sense.set_pixels(twentysix)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -25:
        sense.set_pixels(twentyfive)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -24:
        sense.set_pixels(twentyfour)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -23:
        sense.set_pixels(twentythree)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -22:
        sense.set_pixels(twentytwo)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -21:
        sense.set_pixels(twentyone)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -20:
        sense.set_pixels(twenty)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -19:
        sense.set_pixels(nineteen)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -18:
        sense.set_pixels(eighteen)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -17:
        sense.set_pixels(seventeen)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -16:
        sense.set_pixels(sixteen)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -15:
        sense.set_pixels(fifteen)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -14:
        sense.set_pixels(fourteen)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -13:
        sense.set_pixels(thirteen)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -12:
        sense.set_pixels(twelve)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -11:
        sense.set_pixels(eleven)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -10:
        sense.set_pixels(ten)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -9:
        sense.set_pixels(nine)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -8:
        sense.set_pixels(eight)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -7:
        sense.set_pixels(seven)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -6:
        sense.set_pixels(six)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -5:
        sense.set_pixels(five)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -4:
        sense.set_pixels(four)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -3:
        sense.set_pixels(three)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -2:
        sense.set_pixels(two)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == -1:
        sense.set_pixels(one)
        time.sleep(1)
        sense.set_pixels(minus)
        time.sleep(1)
    elif temp == 0:
        sense.set_pixels(zero)
    elif temp == 1:
        sense.set_pixels(one)
    elif temp == 2:
        sense.set_pixels(two)
    elif temp == 3:
        sense.set_pixels(three)
    elif temp == 4:
        sense.set_pixels(four)
    elif temp == 5:
        sense.set_pixels(five)
    elif temp == 6:
        sense.set_pixels(six)
    elif temp == 7:
        sense.set_pixels(seven)
    elif temp == 8:
        sense.set_pixels(eight)
    elif temp == 9:
        sense.set_pixels(nine)
    elif temp == 10:
        sense.set_pixels(ten)
    elif temp == 11:
        sense.set_pixels(eleven)
    elif temp == 12:
        sense.set_pixels(twelve)
    elif temp == 13:
        sense.set_pixels(thirteen)
    elif temp == 14:
        sense.set_pixels(fourteen)
    elif temp == 15:
        sense.set_pixels(fifteen)
    elif temp == 16:
        sense.set_pixels(sixteen)
    elif temp == 17:
        sense.set_pixels(seventeen)
    elif temp == 18:
        sense.set_pixels(eighteen)
    elif temp == 19:
        sense.set_pixels(nineteen)
    elif temp == 20:
        sense.set_pixels(twenty)
    elif temp == 21:
        sense.set_pixels(twentyone)
    elif temp == 22:
        sense.set_pixels(twentytwo)
    elif temp == 23:
        sense.set_pixels(twentythree)
    elif temp == 24:
        sense.set_pixels(twentyfour)
    elif temp == 25:
        sense.set_pixels(twentyfive)
    elif temp == 26:
        sense.set_pixels(twentysix)
    elif temp == 27:
        sense.set_pixels(twentyseven)
    elif temp == 28:
        sense.set_pixels(twentyeight)
    elif temp == 29:
        sense.set_pixels(twentynine)
    elif temp == 30:
        sense.set_pixels(thirty)
    elif temp == 31:
        sense.set_pixels(thirtyone)
    elif temp == 32:
        sense.set_pixels(thirtytwo)
    elif temp == 33:
        sense.set_pixels(thirtythree)
    elif temp == 34:
        sense.set_pixels(thirtyfour)
    elif temp == 35:
        sense.set_pixels(thirtyfive)
    elif temp == 36:
        sense.set_pixels(thirtysix)
    elif temp == 37:
        sense.set_pixels(thirtyseven)
    elif temp == 38:
        sense.set_pixels(thirtyeight)
    elif temp == 39:
        sense.set_pixels(thirtynine)
    elif temp == 40:
        sense.set_pixels(forty)
    elif temp == 41:
        sense.set_pixels(fortyone)
    elif temp == 42:
        sense.set_pixels(fortytwo)
    elif temp == 43:
        sense.set_pixels(fortythree)
    elif temp == 44:
        sense.set_pixels(fortyfour)
    elif temp == 45:
        sense.set_pixels(fortyfive)
    elif temp == 46:
        sense.set_pixels(fortysix)
    elif temp == 47:
        sense.set_pixels(fortyseven)
    elif temp == 48:
        sense.set_pixels(fortyeight)
    elif temp == 49:
        sense.set_pixels(fortynine)
    elif temp >= 50:
        sense.set_pixels(toocoldorhot)

    print("Displaying temp {0} on Sense Hat screen".format(temp))