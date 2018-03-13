import pygame
import sys

import resources as R
from world import World

class GameState:
    def __init__(self):
        self.world = World(5) 

        self.world_offset = [0, 0]
        self.wov = [0, 0]

    def check_events(self, events):
        for i in events:
            if i.type == pygame.QUIT:
                sys.exit(0)
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_ESCAPE:
                    sys.exit(0)

        if pygame.mouse.get_pos()[0] < 20*R.SCALE:
            self.wov[0] += 0.5
        if pygame.mouse.get_pos()[0] > R.RESOLUTION[0]*R.SCALE-20*R.SCALE:
            self.wov[0] -= 0.5
        if pygame.mouse.get_pos()[1] < 20*R.SCALE:
            self.wov[1] += 0.5
        if pygame.mouse.get_pos()[1] > R.RESOLUTION[1]*R.SCALE-20*R.SCALE:
            self.wov[1] -= 0.5

    def blit(self, surface):
        surface.blit(self.world.blit(), self.world_offset)

    def tick(self):
        self.wov[0] *= 0.8
        self.wov[1] *= 0.8

        self.world_offset[0] += self.wov[0]
        self.world_offset[1] += self.wov[1]
