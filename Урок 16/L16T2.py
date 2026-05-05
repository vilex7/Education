class Turtle:

    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s
        print(f'Черепаха взлетела на {self.s}')
        return self.y

    def go_down(self):
        self.y -= self.s
        print(f'Черепаха упала на {self.s}')
        return self.y

    def go_left(self):
        self.x -= self.s
        print(f'Черепаха подвинулась влево на {self.s}')
        return self.x

    def go_right(self):
        self.x += self.s
        print(f'Черепаха подвинулась вправо на {self.s}')
        return self.x

    def evolve(self):
        self.s += 1
        print(f'Шаг увеличен на 1. Текущий шаг: {self.s}')
        return self.s

    def degrade(self):
        self.s -= 1
        if self.s <= 0:
            raise ValueError('Ну как она может походить на отрицательное или нулевое количество клеток?')
        print(f'Шаг уменьшен на 1. Текущий шаг: {self.s}')
        return self.s
            
    def count_moves():
        pass

    def where(self):
        print(f'Черепаха сейчас располагается по следующим координатам:\nx: {self.x}, y: {self.y}')

cherepakha = Turtle()
print(f'Значит так, черепаха может совершать некоторого рода движения: \nВлево, вправо, вверх и вниз')
print(f'Используй одну их этих комманд, чтобы черепаха перемсилась в заданом направлении на заданое количество клеток\n')
print(f'Длинну шага можно изменять командами:\n"навали" - увеличивает длинну шага на 1\n"тиш"    - уменьшает длинну шага на 1')
print(f'Длинна шага не может быть меньше или равной нулю\n')
print(f'Каждое действие, будь то движение или изменение шага является ходом')
print(f'Задвинь черепаху до нужного места за минимальное количество ходов. GL\n')
print(f'Также есть команда "вхер?". Используй её, чтоб узнать где сейчас черепаха. Команда "скока?" показывает сколько ты сделал ходов и их историю.\nОни кстати за ход не считаются\n')
print(f'Напиши команду "exit", чтоб ливнуть с позором')

steps_count = []

while True:
    try:
        user_input = input('> ').strip()
        if not user_input:
            print('Команда не была введена')
            continue

        parts = user_input.split()
        command = parts[0].lower()

        if command == 'вверх':
            cherepakha.go_up()
            steps_count.append(command)

        elif command == 'вниз':
            cherepakha.go_down()
            steps_count.append(command)

        elif command == 'влево':
            cherepakha.go_left()
            steps_count.append(command)

        elif command == 'вправо':
            cherepakha.go_right()
            steps_count.append(command)
        
        elif command == 'навали':
            cherepakha.evolve()
            steps_count.append(command)

        elif command == 'тиш':
            cherepakha.degrade()
            steps_count.append(command)

        elif command == 'вхер?':
            cherepakha.where()

        elif command == 'скока?':
            print(f'{len(steps_count)} ходов')
            print(f'История команд: {steps_count}')

        elif command == 'exit':
            print('Выход из программы.')
            break

    except ValueError as e:
        print(f'Ошибка: {e}')
    except Exception as e:
        print(f'Непредвиденная ошибка: {e}')