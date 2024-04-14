def search_car(maker, engine, fuel="all"):
	car = {
		"maker": maker,
		"engine": engine,
		"fuel": fuel,
	}
	return car


print(search_car("Audi", "2.0", fuel="diesel"))
print(search_car("BMW", "3.0"))
print(search_car("VW", "1.5"))



