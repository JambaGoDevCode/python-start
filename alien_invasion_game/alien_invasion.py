import pygame
import sys

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                sys.exist()
                pygame.display.flip()
run_game()