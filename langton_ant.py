import pygame, sys
import numpy as np
import time
import random
from pygame.locals import *

size = 5 # size of 1 block in pixels
padding = 10
update_delay = 0

def random_grid(size):
    """100/frac is the percentage of black boxes in the grid"""
    arr = np.empty(size, dtype=int)
    ylen = size[1]
    xlen = size[0]

    for y in xrange(ylen):
        for x in xrange(xlen):
            arr[x,y] = random.choice([0,1,2])

    return arr

def main(xnum, ynum):
    global size, padding, update_delay
    height, width = xnum*size + 2*padding, ynum*size + 2*padding
    
    #arr = random_grid((xnum, ynum))
    arr = np.zeros((xnum,ynum))
    
    # position and direction of ant
    ant = [complex(xnum/2, ynum/2), complex(1,0)]
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((height, width))
    pygame.display.set_caption("Langton's Ant")

    BLUE = (0,0,255)
    GREEN = (0,255,0)
    RED = (255, 0, 0)

    while True:
        # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        X = ant[0].real
        Y = ant[0].imag

        y = padding + size*Y
        x = padding + size*X

        # if cell is red
        if arr[X,Y]==2:
            # change color to blue
            arr[X,Y]=1
            pygame.draw.rect(DISPLAYSURF, BLUE, (x,y,size,size))
            # turn right
            ant[1]*= -1j
        # if cell is blue
        elif arr[X,Y]==1:
            # change color to green
            arr[X,Y]=0
            pygame.draw.rect(DISPLAYSURF, GREEN, (x,y,size,size))
            # turn left
            ant[1]*= 1j         
        # if cell is green
        elif arr[X,Y]==0:
            # change color to red
            arr[X,Y]=2
            pygame.draw.rect(DISPLAYSURF, RED, (x,y,size,size))
            # turn right
            ant[1]*= -1j
            
        ant[0] += ant[1]

        if ant[0].real>=xnum or ant[0].imag>=ynum or ant[0].real<0 or ant[0].imag<0:
            ant[0] -= ant[1]
            ant[1] *= 1j
                
        pygame.display.update()

        #time.sleep(update_delay/1000.0)

if __name__ == '__main__':
    main(100,111)
