from circleshape import *
from constants import *
from logger import *
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)
        

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, 1)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt


    def split(self):
        x = self.position.x
        y = self.position.y
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        vect1 = self.velocity.rotate(angle)
        vect2 = self.velocity.rotate(-angle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(x, y, new_rad)
        ast1.velocity = vect1*1.2
        ast2 = Asteroid(x, y, new_rad)
        ast2.velocity = vect2*1.2



