from graphics import Graphics
from vector import Vector
from particle import Particle

class Environment:
    #initialises an environment with args:
    #number of  randomisd particles
    #total angular momentum
    def __init__(self, noParticle, totalOhm):
        self.particleCount = noParticle
        self.totalOhm = 0
        self.particles = []
        for i in range(0, self.particleCount):
            self.particles.append(Particle.random())
    def updateMomentums(self):
        pass
    #idk physics lol
            
e = Environment(3, 0)
g = Graphics()
g.update(e.particles)
g.close()
