N = int(input("Введите длинну списка: "))

user_list = []
uls = 0

for i in range(N):
    i = int(input(f"Введите {i + 1} число: "))
    while i > 10000 or i < 1:
        i = int(input(f"Число не может быть больше 10000 или меньше 1. Введите число: "))
    user_list.append(i)
    uls += i

if uls > 10e5:
    print("Модуль введённых чисел превышает максимально допустимое значение.")
else:
    print(user_list[::-1])