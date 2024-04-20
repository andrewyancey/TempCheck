from datetime import datetime

# the weatherdata class stores the data for use
class WeatherDataStruct:
    temps = []
    dews = []
    times = []

    def appendWeatherData(self, data):
        self.temps = data.temp
        self.dews = data.dew
        self.times.append(datetime.now().strftime('%m-%d-%y %H:%M'))

    def appendTemp(self, temp):
        self.temps.append(temp)
    
    def appendDew(self, dew):
        self.dews.append(dew)
        
    def appendNowTime(self):
        self.times.append(datetime.now().strftime('%m-%d-%y %H:%M'))

    def to_dict(self):
        return {
        'times': self.times,
        'temps': self.temps,
        'dews': self.dews
        }

# the weatherdata class stores the data for use
class WeatherDataPoint:
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