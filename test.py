
class Grid:
    
    def __init__(self, gridY, gridX, empty_grid):
        self.gridY = gridY
        self.gridX = gridX
        self.empty_grid = empty_grid
        self.grid = []
        
        self.playerY = 0
        self.playerX = 0
        self.plyerChars = {"up":"↑", "down":"↓", "left":"←", "right":"→"}
        
    def make_grid(self):
        for _ in range(self.gridY):
            self.grid.append([self.empty_grid for _ in range(self.gridX)]) 
        
    def print_grid(self):
        for column in self.grid:
            print(*[str(item) + " " for item in column])
            
    def inject_player(self, injectY, injectX):
        self.playerY = injectY
        self.playerX = injectX
        self.grid[injectY][injectX] = self.plyerChars["up"]
        
    def move_player(self, moveY, moveX):
        if (moveY in [0, 1]) and (moveX in [0, 1]) and (moveY == moveX):
            pass
        else:
            return
        if not ((self.playerY + moveY < 0 or self.playerY + moveY > self.gridY) or (self.playerX + moveX < 0 or self.playerX + moveX > self.gridX)):
            self.grid[self.playerY][self.playerX] = self.empty_grid
            self.playerY += moveY
            self.playerX += moveX
            self.grid[self.playerY][self.playerX] = self.playerChar

            
def main():
    
    grid = Grid(10, 10, "#")
    grid.make_grid()
    grid.inject_player(2, 2)
    grid.print_grid()
    
main()