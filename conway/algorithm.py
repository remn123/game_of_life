import numpy as np


class Conway:
    
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        scale = self.settings.get('scale')
        self.J, self.I = self.settings.get('resolution')
        self.I, self.J = self.I // scale, self.J // scale
        self._map = np.zeros((self.I+4, self.J+4))
        
    def step(self, map):
        new_map = self.run(map)
        return new_map

    def run(self, map):
        return self._sequential(map)
    
    def _sequential(self, map):
        IMAX, JMAX = self.I, self.J
        map = self._add_ghost_cells(map, IMAX, JMAX)
        for i in range(1, IMAX+4):
            for j in range(1, JMAX+4):
                lattice = self._get_lattice(i, j, map)
                value = self._apply(lattice)
                self._map[i,j] = value
        return self._map[2:IMAX+2, 2:JMAX+2]
    
    def _add_ghost_cells(self, map, IMAX, JMAX):
        print('map=', map)
        new_map = np.copy(self._map)
        new_map[2:IMAX+2, 2:JMAX+2] = map
        print('new_map=', new_map)
        return new_map
    
    def _get_lattice(self, i, j, map):
        return map[i-1:i+2, j-1:j+2]
    
    def _apply(self, lattice):
        # Any live cell with two or three live neighbours survives.
        # Any dead cell with three live neighbours becomes a live cell.
        # All other live cells die in the next generation. Similarly, all other dead cells stay dead.
        #print(lattice)
        cell = lattice[1,1]
        num_live_neighbors = np.sum(lattice) - cell
        if cell:
            if num_live_neighbors in [2, 3]:
                return 1
        else:
            if num_live_neighbors == 3:
                return 1
        return 0
            
        

    