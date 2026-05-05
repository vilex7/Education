# 🟩 ⬛ 🌲 🌊 🚁 🏆 ❤️ 🏥 🏪 🪣 ☁️ ⚡ 🔥
from map import Map
import time
import os
from helicopter import Helicopter as heli
from pynput import keyboard 

TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 100
MAP_W, MAP_H = 20, 10

tmp = Map(20, 20)

if (tmp.check_bound(20, 30)):
    print("yes")

tmp.generate_forest(1, 100)
tmp.generate_river(5)

helico = heli(MAP_W, MAP_H)

tick = 1

while True:
    os.system("cls")
    print('TICK', tick)
    tmp.print_map(helico)
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        tmp.generate_tree()
    if (tick % FIRE_UPDATE == 0):
        tmp.update_fire()