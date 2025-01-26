import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        # player.draw(screen)
        

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        # player.update(dt)
        for player in updatable:
            player.update(dt)
        for player in drawable:
            player.draw(screen)
            pygame.display.flip()


if __name__ == "__main__":
    main()