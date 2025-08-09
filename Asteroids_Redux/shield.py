import pygame
from constants import *
from circleshape import CircleShape

class ShieldPod(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHIELD_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(screen, BLUE, self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt