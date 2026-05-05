s1 = int(input("Количество элементов первого списка: "))
s2 = int(input("Количество элементов второго списка: "))

while s1 > 100000 or s2 > 100000:
    if s1 > 100000:
        s1 = int(input("Количество элементов первого списка не может превышать 100000. Введите корректное значение: "))
    elif s2 > 100000:
        s2 = int(input("Количество элементов второго списка не может превышать 100000. Введите корректное значение: "))

sp1 = []

for i in range(s1):
    j = int(input(f"Введите {i + 1}-ое число первого списка: "))
    sp1.append(j)

sp2 = []

for i in range(s2):
    j = int(input(f"Введите {i + 1}-ое число второго списка: "))
    sp2.append(j)

first_s = set(sp1)
second_s = set(sp2)

count = 0
for num in first_s:
    if num in second_s:
        count += 1

print(count)