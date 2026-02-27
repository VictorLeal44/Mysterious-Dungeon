import arcade
import src
import threading
# ... constantes igual ...

class GameView(arcade.Window):
    def __init__(self):
        super().__init__(1280, 720, "Mysterious Dungeon")
        self.background_color = arcade.csscolor.DARK_GRAY

        self.camera = arcade.Camera2D()
        self.player = src.player()
        self.enemy = src.basic_enemy()
        self.ranged_enemy = src.ranged_enemy()
        self.world_generation = src.world_generation()
        self.world_generation.only_floor()

        self.GRAVITY = 1
        self.PLAYER_JUMP_SPEED = 20
        self.PLAYER_MOVEMENT_SPEED = 5

        self.key_stack = []

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player.player_sprite,
            self.world_generation.wall_list,
            gravity_constant=self.GRAVITY
        )

        self.enemy_physics_engine = arcade.PhysicsEnginePlatformer(
            self.enemy.enemy_sprite,
            self.world_generation.wall_list,
            gravity_constant=self.GRAVITY
        )
        self.ranged_enemy_physics_engine = arcade.PhysicsEnginePlatformer(
            self.ranged_enemy.enemy_sprite,
            self.world_generation.wall_list,
            gravity_constant=self.GRAVITY
        )

    def update_player_speed(self):
        """Usa la última tecla de la lista para decidir la dirección."""
        if self.key_stack:
            last_key = self.key_stack[-1] # Miramos la última tecla presionada
            if last_key == arcade.key.LEFT or last_key == arcade.key.A:
                self.player.player_sprite.change_x = -self.PLAYER_MOVEMENT_SPEED
            elif last_key == arcade.key.RIGHT or last_key == arcade.key.D:
                self.player.player_sprite.change_x = self.PLAYER_MOVEMENT_SPEED
        else:
            self.player.player_sprite.change_x = 0

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player.player_sprite.change_y = self.PLAYER_JUMP_SPEED

        # Si presionamos una tecla de dirección, la añadimos a la pila
        elif key in (arcade.key.LEFT, arcade.key.A, arcade.key.RIGHT, arcade.key.D):
            if key not in self.key_stack:
                self.key_stack.append(key)
            self.update_player_speed()

    def on_key_release(self, key, modifiers):
        # Al soltar, la quitamos de la pila
        if key in (arcade.key.LEFT, arcade.key.A, arcade.key.RIGHT, arcade.key.D):
            if key in self.key_stack:
                self.key_stack.remove(key)
            self.update_player_speed()

    def on_update(self, delta_time):
        self.physics_engine.update()
        self.enemy_physics_engine.update()
        self.ranged_enemy_physics_engine.update()
        #self.enemy.ia_patrol()
        #self.enemy.ia_persuit(self.player.player_sprite.position)
        self.enemy.ia_basic(self.player.player_sprite.position)
        self.ranged_enemy.ia_ranged_logic(self.player.player_sprite.position)
        self.camera.position = self.player.player_sprite.position

    def on_draw(self):
        self.clear()
        self.camera.use()
        self.world_generation.wall_list.draw()
        arcade.draw_sprite(self.enemy.enemy_sprite)
        arcade.draw_sprite(self.player.player_sprite)
        arcade.draw_sprite(self.ranged_enemy.enemy_sprite)
        if self.enemy.hide == True:
            arcade.draw_sprite(self.enemy.attack_sprite)

if __name__ == "__main__":
    game = GameView()
    arcade.run()
