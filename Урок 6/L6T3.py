A = int(input("Введите переменную A: "))
B = int(input("Введите переменную B: "))

arr = []

if A>B:
    print("A меньше B")
else:
    while (A<=B): # Поиск чётных элементов на отрезке
        if A % 2 == 0: arr.append(A)
        A += 1

for i in arr:
    print(i, end=" ") # Вывод чётных элементов