import pygame

class Ship:
    """Configuration for ship"""

    def __init__(self, si_game):
        """Initialize the ship at the position"""
        self.screen = si_game.screen
        self.settings = si_game.settings
        self.screen_rect = si_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load(self.settings.ship_sprite).convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 120))
        self.rect = self.image.get_rect()

        # Place ship at the bottom of the game window
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag
        self.moving_right = False
        self.moving_left = False

        # Store a decimal value for the ship's  X axis.
        self.x = float(self.rect.x)

    def update(self):
        """Update ship position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def centre_ship(self):
        """Centre ship"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

