numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# находим индекс None для того, чтобы написать список чисел без None
index = numbers.index(None)

# список чисел без None(пропуск)
numbers_list_no_none = numbers[0:index] + numbers[index + 1:]

# среднее арифметическое
average = sum(numbers_list_no_none) / len(numbers)

# заменяем неизвестное число None
numbers[index] = average

# TODO заменить значение пропущенного элемента средним арифметическим
print("Измененный список:", numbers)
