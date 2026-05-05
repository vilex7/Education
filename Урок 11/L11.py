def chet(a): # Объявление функции / назвние функции / параметр
    if a % 2 == 0: # Проверка числа: чётное/нечётное
        return True # После return функция завершается.
    a += 2
    print(a)
    # Return False / Не обязательно писать else, так как эта строчка выполнится только в случае, если не выполнится условие if

print(chet(4)) # Вызов функции. Функция не выполняется до тех пор, пока ее не вызвали
print(chet(5)) # В этом случае функция вернёт None


def tmp(name):
    print(f'Hello, {name}')

tmp('MARK') # Если написать print(tmp('MARK')) - вернётся None т.к. мы не возвращаем ничего из функции


# Проверка года: високосный/не високосный
def vis(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

y = int(input())
print(vis(y))


# Проверяем все элементы списка и возвращаяем только чётные
def nechet(n):
    return (n % 2 != 0)

def res(l):
    for el in l:
        if nechet(el):
            print(el)

tmpp = [1, 3, 4, 9, 2, 7]
res(tmpp)


# 
def new_year():
    print('Happy new year')

def birthday():
    name = input()
    print(f'Happy Birthday, {name}!')

def march8():
    print('Happy 8th of March')


n = int(input())
for i in range(n):
    cm = input()
    if cm == 'New Year':
        new_year()
    elif cm == 'birthday':
        name = input()
        birthday()
    elif cm == 'march8':
        march8()
    else:
        print('Wrong command')