import pygame as pg
import src.walls as walls


def zoner(zone):
    """dict of zones and their connections
    """
    d = {'hero_house': {'OUT': [{'zone': 'world',    # Next zone
                                 'area': [5, 6, 14, 11], # Left, Top, Width, Height
                                 'load_point': [5, 6],
                                }],
                       }, 
        }
    return d[zone]


def load_zone(zone):
    """load an image of the zone
    """
    z = pg.image.load('zones/' + zone + '.png').convert()
    return z


def get_walls(zone, x, y):
    """load walls in .w file
    """
    wall_list = walls.set_walls('zones/' + zone + '.w', x, y)
    wall = pg.sprite.RenderPlain(wall_list)
    return wall

def get_zones(zone, x, y):
    """
    """
    zone_list = walls.set_zones('zones/' + zone + '.z', x, y)
    z = pg.sprite.RenderPlain(zone_list)
    return z