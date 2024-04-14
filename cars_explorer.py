from car import Car, Bicycle

# object
victorias_car = Car(
	"Victoria",
	"navy",
	"MB",
	"CLA300",
	4,
	True,
	True,
	False,
	2,
)

print(victorias_car.owner)
print(victorias_car.color)
print(victorias_car.brand)
print(victorias_car.model)
print(victorias_car.transmission_type)
print(f"Car is moving: {victorias_car.is_vehicle_moving}")

victorias_car.push_the_vehicle()

print(f"Car is moving: {victorias_car.is_vehicle_moving}")

vlads_bicycle = Bicycle(
	2,
	False,
	False,
	False,
	0,
)

vlads_bicycle.push_the_vehicle()
print(f"Is bicycle moving? {vlads_bicycle.is_vehicle_moving}")

print(vlads_bicycle.do_a_wheelie())

while True:
	players_input = input("<-, ->, |")
	vlads_bicycle.key_input(players_input)
