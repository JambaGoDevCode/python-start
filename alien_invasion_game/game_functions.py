import sys
import pygame

def Check_envents():
    """Responde a eventos de pressionamento de teclas e de mouse."""
    # Observa enventos de teclado e de mouse
    for event in pygame.event.get(): #
        if event.type == pygame.QUIT: 
            sys.exit()


def Update_screen(ai_settings, screen, rocket):
    """Atualiza as imagens na tela e alterna para a nova tela."""
    # Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)
    rocket.blitme()
    # Deixa a tela mais recente visível 
    pygame.display.flip()
