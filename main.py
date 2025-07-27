import pygame
import sys
import asteroid
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    font = pygame.font.Font("DejaVuSansMono.ttf", 36)

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Shot.containers = (updatable, drawable, shots)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0, 0, 0))
        updatable.update(dt)

        for ast in asteroids:
            if player.collision_check(ast):
                print("Game Over!")
                sys.exit()
            for bullet in shots:
                if bullet.collision_check(ast):
                    ast.split()
                    bullet.kill()
        
        score_text = font.render("Score: " + str(asteroid.score), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000

        
if __name__ == "__main__":
    main()
