import pygame, sys
from pygame.locals import *
from gameconst import *
from cursor import Cursor
from tilemap import TileMap, Point
from action import ActionManager, MoveSightAction
from soldier import SoldierManager

pygame.init()

display_surf = pygame.display.set_mode((GAME_WINDOW_WIDTH , GAME_WINDOW_HEIGHT))

pygame.display.set_caption('BattleWar')
pygame.mouse.set_visible(False)

fps_clock = pygame.time.Clock()
cur = Cursor(display_surf)
map_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
map_manager = TileMap(map_surf)
action_manager = ActionManager()
soldier_manager = SoldierManager()

PROGRAM_STAT = NORMAL

TARGET_FOCUS = Point((700, 1000))
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == MOUSEMOTION:
            # print event.pos

        if event.type == KEYUP:
            if event.key in (K_s, ):
                if PROGRAM_STAT != PAUSE:
                    PRESTATE = PROGRAM_STAT
                    PROGRAM_STAT = PAUSE
                else:
                    PROGRAM_STAT = PRESTATE

            if event.key in (K_g, ):
                PROGRAM_STAT = ACTION
                action_manager.add_action(MoveSightAction(map_manager, TARGET_FOCUS))

        if event.type == MOUSEBUTTONUP:
            row, col = map_manager.handler_click(Point(event.pos))
            print event.pos, (row, col)
            if row is not None and col is not None:
                if not soldier_manager.add_soldier(row, col, 1):
                    soldier_manager.remove_soldier_by_coor(row, col)

    mouse_pos = Point(pygame.mouse.get_pos())
    cur.set_position(mouse_pos)
    if PROGRAM_STAT == NORMAL:
        cur.set_visible(True)
        map_manager.move_sight(mouse_pos)

    if PROGRAM_STAT == PAUSE:
        cur.set_visible(True)

    if PROGRAM_STAT == ACTION:
        cur.set_visible(False)
        if action_manager.play():
            PROGRAM_STAT = NORMAL

    #draw background
    display_surf.fill(WHITE)

    #draw elements    
    map_manager.draw()
    soldier_manager.draw(map_manager)
    display_surf.blit(map_surf, (OFFSET_X, OFFSET_Y))

    #draw cursor
    cur.draw()

    pygame.display.update()
    fps_clock.tick(60)