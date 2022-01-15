# 1) Создать переменную типа String

varString = 'type string'

# 2) Создать переменную типа Integer

varInteger = 343

# 3) Создать переменную типа Float

varFloat = 23.1

# 4) Создать переменную типа Bytes

varBytes = bytes(varInteger)


# 5) Создать переменную типа List

varList = [1, 2, 3, 4]


# 6) Создать переменную типа Tuple

varTuple = ('first', 'second', 'third',)

# 7) Создать переменную типа Set

varSet = {1, 2, 3, 4, 5, 6}

# 8) Создать переменную типа Frozen set

varFrozenSet = frozenset(varSet)

# 9) Создать переменную типа Dict

varDict = {1: 'One', 2: 'two', 3: 'Third'}

# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.

print(varString, type(varString))
print(varInteger, type(varInteger))
print(varFloat, type(varFloat))
print(varBytes, type(varBytes))
print(varList, type(varList))
print(varTuple, type(varTuple))
print(varSet, type(varSet))
print(varFrozenSet, type(varFrozenSet))
print(varDict, type(varDict))

# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.

# 1 способ

s_1 = 'Hello '
s_2 = 'World!'
s_3 = s_1 + s_2

print(s_3)

# 2 способ

s_1 = 'Hello'
s_2 = 'World!'

print(s_1, s_2)

# 3 способ

s_1 = 'Hello '
s_2 = 'World!'

print(''.join([s_1, s_2]))

# 4 способ

s_1 = 'Hello'
s_2 = 'World!'
s_3 = '%s %s' % (s_1, s_2)

print(s_3)

# 5 способ

s_1 = 'Hello'
s_2 = 'World!'
s_3 = f'{s_1} {s_2}'

print(s_3)

# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)

q_1 = 'I was born in'
q_2 = 1996

print(q_1, q_2)

# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)

q_1 = 'I was born in '
q_2 = 1996

print(q_1 + str(q_2))