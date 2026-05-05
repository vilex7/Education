N = int(input("Введите количество элементов массива: "))

while N > 100000 or N < 1:
    N = int(input("Количесво элементов массива не может быть больше 100000 или меньше 1. Введите количество элементов массива: "))

user_list = list(map(int, input("Введите элементы массива через пробел: ").split()))

while len(user_list) != N:
    user_list = list(map(int, input("Введённое колличество значений не соответствует с указанным ранее. Введите элементы массива через пробел: ").split()))

for i in user_list:
    while i < 1 or i > 10e9:
        user_list[i] = int(input("Введённое значение не соответствует критерию 1<=значение<=10e9. Введите корректное значение: "))

b = user_list[-1]
user_list.insert(0, b)
user_list.pop()

print(user_list)