# simple AI
import random

print("====NUMBER GUESSING GAME====")
print("Choose difficulty: ")
difficulty = input("1 - easy, 2 - normal, 3 - hard, 4 - HELLLLLL!: ")

range_limit = 4

if difficulty == "1":
	range_limit = 4
elif difficulty == "2":
	range_limit = 6
elif difficulty == "3":
	range_limit = 11
elif difficulty == "4":
	range_limit = 51

game_on = True

print(f"Guess a number between 1 and {range_limit - 1}")
cpus_number = random.randrange(1, range_limit)

while game_on:
	players_number = int(input("Type in a number: "))

	if players_number == cpus_number:
		print(f"You guessed it! It is {players_number}!")
		game_on = False
	else:
		print("Try again!")
