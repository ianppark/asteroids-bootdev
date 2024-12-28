import pygame
from pygame import Color
from constants import *
from player import Player

def main():
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    # Main Game Loop
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            

        screen.fill(Color(0, 0, 0))
        player.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()