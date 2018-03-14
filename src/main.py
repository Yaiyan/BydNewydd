import resources as r

import pygame

from gamestate import GameState

class Main:
    def __init__(self):
        self.states = {'GameState': GameState()}
        self.current_state = 'GameState'

    def check_events(self):
        pygame.event.pump()

        events = [i for i in pygame.event.get()]

        self.states[self.current_state].check_events(events)
    
    def tick(self):
        self.states[self.current_state].tick()

    def blit(self, draw_surface, surface):
        draw_surface.fill((78,156,245))

        self.states[self.current_state].blit(draw_surface)
        
        surface.blit(pygame.transform.scale(draw_surface, (r.RESOLUTION[0]*r.SCALE, r.RESOLUTION[1]*r.SCALE)), (0,0))

        pygame.display.flip()
    
    def run(self):
        draw_surface = pygame.Surface(r.RESOLUTION)
        surface = pygame.display.set_mode((r.RESOLUTION[0]*r.SCALE, r.RESOLUTION[1]*r.SCALE))

        while True:
            self.check_events()
            self.tick()
            self.blit(draw_surface, surface)

M = Main()
M.run()
