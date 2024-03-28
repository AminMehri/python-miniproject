'''
snakes and ladders game!
design and developed by: Kaylan-mahmoodi-rad & Amin-mehri
'''
import time
import random
from tinydb import TinyDB

# constant: for make delay
DELAY = 0.5

# key: down the ladder - value: top of the ladder
ladders = {  

}

# key: head of the snake - value: tail of the snake
snakes = {

}


def map_design():
	print("Welcome to snake and ladder game!!!\n\n")
	print("You can design your favorite map. stay with us!")
	time.sleep(DELAY)
	design_map = input("do you want design a map? yes or no\n")
	if design_map == 'yes':
		print("Please enter your ideal map width and height")
		width = int(input("width: "))
		height = int(input("height: "))

		# LAST_STEP: number of playhouses
		global LAST_STEP
		LAST_STEP = width * height

		print("You can also set the position of snakes and ladders. let's go")
		time.sleep(DELAY)

		# get head and tail of the snake from user. (press enter when you finished)
		snake = [0]
		while len(snake) != 0:
			snake = input("Enter custom snake from(int) to (int): ").split()
			if len(snake) != 2 or int(snake[0]) <= int(snake[1]):
				print("It's not acceptable")
				continue
			snakes.update({int(snake[0]): int(snake[1])})

		print("\n\n")
		
		# get down and top of the ladder from user. (press enter when you finished)
		ladder = [0]
		while len(ladder) != 0:
			ladder = input("Enter custom ladder from(int) to (int): ").split()
			if len(ladder) != 2 or int(ladder[0]) >= int(ladder[1]) or ladder[0] in snakes or ladder[0] in snakes.values():
				print("It's no acceptable")
				continue
			ladders.update({int(ladder[0]): int(ladder[1])})

		# save map detail in database
		db = TinyDB('db.json')
		db.insert({'height': height, 'width': width, 'LAST_STEP': LAST_STEP, 'snakes': snakes, 'ladders': ladders})
	else:
		# read saved map from data base
		db = TinyDB('db.json')
		for data in db.all():
			print(data)
		map_number = int(input("choose one of these maps\n"))
		new_map = db.all()[map_number]
		print(new_map)
		width = new_map.get('width')
		height = new_map.get('height')
		LAST_STEP = new_map.get('LAST_STEP')

		# save snake position in dictionary
		for snake in new_map.get('snakes'):
			snakes.update({int(snake): new_map.get('snakes')[snake]})
		
		# save ladder position in dictionary
		for ladder in new_map.get('ladders'):
			ladders.update({int(ladder): new_map.get('ladders')[ladder]})
				
	start_game()


def rolling_dice():
	time.sleep(DELAY)
	dice_value = random.randint(1, 6)
	print(f"it's {dice_value}")
	return dice_value


def ladder_jump(player_name, current_pos, next_pos):
	print(f"\n{player_name} jump from {current_pos} to {next_pos}")


def snake_bite(player_name, current_pos, next_pos):
	print(f"\n{player_name} got bite by a snake and fall from {current_pos} to {next_pos}")


def set_pos(player_name, current_pos, dice_value):
	time.sleep(DELAY)
	previous_pos = current_pos
	current_pos = current_pos + dice_value
	if current_pos > LAST_STEP:
		print("you can't move\n")
		return previous_pos
	
	print(f"{player_name} moved from {previous_pos} to {current_pos}\n\n")

	# check for head of snake in this position
	if current_pos in snakes:
		next_pos = snakes.get(current_pos)
		snake_bite(player_name, current_pos, next_pos)
	# check for down of the ladder in this position
	elif current_pos in ladders:
		next_pos = ladders.get(current_pos)
		ladder_jump(player_name, current_pos, next_pos)
	else:
		next_pos = current_pos
	return next_pos


def check_win(player_name, pos):
	time.sleep(DELAY)
	if LAST_STEP == pos:
		print(f"{player_name} won the game!!! \n")
		play_again = input("Do you wanna play again?? (yes) or (no):\n")	
		if play_again == 'no':
			exit()
		elif play_again == 'yes':
			map_design()
		else:
			print("invalid input")
			exit()


def start_game():
	print("I will show you ladders and snakes position\n")
	time.sleep(DELAY)

	# print snake position
	for snake in snakes:
		print(f"there is a snake from {snake} to {snakes[snake]}")
		time.sleep(DELAY)

	print("\nYou got it???\n")

	time.sleep(DELAY + 1)

	# print ladder position
	for ladder in ladders:
		print(f"there is a ladder from {ladder} to {ladders[ladder]}")
		time.sleep(DELAY)
	print("\nNow, let's play game!!!\n")
	play_with_computer = input("do you want to play with computer? yes or no\n")
	time.sleep(DELAY)
	# permission to start moving
	player1_allowed_to_move = False
	player2_allowed_to_move = False

	# players position
	player1_pos = 0
	player2_pos = 0

	# count of 6
	player1_count_6 = 0
	player2_count_6 = 0

	while True:
		input("player1. press enter to roll dice")
		print("Rolling dice")
		dice_value = rolling_dice()
		time.sleep(DELAY)

		# player must roll 6 to start moving
		if player1_count_6 == 0:
			if dice_value == 6:
				player1_count_6 += 1
				player1_allowed_to_move = True
			else:
				print("for start, you must roll 6\n")

		if player1_allowed_to_move:
			# with the first 6, player don't move and just have permission to start moving
			if player1_count_6 != 1:
				print("player 1 is moving...")
				player1_pos = set_pos('player1', player1_pos, dice_value)
				check_win('player1', player1_pos)
			# 6 have bonus and player should roll the dice again
			while dice_value == 6:
				player1_count_6 += 1
				print("You have another chance!\n")
				input("player1. press enter to roll dice")
				dice_value = rolling_dice()
				print("Rolling dice")
				time.sleep(DELAY)
				print("player 1 is moving...")
				player1_pos = set_pos('player1', player1_pos, dice_value)
				check_win('player1', player1_pos)

		if play_with_computer == 'yes':
			print("ok, computer playing as player 2")
		else:
			input("player2. press enter to roll dice")

		dice_value = rolling_dice()
		print("Rolling dice")
		time.sleep(DELAY)
		# player must roll 6 to start moving
		if player2_count_6 == 0:
			if dice_value == 6:
				player2_count_6 += 1
				player2_allowed_to_move = True
			else:
				print("for start, you must roll 6\n")

		if player2_allowed_to_move:
			# with the first 6, player don't move and just have permission to start moving
			if player2_count_6 != 1:
				print("player 2 is moving...")
				player2_pos = set_pos('player2', player2_pos, dice_value)
				check_win('player2', player2_pos) 
			# 6 have bonus and player should roll the dice again
			while dice_value == 6:
				player2_count_6 += 1
				print("You have another chance!\n")
				if play_with_computer == 'yes':
					print("player 2 is rolling")
					time.sleep(DELAY+2)
				else:
					input("player2. press enter to roll dice")

				dice_value = rolling_dice()
				print("Rolling dice")
				time.sleep(DELAY)
				print("player 2 is moving...")
				player2_pos = set_pos('player2', player2_pos, dice_value)
				check_win('player2', player2_pos)
		

map_design()
