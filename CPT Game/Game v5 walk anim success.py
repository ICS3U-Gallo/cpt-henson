import arcade
import os

SPRITE_SCALING = 4

SCREEN_WIDTH = 896
SCREEN_HEIGHT = 672
SCREEN_TITLE = "Game"

#8, 25, 12, 14
MOVEMENT_SPEED = 8
JUMP_SPEED = 25
GRAVITY = 12
JUMP_FRAME = 14

SPRITE_CHANGE_DISTANCE = 6

JUMP_CHECK = False
JUMP_CLOCK = 0

class Player(arcade.Sprite):

    def __init__(self):
        super().__init__()
        self.side_check = 1
        self.texture_check = 0
        self.LSPRITE_TEXTURE = 0
        self.RSPRITE_TEXTURE = 2

        # 1,2   3,4
        texture = arcade.load_texture("images/CharR.png", mirrored=True, scale=SPRITE_SCALING)
        self.textures.append(texture)
        texture = arcade.load_texture("images/CharR1.png", mirrored=True, scale=SPRITE_SCALING)
        self.textures.append(texture)

        texture = arcade.load_texture("images/CharR.png", scale=SPRITE_SCALING)
        self.textures.append(texture)
        texture = arcade.load_texture("images/CharR1.png", scale=SPRITE_SCALING)
        self.textures.append(texture)

        # By default, face right.
        self.set_texture(1)
    def update(self):

        # walk animation

        if self.texture_check >= SPRITE_CHANGE_DISTANCE:
            self.LSPRITE_TEXTURE = 1
            self.RSPRITE_TEXTURE = 3
        if self.texture_check >= SPRITE_CHANGE_DISTANCE*2:
            self.texture_check = 0
        if self.texture_check <= SPRITE_CHANGE_DISTANCE:
            self.LSPRITE_TEXTURE = 0
            self.RSPRITE_TEXTURE = 2

        # movement

        if self.change_y != 0:
            if self.side_check == 0:
                self.set_texture(0)
            if self.side_check == 1:
                self.set_texture(2)

        if self.change_x < 0:
            self.side_check = 0
            if self.change_y == 0:
                self.texture_check += 1
                self.set_texture(self.LSPRITE_TEXTURE)

        if self.change_x > 0:
            self.side_check = 1
            if self.change_y == 0:
                self.texture_check += 1
                self.set_texture(self.RSPRITE_TEXTURE)

        if self.change_x == 0:
            self.texture_check = 0
            if self.side_check == 0:
                self.set_texture(1)
            if self.side_check == 1:
                self.set_texture(3)
class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Initializer
        """

        # Call the parent class initializer
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Variables that will hold sprite lists
        self.player_list = None
        self.wall_list = None

        # Set up the player info
        self.player_sprite = None
        self.physics_engine = None
        self.physics_engine = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Set the background color
        arcade.set_background_color(arcade.color.BROWN)


    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()


        # Set up the player
        self.player_sprite = Player()
        self.player_sprite.center_x = 80
        self.player_sprite.center_y = SCREEN_HEIGHT // 2
        self.player_list.append(self.player_sprite)

        # draw boxes function

        def draw_box_horizontal(start_x, end_x, y, sprite_gap, scaling):
            for x in range(start_x, end_x, sprite_gap):
                wall = arcade.Sprite("images/boxCrate_double.png", scaling)
                wall.center_x = x
                wall.center_y = y
                self.wall_list.append(wall)
        def draw_box_vertical(start_y, end_y, x, sprite_gap, scaling):
            for y in range(start_y, end_y, sprite_gap):
                wall = arcade.Sprite("images/boxCrate_double.png", scaling)
                wall.center_x = x
                wall.center_y = y
                self.wall_list.append(wall)

        # drawing map

        draw_box_horizontal(16, SCREEN_WIDTH + 32, SCREEN_HEIGHT + 16, 32, 2)
        draw_box_horizontal(16, SCREEN_WIDTH + 32, 16, 32, 2)
        draw_box_vertical(16, SCREEN_HEIGHT + 32, -16, 32, 2)
        draw_box_vertical(16, SCREEN_HEIGHT + 32, SCREEN_WIDTH + 16, 32, 2)

        draw_box_horizontal(173, 650, 150, 32, 2)

        draw_box_vertical(198, 300, 465, 64, 4)
        draw_box_vertical(350, 400, 630, 128, 8)


        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                         self.wall_list, gravity_constant= GRAVITY)


    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.player_list.draw()
        self.wall_list.draw()

    def update(self, delta_time):

        global JUMP_CHECK, JUMP_CLOCK
        """ Movement and game logic """
        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED

        if self.physics_engine.can_jump():
            if self.up_pressed:
                JUMP_CHECK = True
        if JUMP_CHECK == True:
            JUMP_CLOCK += 1
        elif JUMP_CHECK == False:
            JUMP_CLOCK = 0
            self.player_sprite.change_y = 0
        if JUMP_CLOCK > 0 and JUMP_CLOCK < JUMP_FRAME:
            self.player_sprite.change_y = JUMP_SPEED
        elif JUMP_CLOCK > JUMP_FRAME:
            JUMP_CHECK = False

        # Call update to move the sprite
        self.physics_engine.update()
        self.player_sprite.update()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.W:
            self.up_pressed = True
        elif key == arcade.key.S:
            self.down_pressed = True
        elif key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.D:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.W:
            self.up_pressed = False
        elif key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.D:
            self.right_pressed = False


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()