from Vehiculo import Vehicle

class Car(Vehicle):
    def start_engine(self):
        print("The car engine is now running.")

    def stop_engine(self):
        print("The car engine is now off.")

    def get_vehicle_type(self):
        return "Car"

class Truck(Vehicle):
    def start_engine(self):
        print("The truck engine is now running.")

    def stop_engine(self):
        print("The truck engine is now off.")

    def get_vehicle_type(self):
        return "Truck"

class Motorcycle(Vehicle):
    def start_engine(self):
        print("The motorcycle engine is now running.")

    def stop_engine(self):
        print("The motorcycle engine is now off.")

    def get_vehicle_type(self):
        return "Motorcycle"
