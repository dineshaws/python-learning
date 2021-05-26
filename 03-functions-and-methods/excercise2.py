class Excercise():
    def __init__(self) -> None:
        pass
    
    # *agrs returns tuple
    def myfunc(self, *args):
        print( args)
    # **kwargs returns dictionary
    def myfunc2(self, **kwargs):
        print(kwargs)

    def myfunc3(self, *args, **kwargs):
        print(args)
        print(kwargs)

e = Excercise()
e.myfunc(1, 2, 3, 4)
e.myfunc2(fruit='Mango', veggie='Ladyfinger')
e.myfunc3(10, 20, 30, fruit='Mango', veggie='Ladyfinger')