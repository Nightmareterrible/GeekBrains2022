# text = "xxxxx"
# print(f"\033[30m\033[43m {text} \033[0m")
# \033 — обозначение того, что дальше идет какой-то управляющий цветом код;
# [31m — цвет текста (красный);
# [43m — цвет фона (жёлтый).

# \033[0-7m — это различные эффекты, такие как подчеркивание, мигание, жирность и так далее;
# \033[30-37m — коды, определяющие цвет текста (черный, красный, зелёный, жёлтый, синий, фиолетовый, сине-голубой,серый)
# \033[40-47m — коды, определяющие цвет фона.
# 0	Сброс к начальным значениям

class Cell:

    def __init__(self, cells: int):
        self.__cells = min(8, max(1, cells))  # количество ячеек клетки
        if cells not in range(1, 9):
            print(f"Такую клетку создать нельзя. Создана клетка размером {self.cells}")

    def __str__(self):
        s = ""
        font = "30" if self.__cells > 1 else "31"
        back = 40 + self.__cells - 1
        for i in range(self.__cells):
            s = s + f"\033[{font}m\033[{back}m {self.__cells} \033[0m  "
        return s

    @property
    def cells(self):
        return self.__cells

    def __add__(self, other):
        if self.cells != other.cells:
            raise ArithmeticError("Клетка может взаимодействовать только с клеткой того же размера ! ")
        elif self.cells >= 8:
            raise ArithmeticError("Клетка не может стать больше")
        else:
            self.__cells += 1
        return Cell(self.cells)

    def __mul__(self, other):
        if self.cells != other.cells:
            raise ArithmeticError("Клетка может взаимодействовать только с клеткой того же размера ! ")
        elif self.cells >= 8:
            raise ArithmeticError("Клетка не может стать больше")
        else:
            self.__cells *= 2
            if self.cells > 8:
                self.__cells = 8
        return Cell(self.cells)

    def __sub__(self, other):
        if self.cells != other.cells:
            raise ArithmeticError("Клетка может взаимодействовать только с клеткой того же размера ! ")
        elif self.cells <= 1:
            raise ArithmeticError("Клетка не может стать меньше")
        else:
            self.__cells -= 1
        return Cell(self.cells)

    def __truediv__(self, other):
        if self.cells != other.cells:
            raise ArithmeticError("Клетка может взаимодействовать только с клеткой того же размера ! ")
        elif self.cells <= 1:
            raise ArithmeticError("Клетка не может стать меньше")
        else:
            self.__cells /= 2
        return Cell(self.cells)


c1 = Cell(3)
c2 = Cell(3)
c3 = Cell(4)

print(f"Клетка 1 : {c1}, Клетка 2 : {c2}, Клетка 3 : {c3}")

print(f"Объединение : {c1 + c2}")
print(f"Клетка 1 : {c1}, Клетка 2 : {c2}, Клетка 3 : {c3}")

print(f"Вычитание : {c1 - c3}")
print(f"Клетка 1 : {c1}, Клетка 2 : {c2}, Клетка 3 : {c3}")

print(f"Умножение : {c1 * c2}")
print(f"Клетка 1 : {c1}, Клетка 2 : {c2}, Клетка 3 : {c3}")

print(f"деление  : {c1 / c2}")  # А вот здесь будет ошибка, потому что клетки разного размера
print(f"Клетка 1 : {c1}, Клетка 2 : {c2}, Клетка 3 : {c3}")
