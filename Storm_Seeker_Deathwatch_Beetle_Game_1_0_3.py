import pygame
import random

pygame.init()

screenWidth = 800
screenHeight = 256

win = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption('Deathwatch Beetle Runner')
#load images
background = pygame.image.load('game_data/background.png')
walk_right = [pygame.image.load('game_data/R1.png'), pygame.image.load('game_data/R2.png'), pygame.image.load('game_data/R3.png'), pygame.image.load('game_data/R4.png'), pygame.image.load('game_data/R5.png'), pygame.image.load('game_data/R6.png'), pygame.image.load('game_data/R7.png'), pygame.image.load('game_data/R8.png'), pygame.image.load('game_data/R9.png')]
hamster_anim = [pygame.image.load('game_data/hamster1.png'), pygame.image.load('game_data/hamster2.png'), pygame.image.load('game_data/hamster3.png')]
parrot_anim = [pygame.image.load('game_data/parrot1.png'), pygame.image.load('game_data/parrot2.png'), pygame.image.load('game_data/parrot3.png')]
beetle_anim = [pygame.image.load('game_data/deathwatch_beetle1.png'), pygame.image.load('game_data/deathwatch_beetle2.png'), pygame.image.load('game_data/deathwatch_beetle3.png')]
char = pygame.image.load('game_data/standing.png')
logo = pygame.image.load('game_data/Logo.png')
music = pygame.mixer.music.load('game_data/Deathwatch_Game_Music.wav')

clock = pygame.time.Clock()

