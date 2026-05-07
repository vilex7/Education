# 🟩 ⬛ 🌲 🌊 🚁 🏆 ❤️ 🏥 🏪 🪣 ⬜ 🟨 🔥
from map import Map
import time
import os
import json
from clouds import Clouds
from helicopter import Helicopter as heli
from pynput import keyboard 


TICK_SLEEP = 0.05
TREE_UPDATE = 50
CLOUDS_UPDATE = 100
FIRE_UPDATE = 75
MAP_W, MAP_H = 20, 20


MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}


field = Map(20, 20)
clouds = Clouds(MAP_W, MAP_H)
helico = heli(MAP_W, MAP_H)
tick = 1

# f - save, g - load

def process_key(key):
    global helico, tick, clouds, field
    c = key.char.lower()
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)
    if c == 'f':
        data = {'helicopter': helico.export_data(), 
                'clouds': clouds.export_data(), 
                'field': field.export_data(),
                'tick': tick}
        with open('level.json', 'w') as lvl:
            json.dump(data, lvl)
    elif c == 'g':
        with open('level.json', 'r') as lvl:
            data = json.load(lvl)
            helico.import_data(data['helicopter'])
            tick = data['tick'] or 1
            field.import_data(data['field'])
            clouds.import_data(data['clouds'])
    
listener = keyboard.Listener(
    on_press=None,
    on_release=process_key)
listener.start()


while True:
    os.system("cls")
    print('TICK', tick)
    field.print_map(helico, clouds)
    helico.print_stats()
    field.process_helicopter(helico, clouds)
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        field.generate_tree()
    if (tick % FIRE_UPDATE == 0):
        field.update_fire()
    if (tick % CLOUDS_UPDATE == 0):
        clouds.update()