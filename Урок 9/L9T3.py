num_list = list(map(int, input("Введите элементы через пробел: ").split()))

seen = set()

for num in num_list:
    if num in seen:
        print(f"{num} - YES")
    else:
        print(f"{num} - NO")
        seen.add(num)