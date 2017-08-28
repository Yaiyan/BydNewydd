import pygame

from gamestate import GameState

RESOLUTION = (960,540) #Internal resolution
SCALE = 2

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
        self.states[self.current_state].blit(draw_surface)
        
        surface.fill((0,0,0))
        surface.blit(pygame.transform.scale(draw_surface, (RESOLUTION[0]*SCALE, RESOLUTION[1]*SCALE)), (0,0))

        pygame.display.flip()
    
    def run(self):
        draw_surface = pygame.Surface(RESOLUTION)
        surface = pygame.display.set_mode((RESOLUTION[0]*SCALE, RESOLUTION[1]*SCALE))

        while True:
            self.check_events()
            self.tick()
            self.blit(draw_surface, surface)

M = Main()
M.run()
