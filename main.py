import os
import numpy as np
import pygame as pg

import src.settings as settings
import src.zone as zones
import src.user as avatar
import src.walls as walls
import src.music as music


SQ = 32
MSIZE = 3.5


def run():
    """Run game
    """
    pg.init()

    # Get game params
    params = settings.params()
    try:
        pygame.mixer.init()
    except:
        pass

    h2 = params['screen_height'] / 2
    w2 = params['screen_width'] / 2
    
    # init clock
    clock = settings.get_game_clock()
    screen = settings.get_screen(params)
    screen.set_alpha(0)
    
    # init font
    font = pg.font.Font('misc/Anonymous_Pro.ttf', params['font_size'])
    
    # Select from menu (eventually)
    new_game = True
    if new_game:
        game = settings.new_game()
        
    zone = zones.load_zone(game['zone'])
    r = settings.get_screen_rect(zone)
    
    shift_x, shift_y = settings.get_screen_shift(zone)
    # =============================================
    tmp_x = game['x'] * SQ
    tmp_y = game['y'] * SQ
    
    shift_x, shift_y = settings.load_shift_zone(r, shift_x, shift_y, tmp_x, tmp_y)

    # get zone walls
    wall = zones.get_walls(game['zone'], shift_x, shift_y)
    
    # player starting point and direction
    DIR = 'D'
    player = avatar.Player(tmp_x + shift_x, tmp_y + shift_y)
    
    # MUSIC
    try:
        song = music.music_list(game['zone'])
        music.play_music(song)
    except:
        pass
    
    
    player.get_image(DIR, False)

    movingSprites = pg.sprite.RenderPlain((player))
    
    moving = False
    play = True
    
    while play:
        screen.fill((0, 0, 0))
        screen.blit(zone, (shift_x, shift_y), zone.get_rect())

        for e in pg.event.get():
            if e.type == pg.QUIT:
                play = False
                continue

            if e.type == pg.KEYDOWN:
                if e.key == pg.K_LEFT:
                    moving = True
                    DIR = 'L'
                    player.move(-params['speed'], 0)
                elif e.key == pg.K_RIGHT:
                    moving = True
                    DIR = 'R'
                    player.move(params['speed'], 0)
                elif e.key == pg.K_UP:
                    moving = True
                    DIR = 'U'
                    player.move(0, -params['speed'])
                elif e.key == pg.K_DOWN:
                    moving = True
                    DIR = 'D'
                    player.move(0, params['speed'])
                elif e.key == pg.K_q:
                    play = False
                    continue
            elif e.type == pg.KEYUP:
                moving = False
                if e.key == pg.K_LEFT:
                    DIR = 'L'
                elif e.key == pg.K_RIGHT:
                    DIR = 'R'
                elif e.key == pg.K_UP:
                    DIR = 'U'
                elif e.key == pg.K_DOWN:
                    DIR = 'D'
                player.move(0, 0, stop=True)
            # Troubleshooting
            print(player.rect.topleft)
            
            
            
        player.get_image(DIR, moving).get_rect()
        player.update(wall)
            
        new_zone = player.change_zone(zones.zoner(game['zone']), shift_x, shift_y)
            
            
        if moving:
            px, py = settings.get_move_background(zone, shift_x, shift_y, 
                                                  player.rect.top,
                                                  player.rect.left)
            if py != shift_y:
                if DIR == 'U':
                    player.rect.top += params['speed']
                    shift_y += params['speed']
                    if shift_y > 0:
                        shift_y = 0
                    else:
                        walls.update_walls(wall, 0, params['speed'])
                if DIR == 'D':
                    player.rect.top -= params['speed']
                    shift_y -= params['speed']
                    if shift_y < h2 - r.height:
                        shift_y = h2 - r.height
                    else:
                        walls.update_walls(wall, 0, -params['speed'])
            if px != shift_x:
                if DIR == 'R':
                    player.rect.left -= params['speed']
                    shift_x -= params['speed']
                    if shift_x < w2 - r.width:
                        shift_x = w2 - r.width
                    else:
                        walls.update_walls(wall, -params['speed'], 0)
                if DIR == 'L':
                    player.rect.left += params['speed']
                    shift_x += params['speed']
                    if shift_x > 0:
                        shift_x = 0
                    else:
                        walls.update_walls(wall, params['speed'], 0)

        for zz in zones.zoner(game['zone'])['OUT']:
            aa = zz['area']
            aa[0] += shift_x
            aa[1] += shift_y
            pg.draw.rect(screen, (0, 0, 0), aa)
        for ww in wall:
            pg.draw.rect(screen, (255, 0, 0), ww)


        movingSprites.draw(screen)
        pg.display.flip()

        try:
            if music.music_list(game['zone']) is not song:
                song = music.music_list(game['zone'])
                music.play_music(song)
        except:
            pass

        # 30 frames per second
        clock.tick(params['frames_per_second'])

    pg.quit()
    return

if __name__ == '__main__':
    run()