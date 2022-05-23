from time import sleep
from itertools import cycle


class TrafficLight:
    #    __color = [[' RED ', 'YELLOW', 'GREEN'], [7, 2, 4],
    __color = ["   ", [1, 1, 1], ["\033[41m\033[1m", "\033[43m\033[1m", "\033[42m\033[1m"]]

    def running(self):
        col_lst = ["", ""]
        for n in cycle((0, 1, 2)):
            col_lst[1] = self.__color[2][n]
            print(f"\r({col_lst[int(n == 0)]}{self.__color[0]}\033[0m)"
                  f"({col_lst[int(n == 1)]}{self.__color[0]}\033[0m)"
                  f"({col_lst[int(n == 2)]}{self.__color[0]}\033[0m)", end='')
            sleep(self.__color[1][n])


tr_light = TrafficLight()
tr_light.running()