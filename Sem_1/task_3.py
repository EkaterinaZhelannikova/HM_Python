# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
# пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = int(input('Введите число: '))
temp = str(n)
n1 = temp + temp
n2 = temp + temp + temp
total = n + int(n1) + int(n2)
print(total)
