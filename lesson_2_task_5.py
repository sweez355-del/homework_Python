n = int(input("Введите номер месяца: "))


def month_to_season(n):
    z = "Зима"
    s = "Лето"
    o = "Осень"
    v = "Весна"

    if n == 1 or n == 2 or n == 12:
        print(z)
    elif n == 3 or n == 4 or n == 5:
        print(v)
    elif n == 6 or n == 7 or n == 8:
        print(s)
    elif n == 9 or n == 10 or n == 11:
        print(o)
    else:
        print("Ошибка: введите число от 1 до 12")


month_to_season(n)
