import os
import sys
import math

import pygame

from particle import Particle
from vector import Vector


class Graphics:

    def __init__(self, width=1000, height=500):
        self.dragging = False
        self.mouseDownPos = Vector(0, 0)
        self.mouseUpPos = Vector(0, 0)
        self.cameraPosition = Vector(0, 0)
        self.zoom = 1
        self.size = width, height
        self.background = 10, 30, 43
        self.foreground = 255, 255, 255
        pygame.init()
        pygame.display.set_caption('Dust in Space')
        self.d = pygame.display.set_mode(self.size)
        self.uILandingOpen = True
        self.font = pygame.font.Font('freesansbold.ttf', 16)
        self.text = self.font.render('No Mouse Connected', True, self.foreground, self.background)
        self.textRect = self.text.get_rect()
        self.textRect.center = (100, 20)
        self.trackingCOM = False
        self.uIParticleSpawn = False
    def close(self):
        pygame.time.delay(100)
        pygame.display.quit()
        pygame.quit()

    def drawParticle(self, p: Particle):
        drawnRadius = math.floor(p.radius * self.zoom)
        pygame.draw.circle(
                self.d,
                self.foreground,
                (int((p.position.x - self.cameraPosition.x) * self.zoom), int((p.position.y - self.cameraPosition.y) * self.zoom)),
                drawnRadius,
                drawnRadius)

    def update(self, ls: list):
        self.d.fill(self.background)
        self.eventHandler()
        self.updateCameraPosition(ls)    
        for p in ls:
            self.drawParticle(p)        
        self.drawUI()
        self.text = self.font.render(
                ('%i, %i   zoom: %i %%'
                    % (*pygame.mouse.get_pos(), self.zoom * 100)),
                True,
                self.foreground,
                self.background)
        self.d.blit(self.text, self.textRect) 
        pygame.display.update()

    def eventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouseDownHandler(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouseUpHandler(event)
            elif event.type == pygame.KEYDOWN:
                self.keyDownHandler(event)
            elif event.type == pygame.QUIT:
                self.close()
                sys.exit()

    def mouseDownHandler(self, event):
        if event.button == 4:
            self.zoom = self.zoom * 1.1
        elif event.button == 5:
            self.zoom = self.zoom * 0.9
        elif event.button == 1:
            self.mouseDownPos = Vector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            if self.uILandingOpen:
                self.initialUIClicks(event)
            elif self.uIParticleSpawn:
                self.particleSpawnerClicks(event)
            else:
                self.noUIClicks(event)
    def initialUIClicks(self, event):
        if self.mouseDownPos.x < self.size[0] - 200:
            self.dragging = True
        elif self.withinRect(pygame.Rect((self.size[0] - 190, 100),(180, 45))):
            self.uILandingOpen = False
            self.uIParticleSpawn = True
        elif self.withinRect(pygame.Rect((self.size[0] - 190, 9),(180 , 20))):
                self.uILandingOpen = False
        elif self.withinRect(pygame.Rect((self.size[0] - 190, 45),(180 , 45))):
                self.trackingCOM = ~self.trackingCOM
    def noUIClicks(self, event):
        if self.withinRect(pygame.Rect((self.size[0] - 20, 0), (20, 20))):
            self.uILandingOpen = True
        else:
            self.dragging = True
    def particleSpawnerClicks(self, event):
        if self.mouseDownPos.x < self.size[0] - 200:
            self.dragging = True
        elif self.withinRect(pygame.Rect((self.size[0] - 95, 420),(80,40))):
            self.uIParticleSpawn = False
            self.uILandingOpen = True
    def withinRect(self, r: pygame.Rect):
        if self.mouseDownPos.x > r.left and self.mouseDownPos.y > r.top \
        and self.mouseDownPos.x < r.left + r.width and self.mouseDownPos.y < r.top + r.height:
            return True
        else:
            return False

    def mouseUpHandler(self, event):
        if event.button == 1:
            self.dragging = False
            self.mouseDownPos = 0

    def keyDownHandler(self, event):
        if event.key == pygame.K_ESCAPE:
            self.close()
            sys.exit()
        elif event.key == pygame.K_1:
            pass

    def updateCameraPosition(self, ls: list):
        if self.dragging:
            self.cameraPosition = self.cameraPosition + (self.mouseDownPos - Vector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])) * (1 / self.zoom) 
            self.mouseDownPos = Vector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        elif self.trackingCOM:
            self.cameraPosition = sum(ls).position - Vector((self.size[0] - 200)/2, self.size[1]/2)

    def drawUI(self):
        currentdir = os.path.dirname(os.path.realpath(__file__))
        if self.uILandingOpen:
            path = os.path.join(currentdir, "UserInterface/uILanding.jpg")
            UI = pygame.image.load(path)
            self.d.blit(UI, (self.size[0] - 200, 0))
        elif self.uIParticleSpawn:
            path = os.path.join(currentdir, "UserInterface/particleSpawner.jpg")
            UI = pygame.image.load(path)
            self.d.blit(UI, (self.size[0] - 200, 0))
        else:
            path = os.path.join(currentdir, "UserInterface/openSettings.jpg")
            UI = pygame.image.load(path)
            self.d.blit(UI, (self.size[0] - 20, 0))


# this gon' be sicks

# call close to get rid of window
# call update and pass list of particles to update graphics
