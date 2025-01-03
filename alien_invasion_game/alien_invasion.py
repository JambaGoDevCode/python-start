import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from rocket import Rocket

def run_game():
    """Inicializando o jogo e cria um objeto para a tela"""
    pygame.init() 
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    """Criar uma espaçonave"""
    rocket = Rocket(ai_settings,screen)
    """Cria um grupo no qual serão armazenados os projéteis"""
    bullets = Group()
    """Inicia olaço principal do jogo"""
    while True: 
        gf.Check_envents(ai_settings, screen,rocket, bullets)
        rocket.Update()
        bullets.UpdateBullet()
        gf.Update_screen(ai_settings, screen, rocket, bullets)
run_game()