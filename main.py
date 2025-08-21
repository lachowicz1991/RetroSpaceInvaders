import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from sfx import Sound_Manager

class SpaceInvaders:
    """Main class for the game"""

    def __init__(self):
        """Initialize the game and create resources"""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Space Invaders")
        self.background = pygame.image.load(self.settings.bg_art).convert()
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.sfx = Sound_Manager(self)

    def run_game(self):
        """Start the main loop of the game."""

        self.screen.blit(self.background, (0, 0))
        self.sfx.play_main_theme()
        self.sfx.play_ship_sound()

        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._screen_update()

            # Remove redundant bullets.
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            print(len(self.bullets))

    def _check_events(self):
        """Watch for keyboad and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Handles key presses"""
        if event.key == pygame.K_RIGHT:
            # Move ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move ship to the left
            self.ship.moving_left = True

        elif event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Handles key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullet group"""
        if len(self.bullets) < self.settings.bullet_limit:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.sfx.play_bullet_sound()


    def _screen_update(self):
        """Updates the screen and flips to the new one"""
        # Redraw the screen during each pass through the loop.
        # self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.background, (0, 0))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Make the most recently drawn screen visible.
        pygame.display.flip()



if __name__ == '__main__':
    # Make a game instance, and run the game
    si = SpaceInvaders()
    si.run_game()
