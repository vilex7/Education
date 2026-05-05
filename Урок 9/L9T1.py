N = int(input("Введите количество элементов: "))

while N > 100000 or N < 1:
    N = int(input("Количесво элементов не может быть больше 100000 или меньше 1. Введите количество элементов: "))

user_list = list(map(int, input("Введите элементы через пробел: ").split()))

while len(user_list) != N:
    user_list = list(map(int, input("Введённое колличество значений не соответствует с указанным ранее. Введите элементы через пробел: ").split()))

for i in range(len(user_list)):
    while abs(user_list[i]) > 2 * 10e9:
        user_list[i] = int(input(f"Модуль числа {user_list[i]} превышает максимально допустимое (2*10e9). Введите корректное значение: "))

ul = set(user_list)
print(f"Количество уникальных элементов: {len(ul)}")