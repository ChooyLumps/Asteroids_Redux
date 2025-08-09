import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from shieldfield import ShieldField
from shield import ShieldPod

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    score = 0
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    astertoids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    shields = pygame.sprite.Group()

    Player.containers = updateable, drawable
    Asteroid.containers = updateable, drawable, astertoids
    AsteroidField.containers = updateable
    Shot.containers = updateable, drawable, shots
    ShieldPod.containers = updateable, drawable, shields
    ShieldField.containers = updateable
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    shield_field = ShieldField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))  # Clear the screen with black
        updateable.update(dt)

        # Check for collisions
        for asteroid in astertoids:
            if asteroid.get_collision(player) == True:
                if player.shield > 0:
                    player.shield -= 1
                    asteroid.kill()  # Destroy the asteroid if player has shield
                else:
                    print("Game Over")
                    print(f"Final Score: {score}")
                    exit()
            for shot in shots:
                if asteroid.get_collision(shot) == True:
                    asteroid.split()
                    shot.kill()
                    score += 10
        for shield in shields:
            if shield.get_collision(player) == True:
                player.gain_shield()
                shield.kill()
                score += 5
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()  # Update the display
        dt = clock.tick(60) / 1000 # Limit to 60 FPS
        score += 1
        

if __name__ == "__main__":
    main()
