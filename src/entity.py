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

        self.enemy_speed = 2
        self.patrol_range = 200
        self.start_x = 300

        self.attack_texture = './assets/ataque.png'
        self.attack_sprite = arcade.Sprite(self.attack_texture)
        self.attack_sprite.width = 64
        self.attack_sprite.height = 64
        self.hide = True

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

    def ia_persuit(self,objetive):
        #objetive posicion del jugador (x y)
        limit_objetive = 300
        move = {
            'left':-self.enemy_speed,
            'right':self.enemy_speed,
            'stop': 0
        }

        self.enemy_sprite.center_x += move[self.direction]

        if 0 <=(objetive[0] - self.enemy_sprite.center_x) and 0 + limit_objetive >= (objetive[0] - self.enemy_sprite.center_x):
            self.direction = 'right'
        elif 0 >=(objetive[0] - self.enemy_sprite.center_x) and 0 - limit_objetive <=(objetive[0] - self.enemy_sprite.center_x):
            self.direction = 'left'
        else:
            self.direction = 'stop'

    def ia_basic(self,objetive):
        limit_objetive = 300
        move = {
            'left':-self.enemy_speed,
            'right':self.enemy_speed,
            'stop': 0
        }

        self.enemy_sprite.center_x += move[self.direction]

        if 0 <=(objetive[0] - self.enemy_sprite.center_x) and 0 + limit_objetive >= (objetive[0] - self.enemy_sprite.center_x):
            self.direction = 'right'
            self.ia_attack(objetive)
        elif 0 >=(objetive[0] - self.enemy_sprite.center_x) and 0 - limit_objetive <=(objetive[0] - self.enemy_sprite.center_x):
            self.direction = 'left'
            self.ia_attack(objetive)
        else:
            self.ia_patrol()

    def ia_attack(self,objetive):
        self.attack_sprite.angle = 0
        distancia_x = objetive[0] - self.enemy_sprite.center_x

        if abs(distancia_x) <= 100:
            self.hide = True
            self.attack_sprite.center_y = self.enemy_sprite.center_y

            if distancia_x > 0: # Derecha
                self.attack_sprite.scale = 0.4
                self.attack_sprite.center_x = self.enemy_sprite.center_x + 40
            else: # Izquierda
                self.attack_sprite.scale = -0.4
                self.attack_sprite.center_x = self.enemy_sprite.center_x - 40
        else:
            self.hide = False
        self.attack_sprite.update()
