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
        self.moving_right = False
        self.moving_left = False
    
    def Update(self):
        """Atualiza a posição da espaçonave de acordo com a flag de movimento"""
        if self.moving_right:
            self.rect.centerx += 1
        elif self.moving_left:
            self.rect.centerx -= 1
            
    def blitme(self):
        """Desenha a espaçonave em sua posição atual"""
        self.screen.blit(self.image, self.rect)