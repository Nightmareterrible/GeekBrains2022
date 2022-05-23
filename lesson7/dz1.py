import random


class Matrix:

    def __init__(self, new_matrix: list):
        self.__M = []
        if type(new_matrix) == list:
            self.__m = len(new_matrix)
        else:
            raise TypeError("Матрица задана неверно. Работа с ней невозможна")
        self.__n = len(new_matrix[0])
        for i in new_matrix:
            if type(i) != list or len(i) != self.__n:
                print("error")
                raise TypeError("Матрица задана неверно. Работа с ней невозможна")
            self.__M.append(i)
        print("Матрица создана успешно")

    def __str__(self):
        res = ""
        for i in self.__M:
            res = res + str(i) + "\n"
        return res

    @property
    def n(self):
        return self.__n

    @property
    def m(self):
        return self.__m

    @property
    def get_matrix(self):
        return self.__M

    def __add__(self, second_matrix):
        if self.n != second_matrix.n or self.m != second_matrix.m:
            raise TypeError("Размерности матриц не совпадают")
        a = self.get_matrix
        b = second_matrix.get_matrix
        return Matrix([[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))])


m = 5
n = 10
myMatrix1 = Matrix([[random.randint(1, 11) for j in range(n)] for i in range(m)])
myMatrix2 = Matrix([[random.randint(1, 11) for k in range(n)] for o in range(m)])
myMatrix3 = Matrix([[random.randint(1, 11) for x in range(n)] for y in range(m)])
print('Matrix1:')
print(myMatrix1)
print('Matrix2:')
print(myMatrix2)
print('Matrix3:')
print(myMatrix3)

print('Результат сложения:')
print(myMatrix1 + myMatrix2 + myMatrix3)
# по 2-м принтам "Матрица создана успешно" в консоли видно, что конструктор Matrix() будет вызываться 2 раза
