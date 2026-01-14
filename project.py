import pyxel

field_size = 150
SCREEN_WIDTH = 256
SCREEN_HEIGHT = 256


class Enemy:
    speed = 1

    def __init__(self):
        self.w =12
        self.h = 8
        self.x = pyxel.rndi(0, SCREEN_WIDTH - self.w)
        self.y = 0
        self.vx = 0
        self.vy = 1
        self.shot = 1

    def move(self):
        self.y += Enemy.speed * self.vy
        
class Ball:
    speed = 10

    def __init__(self, x, y, vy):
        self.x = x
        self.y = y
        self.vy = vy
        self.r = 2

class Player:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - 20
        self.w = 12
        self.h = 8
        self.max_life = 5
        self.life = self.max_life
        self.recover_life = 2
        self.shot = 1
        

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title= "PROTECT OUR HOMELAND!", capture_scale= 1)
        pyxel.mouse(True)
        pyxel.load("my_resource.pyxres")

        self.player = Player()
        self.enemies = []
        self.player_Ball = []
        self.enemy_Ball = []
        self.score = 0
        self.game_over = False

        pyxel.run(self.update, self.draw)

    def reset(self):
        self.player = Player()
        self.enemies = []
        self.player_Ball = []
        self.enemy_Ball = []
        self.score = 0
        self.game_over = False

    def update(self):
        if self.game_over:
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.reset()
            return

        self.player.x = pyxel.mouse_x
        self.player.shot +=1

        if self.player.shot >5:
            self.player_Ball.append(Ball(self.player.x + self.player.w//2, self.player.y, -5))
            self.player.shot = 0

        if pyxel.frame_count % 40 == 0:
            self.enemies.append(Enemy())

        for i in range(len(self.enemies)-1, -1, -1):
            e = self.enemies[i]
            e.y += e.speed
            e.shot += 1

            if e.shot > 25:
                self.enemy_Ball.append(Ball(e.x + e.w//2, e.y, +5))
                e.shot = 0
            
            if e.y > SCREEN_HEIGHT:
                self.game_over = True

            for i in range(len(self.player_Ball)-1, -1, -1):
                b = self.player_Ball[i]
                b.y += b.vy

                if b.y + b.r < 0:
                    del self.player_Ball[i]

        for i in range(len(self.player_Ball) -1, -1, -1):
            b = self.player_Ball[i]
            
            for j in range(len(self.enemies)-1, -1, -1):
                e = self.enemies[j]

                if (e.x - b.r < b.x <e.x + e.w + b.r and e.y - b.r < b.y < e.y + e.h + b.r):
                    del self.player_Ball[i]
                    del self.enemies[j]
                    self.score += 100
                    break

            for i in range(len(self.enemy_Ball)-1, -1, -1):
                b = self.enemy_Ball[i]
                b.y += b.vy

                if b.y > SCREEN_HEIGHT:
                    del self.enemy_Ball[i]

            for i in range(len(self.player_Ball)-1, -1, -1):
                b = self.player_Ball[i]

                for j in range(len(self.enemy_Ball)-1, -1, -1):
                    e = self.enemy_Ball[j]

                    if abs(b.x - e.x) < b.r + e.r and abs(b.y - e.y) < b.r + e.r:
                        del self.player_Ball[i]
                        del self.enemy_Ball[j]

                        if self.player.life < self.player.max_life - self.player.recover_life:
                            self.player.life += 1
                        else:
                            self.score += 100
                    break

            for i in range(len(self.enemy_Ball)-1, -1, -1):
                b = self.enemy_Ball[i]

                if (self.player.x < b.x < self.player.x + self.player.w and self.player.y < b.y < self.player.y + self.player.h):
                    del self.enemy_Ball[i]
                    self.player.life -= 1

                    if self.player.life <= 0:
                        self.game_over = True
        
    def draw(self):
        pyxel.cls(0)

        pyxel.blt(self.player.x, self.player.y, 0, 24, 48, 28, 25, 0)
        for i in range(len(self.enemies)):
            e = self.enemies[i]
            pyxel.blt(e.x, e.y, 0, 18, 36, 12, 10, 0)

        for i in range(len(self.player_Ball)):
            b = self.player_Ball[i]
            pyxel.circ(b.x, b.y, b.r, 9)

        for i in range(len(self.enemy_Ball)):
            b = self.enemy_Ball[i]
            pyxel.circ(b.x, b.y, b.r, 8)

        pyxel.text(5, 5, f"SCORE{self.score}", 7)
        pyxel.text(5, 15, f"LIFE{self.player.life}", 7)

        if self.game_over:
            pyxel.text(110, 120, "GAME OVER", 9)
            pyxel.text(70, 140, "Press the spacebar to restart", 9)

App()