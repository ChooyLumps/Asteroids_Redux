import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))  # Clear the screen with black
        player.draw(screen)  # Draw the player
        pygame.display.flip()  # Update the display
        dt = clock.tick(60) / 1000 # Limit to 60 FPS
        

if __name__ == "__main__":
    main()
