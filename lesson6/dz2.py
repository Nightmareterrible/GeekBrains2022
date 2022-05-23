class Road:
    __length = 0
    __width = 0

    def __init__(self, lens, wid):
        self.__length = lens
        self.__width = wid

    def get_mass(self, one_kv, thin):
        return self.__length * self.__width * one_kv * thin / 1000


r = Road(10, 1000)
print(f"итоговая масса асфальта {r.get_mass(25, 5):.0f} т")