#defining classes (player, enemy, beetle)
class player(object):
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self. width = width
		self.height = height
		self.isJump = False
		self.jumpcount = 15
		self.right = True
		self.walkCount = 0
		self.hitbox = (self.x + 19, self.y + 10, 25, 51)

	def draw(self, win):
		if self.walkCount + 1 >= 27:
			self.walkCount = 0

		if self.right:
			win.blit(walk_right[self.walkCount//3], (self.x,self.y))
			self.walkCount +=1
		# draw hitbox
		self.hitbox = (self.x + 19, self.y + 10, 25, 51)
		#pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class enemy(object):
	def __init__(self, x, y, width, height, e_type, velocity):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.walkCount = 0
		self.vel = velocity
		self.e_type = e_type
		self.hitbox = (self.x + 6, self.y + 6, 56, 50)

	def draw(self, win):
		if self. walkCount + 1 >= 27:
			self.walkCount = 0

		if self.e_type == 'hamster':
			win.blit(hamster_anim[self.walkCount//7], (self.x, self.y))

		if self.e_type == 'parrot':
			win.blit(parrot_anim[self.walkCount//7], (self.x, self.y))
		# draw hitbox
		self.hitbox = (self.x + 6, self.y + 6, 56, 50)
		#pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class beetle(object):
	def __init__(self, x, y, width, height, velocity):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.walkCount = 0
		self.vel = velocity
		self.hitbox = (self.x + 6, self.y + 12, 58, 50)

	def draw(self, win):
		win.blit(beetle_anim[self.walkCount//7], (self.x, self.y))
		# draw hitbox
		self.hitbox = (self.x + 6, self.y + 12, 58, 50)
		#pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class bg_anim(object):
	def __init__(self, x):
		self.x = x
		self.y = 0
		walkCount = 0

	def draw(self, win):
		win.blit(background[self.walkCount])

def ending_screen():
	for backgrounds in background_list:
		win.blit(background, (backgrounds.x, backgrounds.y))
	win.blit(logo, (10,5))
	text = credits_font.render('created by Cpt Timothy Abor', 1, (0,0,0))
	win.blit(text, (10, screenHeight - 20))
	win.blit(char, (pirate.x, pirate.y))
	for enemy_var in enemy_list:
		enemy_var.draw(win)
	for beetle_var in beetle_list:
		beetle_var.draw(win)
	if score == 1:
		text1 = ending_screen_font.render('Arr, you collected', 1, (0,0,0))
		text2 = ending_screen_font.render(str(score), 1, (0,0,0))
		text3 = ending_screen_font.render('parrtying Deathwatch-Beetle!', 1, (0,0,0))
		win.blit(text1, (100, 70))
		win.blit(text2, (100, 110))
		win.blit(text3, (100, 150))
	elif score == 0:
		text1 = ending_screen_font.render('Arr, you collected', 1, (0,0,0))
		text2 = ending_screen_font.render('not a single of those sweet,', 1, (0,0,0))
		text3 = ending_screen_font.render('parrtying Deathwatch-Beetles!', 1, (0,0,0))
		win.blit(text1, (100, 70))
		win.blit(text2, (100, 110))
		win.blit(text3, (100, 150))
	else:
		text1 = ending_screen_font.render('Arr, you collected', 1, (0,0,0))
		text2 = ending_screen_font.render(str(score), 1, (0,0,0))
		text3 = ending_screen_font.render('parrtying Deathwatch-Beetles!', 1, (0,0,0))
		win.blit(text1, (100, 70))
		win.blit(text2, (100, 110))
		win.blit(text3, (100, 150))
	pygame.display.update()


#drawing
def redrawGameWindow():

	for backgrounds in background_list:
		win.blit(background, (backgrounds.x, backgrounds.y))
	pirate.draw(win)
	win.blit(logo, (10,5))
	text = credits_font.render('created by Cpt Timothy Abor', 1, (0,0,0))
	win.blit(text, (10, screenHeight - 20))
	for enemy_var in enemy_list:
		enemy_var.draw(win)
	for beetle_var in beetle_list:
		beetle_var.draw(win)
	text = game_font.render(str(score), 1, (87,89,0))
	win.blit(text, (screenWidth - 100, 10))

	pygame.display.update()

background_list = [bg_anim(0), bg_anim(128), bg_anim(256), bg_anim(384), bg_anim(512), bg_anim(640), bg_anim(768), bg_anim(896)]
game_font = pygame.font.SysFont('nordin', 40, True)
ending_screen_font = pygame.font.SysFont('nordin', 50, True)
credits_font = pygame.font.SysFont('nordin', 20, True)
enemy_list = []
beetle_list = []
pirate = player(50, screenHeight - 100, 64, 64)
durchlauf = 0
velocity = 7
bg_velo = 4
hamster_buffer = 0
parrot_buffer = 0
score = 0

pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

#mainloop
ending_loop = False
run =  True
while run:
	clock.tick(27)



	if ending_loop:
		ending_screen()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			run = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

	else:

		durchlauf += velocity
		if durchlauf > 210:
			zufall = random.randint(0,5)
			if zufall < 2:
				#hamster
				if hamster_buffer < 3:
					enemy_list.append(enemy(screenWidth, screenHeight-100, 64, 64, 'hamster', velocity))
					hamster_buffer += 1
				else:
					hamster_buffer = random.randint(0,2)
			if zufall > 1 and zufall < 4:
				#parrot
				if parrot_buffer <3:
					enemy_list.append(enemy(screenWidth, screenHeight-200, 64, 64, 'parrot', velocity))
					parrot_buffer +=1
				else:
					parrot_buffer = random.randint(0,2)
			if zufall == 4:
				beetle_list.append(beetle(screenWidth, screenHeight-100, 64, 64, velocity))
				#beetle
			durchlauf = 0

		for enemy_var in enemy_list:
			if enemy_var.y < pirate.hitbox[1] + pirate.hitbox[3] and enemy_var.y + enemy_var.height > pirate.hitbox[1]:
				if enemy_var.x < pirate.hitbox[0] + pirate.hitbox[2] and enemy_var.x + enemy_var.width > pirate.hitbox[0]:
					#end the game
					ending_loop = True


			if enemy_var.x < screenWidth+100 and enemy_var.x > -64:
				enemy_var.x -= velocity
			else:
				enemy_list.pop(enemy_list.index(enemy_var))

		for beetle_var in beetle_list:
			if beetle_var.y < pirate.hitbox[1] + pirate.hitbox[3] and beetle_var.y + beetle_var.height > pirate.hitbox[1]:
				if beetle_var.x < pirate.hitbox[0] + pirate.hitbox[2] and beetle_var.x + beetle_var.width > pirate.hitbox[0]:
					#define function to end the game
					beetle_list.pop(beetle_list.index(beetle_var))
					score += 1
					#print(score)
					velocity += 1
					bg_velo += 1
			if beetle_var.x < screenWidth+100 and beetle_var.x > -64:
				beetle_var.x -= velocity
			else:
				beetle_list.pop(beetle_list.index(beetle_var))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False



		for backgrounds in background_list:
			backgrounds.x -= bg_velo
			if backgrounds.x < -128:
				background_list.pop(background_list.index(backgrounds))
				background_list.append(bg_anim(896))

		
		keys = pygame.key.get_pressed()
		if not(pirate.isJump):
			if keys[pygame.K_SPACE]:
				pirate.isJump = True
		else:
			if pirate.jumpcount >= -15:
				neg = 1
				if pirate.jumpcount <0:
					neg = -1
				pirate.y -= ((pirate.jumpcount ** 2) * 0.10) * neg
				pirate.jumpcount -= 1
			else:
				pirate.isJump = False
				pirate.jumpcount = 15

		redrawGameWindow()




pygame.quit()

"""
while ending_loop:
	clock.tick(27)
	ending_screen
	keys = pygame.key.get_pressed()
	if keys[pygame.K_SPACE]:
		break
"""


