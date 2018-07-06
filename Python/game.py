import os, pygame, random

from settings import Settings
from button import Button
from mit import MIT


class Game():
	def __init__(self):
		self.background = pygame.image.load("images/egg.jpg")
		self.enemy = None
		self.mits = [
		MIT("R"),
		MIT("Garfield"),
		MIT("Soup"),
		MIT("Cosmic Egg"),
		MIT("Cholesterol"),
		MIT("Shigeru Miyamoto"),
		MIT("Business man"),
		MIT("Vladimir Putin")
		]
		random.shuffle(self.mits)

		self.font = pygame.font.SysFont('Comic Sans MS', 20)

		self.buttons = [

			Button(0, Settings.height - 100, 100, 100, "fight", "Fight"),
			Button(Settings.width - 100, Settings.height - 100, 100, 100, "flee", "Flee"),
		]

	def loop(self, screen):
		clock = pygame.time.Clock()

		while True:

			if not self.enemy:
				self.enemy = self.mits.pop()
				self.text = self.font.render(self.enemy.name, False, (0, 0, 0))

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

			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					x, y = event.pos
					for button in self.buttons:
						if button.isClicked(x, y):
							if button.id == "fight":
								damage = self.attack()
								if self.enemy.isAlive():
									self.enemy.health -= self.enemy.damage
									if self.enemy.health < 0:
										self.enemy = None
									elif self.enemy.health == 0:
										self.enemy = None
								elif button.id == "flee":
									caught = random.randint(1,5) == 1
									if not caught:
										print("Your score was {}".format(score))
										sys.exit(0)
									else:
										print("You failed to flee!")

	def attack(self):
		return random.randint(1, 10)
	def quit(self):
		pass
