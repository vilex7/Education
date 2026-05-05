start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

# Определение направления обхода
if start <= end:
    step = 1
else:
    step = -1

my_dict = {}
for num in range(start, end + step, step): # end + step - чтобы включить конечное значение, а следующий step задаёт шаг
    my_dict[num] = num ** num

for key, value in my_dict.items():
    print(f"{key} - {value}")