class cashbox:
    def __init__(self, initial_amount=0):
        self.money = initial_amount   # обязательно!

    def top_up(self, X):
        self.money += X

    def count_1000(self):
        return int(self.money // 1000)

    def take_away(self, X):
        if self.money >= X:
            self.money -= X
        else:
            raise ValueError("Недостаточно денег в кассе")

    def cashbox_status(self):
        return self.money


if __name__ == '__main__':
    cb = cashbox()
    print('Касса создана. Доступные команды:')
    print('  top_up <сумма>   - пополнить кассу')
    print('  take_away <сумма> - изъять сумму из кассы')
    print('  status           - показать текущую сумму')
    print('  count_1000       - показать количество целых тысяч')
    print('  exit             - завершить работу')

    while True:
        try:
            user_input = input('> ').strip()
            if not user_input:
                print('Команда не была введена')
                continue

            parts = user_input.split()
            command = parts[0].lower()

            if command == 'top_up':
                if len(parts) != 2:
                    print('Ошибка: укажите сумму для пополнения')
                    continue
                amount = float(parts[1])  # используем float для поддержки копеек
                cb.top_up(amount)
                print(f'Касса пополнена на {amount}. Текущий баланс: {cb.cashbox_status()}')

            elif command == 'take_away':
                if len(parts) != 2:
                    print('Ошибка: укажите сумму для изъятия')
                    continue
                amount = float(parts[1])
                cb.take_away(amount)
                print(f'Из кассы изъято {amount}. Текущий баланс: {cb.cashbox_status()}')

            elif command == 'status':
                print(f'Текущая сумма в кассе: {cb.cashbox_status()}')

            elif command == 'count_1000':
                thousands = cb.count_1000()
                print(f'В кассе {thousands} целых тысяч')

            elif command == 'exit':
                print('Выход из программы.')
                break

            else:
                print('Неизвестная команда. Доступные: top_up, take_away, status, count_1000, exit')

        except ValueError as e:
            print(f'Ошибка: {e}')
        except Exception as e:
            print(f'Непредвиденная ошибка: {e}')