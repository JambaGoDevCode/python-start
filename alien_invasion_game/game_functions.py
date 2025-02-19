import sys
import pygame
from bullet import Bullet

def Check_events(event, rocket, ai_settings, screen, bullets):
    """Responde a eventos de pressionamento de teclas e de mouse."""
    # Observa enventos de teclado e de mouse
    for event in pygame.event.get(): #
        if event.type == pygame.QUIT: 
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rocket, ai_settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)
            
def check_keydown_events(event, rocket, ai_settings, screen, bullets):
    """Responde a pressionamentos de tecla"""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = True
    elif event.key == pygame.K_SPACE:
        """Cria um novo projétil e o adiciona ao grupo de projéteis"""
        new_bullet = Bullet(ai_settings, screen, rocket)
        bullets.add(new_bullet)
        
def check_keyup_events(event, rocket):
    """Responde a solturas de tecla"""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False

def Update_screen(ai_settings, screen, rocket, bullets):
    """Atualiza as imagens na tela e alterna para a nova tela."""
    """Redesenha a tela a cada passagem pelo laço"""
    screen.fill(ai_settings.bg_color)
    """Redesenha todos os projéteis atrás da espaçonave e dos  alienígenas"""
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    rocket.blitme()
    """Deixa a tela mais recente visível"""
    pygame.display.flip()

