import pygame
from constants import * 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main(): 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2  
    player = Player(x, y)
    asteroid_field = AsteroidField()    
    dt = 0 
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for u in updatable: 
            u.update(dt)

        for a in asteroids: 
            if a.detect_collision(player): 
                print("Game over!")
                return
            for s in shots: 
                if s.detect_collision(a): 
                    s.kill()
                    a.split()

        screen.fill("black")
        
        for d in drawable: 
            d.draw(screen)

        pygame.display.flip()
       
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()