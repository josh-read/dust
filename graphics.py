import pygame
from particle import Particle
from vector import Vector
import math

class Graphics:
    def __init__(self):
        self.size = width, height = 800, 500
        self.black = 0, 0, 0
        self.white = 255,255,255
        pygame.init()
        self.d = pygame.display.set_mode(self.size)
        self.d.fill(self.black)
    def close(self):
        pygame.time.delay(2000)
        pygame.display.quit()
        pygame.quit()
    def drawParticle(self, p: Particle):
        pygame.draw.circle(self.d, self.white, (int(p.position.x), int(p.position.y)) , math.floor(p.radius * 50), 3)
        pygame.display.update()
    def update(self, ls: list):
        self.d.fill(self.black)
        for p in ls:
            self.drawParticle(p)
            
#this gon' be sick

#call close to get rid of window
#call update and pass list of particles to update graphics
