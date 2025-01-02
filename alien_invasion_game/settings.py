class Settings():
    """Uma classe para armazenar todas as configurações da Invasão Alienígena."""
    """Inicializa as configurações do jogo"""
    def __init__(self):
        # Configurações da tela 
        self.screen_width = 800
        self.screen_height = 400
        self.bg_color = (230,230,230)
        """Configurações da espaçonave"""
        self.rocket_speed_factor = 1.5
        """Configurações dos projéteis """
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60