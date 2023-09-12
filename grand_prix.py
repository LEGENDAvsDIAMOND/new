# from time_grand import Time
# from driver import Driver

class GrandPrix:
    
    def __init__(self, name):
        self.time_list = []
        self._name = name

    # def get_position(self, driver:Driver):
    #     time: Time
    #     time_list = sorted(self.time_list)
    #     count = 0
    #     for time in time_list:
    #         if time.get_driver():
    #             count == 1 
    #         else:
    #             count += 1
    #     return count

    def get_name(self):
        return self._name

    def get_GP_rankin(self):
        # time: Time
        driver_time_dict = {}
        for time in self.time_list:
            driver_time_dict[time.get_driver().get_name()] = time.get_time()
        drivers = sorted(driver_time_dict.items(), key=lambda x:x[1])
        return dict(drivers)

    def get_position(self, driver):
        driver_time = self.get_GP_rankin()
        driver = driver.get_name()
        position = 0
        for driver_in, time in driver_time.items():
            position += 1
            if driver_in == driver:
                return position
        return None

    def add_time(self, time):
        self.time_list.append(time)