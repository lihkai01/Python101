class Settings:
    """A class to store all setting for Alien Invasion."""

    def __init__(self):
        # Screen Settings
        self.screen_width  = 1200
        self.screen_height = 600
        self.bg_color = (230,230,230)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 0.5
        self.bullet_width = 3
        self.bullet_height = 5
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3