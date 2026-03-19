import math

side = input("Введите сторону квадрата: ")
side = float(side)


def square(side):
    return math.ceil(side*side)


print(square(side))
