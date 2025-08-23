import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from sfx import Sound_Manager
from alien import Alien

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
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
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

    def _create_fleet(self):
        """Creates hostile fleet"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        avalible_space_x = self.settings.screen_width - (2 * alien_width)
        number_alien_x = avalible_space_x // (2 * alien_width)

        ship_height = self.ship.rect.height
        avalible_space_y = (self.settings.screen_height - (3*alien_height) - ship_height)
        number_rows = avalible_space_y // (2 * alien_height)

        # Create the first row of aliens
        for r in range(number_rows):
            for alien_number in range(number_alien_x):
                self._create_alien(alien_number, r)

    def _screen_update(self):
        """Updates the screen and flips to the new one"""
        # Redraw the screen during each pass through the loop.
        # self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.background, (0, 0))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)


if __name__ == '__main__':
    # Make a game instance, and run the game
    si = SpaceInvaders()
    si.run_game()
