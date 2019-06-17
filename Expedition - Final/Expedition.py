import arcade
import os
import random
import time
import math

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 512
SCREEN_TITLE = "Game"
FPS = 0

LEFT_VIEWPORT_MARGIN = 300
RIGHT_VIEWPORT_MARGIN = 400
BOTTOM_VIEWPORT_MARGIN = 75
TOP_VIEWPORT_MARGIN = 200
shake = False
shakevalue = 0
shakevalue1 = 0
perm_shakevalue = 0
perm_shakevalue1 = 0
start = False
pause = False
win = False

#8, 25, 12, 14
RIGHT_MOVE = False
LEFT_MOVE = False
MOVEMENT_SPEED = 8
JUMP_SPEED = 20
GRAVITY = 10
JUMP_FRAME = 14

SPRITE_CHANGE_DISTANCE = 7

JUMP_gCHECK = 3
JUMP_gCLOCK = 0
JUMP_CHECK = False
JUMP_CLOCK = 0

ammo1 = 40
ammo2 = 0
ammo3 = 0
ammo = 1
empty = False
loadout = 1
recoil = 0

clock = 0
fire_check = True
firerate_clock = 0


class Player(arcade.Sprite):

    def __init__(self):
        super().__init__()
        self.side_check = 1
        self.texture_check = 0
        self.LSPRITE_TEXTURE = 0
        self.RSPRITE_TEXTURE = 2
        self.health = 5
        # player_0 standing
        # player_1 leg up1
        # player_2 leg up2

        # gun 1, 0-5
        texture = arcade.load_texture("images/player_0.png", mirrored=True, scale=SPRITE_SCALING)
        self.textures.append(texture)
        texture = arcade.load_texture("images/player_1.png", mirrored=True, scale=SPRITE_SCALING)
        self.textures.append(texture)
        texture = arcade.load_texture("images/player_2.png", mirrored=True, scale=SPRITE_SCALING)
        self.textures.append(texture)
        texture = arcade.load_texture("images/player_0.png", scale=SPRITE_SCALING)
        self.textures.append(texture)
        texture = arcade.load_texture("images/player_1.png", scale=SPRITE_SCALING)
        self.textures.append(texture)
        texture = arcade.load_texture("images/player_2.png", scale=SPRITE_SCALING)
        self.textures.append(texture)
        # gun 2. 6-11
        texture = arcade.load_texture("images/playerRED_0.png", mirrored=True, scale=SPRITE_SCALING)
        self.textures.append(texture)
        texture = arcade.load_texture("images/playerRED_1.png", mirrored=True, scale=SPRITE_SCALING)
        self.textures.append(texture)
        texture = arcade.load_texture("images/playerRED_2.png", mirrored=True, scale=SPRITE_SCALING)
        self.textures.append(texture)
        texture = arcade.load_texture("images/playerRED_0.png", scale=SPRITE_SCALING)
        self.textures.append(texture)
        texture = arcade.load_texture("images/playerRED_1.png", scale=SPRITE_SCALING)
        self.textures.append(texture)
        texture = arcade.load_texture("images/playerRED_2.png", scale=SPRITE_SCALING)
        self.textures.append(texture)
        # gun 3. 12-17
        texture = arcade.load_texture("images/playerBROWN_0.png", mirrored=True, scale=SPRITE_SCALING)
        self.textures.append(texture)
        texture = arcade.load_texture("images/playerBROWN_1.png", mirrored=True, scale=SPRITE_SCALING)
        self.textures.append(texture)
        texture = arcade.load_texture("images/playerBROWN_2.png", mirrored=True, scale=SPRITE_SCALING)
        self.textures.append(texture)
        texture = arcade.load_texture("images/playerBROWN_0.png", scale=SPRITE_SCALING)
        self.textures.append(texture)
        texture = arcade.load_texture("images/playerBROWN_1.png", scale=SPRITE_SCALING)
        self.textures.append(texture)
        texture = arcade.load_texture("images/playerBROWN_2.png", scale=SPRITE_SCALING)
        self.textures.append(texture)
        # By default, face right.
        self.set_texture(3)

    def update(self):
        global RIGHT_MOVE, LEFT_MOVE
        # walk animation

        if self.texture_check <= SPRITE_CHANGE_DISTANCE:
            if loadout == 1:
                self.LSPRITE_TEXTURE = 1
                self.RSPRITE_TEXTURE = 4
            if loadout == 2:
                self.LSPRITE_TEXTURE = 7
                self.RSPRITE_TEXTURE = 10
            if loadout == 3:
                self.LSPRITE_TEXTURE = 13
                self.RSPRITE_TEXTURE = 16
        if self.texture_check >= SPRITE_CHANGE_DISTANCE:
            if loadout == 1:
                self.LSPRITE_TEXTURE = 0
                self.RSPRITE_TEXTURE = 3
            if loadout == 2:
                self.LSPRITE_TEXTURE = 6
                self.RSPRITE_TEXTURE = 9
            if loadout == 3:
                self.LSPRITE_TEXTURE = 12
                self.RSPRITE_TEXTURE = 15
        if self.texture_check >= SPRITE_CHANGE_DISTANCE*2:
            if loadout == 1:
                self.LSPRITE_TEXTURE = 2
                self.RSPRITE_TEXTURE = 5
            if loadout == 2:
                self.LSPRITE_TEXTURE = 8
                self.RSPRITE_TEXTURE = 11
            if loadout == 3:
                self.LSPRITE_TEXTURE = 14
                self.RSPRITE_TEXTURE = 17
        if self.texture_check >= SPRITE_CHANGE_DISTANCE*3:
            if loadout == 1:
                self.LSPRITE_TEXTURE = 0
                self.RSPRITE_TEXTURE = 3
            if loadout == 2:
                self.LSPRITE_TEXTURE = 6
                self.RSPRITE_TEXTURE = 9
            if loadout == 3:
                self.LSPRITE_TEXTURE = 12
                self.RSPRITE_TEXTURE = 15
        if self.texture_check >= SPRITE_CHANGE_DISTANCE*4:
            self.texture_check = 0

        # movement

        if LEFT_MOVE is True:
            self.side_check = 0
            if self.change_y == 0:
                self.texture_check += 1
                self.set_texture(self.LSPRITE_TEXTURE)

        if RIGHT_MOVE is True:
            self.side_check = 1
            if self.change_y == 0:
                self.texture_check += 1
                self.set_texture(self.RSPRITE_TEXTURE)

        if self.change_x == 0 or self.change_y != 0:
            self.texture_check = 0
            if self.side_check == 0:
                if loadout == 1:
                    self.set_texture(0)
                if loadout == 2:
                    self.set_texture(6)
                if loadout == 3:
                    self.set_texture(12)
            if self.side_check == 1:
                if loadout == 1:
                    self.set_texture(3)
                if loadout == 2:
                    self.set_texture(9)
                if loadout == 3:
                    self.set_texture(15)


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

        self.player_list = None
        self.wall_list = None
        self.bullet_list = None
        self.enemy_list = None
        self.enemy_bullet_list = None
        self.pickup_list = None
        self.toxin = None
        self.boss_list = None
        self.boss_bullet_list = None

        self.player_sprite = None
        self.physics_engine = None
        self.konami = False

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.p_pressed = False
        self.m_pressed = False

        self.arrow_up_pressed = False
        self.arrow_down_pressed = False
        self.arrow_left_pressed = False
        self.arrow_right_pressed = False
        self.A_pressed = False
        self.B_pressed = False

        self.view_bottom = 0
        self.view_left = 0

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        global ammo1, ammo2, ammo3
        """ Set up the game and initialize the variables. """
        self.background = arcade.load_texture("images/background.png", scale=0.5)
        self.background1 = arcade.load_texture("images/background1.png", scale=0.5)
        self.title = arcade.load_texture("images/title.png")

        self.red_texture = arcade.load_texture("images/gun_0.png")
        self.red_texture1 = arcade.load_texture("images/gun_1.png")
        self.red_texture2 = arcade.load_texture("images/gun_0.png", mirrored=True)
        self.red_texture3 = arcade.load_texture("images/gun_1.png", mirrored=True)
        self.brown_texture = arcade.load_texture("images/gunBrown_0.png")
        self.brown_texture1 = arcade.load_texture("images/gunBrown_1.png")
        self.brown_texture2 = arcade.load_texture("images/gunBrown_0.png", mirrored=True)
        self.brown_texture3 = arcade.load_texture("images/gunBrown_1.png", mirrored=True)

        self.enemy_gun = arcade.load_texture("images/tank_1.png")
        self.boss_gun = arcade.load_texture("images/boss_1.png")

        self.hp = []
        self.hp.append(arcade.load_texture("images/dead.png"))
        self.hp.append(arcade.load_texture("images/hp_4.png"))
        self.hp.append(arcade.load_texture("images/hp_3.png"))
        self.hp.append(arcade.load_texture("images/hp_2.png"))
        self.hp.append(arcade.load_texture("images/hp_1.png"))
        self.hp.append(arcade.load_texture("images/hp_0.png"))
        self.god = arcade.load_texture("images/god.png")

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.enemy_bullet_list = arcade.SpriteList()
        self.pickup_list = arcade.SpriteList()
        self.toxin_list = arcade.SpriteList()
        self.boss_list = arcade.SpriteList()
        self.boss_bullet_list = arcade.SpriteList()

        self.player_sprite = Player()
        self.player_sprite.center_x = 80
        self.player_sprite.center_y = SCREEN_HEIGHT // 2
        self.player_list.append(self.player_sprite)
        self.view_left = 0
        self.view_bottom = 0

        ammo1 = 40
        ammo2 = 0
        ammo3 = 0
        # draw boxes function

        def draw_box_horizontal(type, start_x, num, y, scaling):
            if type == -1:
                wall_sprite = "images/boxFloor.png"
            if type == 0:
                wall_sprite = "images/blank128x128.png"
            if type == 1:
                wall_sprite = "images/platform.png"
            if type == 2:
                wall_sprite = "images/box.png"
            if type == 3:
                wall_sprite = "images/frame.png"
            for x in range(start_x, start_x+num*int(128*scaling), int(128*scaling)):
                wall = arcade.Sprite(wall_sprite, scaling)
                if type == 4:
                    wall.death = True
                wall.center_x = x
                wall.center_y = y
                self.wall_list.append(wall)

        def draw_box_vertical(type, start_y, num, x, scaling):
            if type == 0:
                wall_sprite = "images/blank128x128.png"
            if type == 1:
                wall_sprite = "images/platform.png"
            if type == 2:
                wall_sprite = "images/box.png"
            if type == 3:
                wall_sprite = "images/frame.png"
            for y in range(start_y, start_y+num*int(128*scaling), int(128*scaling)):
                wall = arcade.Sprite(wall_sprite, scaling)
                wall.center_x = x
                wall.center_y = y
                self.wall_list.append(wall)

        def pickup_spawn(type, x, y, amount):
            if type == 0:
                pickup = arcade.Sprite("images/heart.png", 0.5)
            if type == 1:
                pickup = arcade.Sprite("images/ammo_0.png", 1.5)
            if type == 2:
                pickup = arcade.Sprite("images/ammo_1.png", 1.5)
            if type == 3:
                pickup = arcade.Sprite("images/ammo_2.png", 1.5)
            pickup.type = type
            pickup.center_y = y
            pickup.center_x = x
            pickup.amount = amount
            self.pickup_list.append(pickup)

        def toxin_spawn(start_x, num, y, scaling):
            for x in range(start_x, start_x+num*int(128*scaling), int(128*scaling)):
                toxin = arcade.Sprite("images/toxin.png", scaling)
                toxin.center_x = x
                toxin.center_y = y
                self.toxin_list.append(toxin)

        def enemy_spawn(x, y, start_x, end_x, stationary, detection_range):
            enemy = arcade.Sprite('images/tank_0.png')
            if stationary is True:
                enemy.change_x = 0
            else:
                enemy.change_x = 1
            enemy.boundary_left = start_x
            enemy.boundary_right = end_x
            enemy.bottom = y + 32
            enemy.left = x
            enemy.clock = 0
            enemy.health = 10
            enemy.gun_angle = 90
            enemy.detection_range = detection_range
            self.enemy_list.append(enemy)

        # drawing map
        draw_box_horizontal(-1, -640, 400, 16 - 28*2, 1 / 4)
        draw_box_horizontal(-1, -640-16, 400, 16 - 28, 1/4)
        draw_box_horizontal(-1, -640, 400, 16, 1 / 4)
        draw_box_vertical(0, 1, 50, -256, 1/4)

        enemy_spawn(580, 412, None, None, True, 600)
        pickup_spawn(2, 700, 460, 5)

        draw_box_horizontal(1, 173, 20, 140, 3/16)
        pickup_spawn(1, 1060, 48, 50)

        draw_box_vertical(2, 184, 2, 465, 1/2)
        draw_box_vertical(2, 380, 1, 630, 1)
        draw_box_horizontal(1, 758-48, 2, 380+48, 1/4)

        draw_box_horizontal(3, 792+48, 1, 300, 1/4)
        draw_box_horizontal(1, 806, 6, 180, 1/4)

        enemy_spawn(1300, 192, 1170, 1420, False, 400)

        draw_box_horizontal(2, 1200, 2, 64, 1/2)
        draw_box_horizontal(2, 1200, 1, 128, 1 / 2)
        draw_box_horizontal(3, 1264, 1, 128, 1 / 2)
        draw_box_horizontal(2, 1200, 1, 192, 1 / 2)
        draw_box_horizontal(2, 1264, 3, 192, 1 / 2)
        draw_box_horizontal(1, 1296+8, 8, 192-40, 1/8)
        draw_box_horizontal(2, 1264+64*5, 1, 128, 1 / 2)
        draw_box_horizontal(1, 1584 - 24, 4, 40, 1/8)
        draw_box_horizontal(1, 1584 - 24, 4, 40+3*16, 1 / 8)
        draw_box_horizontal(2, 1560 + 160, 1, 44, 3/16)

        enemy_spawn(1400, 0, None, None, True, 450)
        pickup_spawn(2, 1325, 48, 10)
        pickup_spawn(0, 1950, 200, 0)

        draw_box_horizontal(1, 2500-64-32, 1, 48, 1/4)
        draw_box_horizontal(2, 2500-48, 1, 64, 1/2)
        toxin_spawn(2500, 6, 48, 1/4)

        draw_box_vertical(2, 48, 2, 3200, 1/4)
        draw_box_horizontal(3, 3360, 1, 140, 1/4)
        draw_box_horizontal(3, 3360+192, 1, 140, 1 / 4)
        draw_box_horizontal(3, 3360 + 192*2, 1, 140, 1 / 4)
        draw_box_horizontal(3, 3360 + 192*3, 1, 140, 1 / 4)
        draw_box_horizontal(3, 3360 + 192*4, 1, 140, 1 / 4)
        pickup_spawn(3, 4128, 400, 100)
        draw_box_horizontal(3, 4256, 1, 200, 1 / 4)

        enemy_spawn(3300, 0, None, None, False, 600)
        enemy_spawn(3780, 0, None, None, True, 600)
        enemy_spawn(3780, 0, None, None, False, 600)
        enemy_spawn(4380-128, 0, None, None, False, 400)
        draw_box_vertical(2, 40, 1, 4380, 1/8)

        draw_box_horizontal(1, 4890, 20, 140, 3/16)
        toxin_spawn(4980, 2, 164, 3/16)
        toxin_spawn(4980, 2, 164+24, 3 / 16)
        pickup_spawn(0, 5100, 170, None)
        toxin_spawn(5250, 3, 164, 3/16)
        enemy_spawn(5000, 0, None, None, True, 500)
        enemy_spawn(5512, 0, None, None, True, 500)
        pickup_spawn(2, 5930, 64, 20)

        boss = arcade.Sprite("images/boss_0.png")
        boss.bottom = 32
        boss.left = 7000
        boss.change_x = 0
        boss.health = 150
        boss.gun_angle = 180
        boss.clock = 0
        boss.random_clock = 0
        self.boss_list.append(boss)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                         self.wall_list, gravity_constant=GRAVITY)

    def on_draw(self):
        global FPS
        """
        Render the screen.
        """
        def loadout_texture_fix(num, texture0, texture1, texture2, texture3):
            if loadout == num:
                if pause is False:
                    if self.player_sprite.side_check == 1:
                        if self.player_sprite.RSPRITE_TEXTURE % 6 - 3 == 0 or RIGHT_MOVE is False:
                            arcade.draw_texture_rectangle(self.player_sprite.center_x + 9, self.player_sprite.center_y, 66,
                                                          63, texture0)
                        else:
                            arcade.draw_texture_rectangle(self.player_sprite.center_x + 9, self.player_sprite.center_y, 66,
                                                          63, texture1)
                    if self.player_sprite.side_check == 0:
                        if self.player_sprite.LSPRITE_TEXTURE % 6 == 0 or LEFT_MOVE is False:
                            arcade.draw_texture_rectangle(self.player_sprite.center_x - 9, self.player_sprite.center_y, 66,
                                                          63, texture2)
                        else:
                            arcade.draw_texture_rectangle(self.player_sprite.center_x - 9, self.player_sprite.center_y, 66,
                                                          63, texture3)

        arcade.start_render()
        if start is False:
            if self.konami is False:
                arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.title)
                arcade.draw_text("Press 'M' to start, 'N' to pause", SCREEN_WIDTH/6, SCREEN_HEIGHT/2 -
                                 60, arcade.color.WHITE, 30)
                arcade.draw_text("'WAS' for movement", SCREEN_WIDTH / 6,
                                 SCREEN_HEIGHT / 2 - 105,
                                 arcade.color.WHITE, 30)
                arcade.draw_text("'123' to switch weapons", SCREEN_WIDTH / 6,
                                 SCREEN_HEIGHT / 2 - 150,
                                 arcade.color.WHITE, 30)
                arcade.draw_text("'P' to shoot", SCREEN_WIDTH / 6,
                                 SCREEN_HEIGHT / 2 - 195,
                                 arcade.color.WHITE, 30)
            if self.konami is True:
                arcade.draw_text('Cheats Enabled', SCREEN_WIDTH / 6 + self.view_left + perm_shakevalue,
                                 SCREEN_HEIGHT / 2 + self.view_bottom + perm_shakevalue1, arcade.color.RED, 70)
                arcade.draw_text("Infinite ammo", SCREEN_WIDTH / 6 + self.view_left + perm_shakevalue1/1.5,
                                 SCREEN_HEIGHT / 2 - 55 + self.view_bottom + perm_shakevalue/1.5,
                                 arcade.color.RED, 30)
                arcade.draw_text("God mode", SCREEN_WIDTH / 6 + self.view_left + perm_shakevalue1 / 1.5,
                                 SCREEN_HEIGHT / 2 - 55 - 55 + self.view_bottom + perm_shakevalue / 1.5,
                                 arcade.color.RED, 30)
                self.player_sprite.health = 999999999

        if start is True and self.player_sprite.center_x < 7500:
            arcade.draw_xywh_rectangle_textured(-64 + self.view_left/1.1, 0 + self.view_bottom/1.05, 1024, 512,
                                                self.background)
            arcade.draw_xywh_rectangle_textured(-64 + 1024 + self.view_left / 1.1, 0 + self.view_bottom / 1.05, 1024, 512,
                                                self.background)
            arcade.draw_xywh_rectangle_textured(-64 + 1024*2 + self.view_left / 1.1, 0 + self.view_bottom / 1.05, 1024,
                                                512,
                                                self.background)
            arcade.draw_xywh_rectangle_textured(-268 + self.view_left / 2, -32 + self.view_bottom/1.5, 2048,
                                                512-64, self.background1)
            arcade.draw_xywh_rectangle_textured(-268 + 2048 + self.view_left / 2, -32 + self.view_bottom / 1.5, 2048,
                                                512 - 64, self.background1)
            arcade.draw_xywh_rectangle_textured(-268 + 2048*2 + self.view_left / 2, -32 + self.view_bottom / 1.5, 2048,
                                                512 - 64, self.background1)
            self.bullet_list.draw()
            self.enemy_bullet_list.draw()
            for enemy in self.enemy_list:
                arcade.draw_texture_rectangle(enemy.center_x, enemy.center_y, 76, 76, self.enemy_gun, enemy.gun_angle)
                arcade.draw_rectangle_filled(enemy.center_x, enemy.center_y+32, 5*enemy.health, 4, arcade.color.GREEN)
            for boss in self.boss_list:
                arcade.draw_texture_rectangle(boss.center_x, boss.center_y, 152, 152, self.boss_gun, boss.gun_angle)
                arcade.draw_rectangle_filled(boss.center_x, boss.center_y+64, 1.5*boss.health, 7, arcade.color.RED)

            self.enemy_list.draw()
            self.player_list.draw()
            self.wall_list.draw()
            self.toxin_list.draw()
            self.pickup_list.draw()
            self.boss_list.draw()
            if pause is False and self.player_sprite.health > 0:
                loadout_texture_fix(2, self.red_texture, self.red_texture1, self.red_texture2, self.red_texture3)
                loadout_texture_fix(3, self.brown_texture, self.brown_texture1, self.brown_texture2, self.brown_texture3)
                arcade.draw_text(str(FPS), SCREEN_WIDTH - 40 + self.view_left, SCREEN_HEIGHT - 30 +
                                 self.view_bottom, arcade.color.GREEN, 20)
            if pause is True:
                arcade.draw_xywh_rectangle_textured(-64 + self.view_left / 1.1, 0 + self.view_bottom / 1.05, 1024, 512,
                                                    self.background)
                arcade.draw_xywh_rectangle_textured(-64 + 1024 + self.view_left / 1.1, 0 + self.view_bottom / 1.05,
                                                    1024, 512,
                                                    self.background)
                arcade.draw_xywh_rectangle_textured(-268 + self.view_left / 2, -32 + self.view_bottom / 1.5, 2048,
                                                    512 - 64, self.background1, alpha=70)
                arcade.draw_xywh_rectangle_textured(-268 + 2048 + self.view_left / 2, -32 + self.view_bottom / 1.5,
                                                    2048,
                                                    512 - 64, self.background1, alpha=70)

                arcade.draw_text("PAUSED", SCREEN_WIDTH/2.5+self.view_left, SCREEN_HEIGHT/2+self.view_bottom, arcade.color.WHITE, 50)
                arcade.draw_text("'M' to restart", SCREEN_WIDTH / 2.5 + self.view_left, SCREEN_HEIGHT / 2 + self.view_bottom - 30,
                                 arcade.color.WHITE, 20)
            if self.player_sprite.health <= 0:
                arcade.draw_xywh_rectangle_textured(-64 + self.view_left / 1.1, 0 + self.view_bottom / 1.05, 1024, 512,
                                                    self.background, alpha=200)
                arcade.draw_xywh_rectangle_textured(-64 + 1024 + self.view_left / 1.1, 0 + self.view_bottom / 1.05,
                                                    1024, 512,
                                                    self.background, alpha=200)
                arcade.draw_text("YOU DIED", SCREEN_WIDTH / 2.5 + self.view_left, SCREEN_HEIGHT / 2 + self.view_bottom,
                                 arcade.color.WHITE, 50)
                arcade.draw_text("'M' to restart", SCREEN_WIDTH / 2.5 + self.view_left,
                                 SCREEN_HEIGHT / 2 + self.view_bottom - 30,
                                 arcade.color.WHITE, 20)
            if self.konami is False:
                arcade.draw_text(str(ammo), SCREEN_WIDTH - 80 + shakevalue + self.view_left, 40 + shakevalue1 + self.view_bottom,
                                 arcade.color.YELLOW, 30)
                arcade.draw_rectangle_filled(30 + self.view_left, SCREEN_HEIGHT - 46 + self.view_bottom, 50, 80,
                                             arcade.color.WHITE)
                arcade.draw_text(str(ammo1), 10 + self.view_left, SCREEN_HEIGHT - 30 + self.view_bottom, arcade.color.BLACK, 20)
                arcade.draw_text(str(ammo2), 10 + self.view_left, SCREEN_HEIGHT - 55 + self.view_bottom, arcade.color.BLACK, 20)
                arcade.draw_text(str(ammo3), 10 + self.view_left, SCREEN_HEIGHT - 80 + self.view_bottom, arcade.color.BLACK, 20)
                if self.player_sprite.health > 0:
                    arcade.draw_texture_rectangle(50 + self.view_left, 50 + self.view_bottom, 64, 52,
                                                  self.hp[self.player_sprite.health])
                if self.player_sprite.health <= 0:
                    arcade.draw_texture_rectangle(50 + self.view_left, 50 + self.view_bottom, 64, 52,
                                                  self.hp[0])

            if self.konami is True:
                arcade.draw_text(str(ammo), SCREEN_WIDTH - 160 + shakevalue + self.view_left,
                                 40 + shakevalue1 + self.view_bottom,
                                 arcade.color.RED, 30)
                arcade.draw_rectangle_filled(67 + self.view_left, SCREEN_HEIGHT - 46 + self.view_bottom, 120, 80,
                                             arcade.color.WHITE)
                arcade.draw_text(str(ammo1), 10 + self.view_left, SCREEN_HEIGHT - 30 + self.view_bottom,
                                 arcade.color.RED, 20)
                arcade.draw_text(str(ammo2), 10 + self.view_left, SCREEN_HEIGHT - 55 + self.view_bottom,
                                 arcade.color.RED, 20)
                arcade.draw_text(str(ammo3), 10 + self.view_left, SCREEN_HEIGHT - 80 + self.view_bottom,
                                 arcade.color.RED, 20)
                arcade.draw_texture_rectangle(50 + self.view_left, 50 + self.view_bottom, 64, 52,
                                              self.god)
                self.player_sprite.health = 9999999999
        if win is True and self.player_sprite.center_x > 7500:
            arcade.draw_texture_rectangle(SCREEN_WIDTH/2+self.view_left, SCREEN_HEIGHT/2+self.view_bottom, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
            arcade.draw_text("You Won!", SCREEN_WIDTH/3+self.view_left, SCREEN_HEIGHT/2+self.view_bottom, arcade.color.YELLOW, 40)

    def update(self, delta_time):
        global JUMP_CHECK, JUMP_CLOCK, JUMP_gCLOCK, JUMP_gCHECK, fire_check, firerate_clock, SPREAD, empty, \
            ammo, ammo1, ammo2, ammo3, shake, shakevalue, shakevalue1, \
            perm_shakevalue, perm_shakevalue1, RIGHT_MOVE, LEFT_MOVE, recoil, pause, clock, FPS, win

        if self.arrow_down_pressed is True and self.arrow_up_pressed is True and self.arrow_left_pressed is True \
                and self.arrow_right_pressed is True and self.A_pressed is True and self.B_pressed is True:
            self.konami = True
            perm_shakevalue = random.randint(-7, 7)
            perm_shakevalue1 = random.randint(-7, 7)
            ammo1 = 999999999
            ammo2 = 999999999
            ammo3 = 999999999

        if start is True:
            clock += 1
            start_time = time.time()
            if self.player_sprite.health <= 0:
                for player in self.player_list:
                    player.kill()
            if pause is False:

                self.player_sprite.change_x = 0
                self.player_sprite.change_y = 0

                if self.player_sprite.health > 0:
                    if self.left_pressed and not self.right_pressed:
                        RIGHT_MOVE = False
                        LEFT_MOVE = True
                        self.player_sprite.change_x = -MOVEMENT_SPEED
                    elif self.right_pressed and not self.left_pressed:
                        RIGHT_MOVE = True
                        LEFT_MOVE = False
                        self.player_sprite.change_x = MOVEMENT_SPEED
                    else:
                        RIGHT_MOVE = False
                        LEFT_MOVE = False

                    if self.player_sprite.side_check == 0:
                        self.player_sprite.change_x += recoil
                    if self.player_sprite.side_check == 1:
                        self.player_sprite.change_x -= recoil

                    if self.physics_engine.can_jump():
                        JUMP_gCLOCK += 1
                        if self.up_pressed and JUMP_gCLOCK >= JUMP_gCHECK:
                            JUMP_gCLOCK = 0
                            JUMP_CHECK = True
                    if JUMP_CHECK is True:
                        JUMP_CLOCK += 1
                    elif JUMP_CHECK is False:
                        JUMP_CLOCK = 0
                        self.player_sprite.change_y = 0
                    if JUMP_CLOCK > 0 and JUMP_CLOCK < JUMP_FRAME:
                        self.player_sprite.change_y = JUMP_SPEED
                    elif JUMP_CLOCK > JUMP_FRAME:
                        JUMP_CHECK = False

                for pickup in self.pickup_list:
                    if arcade.check_for_collision(self.player_sprite, pickup):
                        if pickup.type == 0:
                            if self.player_sprite.health < 5:
                                self.player_sprite.health += 1
                                pickup.kill()
                        if pickup.type == 1:
                            ammo1 += pickup.amount
                            pickup.kill()
                        if pickup.type == 2:
                            ammo2 += pickup.amount
                            pickup.kill()
                        if pickup.type == 3:
                            ammo3 += pickup.amount
                            pickup.kill()

                for bullet in self.bullet_list:
                    hit_list = arcade.check_for_collision_with_list(bullet, self.wall_list)
                    if len(hit_list) > 0:
                        bullet.kill()
                    if len(arcade.check_for_collision_with_list(bullet, self.enemy_list)) > 0:
                        pass
                    if bullet.center_x > 1000 + self.view_left or bullet.center_x < self.view_left:
                        bullet.kill()

                for toxin in self.toxin_list:
                    if arcade.check_for_collision(toxin, self.player_sprite):
                        self.player_sprite.health -= 5

                self.boss_list.update()
                for boss in self.boss_list:
                    if self.player_sprite.center_x - boss.center_x > -700 \
                            and self.player_sprite.center_x - boss.center_x < 700 \
                            and self.player_sprite.health > 0:
                        boss.random_clock = random.randint(40, 80)
                        start_x = boss.center_x
                        start_y = boss.center_y

                        dest_x = self.player_sprite.center_x
                        dest_y = self.player_sprite.center_y + 12

                        x_diff = dest_x - start_x
                        y_diff = dest_y - start_y
                        angle = math.atan2(y_diff, x_diff)

                        boss.gun_angle = math.degrees(angle)
                        if boss.clock == 0:
                            boss_bullet = arcade.Sprite('images/ball.png', 2)
                            boss_bullet.center_x = start_x
                            boss_bullet.center_y = start_y

                            boss_bullet.change_x = math.cos(angle) * 22
                            boss_bullet.change_y = math.sin(angle) * 22
                            self.enemy_bullet_list.append(boss_bullet)
                            boss.clock += 1
                    else:
                        boss.gun_angle = 180

                    if boss.clock < boss.random_clock:
                        boss.clock += 1
                    if boss.clock >= boss.random_clock:
                        boss.clock = 0
                    if len(arcade.check_for_collision_with_list(boss, self.bullet_list)) > 0:
                        for bullet in self.bullet_list:
                            if (arcade.check_for_collision(bullet, boss)) > 0:
                                bullet.kill()
                                boss.health -= bullet.damage
                    if boss.health <= 0:
                        boss.kill()
                        win = True

                for enemy in self.enemy_list:
                    if self.player_sprite.center_x - enemy.center_x > -enemy.detection_range \
                            and self.player_sprite.center_x - enemy.center_x < enemy.detection_range\
                            and self.player_sprite.health > 0:
                        start_x = enemy.center_x
                        start_y = enemy.center_y

                        dest_x = self.player_sprite.center_x
                        dest_y = self.player_sprite.center_y + 6

                        x_diff = dest_x - start_x
                        y_diff = dest_y - start_y
                        angle = math.atan2(y_diff, x_diff)

                        enemy.gun_angle = math.degrees(angle)
                        if enemy.clock == 0:
                            enemy_bullet = arcade.Sprite('images/ball.png')
                            enemy_bullet.center_x = start_x
                            enemy_bullet.center_y = start_y

                            enemy_bullet.change_x = math.cos(angle) * 5
                            enemy_bullet.change_y = math.sin(angle) * 5
                            self.enemy_bullet_list.append(enemy_bullet)
                            enemy.clock += 1
                    else:
                        enemy.gun_angle = 90

                    if enemy.clock < 100:
                        enemy.clock += 1
                    if enemy.clock >= 100:
                        enemy.clock = 0
                    if len(arcade.check_for_collision_with_list(enemy, self.wall_list)) > 0:
                        enemy.change_x *= -1
                    elif enemy.boundary_left is not None and enemy.left < enemy.boundary_left:
                        enemy.change_x *= -1
                    elif enemy.boundary_right is not None and enemy.right > enemy.boundary_right:
                        enemy.change_x *= -1
                    if len(arcade.check_for_collision_with_list(enemy, self.bullet_list)) > 0:
                        for bullet in self.bullet_list:
                            if (arcade.check_for_collision(bullet, enemy)) > 0:
                                bullet.kill()
                                enemy.health -= bullet.damage
                    if enemy.health <= 0:
                        enemy.kill()

                self.enemy_list.update()

                for enemy_bullet in self.enemy_bullet_list:
                    if len(arcade.check_for_collision_with_list(enemy_bullet, self.wall_list)) > 0:
                        enemy_bullet.kill()
                    if (arcade.check_for_collision(self.player_sprite, enemy_bullet)) is True:
                        enemy_bullet.kill()
                        self.player_sprite.health -= 1
                    if enemy_bullet.center_x > 900 + self.view_left or enemy_bullet.center_x < self.view_left:
                        enemy_bullet.kill()

                if loadout == 1:
                    ammo = ammo1
                    BULLET_SPEED = random.randint(11, 13)
                    FIRERATE = random.uniform(14.5, 15.5)
                    BULLET_SPRITE = arcade.Sprite("images/bullet.png", 1/2)
                    SPREAD = random.uniform(-0.3, 0.3)
                    DISPLACEMENT_x = 0
                    DISPLACEMENT_y = 9
                    recoil = int(abs(shakevalue)/5)
                    damage = 2.5
                if loadout == 2:
                    ammo = ammo2
                    BULLET_SPEED = 20
                    FIRERATE = 22
                    BULLET_SPRITE = arcade.Sprite("images/bullet_red.png", 0.5)
                    SPREAD = random.uniform(-0.2, 0.2)
                    DISPLACEMENT_x = 0
                    DISPLACEMENT_y = 10
                    damage = 7
                    recoil = int(abs(shakevalue)/3)
                if loadout == 3:
                    ammo = ammo3
                    BULLET_SPEED = random.uniform(10, 12.0)
                    FIRERATE = 4
                    BULLET_SPRITE = arcade.Sprite("images/bullet_yellow.png", 1)
                    SPREAD = random.uniform(-0.4, 0.4)
                    DISPLACEMENT_x = 26
                    DISPLACEMENT_y = 12
                    recoil = int(abs(shakevalue)/1.25)
                    damage = 2

                if shake is True:
                    shakevalue = random.randint(-5, 5)
                    shakevalue1 = random.randint(-5, 5)
                else:
                    shakevalue = 0
                    shakevalue1 = 0

                if self.p_pressed is True:
                    if ammo == 0:
                        shake = False
                    if firerate_clock == 0 and fire_check is True and ammo > 0:
                        if loadout == 1:
                            ammo1 -= 1
                        if loadout == 2:
                            ammo2 -= 1
                        if loadout == 3:
                            ammo3 -= 1
                        shake = True
                        bullet = BULLET_SPRITE
                        if self.player_sprite.side_check == 1:
                            bullet.angle = -90
                            bullet.change_x = BULLET_SPEED
                            bullet.center_x = self.player_sprite.center_x + DISPLACEMENT_x

                        if self.player_sprite.side_check == 0:
                            bullet.angle = 90
                            bullet.change_x = -BULLET_SPEED
                            bullet.center_x = self.player_sprite.center_x - DISPLACEMENT_x

                        bullet.change_y = SPREAD
                        bullet.bottom = self.player_sprite.center_y - DISPLACEMENT_y
                        bullet.damage = damage
                        self.bullet_list.append(bullet)

                        fire_check = False

                if self.p_pressed is False:
                    shake = False
                if fire_check is False:
                    firerate_clock += 1
                    if firerate_clock >= FIRERATE/2:
                        shake = False
                    if firerate_clock >= FIRERATE:
                        fire_check = True
                        firerate_clock = 0

                changed = False

                left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN
                if self.player_sprite.left < left_boundary:
                    self.view_left -= left_boundary - self.player_sprite.left
                    changed = True

                right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN
                if self.player_sprite.right > right_boundary:
                    self.view_left += self.player_sprite.right - right_boundary
                    changed = True

                top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
                if self.player_sprite.top > top_boundary:
                    self.view_bottom += self.player_sprite.top - top_boundary
                    changed = True

                bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
                if self.player_sprite.bottom < bottom_boundary:
                    self.view_bottom -= bottom_boundary - self.player_sprite.bottom
                    changed = True

                if changed:
                    self.view_bottom = int(self.view_bottom)
                    self.view_left = int(self.view_left)

                    arcade.set_viewport(self.view_left,
                                        SCREEN_WIDTH + self.view_left,
                                        self.view_bottom,
                                        SCREEN_HEIGHT + self.view_bottom)

                self.player_sprite.update()
                self.bullet_list.update()
                self.physics_engine.update()
                self.enemy_bullet_list.update()
                self.pickup_list.update()

                if clock % 30 == 0:
                    FPS = int(1 / (time.time() - start_time))

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        global start, clock
        start = True
        if self.konami is True:
            if button == 4:
                print(x + self.view_left, y + self.view_bottom)
            if start is True and clock > 10:
                if button == 1:
                    self.player_sprite.center_x = x + self.view_left
                    self.player_sprite.center_y = y + self.view_bottom

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        global loadout, start, pause

        if start is False or pause is True:
            if key == arcade.key.M:
                start = True
            if key == arcade.key.UP:
                self.arrow_up_pressed = True
            if key == arcade.key.DOWN:
                self.arrow_down_pressed = True
            if key == arcade.key.LEFT:
                self.arrow_left_pressed = True
            if key == arcade.key.RIGHT:
                self.arrow_right_pressed = True
            if key == arcade.key.A:
                self.A_pressed = True
            if key == arcade.key.B:
                self.B_pressed = True
        if start is True and self.player_sprite.health > 0:
            if key == arcade.key.W:
                self.up_pressed = True
            elif key == arcade.key.S:
                self.down_pressed = True
            elif key == arcade.key.A:
                self.left_pressed = True
            elif key == arcade.key.D:
                self.right_pressed = True

            elif key == arcade.key.N:
                self.m_pressed = True
                pause = not pause

            elif key == arcade.key.P:
                self.p_pressed = True

            elif key == arcade.key.KEY_1 and ammo1 > 0:
                loadout = 1
            elif key == arcade.key.KEY_2 and ammo2 > 0:
                loadout = 2
            elif key == arcade.key.KEY_3 and ammo3 > 0:
                loadout = 3

        if pause is True or self.player_sprite.health <= 0:
            if key == arcade.key.M:
                self.setup()
                pause = False

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        global pause

        if key == arcade.key.W:
            self.up_pressed = False
        elif key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.D:
            self.right_pressed = False

        elif key == arcade.key.P:
            self.p_pressed = False
        elif key == arcade.key.N:
            self.m_pressed = False


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
