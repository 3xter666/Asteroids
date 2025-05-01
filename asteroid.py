from circleshape import *
from constants import *
import random as r
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius,2)
    def update(self,dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = r.uniform(20,50)
            Asteroid_1 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS ))
            Asteroid_2 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS ))
            Asteroid_1.velocity = pygame.math.Vector2.rotate(self.velocity, random_angle) * 1.2
            Asteroid_2.velocity = pygame.math.Vector2.rotate(self.velocity, -random_angle) * 1.2
    