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
        self.width = CELL_SIZE
        self.height = CELL_SIZE

    def draw(self, focus):
        # real_x = offset_x  - focus.x + self.x
        x =- focus.x + self.col * self.width
        y =- focus.y + self.row * self.height

        pygame.draw.rect(self.surface, WHITE, (x, y, self.width, self.height), 0)
        pygame.draw.rect(self.surface, GREY, (x, y, self.width, self.height), 1)

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

    def draw_soldier(self, soldier):
        row, col = soldier.row, soldier.col
        x = int(CELL_SIZE * (col + 0.5) - self.focus.x)
        y = int(CELL_SIZE * (row + 0.5) - self.focus.y)
        pygame.draw.circle(self.surface, BLUE, (x, y), int(CELL_SIZE * 0.4), 1)

    def handler_click(self, mouse_pos):
        if (0 <= mouse_pos.x - OFFSET_X <= WINDOW_WIDTH) and (0 <= mouse_pos.y - OFFSET_Y <= WINDOW_HEIGHT):  
            x = (mouse_pos.x - OFFSET_X + self.focus.x) / CELL_SIZE
            y = (mouse_pos.y - OFFSET_Y + self.focus.y) / CELL_SIZE
            return x, y
        return None, None

