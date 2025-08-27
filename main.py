import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    # top level initialising
    pygame.init()
    clock = pygame.time.Clock()

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # logic initialising
    dt = 0

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update logic
        for thing in updatable:
            thing.update(dt)

        for rock in asteroids:
            if rock.collision_check(player):
                print("Game over!")
                sys.exit()

        # draw logic
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()

        # adjust clock before proceeding
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
