import arcade
import time

class player:
    def __init__(self):
        self.player_texture = './assets/folder.png'
        self.player_sprite = arcade.Sprite(self.player_texture)
        self.player_sprite.width = 132
        self.player_sprite.height = 132
        self.player_sprite.center_x = 128
        self.player_sprite.center_y = 128

class enemy:
    def __init__(self):
        self.enemy_texture = './assets/slime.png'
        self.enemy_sprite = arcade.Sprite(self.enemy_texture)
        self.enemy_sprite.width = 132
        self.enemy_sprite.height = 132
        self.enemy_sprite.center_x = 300
        self.enemy_sprite.center_y = 328
        self.direction = 'left'

        self.enemy_speed = 4
        self.patrol_range = 200
        self.start_x = 300

    def ia_patrol(self):
        move = {
            'left':-self.enemy_speed,
            'right':self.enemy_speed,
        }

        self.enemy_sprite.center_x += move[self.direction]

        if self.enemy_sprite.center_x <= self.start_x:
            #print(self.enemy_sprite.center_x,'<',self.start_x,'izquierda')
            self.direction = 'right'
        elif self.enemy_sprite.center_x >= self.start_x + self.patrol_range:
            #print(self.enemy_sprite.center_x,'>',self.start_x+self.patrol_range,'derecha')
            self.direction = 'left'
