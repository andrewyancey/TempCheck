from datetime import datetime

# the weatherdata class stores the data for use
class WeatherDataStruct:
    temps = []
    dews = []
    pressures = []
    datatimes = []
    times = []

    def appendWeatherData(self, data):
        self.temps.append(data.temp)
        self.dews.append(data.dew)
        self.pressures.append(data.pressure)
        self.datatimes.append(data.datatime)
        self.times.append(datetime.now().strftime('%m-%d-%y %H:%M'))

    def appendTemp(self, temp):
        self.temps.append(temp)
    
    def appendDew(self, dew):
        self.dews.append(dew)

    def appendpressure(self, pressure):
        self.pressures.append(pressure)
        
    def appendNowTime(self):
        self.times.append(datetime.now().strftime('%m-%d-%y %H:%M'))

    def to_dict(self):
        return {
        'times': self.times,
        'temps': self.temps,
        'dews': self.dews,
        'pressures': self.pressures,
        'datatimes': self.datatimes
        }

# the weatherdata class stores the data for use
class WeatherDataPoint:
    temp = 0
    dew = 0
    pressure = 0
    time = 0
    datatime = ""

    def __init__(self, temp, dew, pressure, datatime):
        self.temp = temp
        self.dew = dew
        self.pressure = pressure
        self.datatime = datatime
        self.time = datetime.now().strftime('%m-%d-%y %H:%M')

    def show(self):
        print("the temperature is: " + self.temp)
        print("the dew point is: " + self.dew)
        print("the pressure is: " + self.pressure)
        print("the data time is: " + self.datatime)
        print("the time is:" + self.time)