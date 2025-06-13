#Inheritence

#Inheritence is a fundamental concept in object-oriented programming OOP, that involves creating new clasess (Subclasses or derived classes) based on existing classes (superclass or base classes).

class Vehicule:
  def __init__(self,brand,model,year):
    self.year = year
    self.brand = brand
    self.model = model
    
  def start(self):
    print("Vehicule is stating")
    
  def stop(self):
    print("Vehicule is stopping")
    
class Car(Vehicule):
  def __init__(self,brand,model,year,numer_of_doord,numerber_of_wheels):
    super().__init__(brand,model,year)
    self.numer_of_doord = numer_of_doord
    self.number_of_wheels = numerber_of_wheels
    
class Bike(Vehicule):
  def __init__(self,brand,model,year,number_of_wheels):
    super().__init__(brand,model,year)
    self.number_of_wheels = number_of_wheels
    
car = Car("Ford","Focus",2008, 5, 4)
bike = Bike("Honda","Scoopy",2018, 2)
print(car.__dict__)
print(bike.__dict__)
car.start()
bike.start()