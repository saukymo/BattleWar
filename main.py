import pygame, sys
from pygame.locals import *
from gameconst import *
from cursor import Cursor
from tilemap import TileMap, Point
from action import ActionManager

pygame.init()

display_surf = pygame.display.set_mode((GAME_WINDOW_WIDTH , GAME_WINDOW_HEIGHT))
map_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption('Hello World!')

cur = Cursor(display_surf)


map_manager = TileMap(map_surf)
pygame.mouse.set_visible(False)

fps_clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            print event.pos
            

    
    

    mouse_pos = Point(pygame.mouse.get_pos())
    cur.set_position(mouse_pos)

    #draw background
    display_surf.fill(WHITE)
   

    #draw elements
    map_manager.move_sight(mouse_pos)
    map_manager.draw()
    display_surf.blit(map_surf, (OFFSET_X, OFFSET_Y))

    #draw cursor
    cur.draw()
    pygame.display.update()
    fps_clock.tick(30)