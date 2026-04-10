s = input("Введите строку: ")

# Определяем границу первой половины строки
half = len(s) // 2

result = ""
count = 0
i = 0

# Проходим по всем символам строки
while i < len(s):

    if i < half and s[i] == "!":

        result += "%"
        count += 1

    else:
        result += s[i]

    i += 1

print("Новая строка:", result)
print("Количество замен:", count)