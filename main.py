# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import random
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

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
	shot = pygame.sprite.Group()
#Containers
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable,)
	Shot.containers = (shot, updatable, drawable)
#Creating player instance
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
#Creating asteroid field instance
	asteroid_field = AsteroidField()

#Game loop

	while True:
    # Handle events first
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
    # Get the time delta for this frame
		dt = clock.tick(60) / 1000
    # Update player ONCE and get any new shots
		new_shot = player.update(dt)
		if new_shot:
			shot.add(new_shot)
    # Update all other game objects
    # If player is in updatable group, remove it to avoid double updates
    # updatable.remove(player)  # Uncomment if needed
		updatable.update(dt)
    # Check collisions
		for asteroid in asteroids:
			for bullet in shot:
				if asteroid.collision(bullet):
					bullet.kill()
					asteroid.split()
					break
			if player.collision(asteroid):
				print("Game over!")
				sys.exit()
    # Draw everything
		screen.fill("black")
		for drawable_object in drawable:
			drawable_object.draw(screen)
    # Update the display
		pygame.display.flip()

if __name__ == "__main__":
	main()
