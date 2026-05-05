country = {4: 3} # 4 - ключ, 3 - значение. Можно использовать как строки, так и булевые значения. Также в качестве ключа можно использовать корежи, а вот списки нельзя кстати
print(country[4])


cantri = {'code': 'RU,', 'name': 'Russia', 'population': 144} 
print(cantri['name'])


# Создание словаря через dict() и перебор словарей
cuntri = dict(code='Ru', name='Russia') # При таком способе в качестве ключа могут использоваться только строки
for key in cuntri: # При переборе циклом for при создании только одной переменной будем получать только ключи
    print(key) 
for key, value in cuntri.items(): # Метод .items выводит список, где каждый элемент является кортежем (ключ и значение) 
    print(key, " - ", value)


# Методы словарей
print(cuntri.get('name')) # Выводи значение по ключу. Работает так же как и print(cuntri['name'])
# cuntri.clear() полностью очищает словарь
# cuntri.pop('code') в этом случае в параметре указывается ключ. Удаляет из словаря ключ и его значение
# cuntri.popitem() удаляет последний ключ словаря и его значение
print(cuntri.keys()) # Выводит список, где в качестве элементов - ключи
print(cuntri.values()) # Выводит список, где в качестве элементов - значения
print(cuntri.items()) # Выводит список, где каждый элемент является кортежем (ключ и значение)
cuntri['code'] = 'None' # Меняет значение для определённого ключа. Можно также использовать метод .update()


# Нихуёвый словарик для задачи
person = {
    'user_1': {
        'first_name': 'Jhon',
        'Last name': 'Marley',
        'age': 45,
        'address': ['г. Москва', 'ул.Карла Маркса', '45'], # Можно и кортеж указать
        'grades': {'math': 5, 'physics': 3}
    },
    'user_2': {

    }
}

print(person['user_1']['address'][1])


# Ещё одна задачка
bank = dict()
n = int(input())

for i in range(n):
    req = input() # Вводим тип запроса
    if req == 'create': # Если запрос 'create' - вводим ключ, с которым мы хотим открыть ячейку
        k = input()
        bank[k] = 0
    elif req == 'add': # Если запрос 'add' - вводим значение и присваиваем его ключу
        k = input()
        amount = int(input())
        if k in bank.keys():
            bank[k] += amount
        else:
            print("sorry, no such key")
    else:
        print("bad request")
print(bank)