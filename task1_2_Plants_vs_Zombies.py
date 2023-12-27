# Завдання 1_2 "Рослини проти Зомбі"

def plants_vs_zombies(z, p):
    zombies = z
    plants = p

    try:
        initial_force_of_plants = 0
        initial_force_of_zombies = 0

        for i in range(0, len(plants)):
            initial_force_of_plants += plants[i]

        for i in range(0, len(zombies)):
            initial_force_of_zombies += zombies[i]

        if len(plants) > len(zombies):
            for i in range(len(plants) - 1, len(zombies) - 1, -1):
                zombies.append(0)
        elif len(plants) < len(zombies):
            for i in range(len(zombies) - 1, len(plants) - 1, -1):
                plants.append(0)

        for i in range(0, len(plants)):
            if plants[i] > zombies[i]:
                print("Успішна атака Рослин!")
                plants[i] = 1
                zombies[i] = 0
            elif plants[i] < zombies[i]:
                print("Успішна атака Зомбі!")
                plants[i] = 0
                zombies[i] = 1
            else:
                print("Атака безуспішна з обох сторін!")
                plants[i] = 0
                zombies[i] = 0

        if plants.count(1) > zombies.count(1):
            print("Рослини перемогли!")
            return True
        elif plants.count(1) < zombies.count(1):
            print("Зомбі перемогли!")
            return False
        else:
            if initial_force_of_plants > initial_force_of_zombies:
                print("Рослини перемогли!")
                return True
            elif initial_force_of_plants < initial_force_of_zombies:
                print("Зомбі перемогли!")
                return False
            else:
                print("Нічия!")
                return True
    except ValueError:
        print("Рослини та зомбі мають бути числами!")
    except TypeError:
        print("Рослини та зомбі мають бути числами!")


