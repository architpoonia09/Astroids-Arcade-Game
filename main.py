import pygame as pg
from constants import *
from logger import log_state
import player

def main():
    pg.init()
    print(f"Starting Asteroids with pygame version: {pg.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()
    dt = 0.0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player1 = player.Player(x, y)


    while True:
        log_state()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        screen.fill("black")    
        player1.draw(screen)
        player1.update(dt)

        clock.tick(60)
        dt = clock.tick(60) / 1000
        pg.display.flip()
            

if __name__ == "__main__":
    main()