import pygame as pg

from spirit_game.functions import vector

GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

SCOREBOARD = './spirit_game/scoreboard.txt'
FPS = 80
SCREEN_WIDTH = 1150
SCREEN_HEIGHT = 700
MENU_FONT_COLOR = (255, 140, 0)
BAR_LENGTH = 100
BAR_HEIGHT = 20

NIGHT_COLOR = (15, 15, 15)
LIGHT_RADIUS = (400, 400)
LIGHT_RADIUS_2 = (500, 500)
LIGHT_MASK = 'light_med.png'
LIGHT_MASK_2 = 'light_med2.png'
MINIMAP_WIDTH = 200
MINIMAP_HEIGHT = 150

PLAYER_WIDTH = 20
PLAYER_HEIGHT = 20
PLAYER_LIVES = 3
PLAYER_SHIELD = 200
PLAYER_SPEED = 150
PLAYER_ROTATION_SPEED = 150
PLAYER_IMAGE_NAKED = 'hold.png'
PLAYER_IMAGE_NAKED1 = 'hold1.png'
PLAYER_IMAGE_NAKED2 = 'hold2.png'
PLAYER_IMAGE_PISTOL = 'gun.png'
PLAYER_IMAGE_SHOTGUN = 'machine.png'
PLAYER_IMAGE_UZI = 'gun.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
LIVES_IMG = 'life_heart.png'

spirit_WIDTH = 23
spirit_HEIGHT = 28
spirit_SHIELD = 100
spirit_SPEEDS = [70, 90, 110, 130, 150]
spirit_IMAGE = 'spirit4.png'
spirit_IMAGE2 = 'spirit5.png'
spirit_HIT_RECT = pg.Rect(0, 0, 30, 30)
spirit_DMG = 5
spirit_NORMAL_RATIO = 1.2
spirit_HARD_RATIO = 1.5
spirit_HELL_RATIO = 2
DETECT_RADIUS = 400
AVOID_RADIUS = 80
KICKBACK = 10
BULLET_IMG = 'bulletYellowSilver_outline.png'
WEAPONS = {}
WEAPONS['pistol'] = {
    'bullet_speed': 500,
    'bullet_lifetime': 1000,
    'rate': 300,
    'kickback': 200,
    'spread': 5,
    'damage': 15,
    'bullet_size': 'large',
    'bullet_count': 1,
    'ammo_limit': 90,
}
WEAPONS['shotgun'] = {
    'bullet_speed': 400,
    'bullet_lifetime': 500,
    'rate': 900,
    'kickback': 500,
    'spread': 20,
    'damage': 7,
    'bullet_size': 'small',
    'ammo_limit': 400,
    'bullet_count': 12,
}
WEAPONS['uzi'] = {
    'bullet_speed': 500,
    'bullet_lifetime': 500,
    'rate': 70,
    'kickback': 150,
    'spread': 10,
    'damage': 5,
    'bullet_size': 'small',
    'bullet_count': 1,
    'ammo_limit': 300,
}
WEAPONS['rifle'] = {
    'bullet_speed': 700,
    'bullet_lifetime': 2000,
    'rate': 1500,
    'kickback': 700,
    'spread': 2,
    'damage': 80,
    'bullet_size': 'long',
    'bullet_count': 1,
    'ammo_limit': 20,
}
AMMO = {
    'pistol': 60,
    'shotgun': 228,
    'uzi': 200,
    'rifle': 10
}
BARREL_OFFSET = vector(30, 10)
SMOKE_DURATION = 40

INTRO_IMG = 'arrow_final.png'
INTRO_SPRITE_WIDTH = 40
INTRO_SPRITE_HEIGHT = 40
INTRO_SPRITE_POS_X = 0.35

OPTIONS_SPRITE_WIDTH = 45
OPTIONS_SPRITE_HEIGHT = 45
OPTIONS_SPRITE_POS_X = 0.28

CONTROL_SPRITE_WIDTH = 45
CONTROL_SPRITE_HEIGHT = 45
CONTROL_SPRITE_POS_X = 0.3

