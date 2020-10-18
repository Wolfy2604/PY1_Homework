import itertools, time


class TrafficLight:
    colors = ['red', 'yellow', 'green', 'yellow']

    def __init__(self):
        self.__running()

    def __running(self):
        check_time = [7, 2, 5, 2]
        for t, color in itertools.cycle(zip(check_time, self.colors)):
            print(color)
            time.sleep(t)


traffic_light = TrafficLight()
