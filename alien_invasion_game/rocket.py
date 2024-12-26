import pygame

class Rocket():
    """Incializa a espaçonave e define sua posição inical"""
    def __init__(self, screen):
        self.screen = screen
        """Carregar a imagem da espaçonave e obtém seu rect"""
        self.image = pygame.image.load("C:\\learnigCode\\python-start\\alien_invasion_game\\rocket.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        """Inicia cada nova espaçonave na parte inferior central da tela"""
        self.rect.centerx = self.screen_rect.centerx 
        self.rect.bottom = self.screen_rect.bottom 
    
    def blitme(self):
        """Desenha a espaçonave em sua posição atual"""
        self.screen.blit(self.image, self.rect)