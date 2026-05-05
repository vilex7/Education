import collections

pets = {
    1:
        {
            "Мухтар": {
                "Вид питомца": "Собака",
                "Возраст питомца": 9,
                "Имя владельца": "Павел"
            },
        },
    2:
        {
            "Каа": {
                "Вид питомца": "желторотый питон",
                "Возраст питомца": 19,
                "Имя владельца": "Саша"
            },
        },
}

def create(name: str, type: str, age: int, owner_name: str, pets: dict = pets):
    last = collections.deque(pets, maxlen=1)[0]

    pets.update({last + 1:
                 {name: {"Вид питомца": type,
                         "Возраст питомца": age,
                         "Имя владельца": owner_name
                         }}})

def read(ID: int, pets: dict = pets):
    if ID in pets.keys():
        name, data = list(pets[ID].items())[0]
        type, age, owner_name = data.values()
        return f'Это {type} по кличке {name}. Возраст питомца: {age} {get_suffix(age)}. Имя владельца: {owner_name}'
    else:
        return False

def update(ID: int, name: str, type: str, age: int, owner_name: str, pets: dict = pets):
    for key in pets.keys():
        if key == ID:
            pets[ID] = {name:
                        {"Вид питомца": type, 
                         "Возраст питомца": age, 
                         "Имя владельца": owner_name
                         }}

def delete(ID, pets: dict = pets):
    if ID in pets.keys():
        del pets[ID]
    else:
        return None


def get_suffix(age):
    if 11 <= age % 100 <= 14:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif 2 <= age % 10 <= 4:
        return "года"
    else:
        return "лет"
    
print(get_suffix(12))
        

# pets = {}
# name = input("Для выхода напишите слово stop.\nДля продолжения введите имя питомца: ")

# while name != "stop":
#     pets[name] = {'вид питомца': '', 'возраст': 0, 'имя владельца': ''}
#     pet = pets[name]

#     for key in pets[name]:
#         pet[key] = input(f'Введите {key}: ')
#         while key == 'возраст' and not pet[key].isdigit():
#             pet[key] = input(f"Введено некорректное значение. Введите возраст (целое число): ")
            
#     name = input('Для выхода напишите слово stop.\nДля продолжения введите имя питомца: ')

# # Получаем списки имён и данных внешнего словаря
# pet_names = list(pets.keys())
# pet_data_list = list(pets.values())

# for i in range(len(pet_names)):
#     name = pet_names[i]
#     data = pet_data_list[i]

#     # Получаем ключи и значения внутреннего словаря
#     data_keys = list(data.keys())
#     data_values = list(data.values())

#     # Извлекаем значения (порядок известен)
#     type, age, owner = data_values
#     age = int(age)

#     print(f"Это {type} по кличке \"{name}\". Возраст питомца: {age} {years_word}. Имя владельца: {owner}.")