#!/usr/bin/python3
from matplotlib import pyplot as plt
import urllib.request as web
import xml.etree.ElementTree as ElementTree
import time
import pandas as pd
from datetime import datetime

source = "https://w1.weather.gov/xml/current_obs/KLEX.xml"
savepath = "Data/mycsv.csv"
interval = 30

times = []
temps = []
dews = []
df = pd.DataFrame()

# download the weather data xml from the web
def download_source(src):
    data = web.urlopen(src)
    return data

# parse the xml data and return an object with the data
def parse_xml(data):
    xmldata = ElementTree.parse(data)
    temp = xmldata.find("temp_f").text
    dew = xmldata.find("dewpoint_f").text
    wxdata = weatherdata(temp, dew)
    return wxdata

# the weatherdata class stores the data for use
class weatherdata:
    temp = 0
    dew = 0
    time = 0

    def __init__(self, temp, dew):
        self.temp = temp
        self.dew = dew
        self.time = datetime.now().strftime('%m-%d-%y %H:%M')

    def show(self):
        print("the temperature is: " + self.temp)
        print("the dew point is: " + self.dew)
        print("the time is:" + self.time)

# main loop
while True:
    
    # download and store the weather data
    data = download_source(source)
    wxdata = parse_xml(data)
    wxdata.show()
    # append the data to the lists to be used for the csv
    temps.append(wxdata.temp)
    dews.append(wxdata.dew)
    times.append(wxdata.time)
    # build the dictionary for the csv
    data = {
        'times': times,
        'temps': temps,
        'dews': dews
    }
    # write the csv
    df = df.from_dict(data)
    df.to_csv(savepath, index=False)
    # wait for the next time to update
    time.sleep(interval)
    
