import pygame
from particle import Particle
from vector import Vector
import math
import sys

class Graphics:
    def __init__(self, width = 800, height = 500):
        self.dragging = False
        self.mouseDownPos = Vector(0, 0)
        self.mouseUpPos = Vector(0, 0)
        self.cameraPosition = Vector(0, 0)
        self.zoom = 1
        self.size = width, height
        self.background = 10, 30, 43
        self.foreground = 255,255,255
        pygame.init()
        self.d = pygame.display.set_mode(self.size)
        self.d.fill(self.background)
    def close(self):
        pygame.time.delay(100)
        pygame.display.quit()
        pygame.quit()
    def drawParticle(self, p: Particle):
        drawnRadius = math.floor(p.radius * self.zoom)
        pygame.draw.circle(self.d, self.foreground, (int((p.position.x - self.cameraPosition.x) * self.zoom),
                    int((p.position.y - self.cameraPosition.y) * self.zoom)), drawnRadius, drawnRadius)
        pygame.display.update()
    def update(self, ls: list):
        self.d.fill(self.background)
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
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.dragging = False
                    self.mouseDownPos = 0
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.close()
                    sys.exit()
            elif event.type == pygame.QUIT:
                self.close()
                sys.exit()
    def updateCameraPosition(self):
        if self.dragging == True:
            self.cameraPosition = self.cameraPosition + (self.mouseDownPos - Vector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
            self.mouseDownPos = Vector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
#this gon' be sick

#call close to get rid of window
#call update and pass list of particles to update graphics