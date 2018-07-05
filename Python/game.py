import os, pygame, random

from settings import Settings
from button import Button
from mit import MIT

class Game():
	def __init__(self):
		self.background = pygame.image.load("images/egg.png")
		self.enemy = None
		self.mits = [
		MIT("R"),
		MIT("Garfield")
		]
		random.shuffle(self.mits)

		self.font = pygame.font.SysFont('Comic Sans MS', 30)

		self.buttons = [

			Button(0, Settings.height - 100, 100, 100, "Fight"),
			Button(Settings.width - 100, Settings.height - 100, 100, 100, "Flee"),
		]

	def loop(self, screen):
		clock = pygame.time.Clock()

		if not self.enemy:
			self.enemy = self.mits.pop()
			self.text = self.font.render(self.enemy.name, False, (0, 0, 0))

		while True:
			delta_t = clock.tick(Settings.frameRate)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return

			screen.fill((0, 0, 0))
			screen.blit(self.background, (0, 0))

			screen.blit(self.enemy.img, (Settings.width - 150, 0))
			pygame.draw.rect(screen, (0, 0, 0), (Settings.width - 150, 150, 100, 10))
			pygame.draw.rect(screen, (0, 255, 0), (Settings.width - 150, 150,(self.enemy.health / 20) * 100, 10))
			screen.blit(self.text, (Settings.width -150, 100))

			for button in self.buttons:
				pygame.draw.rect(screen, (0, 0, 255), (button.x, button.y, button.w, button.h))
				screen.blit(button.text, (button.x, button.y))
			pygame.display.flip()

	def quit(self):
		pass
