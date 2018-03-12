class World:
    def __init__(self, size):
        self.size = size

        self.tl = [[(i,j,'tl') for j in range(self.size)] for i in range(self.size)]
        self.bl = [[(i,j,'bl') for j in range(self.size)] for i in range(self.size)]
        self.tr = [[(i,j,'tr') for j in range(self.size)] for i in range(self.size)]
        self.br = [[(i,j,'br') for j in range(self.size)] for i in range(self.size)]
    
    def get_square(self, x, y):
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
            i.append('gl')
        for i in self.bl:
            i.append('gl')
        for i in self.tr:
            i.append('gr')
        for i in self.br:
            i.append('gr')

        self.tl.append(['gt' for i in range(self.size)])
        self.bl.append(['gb' for i in range(self.size)])
        self.tr.append(['gt' for i in range(self.size)])
        self.br.append(['gb' for i in range(self.size)])

    
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
