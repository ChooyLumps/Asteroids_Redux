import pygame
from constants import *
# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def get_collision(self, target):
        distance = self.position.distance_to(target.position)
        if distance <= (self.radius + target.radius):
            return True
        return False
    
    def get_touching_edge(self):
        for edge in EDGES:
            edge_normal = edge[0]
            edge_point = edge[1](self.position.x if edge_normal.y == 0 else self.position.y)
            to_circle = self.position - edge_point
            distance = to_circle.dot(edge_normal)
            if distance < self.radius:
                return True
        return False
        
    def bump(self):
        temp_timer = 0
        def change_course(list_of_objects):
            nonlocal temp_timer
            temp_timer += 1
            if temp_timer > 10:
                for obj in list_of_objects:
                    if self != obj and self.get_collision(obj):
                        self.velocity = -self.velocity

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass