class Worker:
    name = ""
    surname = ""
    position = ""
    __income = {"wage": 0, "bonus": 0}

    def __init__(self, wage, bonus):
        self.__income['wage'] = wage
        self.__income['bonus'] = bonus

    def get_wage(self):
        return self.__income['wage']

    def get_bonus(self):
        return self.__income['bonus']


class Position(Worker):

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self.get_bonus() + self.get_wage()


p1 = Position(100, 20)
p1.name = "Ваня"
p1.surname = "Иванов"
p1.position = "сыровар"
print(p1.get_full_name())
print(p1.get_total_income())
print()

p2 = Position(120, 30)
p2.name = "Петя"
p2.surname = "Петров"
p2.position = "медовар"
print(p2.get_full_name())
print(p2.get_total_income())
