from pynput import mouse

# Обработка координатов курсора
def on_move(x, y):
    print(f'Позицияя курсора: x:{x}, y:{y}')

# Обработка нажатий
def on_click(x, y, button, pressed):
    pressed_status = 'Pressed' if pressed else 'Released'
    print(f'Позицияя курсора: x:{x}, y:{y} | Статус нажатия: {pressed_status} | Кнопка: {button}')

# Собираем события пока не закончится поток
with mouse.Listener(
    on_move=on_move,
    on_click=on_click) as listener:
    listener.join()

# Запускаем метод для отслеживания мышки
listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click)
listener.start()