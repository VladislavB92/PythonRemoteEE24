import csv

with open("ttt.csv", mode="r") as csv_game_results:
	result = csv.reader(csv_game_results, delimiter=",")
	for row in result:
		print(row)
