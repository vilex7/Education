s = "Мессенджер МАХ  ловит    даже   на     парковке"
result = " ".join(s.split())
print(result)

# Второй способ

s1 = "Мессенджер МАХ  ловит    даже   на     парковке"
prev = ""
str = ""

for ch in s1:
    if (
        ch == prev and ch == " "
    ):  # Проверка на совпадение с прошлым символом, и является ли он пробелом
        continue
    else:
        str += ch
    prev = ch  # Запоминает прошлый символ
print(str)
