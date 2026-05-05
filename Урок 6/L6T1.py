N = int(input("Колличество целых чисел: "))
numbers = []
count = 0

for i in range(N):
    numbers.append(int(input(f"{i + 1}-ое число: "))) # Добавление переменных в массив
for n in numbers: # Счётчик нулевых значений
    if n == 0:
        count += 1
print(f"Колличество нулевых значений = {count}")