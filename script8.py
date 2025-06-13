#Polymorphism

#The word polymorphism is derived from Greek, and means "having multiple forms:"

# Poly = many

# Morph = forms

class Car:
  def __init__(self,brand,model,year, number_of_doors):
    self.brand = brand
    self.model = model
    self.year = year
    self.number_of_doors = number_of_doors
    
  def start(self):
    print("Car is stating")
    
  def stop(self):
    print("Car is stopping")
    
class Motorcycle:
  def __init__(self,brand,model,year):
    self.brand = brand
    self.model = model
    self.year = year
    
  def start_bike(self):
    print("Motorcycle is stating")
    
  def stop_bike(self):
    print("Motorcycle is stopping")
 
# Create list of vehicules to inspect    
vehicules = [
  Car("Ford","Focus",2008,5),
  Motorcycle("Honda","Scoopy",2018)
]

# Loop through list of vehicles and inspect them

for vehicle in vehicules:
  if isinstance(vehicle, Car):
    print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
    vehicle.start()
    vehicle.stop()
  elif isinstance(vehicle,Motorcycle):
    print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
    vehicle.start_bike()
    vehicle.start_bike()
  else:
    raise Exception("Object is not a valid vehicle.")