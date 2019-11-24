from environment import Environment
from graphics import Graphics

if __name__ == '__main__':
    e = Environment.nonZeroOhmega(15, 0)
    g = Graphics()
    i = 0
    while True:
        i += 1
        e.move()
        e.collisions()
        if i % 50 == 0:
            i = 0
            g.update(e.particles)
