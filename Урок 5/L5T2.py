word = input("Введите слово: ")
a =  ["a", "i", "e", "o", "u"]
c = 0
b = 0

for ch in word:
    if ch in a:
        c += 1
    else:
        b += 1
print(f"Колличество глассных: {c}.\nКолличесво согласных: {b}.")
