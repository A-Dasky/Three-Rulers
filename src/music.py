import os
import pygame as pg


def music_list(ind):
    """

    Parameters
    ----------
    ind: key
        key identifying path to the music file
    """
    music = {'hero_house': '/music/towns/TownTheme.mp3',
    }
    return music[ind]


def play_music(ind, until=-1):
    """

    """
    if ind == None:
        return
    pg.init()
    cwd = os.getcwd()
    pg.mixer.music.load(cwd + ind)
    pg.mixer.music.play(until, 0.0)
    return


def sound_list(ind):
    """

    Parameters
    ----------
    ind: key
        key identifying path to the sound file
    """
    sounds = {'menu': '/misc/menu/Menu_Selection_Click.wav',
              'rest': '/music/rest/sleep_inn.ogg',
              'buy_sell': '/misc/menu/sell_buy_item.wav',
              'change_equip': '/misc/menu/leather_inventory.wav',
              'menu_heal': '/misc/menu/piano.wav',
              'magicfail': '/misc/menu/magicfail.ogg',
             }
    return sounds[ind]


def play_sound(sound_file, num=1):
    cwd = os.getcwd()
    sound = pg.mixer.Sound(cwd + sound_file)
    pg.mixer.Sound.play(sound, loops=num)


def pause_music():
    pg.mixer.music.pause()


def unpause_music():
    pg.mixer.music.unpause()

def stop_music():
    pg.mixer.music.stop()
