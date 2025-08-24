

class GameStats:
    """Track statistics for Space Invaders"""

    def __init__(self, si_game):
        """Initialize stats"""
        self.setings = si_game.settings
        self.reset_stats()
        # Start game with active state
        self.game_active = True

    def reset_stats(self):
        """Initialize stats that can change during the game"""
        self.ships_left = self.setings.ship_limit
