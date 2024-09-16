import Vehiculos
from factory import VehicleCreator

class CarCreator(VehicleCreator):
    def create_vehicle(self):
        return Vehiculos.Car()

class TruckCreator(VehicleCreator):
    def create_vehicle(self):
        return Vehiculos.Truck()

class MotorcycleCreator(VehicleCreator):
    def create_vehicle(self):
        return Vehiculos.Motorcycle()