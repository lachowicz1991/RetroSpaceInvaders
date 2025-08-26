class Settings:
    def __init__(self):
        """Settings for the game"""
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (74, 13, 74)
        self.bg_art = 'resources/images/background2.png'
        # Ship Settings
        self.ship_speed = 1.5
        self.ship_sprite = 'resources/images/space_ship.png'
        self.ship_limit = 1


        # Bullet settings
        self.bullet_speed = 4
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (149, 255, 0)
        self.bullet_limit = 5

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 100
        # fleet_direction of 1 represents right, -1 left.
        self.fleet_direction = 1




