import sys

# Считывание массива из аргументов командной строки
numbers = []

for arg in sys.argv[1:]:
    numbers.append(int(arg))

# Сумма элементов с четными номерами
sum_even_index = 0

# Произведение элементов с нечетными номерами
product_odd_index = 1

for i in range(len(numbers)):

    if i % 2 == 0:
        sum_even_index = sum_even_index + numbers[i]
    else:
        product_odd_index = product_odd_index * numbers[i]

print("Сумма элементов с четными номерами:", sum_even_index)
print("Произведение элементов с нечетными номерами:", product_odd_index)

# Поиск min и max
min_index = 0
max_index = 0

for i in range(len(numbers)):
    if numbers[i] < numbers[min_index]:
        min_index = i
    if numbers[i] > numbers[max_index]:
        max_index = i

# Меняем местами
numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

print("Массив после замены min и max:")
print(numbers)


