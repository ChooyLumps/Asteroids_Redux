import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 300
PLAYER_SPEED = 200  
PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN = 0.3 # seconds

SHOT_RADIUS = 5

SHIELD_RADIUS = 7
SHIELD_SPAWN_RATE = 5  # seconds

WHITE = (255, 255, 255)
BLUE = (0, 128, 255)
LIGHT_BLUE = (153, 204, 255)
DARK_BLUE = (0, 102, 204)

EDGES = [
    [   # Right edge
        pygame.Vector2(1, 0),
        lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
    ],
    [   # Left edge
        pygame.Vector2(-1, 0),
        lambda y: pygame.Vector2(SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
    ],
    [   # Top edge
        pygame.Vector2(0, 1),
        lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
    ],
    [   # Bottom edge
        pygame.Vector2(0, -1),
        lambda x: pygame.Vector2(x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS),
    ],
]