# функция проверяет является ли входящий параметр положительным числом
def is_positive(number):
    if number > 0:
        return True
    else:
        return False

# функция находит из списка самое большое число и возвращает его как результат,
# если переданный список пуст функция возвращает значение None
def find_largest_number(numbers_list: list):
    max = None
    if len(numbers_list) > 0:
        max = numbers_list[0]
        for x in numbers_list:
            if x > max:
                max = x
    return max
