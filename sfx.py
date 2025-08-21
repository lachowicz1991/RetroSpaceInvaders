import pygame

class Sound_Manager():
    """A class to manage audio"""
    def __init__(self, si_game):
        pygame.mixer.init()
        self.settings = si_game.settings

        # Audio files
        self.main_theme = 'resources/audio/main.mp3'
        self.bullet_sound = 'resources/audio/shot.mp3'
        self.ship_sound = 'resources/audio/ship_sound.mp3'

    def play_bullet_sound(self):
        """ sound effect for the ship weapons"""
        bullet_sound = pygame.mixer.Sound(self.bullet_sound)
        bullet_sound.play()

    def play_main_theme(self):
        """ plays main background theme """
        pygame.mixer.music.load(self.main_theme)
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)

    def play_ship_sound(self):
        """ sound effect for the ship engine """
        play_sound = pygame.mixer.Sound(self.ship_sound)
        play_sound.play(-1)