first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка для первого примера:
#first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))

# Генераторная сборка для второго примера:
#second_result = (len(first[i]) != len(second[i]) for i in range(len(first)))

# Верная сборка:
first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))


print(list(first_result))   
print(list(second_result))


# Ошибка, была во второй конструкции где вместо
# == указано !=, что выдает [True, True, False] вместо [False, False, True]