import pygame
import sys

import resources as R
from world import World

class GameState:
    def __init__(self):
        self.world = World(5) 

    def check_events(self, events):
        for i in events:
            if i.type == pygame.QUIT:
                sys.exit(0)
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_ESCAPE:
                    sys.exit(0)

    def blit(self, surface):
        surface.blit(self.world.blit(), (0,0))

    def tick(self):
        pass

