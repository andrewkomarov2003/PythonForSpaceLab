# Тест для завдання №1_2 "рослини проти зомбі"

from task1_2_Plants_vs_Zombies import plants_vs_zombies
import pytest


@pytest.mark.parametrize("zombies, plants, expected_result", [([1, 3, 5, 7], [2, 4, 6, 8], True),
                                                              ([1, 3, 5, 7], [2, 4], False),
                                                              ([1, 3, 5, 7], [2, 4, 0, 8], True),
                                                              ([2, 1, 1, 1], [1, 2, 1, 1], True)
                                                              ])
def test_plants_vs_zombies(zombies, plants, expected_result):
    assert plants_vs_zombies(zombies, plants) == expected_result



