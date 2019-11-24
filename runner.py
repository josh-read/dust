from environment import Environment
from graphics import Graphics

if __name__ == '__main__':
    e = Environment.random_static(100)
    g = Graphics()
    for i in range(20000):
        e.move()
        e.collisions()
        if i % 50 == 0:
            g.update(e.particles)
    g.close()
