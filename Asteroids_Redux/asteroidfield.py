import pygame
import random
from asteroid import Asteroid
from constants import *


class AsteroidField(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity, edge_number, kind):
        if edge_number == 0:  # Right edge
            x = position.x - radius
            y = position.y
        elif edge_number == 1:  # Left edge
            x = position.x + radius
            y = position.y
        elif edge_number == 2:  # Top edge
            x = position.x
            y = position.y - radius
        elif edge_number == 3:  # Bottom edge
            x = position.x
            y = position.y + radius
        asteroid = Asteroid(x, y, radius)
        asteroid.velocity = velocity


    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge_number = random.randint(0, len(EDGES) - 1)
            edge = EDGES[edge_number]
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            new_radius = ASTEROID_MIN_RADIUS * kind
            self.spawn(new_radius, position, velocity, edge_number, kind)

