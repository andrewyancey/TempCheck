#!/usr/bin/python3
from matplotlib import pyplot as plt
import urllib.request as web
import xml.etree.ElementTree as ElementTree
import time
import pandas as pd
import DirectoryTools
import WeatherData
from datetime import datetime

source = "https://w1.weather.gov/xml/current_obs/KLEX.xml"
savepath = "Data/mycsv.csv"
interval = 120
wxdata = WeatherData.WeatherDataStruct()
df = pd.DataFrame()

# download the weather data xml from the web
def download_source(src):
    try:
        data = web.urlopen(src)
    except:
        print('something went wrong while attempting to load the web data')
        data = None
    return data

# parse the xml data and return an object with the data
def parse_xml(data):
    xmldata = ElementTree.parse(data)
    temp = xmldata.find("temp_f").text
    dew = xmldata.find("dewpoint_f").text
    pressure = xmldata.find("pressure_mb").text
    datatime = xmldata.find("observation_time_rfc822").text
    wxdatapoint = WeatherData.WeatherDataPoint(temp, dew, pressure, datatime)
    return wxdatapoint

# save the data to the csv
def save_data(data):
    wxdatapoint = parse_xml(data)
    wxdatapoint.show()
    # append the data to the lists to be used for the csv
    wxdata.appendWeatherData(wxdatapoint)
    # Ensure the directory exists
    DirectoryTools.EnsureDirectory(savepath)
    # write the csv
    df = pd.DataFrame.from_dict(wxdata.to_dict())
    df.to_csv(savepath, index=False)

# main loop
while True:
    # download and store the weather data
    data = download_source(source)
    #if there was an issue downloading the data
    if data != None: save_data(data)
    # wait for the next time to update
    time.sleep(interval)
    
