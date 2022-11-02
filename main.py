import pygame
import random
import battleV2

pygame.init()

surface = pygame.display.set_mode((200, 150))
pygame.display.set_caption("Pokemon Showdown!")

white = (255, 255, 255)
black = (0, 0, 0)

def battle():
    battleV2.setup()