word = input()
str = ""

str = "".join(c for c in word if c != " ")  # Генераторный цикл
print(str)

if (str.lower()[::1]) == (str.lower()[::-1]):
    print("Yes")
else:
    print("No")
