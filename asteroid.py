import pygame
from constants import *
from circleshape import CircleShape
import random



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle_1 = random.uniform(20, 50)
            angle_2 = -random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            #create two new asteroids at this position
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

            #Give them velocities in a different direction
            new_asteroid_1.velocity = self.velocity.rotate(angle_1)
            new_asteroid_2.velocity = self.velocity.rotate(angle_2)
