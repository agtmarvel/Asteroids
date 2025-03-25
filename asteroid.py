import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y,  radius)
		self.position = pygame.Vector2(x, y)
		self.radius = radius
	def draw(self, surface):
		pygame.draw.circle(surface, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)
	def update(self, dt):
		self.position += self.velocity * dt
	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		
		#print(f"Splitting asteroid at {self.position} with radius {self.radius}")
		
		new_radius = self.radius - ASTEROID_MIN_RADIUS
		random_angle = random.uniform(20, 50)
		new_vel1 = self.velocity.rotate(random_angle) * 1.2
		new_vel2 = self.velocity.rotate(-random_angle) * 1.2
		
		new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
		new_asteroid1.velocity = new_vel1
		new_asteroid1.containers = self.containers

		new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
		new_asteroid2.velocity = new_vel2
		new_asteroid2.containers = self.containers

		#print(f"Created new asteroids with radius {new_radius}")
		#print(f"Original asteroid groups: {self.groups()}")

		for group in self.groups():
			group.add(new_asteroid1)
			group.add(new_asteroid2)
			#print(f"Added new asteroids to group: {group}")
