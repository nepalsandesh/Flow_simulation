import pygame
import numpy
from  calculus import Flow_calculation, Point

pygame.init

width = 1920
height = 1080
resolution = (width, height)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Liquid Flow Simulation")
clock = pygame.time.Clock()
FPS = 60

# color 
background = (0,0,0)
white = (255, 255, 255)

top_array = numpy.arange(0, 1000, 10)

offset = 0



while True:
    
    screen.fill(background)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    

    for height in top_array:
        fl = Flow_calculation(height)
        x_pos = fl.horizontal_flow() * offset
        point = Point(x_pos, height, screen, white)
        point.draw()
        
    offset += 0.01
        
        
        

    
    
    
    pygame.display.flip()
    clock.tick(FPS)