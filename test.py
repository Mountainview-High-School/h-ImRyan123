import time
import os

class Grid:
    
    def __init__(self, gridY, gridX, empty_grid):
        self.gridY = gridY
        self.gridX = gridX
        self.empty_grid = empty_grid
        self.grid = []
        
        self.playerY = 0
        self.playerX = 0
        self.playerChars = {"up":"↑", "down":"↓", "left":"←", "right":"→"}
    
    def make_grid(self):
        for _ in range(self.gridY):
            self.grid.append([self.empty_grid for _ in range(self.gridX)]) 
        
    def print_grid(self):
        for column in self.grid:
            print(*[str(item) + " " for item in column])
            
    def inject_player(self, injectY, injectX):
        self.playerY = injectY
        self.playerX = injectX
        self.grid[injectY][injectX] = self.playerChars["up"]
        
    def move_player(self, moveY, moveX):
        if not ((abs(moveY) == 1 and moveX == 0) or (abs(moveX) == 1 and moveY == 0)):
            return

        newY = self.playerY + moveY
        newX = self.playerX + moveX

        if not (0 <= newY < self.gridY and 0 <= newX < self.gridX):
            return

        self.grid[self.playerY][self.playerX] = self.empty_grid

        self.playerY = newY
        self.playerX = newX

        if moveY == -1:
            inject_phase = self.playerChars["up"]
        elif moveY == 1:
            inject_phase = self.playerChars["down"]
        elif moveX == -1:
            inject_phase = self.playerChars["left"]
        elif moveX == 1:
            inject_phase = self.playerChars["right"]

        self.grid[self.playerY][self.playerX] = inject_phase


            
def main():
    
    grid = Grid(10, 10, "#")
    grid.make_grid()
    grid.inject_player(2, 2)
    grid.print_grid()
    while True:
        os.system("cls")
        grid.move_player(1, 0)
        grid.print_grid()
        time.sleep(0.5)
    
    
main()
