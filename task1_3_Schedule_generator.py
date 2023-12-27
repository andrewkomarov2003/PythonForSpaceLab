# Завдання 1_3 "Генератор розкладу"

import datetime


def schedule_generator(days, work_days, rest_days, start_date):
    schedule = [start_date]

    try:
        if days <= 0 or work_days <= 0 or rest_days <= 0:
            raise ValueError

        counter_work = 1
        counter_rest = 0
        curr_date = start_date

        for i in range(1, days):
            if counter_work < work_days or counter_rest == rest_days:
                if counter_rest == rest_days:
                    counter_work = 0
                    counter_rest = 0

                curr_date += datetime.timedelta(days=1)
                schedule.append(curr_date)
                counter_work += 1
            else:
                curr_date += datetime.timedelta(days=1)
                counter_rest += 1

        print("З ", days, " днів ви працюєте ", len(schedule), " днів, а відпочиваєте ", days - len(schedule), " днів.")
        return schedule
    except ValueError:
        print("Перевірте правильність вводу даних!")
    except TypeError:
        print("Перевірте правильність вводу даних!")




