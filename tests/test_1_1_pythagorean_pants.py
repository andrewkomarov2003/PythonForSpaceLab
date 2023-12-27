# Тест для завдання №1_1 "Піфагорові штани"

from task1_1_Pythagorean_pants import pythagorean_pants
import pytest


@pytest.mark.parametrize("a, b, c, expected_result", [(5, 3, 4, True),
                                                      (6, 8, 10, True),
                                                      (100, 3, 65, False)
                                                      ])
def test_pythagorean_pants(a, b, c, expected_result):
    assert pythagorean_pants(a, b, c) == expected_result



