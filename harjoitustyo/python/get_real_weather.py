import requests, json

apikey_real = "83e000dd31b3c05107e22e406b89a395"
url = "http://api.openweathermap.org/data/2.5/weather?appid=83e000dd31b3c05107e22e406b89a395&q=Vantaa"

def get_real_temp():
    resp = requests.get(url)
    x = resp.json()

    if x["cod"] == 401:
        errormsg = x["message"]
        current_temperature = 0
        print(errormsg)
    elif x["cod"] == "404":
        errormsg = x["message"]
        current_temperature = 0
        print(errormsg)
    elif x["cod"] == 429:
        current_temperature = 0
        print(x)
    else:
        # store the value of "main" 
        # key in variable y 
        y = x["main"] 
    
        # store the value corresponding 
        # to the "temp" key of y
        # and convert Kelvin to Celsius
        # and round to 2 decimals
        current_temperature = round(y["temp"] - 273.15,2)
    
        # store the value corresponding 
        # to the "pressure" key of y 
        # current_pressure = y["pressure"] 
    
        # store the value corresponding 
        # to the "humidity" key of y 
        # current_humidiy = y["humidity"] 
    
        # store the value of "weather" 
        # key in variable z 
        # z = x["weather"] 
    
        # store the value corresponding  
        # to the "description" key at  
        # the 0th index of z 
        # weather_description = z[0]["description"] 
    
        # print following values 
        # print(" Temperature = " +
        #                 str(current_temperature) + "C" +
        #     "\n Atmospheric pressure = " +
        #                 str(current_pressure) + "hPa" +
        #     "\n Humidity = " +
        #                 str(current_humidiy) + "%" +
        #     "\n Description = " +
        #                 str(weather_description))

        return current_temperature