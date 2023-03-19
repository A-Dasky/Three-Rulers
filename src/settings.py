import pygame as pg


def params():
    """Game params stored in a dic
    """
    game_params = {
                   'screen_width': 1280,
                   'screen_height': 720,
#                   'screen_width': 1500,
#                   'screen_height': 800,
                   'frames_per_second': 30,
                   'bck_color': (254, 255, 254),
                   'speed': 2,
                   'char_img_factor': 3.5,
                   'text_padding': 6,
                   'font_size': 28,
                  }
    return game_params

def get_screen(params):
    """Get screen
    """
    return pg.display.set_mode((params['screen_width'], params['screen_height']))

def get_screen_rect(screen):
    return screen.get_rect()


def get_screen_shift(screen):
    param = params()
    r = get_screen_rect(screen)
    shift_x = 0
    shift_y = 0
    if r.width < param['screen_width']:
        shift_x = (param['screen_width'] - r.width) / 2
    if r.height < param['screen_height']:
        shift_y = (param['screen_height'] - r.height) / 2
    return shift_x, shift_y

def get_move_background(zone, mx, my, top=0, left=0):
    """
    mx, my - current shift in background
    top, left - player rect.topleft
    """
    param = params()
    h = param['screen_height']
    w = param['screen_width']
    r = get_screen_rect(zone)
    move_x = mx
    move_y = my


    if r.width > w:
        dx = r.width - w

        if left > w / 2:
            move_x = move_x - 2

            if abs(move_x) > dx:
                move_x = dx * (-1)

        if left < w / 2:
            move_x = move_x + 2

            if move_x > 0:
                move_x = 0

    # if the height is greater than the default screen height
    if r.height > h:
        # total amount of height allowed to shift
        dy = r.height - h

        # If walking down and the top goes past 75 of screen
        if top > h / 2:
            move_y = move_y - 2

            # If move is more than boarder
            if abs(move_y) > dy:
                move_y = dy * (-1)

        # if walking up and the avatar goes above 25% of avail
        if top < h / 2:
            move_y = move_y + 2

            # Cannot pass 0
            if move_y > 0:
                move_y = 0

    return move_x, move_y

def load_shift_zone(r, shift_x, shift_y, tmp_x, tmp_y):
    param = params()
    h2 = param['screen_height'] / 2
    w2 = param['screen_width'] / 2

    shift_x -= tmp_x - w2
    shift_y -= tmp_y - h2

    if shift_x > 0:
        if r.width > w2 * 2:
            shift_x = 0
        else:
            shift_x = (w2 * 2 - r.width) / 2
    if shift_y > 0:
        if r.height > h2 * 2:
            shift_y = 0
        else:
            shift_y = (h2 * 2 - r.height) / 2
    if abs(shift_y) > r.height - h2:
        shift_y = (h2 * 2 - r.height) / 2

    return shift_x, shift_y

def get_game_clock():
    return pg.time.Clock()

def default_ruler_stat():
    """The default stat for all rulers

    The default stat for all rulers:
    stat - They are alive
    allies - Allies are alive
    meet - You have not met them
    fight - You have not fought them
    

    Returns
    -------
    dict
    """
    return {'stat': True,     # Alive or dead
            'allies': True,   # Are allies alive or dead
            'apower': True,   # Allies are alive and not defeated
            'meet': False,    # Have you spoken to them before fighting
            'fight': False,   # Did choose to fight them / cannot talk during fight
            'power': True,    # Did you defeat them
           }

def new_game():
    start = {'zone': 'hero_house',
             'x': 4,
             'y': 5,
             'gold': 100,
             'char': [
                      {'name': '',
                       'class': 'paladin_M',
                       'HP': 50,
                       'MP': 10,
                       'level': 1,
                       'exp': 0,
                       'weapon': {'name': None, 'idx': None},
                       'head': {'name': None, 'idx': None},
                       'body': {'name': None, 'idx': None},
                       'arms': {'name': None, 'idx': None},
                       'legs': {'name': None, 'idx': None},
                      },
                     ],
             'items': [],
             'spells': [],
             'skills': [],
             'rulers': {'king': default_ruler_stat(),
                        'merchant': default_ruler_stat(),
                        'cleric': default_ruler_stat(),
                       }
            }
    return start