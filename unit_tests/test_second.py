import random
import pytest

import unit_tests.hw_5 as hw


@pytest.fixture
def get_list():
    # функция возвращает список из 10ти случайных чисел в диапазоне от 30 до 90
    return [random.randint(30, 90) for iter in range(10)]


# тест должен быть выполнен третим по очередности
# должен получать сгенрированный список из фикстуры
# должен проверить с помощью оператора assert действительно ли самое большое число, полученное
# из функции find_largest_number модуля hw_5, находится в диапозоне от 30 до 90
@pytest.mark.run(order=3)
def test_largest_between_thirty_and_ninty(get_list):
    largest_number = hw.find_largest_number(get_list)
    assert 30 <= largest_number <= 90, f"Число {largest_number} не в диапазоне от 30 до 90"


# тест должен быть выполнен четвертым по очередности
# должен получать сгенрированный список из фикстуры
# должен проверить с помощью оператора assert действительно ли самое большое число, полученное
# из функции find_largest_number модуля hw_5, состоит из двух цифр
@pytest.mark.run(order=4)
def test_largest_consists_of_two_digits(get_list):
    largest_number = hw.find_largest_number(get_list)
    assert 30 <= largest_number < 100, f"Число {largest_number} не является двухзначным"


# тест должен быть выполнен вторым по очередности
# должен получать сгенрированный список из фикстуры
# должен проверить с помощью оператора assert действительно ли самое большое число, полученное
# из функции find_largest_number модуля hw_5, является целым числом
# подсказка функция type() или isinstance()
@pytest.mark.run(order=2)
def test_largest_is_integer(get_list):
    largest_number = hw.find_largest_number(get_list)
    assert isinstance(largest_number, int), f"Число {largest_number} не является целым числом"


# тест должен быть выполнен первым по очередности
# должен проверить с помощью оператора assert действительно ли самое большое число полученное
# из функции find_largest_number модуля hw_5,
# которому необходимо в качестве аргумента передать пустой список [],
# не является целым числом
@pytest.mark.run(order=1)
def test_largest_is_not_integer_with_empty_list():
    largest_number = hw.find_largest_number([])
    assert not isinstance(largest_number, int), f"Число {largest_number} является целым числом"
