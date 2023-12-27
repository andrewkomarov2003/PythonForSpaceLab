from task1_1_Pythagorean_pants import pythagorean_pants
from task1_2_Plants_vs_Zombies import plants_vs_zombies
from task1_3_Schedule_generator import schedule_generator
import datetime


print("Піфагорові штани:")
print(pythagorean_pants(3, 4, 5))

print("\n\n")

print("Рослини проти Зомбі:")
print(plants_vs_zombies([1, 3, 5, 7], [2, 4, 6, 8]))

print("\n\n")

print("Генератор розкладу:")
print(schedule_generator(5, 2, 1, datetime.datetime(2020, 1, 30)))


#Скрапер знаходиться в окремому файлі


