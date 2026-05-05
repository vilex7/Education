nums = [5, 7, 2, 4, 7, True, "hello", 6.7, [5, 7]]

nums[0] = 50
nums[5] = 1.01

print(nums[3])
print(nums[-1][1])

 
# Методы списков

numbers = [5, 2, 7]
numbers.append(100) # Добавление элемента в конец списка
numbers.insert(1, True) # Добавление элемента на место другого со смещением вперёд
numbers.extend([5, 6, 8]) # Добавление нескольких элементов в конец списка
b = [3,2, 2]
numbers.extend(b)
numbers.sort() # Сортировка элементов в списке. При этом если в списке есть True - оно примет значение 1, а False - значение 0
numbers.reverse() # Переворачивает список
numbers.pop() # Удаление элемента из списка. При пустом параметре удаляется послений элемент списка
# numbers.remove(True) Удаление индекса с определённым значением
# numbers.clear() Очистка всего списка. Не принимает никакие параметры
print(numbers.count(5)) # Выводит количество элементов списка, соответствующих указанному в параметре
print(len(numbers)) # Выводит длинну списка

print(numbers)


# -

nums = [5, 2, 7, "50", False]

for el in nums:
    el *= 2
    print(el)


# -

n = int(input("Ведите длинну списка: "))

user_list = []

i = 0
while i < n: # Лучше использовать цикл for, но для парктики используется цикл while
     string = "Введите элемент №" + str(i + 1) + ": "
     user_list.append(input(string))
     i += 1

print(user_list)