import pygame
from particle import Particle
from vector import Vector
import math

class Graphics:
    def __init__(self):
        self.dragging = False
        self.mouseDownPos = Vector(0, 0)
        self.mouseUpPos = Vector(0, 0)
        self.cameraPosition = Vector(0, 0)
        self.zoom = 1
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
        drawnRadius = math.floor(p.radius * self.zoom)
        pygame.draw.circle(self.d, self.white, (int((p.position.x - self.cameraPosition.x) * self.zoom),
                    int((p.position.y - self.cameraPosition.y) * self.zoom)), drawnRadius, drawnRadius)
        pygame.display.update()
    def update(self, ls: list):
        self.d.fill(self.black)
        self.eventHandler()
        self.updateCameraPosition()
        for p in ls:
            self.drawParticle(p)
    def eventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    self.zoom = self.zoom * 1.1
                elif event.button == 5:
                    self.zoom = self.zoom * 0.9
                if event.button == 1:
                    self.dragging = True
                    self.mouseDownPos = Vector(event.pos[0], event.pos[1])
            elif (event.type == pygame.MOUSEBUTTONUP):
                if (event.button == 1):
                    self.dragging = False
                    self.mouseDownPos = 0
    def updateCameraPosition(self):
        if self.dragging == True:
            self.cameraPosition = self.cameraPosition + (self.mouseDownPos - Vector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
            self.mouseDownPos = Vector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
#this gon' be sick

#call close to get rid of window
#call update and pass list of particles to update graphics
