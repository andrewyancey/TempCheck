#!/usr/bin/python3
from matplotlib import pyplot as plt
import pandas as pd
import time
from datetime import datetime

source = "Data/mycsv.csv"
interval = 10

times = []
temps = []
dews = []

def filldata():
    global times
    global temps
    global dews

    data = pd.read_csv(source)
    times = pd.to_datetime(data['times'], format='%m-%d-%y %H:%M')
    temps = data['temps']
    dews = data['dews']

while True:
    plt.clf()
    filldata()
    plt.plot_date(times, temps, linestyle='solid')
    plt.plot_date(times, dews, linestyle='solid')
    plt.gcf().autofmt_xdate()
    plt.ylim(0, 100)
    plt.xlim(times[0], times[len(times)-1])
    plt.pause(60)
    
