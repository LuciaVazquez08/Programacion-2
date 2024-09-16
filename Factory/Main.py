import Vehiculos
from creadores import CarCreator, TruckCreator, MotorcycleCreator

car_creator = CarCreator()
car = car_creator.create_vehicle()
car.start_engine() # Output: "The car engine is now running."
print(car.get_vehicle_type()) # Output: "Car"
car.stop_engine() # Output: "The car engine is now off."
truck_creator = TruckCreator()
truck = truck_creator.create_vehicle()
truck.start_engine() # Output: "The truck engine is now running."
print(truck.get_vehicle_type()) # Output: "Truck"
truck.stop_engine() # Output: "The truck engine is now off."
motorcycle_creator = MotorcycleCreator()
motorcycle = motorcycle_creator.create_vehicle()
motorcycle.start_engine() # Output: "The motorcycle engine is now running."
print(motorcycle.get_vehicle_type()) # Output: "Motorcycle"
motorcycle.stop_engine() # Output: "The motorcycle engine is now off."