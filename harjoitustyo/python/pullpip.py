from bs4 import BeautifulSoup
import time
import requests
import os.path


def getPubIP():

    url = "http://checkip.dyndns.org/"

    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content)

    data = str(soup)

    data = data.replace("<html><head><title>Current IP Check</title></head><body>Current IP Address: ", "")
    data = data.replace("</body></html>", "")

    if os.path.isfile("~/pubip/pubip.txt"):
        f = open("pubip.txt", "a")
        f.write(data)
        f.close
    else:
        f = open("pubip.txt", "w")
        f.write(data)
        f.close

    return data

while(True):
    getPubIP()
    print("IP Refreshed!")
    time.sleep(3600)