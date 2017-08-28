import pygame
import sys

import resources as R

class GameState:
    def __init__(self):
        pass

    def check_events(self, events):
        for i in events:
            if i.type == pygame.QUIT:
                sys.exit(0)
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_ESCAPE:
                    sys.exit(0)

    def blit(self, surface):
        pygame.draw.rect(surface, (255,255,255), (100,100,5,10))

    def tick(self):
        pass
