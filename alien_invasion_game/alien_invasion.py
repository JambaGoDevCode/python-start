import pygame
import sys

def run_game():
    # Inicializando o jogo e cria um objeto para a tela
    pygame.init() 
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)
        # Inicia olaço principal do jogo 
    while True: 
        # Observa enventos de teclado e de mouse
        for event in pygame.event.get(): #
            if event.type == pygame.QUIT: 
                sys.exist()
                # Deixa a tela mais recente visível 
        # Redesenha a tela a cada passagem pelo laço
        screen.fill(bg_color)
        pygame.display.flip()
        
run_game()