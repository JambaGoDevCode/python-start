import pygame

class Rocket():
    """Incializa a espaçonave e define sua posição inical"""
    def __init__(self, ai_settings, screen):
        self.ai_settings = ai_settings
        self.screen = screen
        
        """Carregar a imagem da espaçonave e obtém seu rect"""
        self.image = pygame.image.load("C:\\learnigCode\\python-start\\alien_invasion_game\\rocket.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        """Armazena um valor decimal para o centro espaçonave"""
        self.center = float(self.rect.centerx)
        
        """Inicia cada nova espaçonave na parte inferior central da tela"""
        self.rect.centerx = self.screen_rect.centerx 
        self.rect.bottom = self.screen_rect.bottom 
        self.moving_right = False
        self.moving_left = False
    
    def Update(self):
        """Atualiza a posição da espaçonave de acordo com a flag de movimento"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
            """Atualiza o valor do centro da espaçonave, e não o retângulo"""
            self.center += self.ai_settings.rocket_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1
            self.center -= self.ai_settings.rocket_speed_factor
        """Atualiza o objeto rect de acordo com self.center"""
        self.rect.centerx = self.center
    
            
    def blitme(self):
        """Desenha a espaçonave em sua posição atual"""
        self.screen.blit(self.image, self.rect)