import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    Player.containers = (updatable, drawable,shots)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,PLAYER_RADIUS)
    while True:
        font = pygame.font.Font(None, 36) 
        score_text = font.render(f'Score: {player.score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.collides_with(bullet):
                    asteroid.split()
                    bullet.kill()
                    player.score+=1
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
        pygame.Surface.fill(screen,color=(0,0,0))
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = float(pygame.time.Clock().tick(60)) / 1000
if __name__ == "__main__":
    main()