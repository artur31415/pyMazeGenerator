import pygame
from random import *

from cell import Cell

pygame.init()
pygame.font.init()

# seed random number generator
#seed(1)
################################################################################################
#                                           VARIABLES
################################################################################################
width = 700
height = 700

screen = pygame.display.set_mode([width, height])

myfont = pygame.font.SysFont('Comic Sans MS', 20)

running = True


ticks = 0

clock = pygame.time.Clock()


cells = []
cell_size = 50

grid_resolution_x = int(width / cell_size)
grid_resolution_y = int(height / cell_size)

current_cell_pos = (0, 0)

walk_dirs = [
    (-1, 0), 
    (0, -1),
    (1, 0),
    (0, 1)
]

visited_cell_positions = []
################################################################################################
#                                           FUNCTIONS
################################################################################################
def initCells():
    for i in range(grid_resolution_x):
        cells.append([])
        for j in range(grid_resolution_y):
            new_cell = Cell((i, j), {"Left": True, "Bottom": True, "Right": True, "Top": True})
            cells[i].append(new_cell)
################################################################################################
#                                           MAIN LOOP
################################################################################################

initCells()

# for i in range(len(cells)):
#         for j in range(len(cells[i])):
#             print("cells [", str(i), "][", str(j), "] = ", cells[i][j].to_string())

cells[current_cell_pos[0]][current_cell_pos[1]].visited = True

while running:

    ##################################################################
    # EVENTS
    ##################################################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                pass

    ##################################################################
    # STATE UPDATE
    ##################################################################

    

    search_count = 0
    while True:
        walk_dir = walk_dirs[randint(0, len(walk_dirs) - 1)]
    
        neighbour_pos = (current_cell_pos[0] + walk_dir[0], current_cell_pos[1] + walk_dir[1])
        #print(str(neighbour_pos))
        if neighbour_pos[0] >= 0 and neighbour_pos[0] < grid_resolution_x and neighbour_pos[1] >= 0 and neighbour_pos[1] < grid_resolution_y:
            #print("here1")
            if not cells[neighbour_pos[0]][neighbour_pos[1]].visited:
                current_dir = Cell.grid_to_dir(walk_dir)
                neighbour_dir = Cell.grid_to_dir((-walk_dir[0], -walk_dir[1]))
                cells[current_cell_pos[0]][current_cell_pos[1]].walls[current_dir] = False
                cells[neighbour_pos[0]][neighbour_pos[1]].walls[neighbour_dir] = False
                current_cell_pos = neighbour_pos
                cells[current_cell_pos[0]][current_cell_pos[1]].visited = True
                print(current_dir, "; ", neighbour_dir)
                break
        search_count += 1
        if search_count >= len(walk_dirs):
            print("STUCK! ", str(current_cell_pos))


    ##################################################################
    # DRAW CODE
    ##################################################################

    


    screen.fill((0, 0, 0))

    for i in range(len(cells)):
        for j in range(len(cells[i])):
            cells[i][j].draw(screen, cell_size)
            if (i, j) == current_cell_pos:
                pygame.draw.rect(screen, (100, 100, 0), (i * cell_size + cell_size / 4, j * cell_size + cell_size / 4, cell_size / 2, cell_size / 2))

    # if oldest_vehicle != None:
    #     pygame.draw.circle(screen, (255, 255, 255), oldest_vehicle.position, 20, 2)
    #     textsurface = myfont.render('pop = ' + str(len(vehicles)) + ' ; oldest is ' + str(oldest_vehicle.alive_tick) + ' ticks alive!', False, (255, 255, 255))
    #     screen.blit(textsurface, (20, 20))
    ##################################################################
    # Flip the display
    ##################################################################
    pygame.display.flip()

    clock.tick(5)
    

# Done! Time to quit.
pygame.quit()