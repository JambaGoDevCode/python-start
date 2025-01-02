import pygame
from settings import Settings
from rocket import Rocket
import game_functions as gf

def run_game():
    # Inicializando o jogo e cria um objeto para a tela
    pygame.init() 
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    """Criar uma espaçonave"""
    rocket = Rocket(ai_settings,screen)
        # Inicia olaço principal do jogo 
    while True: 
        gf.Check_envents(rocket)
        rocket.Update()
        gf.Update_screen(ai_settings, screen, rocket)
run_game()