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
################################################################################################
#                                           FUNCTIONS
################################################################################################
def initCells():
    for i in range(int(width / cell_size)):
        cells.append([])
        for j in range(int(height / cell_size)):
            cells[i].append(Cell((i, j)))
################################################################################################
#                                           MAIN LOOP
################################################################################################

initCells()
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


    ##################################################################
    # DRAW CODE
    ##################################################################

    


    screen.fill((0, 0, 0))

    for i in range(len(cells)):
        for j in range(len(cells[i])):
            cells[i][j].draw(screen, cell_size)

    # if oldest_vehicle != None:
    #     pygame.draw.circle(screen, (255, 255, 255), oldest_vehicle.position, 20, 2)
    #     textsurface = myfont.render('pop = ' + str(len(vehicles)) + ' ; oldest is ' + str(oldest_vehicle.alive_tick) + ' ticks alive!', False, (255, 255, 255))
    #     screen.blit(textsurface, (20, 20))
    ##################################################################
    # Flip the display
    ##################################################################
    pygame.display.flip()

    clock.tick(20)
    

# Done! Time to quit.
pygame.quit()