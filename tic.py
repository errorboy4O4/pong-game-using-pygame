import pygame

pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
pink = (255, 0, 255)
blue = (0, 0, 255)
width = 800
height = 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("PING PONG")
# player1

player_x = 10
player_y = 200
player_speed = 0

# player 2

player_1 = 770
player_2 = 200
enemy_speed = 0

# circle

circle_x = 380
circle_y = 300
circle_x_speed = 1
circle_y_speed = 1

# SCORE
score_a = 0
score_b = 0

FPS = 60

clock = pygame.time.Clock()

run = False

while not run:
	win.fill(green)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				player_speed -= 1

			if event.key == pygame.K_DOWN:
				player_speed += 1

			if event.key == pygame.K_RIGHT:
				enemy_speed += 1

			if event.key == pygame.K_LEFT:
				enemy_speed -= 1

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
				enemy_speed = 0
			if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				player_speed = 0

	player_y += player_speed
	player_2 += enemy_speed
	circle_x += circle_x_speed
	circle_y += circle_y_speed

	if player_y < 0:
		player_y = 0
	elif player_y >= 497:
		player_y = 497

	if player_2 < 0:
		player_2 = 0
	elif player_2 >= 497:
		player_2 = 497

	if circle_y > 580:
		circle_y = 580
		circle_y_speed *= -1

	if circle_y < 10:
		circle_y = 10
		circle_y_speed *= -1

	if circle_x > 780:
		circle_x = 380
		circle_x_speed *= -1
		score_a += 1

	if circle_x < 10:
		circle_x = 300
		circle_x_speed *= -1
		score_b += 1

	if circle_x > 760 and circle_y < player_2 + 90 and circle_y > player_2 - 90:
		circle_x = 760
		circle_x_speed *= -1


	elif circle_x < 50 and circle_y < player_y + 90 and circle_y > player_y - 90:
		circle_x = 50
		circle_x_speed *= -1

	font = pygame.font.Font('freesansbold.ttf', 32)
	text = font.render("Player A: " + str(score_a), True, (blue))
	win.blit(text, (200, 10))

	font = pygame.font.Font('freesansbold.ttf', 32)
	text1 = font.render("Player B: " + str(score_b), True, (pink))
	win.blit(text1, (400, 10))

	pygame.draw.rect(win, pink, (player_x, player_y, 20, 100))
	pygame.draw.rect(win, blue, (player_1, player_2, 20, 100))
	pygame.draw.circle(win, black, (circle_x, circle_y), 20)
	# clock.tick(FPS)
	pygame.display.update()
pygame.quit()
