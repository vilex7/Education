def fac(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

def fac_list(n):
    if n < 1:
        raise ValueError("Дрисня, братуха")
    
    fac_n = fac(n)
    current = fac(fac_n)
    result = [current]

    for k in range(fac_n, 1, -1):
        current //= k
        result.append(current)
    
    return result

n = int(input("Введите натуральное целое число: "))
result_list = fac_list(n)

print(f"Факториал числа {n} равен {fac(n)}")
print(f"Список факториалов от {fac(n)} до 1: {result_list}")