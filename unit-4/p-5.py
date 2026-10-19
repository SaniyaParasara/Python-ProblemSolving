# UNIT 4 - Q5: Write a program to implement single, multilevel and multiple
#               inheritance.
# SCENARIO: Vehicle hierarchy in a transport app: Vehicle -> Car (single),
#           Vehicle -> Car -> ElectricCar (multilevel), and a HybridCar that
#           inherits from both Petrol and Electric engines (multiple).

# ---- Single ----
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def start(self):
        print(self.brand, "starts")

class Car(Vehicle):
    def wheels(self):
        print("Car has 4 wheels")

print("-- Single --")
c = Car("Honda"); c.start(); c.wheels()

# ---- Multilevel ----
class ElectricCar(Car):
    def battery(self):
        print("Battery: 75 kWh")

print("-- Multilevel --")
e = ElectricCar("Tesla"); e.start(); e.wheels(); e.battery()

# ---- Multiple ----
class PetrolEngine:
    def fuel(self): print("Runs on petrol")
class ElectricEngine:
    def charge(self): print("Runs on battery")
class HybridCar(PetrolEngine, ElectricEngine):
    pass

print("-- Multiple --")
h = HybridCar(); h.fuel(); h.charge()

# ---- Hierarchical (bonus) ----
class Bike(Vehicle): pass
class Truck(Vehicle): pass
print("-- Hierarchical --")
Bike("Yamaha").start(); Truck("Tata").start()
print(issubclass(ElectricCar, Vehicle), isinstance(e, Car))
