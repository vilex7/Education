from utils import rand_cell

class Helicopter:

    def __init__(self, w, h):
        rc = rand_cell(w, h)
        rx, ry = rc[0], rc[1]
        self.x = rx
        self.h = h
        self.w = w
        self.y = ry
        self.mxtank = 1
        self.tank = 0
        self.score = 0
        self.lifes = 20

    def move(self, dx, dy):
        nx, ny = dx + self.x, dy + self.y
        if (nx >= 0 and ny >= 0 and nx < self.h and ny < self.w):
            self.x, self.y = nx, ny

    def print_stats(self):
        print('🪣 ', self.tank, '/', self.mxtank, sep='', end=' | ')
        print('🏆', self.score, end=' | ')
        print('❤️', self.lifes)

    def export_data(self):
        return {'self.score': self.score,
                'lifes': self.lifes,
                'x': self.x, 'y': self.y,
                'tank': self.tank, 'mxtank': self.mxtank}
    
    def import_data(self, data):
        self.x = data['x'] or 1
        self.y = data['y'] or 1
        self.tank = data['mxtank'] or 1
        self.lifes = data['life'] or 20
        self.score = data['score'] or 0