import os, time

class Grid:
    
    def __init__(self, grid_y, grid_x):
        self.grid_y = grid_y
        self.grid_x = grid_x
        self.player_y = 0
        self.player_x = 0
        
        self.empty_grid = "#"
        self.player_char = "@"
        
        self.grid = [[self.empty_grid for _ in range(grid_x)] for _ in range(grid_y)]
                
    def __str__(self):
        buffer_list = []
        for index, row in enumerate(self.grid):
            if index == self.player_y:
                buffer_list.append(" ".join([self.player_char + " " if index == self.player_x else char + " " for index, char in enumerate(self.grid[index])]))
            else:
                buffer_list.append(" ".join([char + " " for char in row]))
        return "\n".join(buffer_list)

    def move_player(self, dy, dx):
        new_y = self.player_y + dy
        new_x = self.player_x + dx
        
        if new_y < 0 or new_y >= self.grid_y or new_x < 0 or new_x >= self.grid_x:
            return
        
        self.player_y = new_y
        self.player_x = new_x
        
            
def main():
    
    grid = Grid(10, 10)
    
    while True:
        #grid.print_grid()
        print(grid)
        time.sleep(0.2)
        os.system("cls")
        grid.move_player(1, 1)
main()