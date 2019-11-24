from environment import Environment
from graphics import Graphics

if __name__ == '__main__':
    e = Environment(15, 0)
    g = Graphics()
    for i in range(20000):
        e.move()
        e.collisions()
        if i % 10 == 0:
            g.update(e.particles)
    g.close()
