from matplotlib import pyplot as plt
import urllib.request as web
import xml.etree.ElementTree as ElementTree
import time
from datetime import datetime

source = "https://w1.weather.gov/xml/current_obs/KLEX.xml"

times = []
temps = []
dews = []

def download_source(src):
    data = web.urlopen(src)
    return data

def parse_xml(data):
    xmldata = ElementTree.parse(data)
    temp = xmldata.find("temp_f").text
    dew = xmldata.find("dewpoint_f").text
    wxdata = weatherdata(temp, dew)
    return wxdata

class weatherdata:
    temp = 0
    dew = 0

    def __init__(self, temp, dew):
        self.temp = temp
        self.dew = dew

    def show(self):
        print("the temperature is: " + self.temp)
        print("the dew point is: " + self.dew)

while True:
    data = download_source(source)
    wxdata = parse_xml(data)
    wxdata.show()
    current_time = datetime.now().time()
    formatted_time = current_time.strftime('%H:%M:%S')
    # print(formatted_time)
    temps.append(wxdata.temp)
    dews.append(wxdata.dew)
    times.append(formatted_time)
    plt.clf()
    plt.plot(times, temps, marker='.')
    plt.plot(times, dews, marker='.')
    plt.gca().invert_yaxis()
    plt.pause(120)
    
