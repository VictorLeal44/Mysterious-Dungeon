import arcade
import polars
from src import blocks

class world_generation:
    def __init__(self):
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.y, self.x = 720, 1280
        #27
    def only_floor(self):
        for x in range(0, 1250, 64):
            wall = blocks.blocks(64,x,32)
            self.wall_list.append(wall.block_sprite)
#arcade.draw_sprite(self.player.player_sprite)
