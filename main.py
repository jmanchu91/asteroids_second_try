import pygame # type: ignore
import sys
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = clock.tick(60) / 1000

    # Initialize sprite groups
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Assign static containers for classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    # Create instances of Player and AsteroidField
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update all updatable sprites
        updatable.update(dt)

        # Check for asteroid collision with player 
        for asteroid in asteroids:
            if asteroid.check_collision(player) == True:
                print("Game Over!")
                sys.exit()

        # Check for asteroid collision with bullet
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collision(shot) == True:
                    asteroid.split()
                    shot.kill()


        #Clear the screen for refreshing visuals
        screen.fill((0,0,0))

        # Draw all drawable sprites
        for entity in drawable:
            entity.draw(screen)

        # Update the display     
        pygame.display.flip()

        # Limit the frame rate and calculate time delta
        dt = clock.tick(60) /1000

if __name__ == "__main__":
    main()