from circleshape import CircleShape
from constants import *
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen,color="white",center = self.position, radius=self.radius,  width=2)

    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            one_vector = self.velocity.rotate( random_angle)
            two_vector = self.velocity.rotate( -random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            one_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            one_asteroid.velocity = one_vector * 1.2
            two_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            two_asteroid.velocity = two_vector * 1.2

