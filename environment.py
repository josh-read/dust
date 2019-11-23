from graphics import Graphics
from particle import Particle

DT = 1  # Our timestep


class Environment:

    def __init__(self, noParticle, totalOhm):
        """
        initialises an environment with args:
        - number of  randomisd particles
        - total angular momentum"""
        self.particleCount = noParticle
        self.totalOhm = 0
        self.particles = []
        for i in range(0, self.particleCount):
            self.particles.append(Particle.random())

    def collisions(self):
        """Function checks for collisions between particles and merges
        colliding particles."""
        for i, current in enumerate(self.particles):
            for j, other in enumerate(self.particles):
                if i == j:
                    pass
                else:
                    if current % other:
                        # add other particle to current
                        self.particles[i] = current + other
                        # delete other particle from list
                        del self.particles[j]
                    else:
                        pass

    def move(self):
        for particle in self.particles:
            particle.update(self.particles, DT)
        

if __name__ == '__main__':
    e = Environment(1, 0)
    g = Graphics()
    for i in range(3000):
        e.move()
        e.collisions()
        g.update(e.particles)
    g.close()
