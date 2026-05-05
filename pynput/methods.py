from pynput.mouse import Button, Controller

mouse = Controller() # Класс для работы с мышкой
print(f'Текущая позиция курсора: {mouse.position}') # Текущее положение мыши
mouse.position = (10, 20) # Перемещение курсора на (x, y)
print(f'Текущая позиция курсора: {mouse.position}')
mouse.move(20, 10) # Смещение курсора на (x, y)
print(f'Текущая позиция курсора: {mouse.position}')
mouse.press(Button.left) # Нажатие и удерживание ЛКМ. Можно исользовать также right и middle
mouse.release(Button.left) # Отпустить ЛКМ
mouse.click(Button.left, 2) # Даблклик