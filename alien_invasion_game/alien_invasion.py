import pygame
import sys
from settings import Settings
from rocket import Rocket

def run_game():
    # Inicializando o jogo e cria um objeto para a tela
    pygame.init() 
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    """Criar uma espaçonave"""
    rocket = Rocket(screen)
        # Inicia olaço principal do jogo 
    while True: 
        # Observa enventos de teclado e de mouse
        for event in pygame.event.get(): #
            if event.type == pygame.QUIT: 
                sys.exit()
                # Deixa a tela mais recente visível 
        # Redesenha a tela a cada passagem pelo laço
        screen.fill(ai_settings.bg_color)
        rocket.blitme()
        pygame.display.flip()
        
run_game()