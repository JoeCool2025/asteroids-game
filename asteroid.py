import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

score = 0

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (int(self.position.x), int(self.position.y)),
            self.radius,
            2
        )

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        global score
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            score += 100
            return
        if ASTEROID_MIN_RADIUS <= self.radius <= ASTEROID_MIN_RADIUS * 2:
            score += 50
        if self.radius > ASTEROID_MIN_RADIUS * 2:
            score += 20
        new_angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(new_angle)
        vector2 = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vector1 * 1.2
        asteroid2.velocity = vector2 * 1.2