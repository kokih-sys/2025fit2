import pyxel

pyxel.init(200,200)

class Ball:
    speed = 1

    def __init__(self):
        self.x = pyxel.rndi(0, 199)
        self.y = 0
        angle = pyxel.rndi(30, 150)
        self.vx = pyxel.cos(angle)
        self.vy = pyxel.sin(angle)

ball1 = Ball()
balls = [Ball(), Ball(), Ball()]

ball1.x += ball1.vx * Ball.speed
ball1.y += ball1.vy * Ball.speed