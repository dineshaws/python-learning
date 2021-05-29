class Animal():
    def __init__(self, name) -> None:
        self.name = name
        print('Animal created')

    def speak(self):
        print(f'Animal {self.name} speak')

    def parent_method(self):
        print(f'Parent method {self.name}')

    def bark(self):
        raise NotImplementedError('This method must be defined at child class') # throw error


class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
        print('Dog created')

    def speak(self):
        print(f'Dog {self.name} speak')

    def child_method(self):
        print(f'Child method {self.name}')

mydog = Dog('Sheru')
mydog.speak()
mydog.child_method()
mydog.parent_method()
mydog.bark()