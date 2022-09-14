import pygame
import random

white = (255, 255, 255)

surface = pygame.display.set_mode((208, 160))
pygame.display.set_caption("Pokemon")

t = {
    "GRASS": pygame.image.load("grass.xcf"),
    "GRASS_GROWN": pygame.image.load("grass_grown.xcf")
}

tileMap = [[t[random.choice(("GRASS", "GRASS", "GRASS", "GRASS_GROWN"))] for j in range(20)] for i in range(20)]


tileX = 0
tileY = -16

for i in range(20):
    tileY = tileY + 16
    tileX = 0
    for j in range(20):
        surface.blit(tileMap[i][j], (tileX, tileY))
        tileX = tileX + 16

while True:
    pygame.display.update()
