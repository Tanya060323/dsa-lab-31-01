# Ввод трёх чисел с клавиатуры
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

# Поиск минимального числа
minimum = a

if b < minimum:
    minimum = b

if c < minimum:
    minimum = c

print("Минимальное число:", minimum)

