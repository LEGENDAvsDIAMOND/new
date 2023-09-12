# from time_grand import Time
class Driver:

    point = [0, 25, 18, 15, 12, 10, 8, 6, 4, 2, 1]

    def __init__(self, name):
        self.time_list = []
        self._name = name

    def get_name(self):
        return self._name

    def add_time(self, time):
        self.time_list.append(time)

    def __eq__(self, _o):
        d:Driver = _o
        return self._name == d._name
    
    def get_raced(self):
        # gp:Time
        list_gp = []
        for gp in self.time_list:
           list_gp.append(gp.get_grand_prix().get_name())
        return list_gp
    
    def get_points(self):
        res = 0
        # time:Time
        for time in self.time_list:
            ord = time.get_grand_prix().get_position(time.get_driver())
            res += self.point[ord]
        return res


