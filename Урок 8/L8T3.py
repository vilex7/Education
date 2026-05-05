capacity = int(input("Грузоподъёмность лодки: "))
fishers = int(input("Количество рыбаков: "))

while capacity < 1 or capacity > 10e6 or fishers < 1 or fishers > 100:
    if capacity < 1 or capacity > 10e6:
        capacity = int(input("Грузоподъёмность должна соответствовать критерию 1<=грузоподъёмность<=10e6. Введите корректное значение: "))
    else:
        fishers = int(input("Клочество рыбаков должно соответствовать критерию 1<=рыбаки<=100. Введите корректное значение: "))

fisher_weight = []

for i in range(fishers):
    j = int(input(f"Вес {i + 1}-ого рыбака: "))
    while j > capacity or j < 1:
        j = int(input("Вес рыбака не может превышать грузоподъёность лодки или быть меньше 1. Введите корректное значение: "))
    fisher_weight.append(j)

boats = 0
fisher_weight.sort()

while max(fisher_weight) + min(fisher_weight) > capacity:
    fisher_weight.pop(fisher_weight.index(max(fisher_weight)))
    boats += 1

while len(fisher_weight):
    for i in range(len(fisher_weight)):
        weight = max(fisher_weight) + fisher_weight[i]

        if weight <= capacity and not 2 * max(fisher_weight) <= capacity:
            continue
        else:
            fisher_weight.pop(fisher_weight.index(max(fisher_weight)))
            fisher_weight.pop(i - 1)
            boats += 1
            break

    if len(fisher_weight) == 1:
        fisher_weight.pop(i)
        boats += 1

print(f"Минимально необходимое количество лодок: {boats}")