import pygame
import math

class Flow_calculation:
    """computation part of liquid flow"""
    def __init__(self, height_position):
        self.height_position = height_position
        # self.x = height_position[0]
        # self.y = height_position[1]
        
    def velocity(self):
        pass
    
    def horizontal_flow(self):
        self.x = self.height_position
        return self.x
     

class Point:
    """about location of point"""
    def __init__(self, x , y, screen, color):
        self.x = x
        self.y = y
        self.screen = screen
        self.color = color
        
        
    def draw(self):
        rect = pygame.Rect(self.x, self.y, 10, 10)
        pygame.draw.ellipse(self.screen, self.color, rect)