from operator import truediv
import random
import time
import pygame
from chicken import Chicken
from environment import Environment
from graphik import Graphik
from grass import Grass


pygame.init()

black = (0,0,0)
white = (255,255,255)

displayWidth = 640
displayHeight = 640

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))

graphik = Graphik(gameDisplay)

pygame.display.set_caption("EWPELG")

clock = pygame.time.Clock()

environment = Environment("Test", 4)
chicken = Chicken("Gerald")

environment.addEntity(chicken)
environment.printInfo()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        gameDisplay.fill(white)

        locationWidth = displayWidth/environment.getGrid().getRows()
        locationHeight = displayHeight/environment.getGrid().getColumns()

        # draw environment
        for location in environment.getGrid().getLocations():
            color = white
            if location.getNumEntities() > 0:
                color = black
            graphik.drawRectangle(location.getX() * locationWidth, location.getY() * locationHeight, locationWidth, locationHeight, color)

        pygame.display.update()