from functions import plus_operation

# Python dictionary (dict)

fruits = ["apple", "banana", "pear", "cherry", 420, 69, None, True, {"my_dict": "test"}]
print(f"My fruits got a sum of {plus_operation(fruits[4], fruits[5])}")


# key, value pair
cherry = {
	"name": "Cherry",
	"color": "red",
	"shape": "round",
	"taste": "sweet",
	"weight": 5.0,
	"grows_during_winter": False,
	"parasites": None,
}

sun = {
	"name": "Sol",
	"age": 4.6,
	"surface_temperature": 5772,
	"hot": True,
	"is_white_dwarf": False,
	"planetary_system": [
		"Mercury",
		"Venus",
		"Earth",
		"Jupiter",
		"Saturn",
		"Neptune",
		"Uranus",
		"Pluto",
		{
			"Vlad's belt": {
				"Charon": "Dwarf planet"
			}
		}
	],
	"habitable planets": {
		"Earth": {
			"moon": True,
			"atmosphere": True,
			"water": True,
		},
		"Venus": "hell",
		"Mars": "Too cold, and no air",
	}
}

# print(sun["planetary_system"][8]["Kuiper belt"]["Charon"])
# print(sun.get("planetary_system")[8].get("Kuiper belt", {}).get("Charon"))

cars_list = ["Audi", "BMW", "Volvo", "VW", "Aston Martin", "Audi"]


# We cannot order (subscript)
# Cannot slice by smaller elements/values
cars_set = {"Audi", "BMW", "Volvo", "VW", "Aston Martin", "Audi"}


# We cannot modify (mutate)
cars_tuple = ("Audi", "BMW", "Volvo", "VW", "Aston Martin", "Audi")


print(cars_set)
