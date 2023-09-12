from driver import Driver
from grand_prix import GrandPrix
from time_grand import Time

class Championship:
    drivers_list = []
    grand_prix_list = []
    time_list = []

    def set_time(self, GP:GrandPrix, Driver:Driver, hours, minutes, seconds, ms):
        time = Time(GP, Driver, hours, minutes, seconds, ms)
        self.time_list.append(time)
        GP.add_time(time)
        Driver.add_time(time)
        return time

    def get_grand_prix(self, name):
        grand_prix:GrandPrix
        for grand_prix in self.grand_prix_list:
            if grand_prix.get_name() == name:
                return grand_prix
        return None

    def difine_grand_prix(self, name):
        GP:GrandPrix= GrandPrix(name)
        self.grand_prix_list.append(GP)
        return GP


    def creat_driver(self, name):
        driver = Driver(name)
        self.drivers_list.append(driver)
        return driver

    def get_drivers(self):
        return self.drivers_list

    def get_driver(self, name):
        driver:Driver
        for driver in self.drivers_list:
            if driver.get_name() == name:
                return driver
        return "Sorry I can not find him!!.."
            
    def get_championship_ranking(self):
        driver_point_dict = {}
        driver:Driver
        for driver in self.drivers_list:
            driver_point_dict[driver.get_name()] = driver.get_points()
        drivers = sorted(driver_point_dict.items(), key=lambda x:x[1], reverse=True)
        return dict(drivers)