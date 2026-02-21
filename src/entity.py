import arcade

class player:

    def __init__(self):
        self.player_texture = './assets/folder.png'
        self.player_sprite = arcade.Sprite(self.player_texture)
        self.player_sprite.width = 132
        self.player_sprite.height = 132
        self.player_sprite.center_x = 128
        self.player_sprite.center_y = 128

#    def on_key_release(self, key, modifiers):
#        """Called whenever a key is released."""
#
#        if key == arcade.key.UP or key == arcade.key.W:
#            self.player_sprite.change_y = 0
#        elif key == arcade.key.DOWN or key == arcade.key.S:
#            self.player_sprite.change_y = 0
#        elif key == arcade.key.LEFT or key == arcade.key.A:
#            self.player_sprite.change_x = 0
#        elif key == arcade.key.RIGHT or key == arcade.key.D:
#            self.player_sprite.change_x = 0
