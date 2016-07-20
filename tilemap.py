import pygame, sys
from pygame.locals import *

from gameconst import *

class Point:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]

class TileBase:
    def __init__(self, surface, row, col):
        self.surface = surface
        self.row = row
        self.col = col
        self.width = MAP_WIDTH / COLS
        self.height = MAP_HEIGHT / ROWS

    def draw(self, focus):
        # real_x = offset_x  - focus.x + self.x
        x =- focus.x + self.col * self.width
        y =- focus.y + self.row * self.height

        pygame.draw.rect(self.surface, WHITE, (x, y, self.width, self.height), 0)
        pygame.draw.rect(self.surface, (150, 150, 150), (x, y, self.width, self.height), 1)

        # print x, y

class TileMap:

    def __init__(self, surface):
        self.surface = surface
        self.tiles = [[TileBase(surface, i, j) for j in range(COLS)] for i in range(ROWS)]
        self.focus = Point((0, 0))
        self.delta = 20

    def draw(self):
        self.surface.fill(BLACK)

        for tile_row in self.tiles:
            for tile in tile_row:
                tile.draw(self.focus)

        pygame.draw.rect(self.surface, (0, 0, 0), (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT), 1)

    def move_sight(self, mouse_pos):
        if mouse_pos.x <= SIGHT_MOVE_PADDING and self.focus.x >= 0:
            self.focus.x -= self.delta
        if mouse_pos.x >= GAME_WINDOW_WIDTH - SIGHT_MOVE_PADDING and self.focus.x <= MAP_WIDTH - WINDOW_WIDTH:
            self.focus.x += self.delta
        if mouse_pos.y <= SIGHT_MOVE_PADDING and self.focus.y >= 0:
            self.focus.y -= self.delta
        if mouse_pos.y >= GAME_WINDOW_HEIGHT - SIGHT_MOVE_PADDING and self.focus.y <= MAP_HEIGHT - WINDOW_HEIGHT:
            self.focus.y += self.delta


