from environment import Environment
from graphics import Graphics

if __name__ == '__main__':
    try:
        e = Environment.random_static(15)
        g = Graphics()
        i = 0
        while True:
            i += 1
            e.move()
            e.collisions()
            if i % 50 == 0:
                i = 0
                g.update(e.particles)
        g.close()
    except:
        g.close()