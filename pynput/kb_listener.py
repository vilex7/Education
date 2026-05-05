from pynput import keyboard

def on_press(key):
    try:
        print(f'Клавиша: {key.char}')
    except AttributeError:
        print(f'Спец.клавиша: {key}')

def on_release(key):
    if key == keyboard.Key.esc:
        # Остановить слушатель
        return False

with keyboard.Listener(
    on_press=on_press,
    on_release=on_release) as  listener:
    listener.join()

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()