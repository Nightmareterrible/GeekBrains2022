class Stationery:
    title = ""

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def draw(self):
        print("Рисуем ручкой")


class Pencil(Stationery):

    def draw(self):
        print("Рисуем карандашом")


class Handle(Stationery):

    def draw(self):
        print("Рисуем маркером")


pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

han = Handle()
han.draw()
