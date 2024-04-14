#  Operations with external files.
#  Operations like open, write inside the file, edit the file, create, delete.
#  CSV, JSON, TXT ...


# greeting_file = open("greeting.txt", "r")  # r = read
#
# print(greeting_file.read())


# with open("greeting.txt", "r") as greeting_file:
# 	greeting = greeting_file.read()
#
# # file is closed automatically
# print(greeting)

with open("greeting.txt", "a") as greeting_file:
	greeting = greeting_file.write("69 + 420 = 489\n")

print("Welcome to calculator")
print("1 Calculate")
print("2 See history")
calculate_or_history = input()

if calculate_or_history == "2":

	with open("greeting.txt", "r") as greeting_file:
		greetings = greeting_file.readlines()
		for line in greetings:
			print(line)
