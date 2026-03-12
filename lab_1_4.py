# Считываем строку с числами
numbers = input("Введите целые числа через пробел: ")

# Добавляем пробел в конец строки,
numbers += " "

current_number = "" 
total_sum = 0       
count = 0            
i = 0             

# Проходим по всем символам строки
while i < len(numbers):

    if numbers[i] != " ":
        # Если символ не пробел, добавляем его к текущему числу
        current_number += numbers[i]

    else:
        # Если встретился пробел, то число закончилось
        total_sum += int(current_number)
        count += 1
        current_number = "" 

    i += 1  # переходим к следующему символу

print("Сумма:", total_sum)
print("Количество:", count)