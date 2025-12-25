import pyxel

pyxel.init(200, 200)
pyxel.cls(7)

xs = [10, 70, 145, 150]
ys = [50, 160, 30, 130]
rs = [5, 20, 10, 15]
cs = [1, 4, 14, 6]

for i in range(0, len(xs)):
    pyxel.circ(xs[i], ys[i], rs[i], cs[i])
pyxel.show()