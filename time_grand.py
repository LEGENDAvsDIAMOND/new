from driver import Driver
from grand_prix import GrandPrix

class Time:

    def __init__(self, GP:GrandPrix, Driver:Driver, hours, minutes, seconds, ms):
        self._GP = GP
        self._Driver = Driver
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
        self._ms = ms

    def to_string(self):
        return f"{self._hours}:{self._minutes}:{self._seconds}.{self._ms}"

    def get_time(self):
        return self._ms + self._seconds * 1000 + self._minutes * 60000 + self._hours * 3600000
    
    def get_driver(self):
        return self._Driver

    def get_grand_prix(self):
        return self._GP


