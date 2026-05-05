from pynput.keyboard import Key, Controller

keyboard = Controller()

# Нажимаем и отпускаем пробел
keyboard.press(Key.space)
keyboard.release(Key.space)

# Нажимаем и отпускаем 'a'
keyboard.press('a')
keyboard.release('a')

# Удерживаем shift и вводим 'a'. После завершения отпускаем его
with keyboard.pressed(Key.shift):
    keyboard.press('a')
    keyboard.release('a')

# Вводим текст
keyboard.type('Hello World')