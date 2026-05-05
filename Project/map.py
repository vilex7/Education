from utils import rand_bool
from utils import rand_cell
from utils import rand_direction

# 0 - поле
# 1 - дерево
# 2 - река
# 3 - госпиталь
# 4 - шоп
# 5 - огонь

CELL_TYPES = "🟩🌲🌊🏥🏪🔥"

class Map:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for _ in range(w)] for _ in range(h)]

    def check_bound(self, x, y):
        if (x < 0 or y < 0 or x >= self.h or y >= self.w):
            return False
        return True
    
    def print_map(self, helico):
        print('⬛' * (self.w + 2))
        for ri in range(self.h):
            print('⬛', end='')
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if (helico.x == ri and helico.y == ci):
                    print('🚁', end='')
                elif (cell >= 0 and cell < len(CELL_TYPES)):
                    print(CELL_TYPES[cell], end="")
            print('⬛')
        print('⬛' * (self.w + 2))
    
    def generate_river(self, l):
        root = rand_cell(self.w, self.h)
        rx, ry = root[0], root[1]
        self.cells[rx][ry] = 2
        
        river = set()
        river.add(root)
        
        while l:
            flow = rand_direction(rx, ry)
            fx, fy = flow[0], flow[1]
        
            if flow in river:
                continue
            river.add(flow)
        
            if (self.check_bound(fx, fy)):
                self.cells[fx][fy] = 2
                rx, ry = fx, fy
                l -= 1

    def generate_forest(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if rand_bool(r, mxr):
                    self.cells[ri][ci] = 1

    def generate_tree(self):
        c = rand_cell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.check_bound(cx, cy) and self.cells[cx][cy] == 0):
            self.cells[cx][cy] = 1

    def add_fire(self):
        c = rand_cell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 1:
            self.cells[cx][cy] == 5

    def update_fire(self):
        for ri in range(self.h):
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if cell == 5:
                    self.cells[ri][ci] = 0
        for i in range(5):
            self.add_fire()


    