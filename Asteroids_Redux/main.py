import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    astertoids = pygame.sprite.Group()

    Player.containers = updateable, drawable
    Asteroid.containers = updateable, drawable, astertoids
    AsteroidField.containers = updateable
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))  # Clear the screen with black
        updateable.update(dt)
        for asteroid in astertoids:
            if asteroid.get_collision(player):
                print("Game Over!")
                exit()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()  # Update the display
        dt = clock.tick(60) / 1000 # Limit to 60 FPS
        

if __name__ == "__main__":
    main()
