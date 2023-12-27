# Тест для завдання №1_3 "Генератор розкладу"

from task1_3_Schedule_generator import schedule_generator
import pytest
import datetime


@pytest.mark.parametrize("days, work_days, rest_days, start_date, expected_date", [(5, 2, 1,
                                                                                    datetime.datetime(2020, 1, 30),
                                                                                    [datetime.datetime(2020, 1, 30),
                                                                                     datetime.datetime(2020, 1, 31),
                                                                                     datetime.datetime(2020, 2, 2),
                                                                                     datetime.datetime(2020, 2, 3)]),
                                                                                   (7, 2, 2,
                                                                                    datetime.datetime(2023, 12, 25),
                                                                                    [datetime.datetime(2023, 12, 25),
                                                                                     datetime.datetime(2023, 12, 26),
                                                                                     datetime.datetime(2023, 12, 29),
                                                                                     datetime.datetime(2023, 12, 30)])
                                                                                   ])
def test_schedule_generator(days, work_days, rest_days, start_date, expected_date):
    assert schedule_generator(days, work_days, rest_days, start_date) == expected_date




