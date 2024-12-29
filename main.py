import pygame
import sys
from pygame import Color
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0


    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)




    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    # Main Game Loop
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for ob in updateable:
            ob.update(dt)

        for asteroid in asteroids:
            if asteroid.collides(player):
                print("Game over!")
                sys.exit()
        
        screen.fill(Color(0, 0, 0))
        
        for ob in drawable:
            ob.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()