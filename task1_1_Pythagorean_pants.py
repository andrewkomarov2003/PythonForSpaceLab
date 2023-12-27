# Завдання 1_1 "Піфагорові штани"

from math import sqrt


def pythagorean_pants(side_1, side_2, side_3):
    a = side_1
    b = side_2
    c = side_3

    try:
        side = [float(a), float(b), float(c)]
        side.sort()

        if side[0]**2 + side[1]**2 == side[2]**2:
            print("Трикутник з такими сторонами є Піфагорівським.")
            return True
        else:
            print("Трикутник з такими сторонами не є Піфагорівським.")
            return False
    except ValueError:
        print("Функція має приймати числові значення!")



