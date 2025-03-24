import pygame
from circleshape import *

class Shot(CircleShape):
	def __init__(self, x, y):
		SHOT_RADIUS = 5
		super().__init__(x, y, SHOT_RADIUS)
		self.lifetime = 1.5
	def draw(self, surface):
		pygame.draw.circle(surface, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius)
	def update(self, dt):
		self.position += self.velocity * dt
		self.lifetime -= dt
		if self.lifetime <= 0:
			self.kill()
