x = int(input("Введите натуральное число: "))
count = 0

for i in range(x):
    if x % (i + 1) == 0:
        count += 1
print("Колличество натуральных делителей:", count)