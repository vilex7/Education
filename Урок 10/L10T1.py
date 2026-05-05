pets = {}
name = input("Для выхода напишите слово stop.\nДля продолжения введите имя питомца: ")

while name != "stop":
    pets[name] = {'вид питомца': '', 'возраст': 0, 'имя владельца': ''}
    pet = pets[name]

    for key in pets[name]:
        pet[key] = input(f'Введите {key}: ')
        while key == 'возраст' and not pet[key].isdigit():
            pet[key] = input(f"Введено некорректное значение. Введите возраст (целое число): ")
            
    name = input('Для выхода напишите слово stop.\nДля продолжения введите имя питомца: ')

# Получаем списки имён и данных внешнего словаря
pet_names = list(pets.keys())
pet_data_list = list(pets.values())

for i in range(len(pet_names)):
    name = pet_names[i]
    data = pet_data_list[i]

    # Получаем ключи и значения внутреннего словаря
    data_keys = list(data.keys())
    data_values = list(data.values())

    # Извлекаем значения (порядок известен)
    type, age, owner = data_values
    age = int(age)

    # Склонение слова "год"
    if 11 <= age % 100 <= 14:
        years_word = "лет"
    elif age % 10 == 1:
        years_word = "год"
    elif 2 <= age % 10 <= 4:
        years_word = "года"
    else:
        years_word = "лет"
        
    print(f"Это {type} по кличке \"{name}\". Возраст питомца: {age} {years_word}. Имя владельца: {owner}.")