import resources as r

import pygame

class GameTile:
    def __init__(self, colour=(87, 157, 46)):
        self.colour = colour

    def blit(self):
        surface = pygame.Surface((r.TILESIZE,r.TILESIZE))
        pygame.draw.rect(surface,
                         self.colour,
                         (0,
                          0,
                          r.TILESIZE,
                          r.TILESIZE)
                        )
        pygame.draw.rect(surface,
                         (0,0,0),
                         (0,
                          0,
                          r.TILESIZE,
                          r.TILESIZE),
                         1
                        )
        return surface
