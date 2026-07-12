from circleshape import *
from constants import *
import pygame as pg



class Shot(CircleShape):
    def __init__(self, x,y):
        super().__init__( x,y, SHOT_RADIUS)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, 1)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt