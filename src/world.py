from gametile import GameTile

class World:
    def __init__(self, size):
        self.size = size

        self.tl = [[GameTile() for j in range(self.size)] for i in range(self.size)]
        self.bl = [[GameTile() for j in range(self.size)] for i in range(self.size)]
        self.tr = [[GameTile() for j in range(self.size)] for i in range(self.size)]
        self.br = [[GameTile() for j in range(self.size)] for i in range(self.size)]
    
    def get_tile(self, x, y):
        if y >= 0:
            if x >= 0:
                return self.tr[y][x]
            else:
                return self.tl[y][-x-1]
        else:
            if x >= 0:
                return self.br[-y-1][x]
            else:
                return self.bl[-y-1][-x-1]

    def grow(self, amount):
        self.size += amount

        for i in self.tl:
            i.append(GameTile())
        for i in self.bl:
            i.append(GameTile())
        for i in self.tr:
            i.append(GameTile())
        for i in self.br:
            i.append(GameTile())

        self.tl.append([GameTile() for i in range(self.size)])
        self.bl.append([GameTile() for i in range(self.size)])
        self.tr.append([GameTile() for i in range(self.size)])
        self.br.append([GameTile() for i in range(self.size)])

    ################
    ## Blit logic ##
    ################

    def blit(self, surface):
        for x in range(-self.size,0):
            for y in range(-self.size,0):
                surface.blit(self.get_tile(x,y).blit(), (self.size*20 + x*20,
                                                         self.size*20 + y*20))
        for x in range(self.size):
            for y in range(-self.size,0):
                surface.blit(self.get_tile(x,y).blit(), (self.size*20 + x*20,
                                                         self.size*20 + y*20))
        for x in range(-self.size,0):
            for y in range(self.size):
                surface.blit(self.get_tile(x,y).blit(), (self.size*20 + x*20,
                                                         self.size*20 + y*20))
        for x in range(self.size):
            for y in range(self.size):
                surface.blit(self.get_tile(x,y).blit(), (self.size*20 + x*20,
                                                         self.size*20 + y*20))

    def display(self):
        for i in range(self.size-1,-1,-1):
            print self.tl[i][::-1] + self.tr[i]
        for i in range(self.size):
            print self.bl[i][::-1] + self.br[i]

    def db_display(self):
        for i in range(self.size):
            print self.tl[i] + self.tr[i]
        for i in range(self.size):
            print self.bl[i] + self.br[i]
