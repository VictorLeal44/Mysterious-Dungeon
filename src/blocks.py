import arcade


class blocks:
    def __init__(self, size, x, y):
        self.block_texture = './assets/suelo.jpg'
        self.block_sprite = arcade.Sprite(self.block_texture)
        self.block_sprite.width = size #48 es el numero base
        self.block_sprite.height = size
        self.block_sprite.center_x = x
        self.block_sprite.center_y = y

class EventZone:
    def __init__(self, x, y, width, height, event_type="trap"):
        # Usamos un sprite invisible o un marcador para debug
        self.sprite = arcade.SpriteSolidColor(width, height, arcade.color.TRANSPARENT)
        self.sprite.center_x = x
        self.sprite.center_y = y
        self.event_type = event_type
        self.activated = False
