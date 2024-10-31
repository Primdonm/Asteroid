# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
i = True
def main():
    pygame.init()
    dt=0
    delta_Clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while i is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000000)
        pygame.display.flip()
        delta_Clock.tick(60)
        dt = delta_Clock.tick(60) / 1000
        #print(f"{dt}")
if __name__ == "__main__":
    main()

