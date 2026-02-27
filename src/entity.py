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

    def ia_patrol(self):
        # 1. Detectar si llegamos a los límites y cambiar el estado de la dirección
        if self.enemy_sprite.center_x <= self.start_x:
            self.direction = 'right'
        elif self.enemy_sprite.center_x >= self.start_x + self.patrol_range:
            self.direction = 'left'

        # 2. Aplicar la velocidad al change_x para que el motor de física lo mueva
        if self.direction == 'right':
            self.enemy_sprite.change_x = self.enemy_speed
        elif self.direction == 'left':
            self.enemy_sprite.change_x = -self.enemy_speed
        else:
            self.enemy_sprite.change_x = 0

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

class basic_enemy(enemy):
    def __init__(self):
        super().__init__()
        self.attack_texture_left = arcade.load_texture('./assets/ataque.png')
        self.attack_texture_right = self.attack_texture_left.flip_left_right()
        self.attack_sprite = arcade.Sprite(self.attack_texture_left)
        self.attack_sprite.width = 64
        self.attack_sprite.height = 64
        self.hide = True

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
            self.melee_attack(objetive)
        elif 0 >=(objetive[0] - self.enemy_sprite.center_x) and 0 - limit_objetive <=(objetive[0] - self.enemy_sprite.center_x):
            self.direction = 'left'
            self.melee_attack(objetive)
        else:
            self.ia_patrol()

    def melee_attack(self, objetive):
        distancia_x = objetive[0] - self.enemy_sprite.center_x

        if abs(distancia_x) <= 100:
            self.hide = True
            self.attack_sprite.center_y = self.enemy_sprite.center_y

            if distancia_x > 0: # El jugador está a la derecha
                self.attack_sprite.texture = self.attack_texture_left
                self.attack_sprite.center_x = self.enemy_sprite.center_x + 40
            else: # El jugador está a la izquierda
                self.attack_sprite.texture = self.attack_texture_right
                self.attack_sprite.center_x = self.enemy_sprite.center_x - 40
        else:
            self.hide = False


class ranged_enemy(enemy):
    def __init__(self):
        super().__init__()
        """Enemigo específico que ataca a distancia."""
        # Atributos específicos de ataque a distancia
        self.bullet_list = arcade.SpriteList()
        self.bullet_speed = 5
        self.shoot_cooldown = 1.5
        self.last_shoot_time = 0

        # Texturas para el proyectil
        self.bullet_texture_right = arcade.load_texture('./assets/ataque.png')
        self.bullet_texture_left = self.bullet_texture_right.flip_left_right()

    def ia_ranged_logic(self, player_pos):
        """Lógica de disparo y movimiento específica."""
        distancia_x = player_pos[0] - self.enemy_sprite.center_x
        current_time = time.time()

        # Lógica de disparo
        if 100 < abs(distancia_x) < 500:
            if current_time - self.last_shoot_time > self.shoot_cooldown:
                self.shoot(distancia_x)
                self.last_shoot_time = current_time

        # Actualizar proyectiles
        self.bullet_list.update()

    def shoot(self, direction_x):
        """Crea el objeto proyectil."""
        bullet = arcade.Sprite()
        bullet.scale = 0.2
        bullet.center_y = self.enemy_sprite.center_y

        if direction_x > 0:
            bullet.texture = self.bullet_texture_right
            bullet.center_x = self.enemy_sprite.center_x + 50
            bullet.change_x = self.bullet_speed
        else:
            bullet.texture = self.bullet_texture_left
            bullet.center_x = self.enemy_sprite.center_x - 50
            bullet.change_x = -self.bullet_speed

        self.bullet_list.append(bullet)

class air_enemy(enemy):
    def __init__(self):
        super().__init__()

class strong_basic_enemy(basic_enemy):
    def __init__(self):
        super().__init__()
