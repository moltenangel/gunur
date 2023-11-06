# FreeCodeCamp's Ultimate Beginner's Python Course:
# https://www.freecodecamp.org/news/ultimate-beginners-python-course/
# Lesson 18 - Classes & Objects
# Time stamp: 5:56:54
# In this lesson, we cover:
# - Classes = Blueprints for creating objects
# - Objects = How you create them from classes
# - Inheritance = Child classes inherit variables/methods from parent classes
# - Polymorphism describes the concept that you can access objects of different types through the same interface. Each type can provide its own independent implementation of this interface.
# Polymorphism: https://stackify.com/oop-concept-polymorphism/
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('Moves along...')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


my_car = Vehicle('Tesla', 'Model 3')

# print(my_car.make)  # Tesla
# print(my_car.model)  # Model 3
my_car.get_make_model()  # I'm a Tesla Model 3
my_car.moves()  # 'moves along...'

your_car = Vehicle('Cadillac','Escalade')
your_car.get_make_model()  # I'm a Cadillac Escalade.
your_car.moves()  # 'moves along...'


class Airplane(Vehicle):  # Airplane inherits from the Vehicle class
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)  # This means we will inherit these values from the parent object
        self.faa_id = faa_id

    def moves(self):  # This method overwrites the inherited method
        print('Flies along...')


class Truck(Vehicle):
    def moves(self):
        print('Rumbles along...')


class GoldCart(Vehicle):
    pass


cessna = Airplane('Cessna','Skyhawk','N-12345')
mack = Truck('Mack','Pinnacle')
golfwagon = GoldCart('Yamaha','GC100')

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()


########################
# Polymorphism
print('\n\n')

for v in (my_car, your_car, cessna, mack, golfwagon):
    v.get_make_model()
    v.moves()

