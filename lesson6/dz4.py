import time
from random import randint


class Car:
    __speed = 0.0
    color = ""
    name = ""
    __is_police = False
    __turns = 0
    __orientations = list("NEWS")
    __orientation = __orientations[0]

    def go(self):
        """
        Запускает машину, проверяет количество оборотов холостого хода, и сообщает завелась ли машина
        :return: None
        """

        print(f"Запускаем автомобиль {self.name}")
        self.__turns = randint(500, 1500)
        for _ in range(3):
            print("-" * 30, end="")
            time.sleep(1)
        print()
        if self.__turns < 700:
            __turns = 0
            print("Двигатель заглох. Необходимо обратиться в сервисный центр, возможно неисправлен двигатель.")
        elif self.__turns > 1200:
            print("Двигатель запущен на повышенных оборотах. Рекомендуется обратиться в сервисный центр.")
        else:
            print("Автомобиль готов к движению. Будьте внимательны на дороге. Приятной поездки.")

    def __init__(self, n, c):
        self.name = n
        self.color = c
        self.is_police = False

    def stop(self):
        """
        Глушит зажигание
        :return: None
        """
        self.__turns = 0
        self.__speed = 0
        print("Приехали. Не забудьте поставить автомобиль на ручной тормоз.")
        print("-"*90)
        print()

    def turn(self, direction: int):
        """
        Совершает поворот. Сообщает о повороте
        :param direction: указывает направление поворота : -1, 0, 1 (лево, прямо, право)
        :return:
        """
        if self.__turns == 0:
            print("Для продолжения движения запустите двигатель !")
            return
        if direction == -1:
            print("Вы повернули налево. ", end="")
        elif direction == 1:
            print("Вы повернули направо. ", end="")
        else:
            print("Едем прямо. ", end="")
        index = (self.__orientations.index(self.__orientation) + direction) % 4
        self.__orientation = self.__orientations[index]
        print(f"Ваше направление : {self.__orientation}")

    def show_speed(self, do_print=True) -> int:
        """
        Отображает текущую скорость автомобиля
        :return int: Возвращает целое число : скорость автомобиля
        """
        if do_print:
            print(f"Текущая скорость : {self.__speed}")
        return self.__speed

    def pedal_to_the_metal(self):
        """
        "Педаль в пол !", "Добавь газку", "Запахло палёной резиной" - навеяно Гелионом из StarCraft2
        Увеличиваем подачу топлива, едем быстрее
        :return: None
        """
        if self.__turns == 0:
            print("Для продолжения движения запустите двигатель !")
            return
        self.__speed = min(240, self.__speed + randint(10, 50))

    def slow_down(self):
        """
        Тормозим. Автомобиль не может остановиться мгновенно, поэтому педаль тормоза придётся жать неоднократно
        :return: None
        """
        self.__speed = max(0, self.__speed - randint(10, 50))


class TownCar(Car):

    def show_speed(self, do_print=True) -> int:
        if super().show_speed(False) > 60:
            print("ВНИМАНИЕ! Вы превышаете допустимую скорость")
        return super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self, do_print=True) -> int:
        if super().show_speed(False) > 40:
            print("ВНИМАНИЕ! Вы превышаете допустимую скорость")
        return super().show_speed()
    pass


class PoliceCar(Car):

    def __init__(self, n, c):
        super().__init__(n, c)
        self.is_police = True


my_car = WorkCar("VW Golf 2", "pink")
my_car.go()
r = randint(2, 10)
print(f"До работы необходимо проехать {r} перекрёстков")
for i in range(r):
    my_car.pedal_to_the_metal()
    my_car.turn(randint(-1, 1))
    my_car.slow_down()
    my_car.show_speed()
    time.sleep(1)
my_car.stop()
time.sleep(2)

neighbor_car = TownCar("Geely M-Grant Pro", "white")
neighbor_car.go()
r = randint(2, 10)
print(f"До магазина необходимо проехать {r} перекрёстков")
for i in range(r):
    neighbor_car.pedal_to_the_metal()
    neighbor_car.turn(randint(-1, 1))
    neighbor_car.slow_down()
    if i % 3 == 0:
        neighbor_car.show_speed()
    time.sleep(1)
neighbor_car.stop()
