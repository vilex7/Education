Mickle = int(input("Капитал Майкла: "))
Ivan = int(input("Капитал Ивана: "))
invest_sum = int(input("Минимальная сумма инвестиций: "))

if (Mickle >= invest_sum) and (Ivan >= invest_sum):
    print(2)
elif (Mickle <= invest_sum) and (Ivan >= invest_sum) or (Mickle >= invest_sum) and (Ivan <= invest_sum) or (Ivan + Mickle >= invest_sum):
    print(1)
else:
    print(0)