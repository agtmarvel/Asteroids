# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

#FPS
	clock = pygame.time.Clock()


#Groups
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	
#Containers
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable,)

#Creating player instance
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
#Creating asteroid field instance
	asteroid_field = AsteroidField()

#Game loop

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		#print(f"FPS: {clock.get_fps()}")
		screen.fill("black")
		for drawable_object in drawable:
			drawable_object.draw(screen) #Draw Player
		pygame.display.flip()
		dt = clock.tick(60) / 1000
		updatable.update(dt)


if __name__ == "__main__":
	main()
