import sys

import pygame as pg
from constants import *
from logger import log_state
from player import *
from asteroid import *
from asteroidfield import *
from logger import *
from shot import *

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

    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()
    Player.containers = (updatable, drawable)
    player1 = Player(x, y)
    asteroids = pg.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    astroidfield = AsteroidField()
    shots = pg.sprite.Group()
    Shot.containers = (updatable, drawable, shots)

    while True:
        log_state()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        screen.fill("black")    
        updatable.update(dt)
        for drawa in drawable:
            drawa.draw(screen)

        for ast in asteroids:

            for shot in shots:
                if shot.collides_with(ast):
                    log_event("asteroid_shot")
                    ast.split()
                    shot.kill()
                    break

            if player1.collides_with(ast):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
                return     
        

       

        dt = clock.tick(60) / 1000
        pg.display.flip()
            

if __name__ == "__main__":
    main()