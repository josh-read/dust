import pygame
from particle import Particle
from vector import Vector
import math
import sys

class Graphics:
    def __init__(self, width = 1000, height = 500):
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
        self.UIOpen = True
        self.font = pygame.font.Font('freesansbold.ttf', 16) 
        self.text = self.font.render('No Mouse Connected', True, self.foreground, self.background) 
        self.textRect = self.text.get_rect()  
        self.textRect.center = (100, 20) 

    def close(self):
        pygame.time.delay(100)
        pygame.display.quit()
        pygame.quit()
    def drawParticle(self, p: Particle):
        drawnRadius = math.floor(p.radius * self.zoom)
        pygame.draw.circle(self.d, self.foreground, (int((p.position.x - self.cameraPosition.x) * self.zoom),
                    int((p.position.y - self.cameraPosition.y) * self.zoom)), drawnRadius, drawnRadius)       
    def update(self, ls: list):
        self.d.fill(self.background)
        self.eventHandler()
        self.updateCameraPosition()    
        for p in ls:
            self.drawParticle(p)
        if self.UIOpen:
            self.drawUI()
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
            self.mouseDownPos = Vector(event.pos[0], event.pos[1])
            self.text = self.font.render(('%i, %i' % (int(self.mouseDownPos.x), int(self.mouseDownPos.y))), True, self.foreground, self.background)
            if self.mouseDownPos.x < self.size[0] - 200 or self.UIOpen == False:
                self.dragging = True
            elif self.withinRect(pygame.Rect((808, 9),(180 , 20))):
                self.UIOpen = False
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
    def updateCameraPosition(self):
        if self.dragging == True:
            self.cameraPosition = self.cameraPosition + (self.mouseDownPos - Vector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])) * (1 / self.zoom) 
            self.mouseDownPos = Vector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    def drawUI(self):
        UI = pygame.image.load("UserInterface/uILanding.jpg")
        self.d.blit(UI, (self.size[0] - 200, 0))
  
  
#this gon' be sicks

#call close to get rid of window
#call update and pass list of particles to update graphics