import pygame

class GameTile:
    def __init__(self):
        pass

    def blit(self):
        surface = pygame.Surface((20,20))
        pygame.draw.rect(surface,
                         (103, 187, 76),
                         (0,
                          0,
                          20,
                          20)
                        )
        return surface
