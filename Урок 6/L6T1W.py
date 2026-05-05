N = int(input("Введите колличество натуральных чисел: "))
count = 0

for i in range(N):
    num = int(input(f"{i + 1}-ое число: "))
    if num == 0:
        count += 1
print(f"Колличество нулевых значений: {count}")