DIFFICULT_SPRITE_WIDTH = 40
DIFFICULT_SPRITE_HEIGHT = 40
DIFFICULT_SPRITE_POS_X = 0.25

ITEM_LAYER = 1
SPLAT_LAYER = 1
PLAYER_LAYER = 2
spirit_LAYER = 2
BULLET_LAYER = 3
SMOKE_LAYER = 5

ITEM_BOB_RANGE = 20
ITEM_BOB_SPEED = 0.4
BIG_HEALTH_PACK = PLAYER_SHIELD * 0.5
MINI_HEALTH_PACK = PLAYER_SHIELD * 0.3
ITEM_SIZE = 40
ITEM_IMAGES = {
    'health': 'first_aid1.png',
    'mini_health': 'first_aid1.png',
    'key': 'genericItem_color_155.png',
    'ammo_small': 'bullets1.png',
    'ammo_big': 'bullets1.png',
    'pistol': 'pistol.png',
    'shotgun': 'shotgun.png',
    'rifle': 'rifle.png',
    'uzi': 'uzi.png',
    'fuel_bottle' : 'fuel_bottle.png',
    'coins' : 'coins1.png',
    'coffee' : 'speed.png'
}
GREEN_SMOKE = [
    'fart00.png',
    'fart01.png',
    'fart02.png',
    'fart03.png',
    'fart04.png',
    'fart05.png',
    'fart06.png',
    'fart07.png',
    'fart08.png',
]
FLASH_SMOKE = [
    'flash00.png',
    'flash01.png',
    'flash02.png',
    'flash03.png',
    'flash04.png',
    'flash05.png',
    'flash06.png',
    'flash07.png',
    'flash08.png',
]
SPLATS = [
    'bloodsplats_0003.png',
    'bloodsplats_0004.png',
    'bloodsplats_0006.png',
    'bloodsplats_0007.png',
]
SOUND_EFFECTS = {
    'heal': 'healed.wav',
    'heal_mini': 'healed.wav',
    'pistol': 'pistol_reload.wav',
    'uzi': 'pistol_reload.wav',
    'rifle': 'rifle_pickup.wav',
    'locked_door': 'locked_door.wav',
    'out_of_ammo': 'outofammo.ogg',
    'shotgun': 'shotgun_reload.wav',
    'coins' : 'coins_collect.wav'
}
SOUND_EFFECTS_EMPTY = {
    'heal': '',
    'heal_mini': '',
    'pistol': '',
    'uzi': '',
    'rifle': '',
    'locked_door': '',
    'out_of_ammo': '',
    'shotgun': ''
}

spirit_MOAN_SOUNDS = [
    'spirit-1.wav',
    'spirit-2.wav',
    'spirit-3.wav',
    'spirit-4.wav',
    'spirit-5.wav'
]
spirit_PAIN_SOUNDS = [
    'monster-2.wav',
    'monster-3.wav',
    'monster-4.wav',
    'monster-5.wav',
    'monster-6.wav',
    'monster-7.wav',
]
spirit_DIE_SOUNDS = [
    'spirit_die.wav'
]

spirit_MOAN_SOUNDS_EMPTY = []
spirit_PAIN_SOUNDS_EMPTY = []
spirit_DIE_SOUNDS_EMPTY = []

WEAPON_SOUNDS = {
    'pistol': [
        'pistol.ogg',
        'pistol2.ogg',
        'pistol3.ogg'
    ],
    'shotgun': [
        'shotgun.ogg',
        'shotgun2.ogg',
        'shotgun3.ogg'
    ],
    'rifle': [
        'rifle.ogg',
        'rifle2.ogg',
        'rifle3.ogg'
    ],
    'uzi': [
        'pistol.ogg',
        'pistol2.ogg',
        'pistol3.ogg'
    ]
}

WEAPON_SOUNDS_EMPTY = {
    'pistol': [],
    'shotgun' : [],
    'rifle' : [],
    'uzi' : []
}