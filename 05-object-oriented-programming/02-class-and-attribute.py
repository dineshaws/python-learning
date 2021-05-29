class Dog():
    # CLASS OBJECT ATTRIBUTES
    # same for any class instance
    species = 'mammal'

    def __init__(self, breed, name, spots) -> None:
        # attributes
        # accept arguements
        # self.attributes = arguements
        self.breed = breed
        self.name = name
        # expects boolean True/False
        self.spots = spots
        
    # OPERATIONS/ACTIONS --> METHODS
    def bark(self, number):
        print(f'The Dog {self.name} barks {number} times in a day')

mydog = Dog(breed='Lab', name='Foo', spots=False)
print(type(mydog)) # __main__.Dog
print(mydog.breed) # Lab
print(mydog.name) # Foo
print(mydog.spots) # False
print(mydog.species) # mammal
mydog.bark(10)