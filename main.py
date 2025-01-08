# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import AsteroidField
from shot import Shot
#from circleshape import CircleShape

def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField()
    #CircleShape()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt=0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000000)
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:  # iterate through asteroids
            if player.collisions(asteroid):  # assuming this is your collision method
                print("Game over!")
                sys.exit()

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()        
        dt = clock.tick(60) / 1000
        #print(f"{dt}")
if __name__ == "__main__":
    main()

