# Let's define each variable we are going to use
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
# Cars that wont be driven, cause only have 30 drives
cars_not_driven = cars - drivers
cars_driven = drivers
# The capacity is given by how many people in each car go
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car")