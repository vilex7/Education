X = int(input("Введите натуральное число: "))
count = 0

for i in range(X):
    if X % (i + 1) == 0:
        count += 1
print(f"Количество натуральных делителей для числа {X}: {count}")