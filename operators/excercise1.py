class Test:
    def __init__(self, name) -> None:
        self.name = name
    
    def comparison_operators(self):
        print(f'\n\nDeveloper {self.name} and function comparison_operators')

        print(2 ==2) # True
        print(2 == 2.0) # True
        print(2 == '2') # False
        print(2 != 3) # True
        print(2 > 3) # False
        print(2 < 3) # True
        print(2 >= 2) # True
        print(2 <= 2) # True


    def logical_operators(self):
        print(f'\n\nDeveloper {self.name} and function logical_operators')
        print(1 < 2 < 3) # True , chaining of operators
        print(1 < 2 > 3) # False
        print(1 < 2 and 2 > 3) # False
        print(('h' == 'h') and (2 == 2)) # True

        print(1 == 1 or 2 == 2) # True
        print(1 == 1 or 2 == 3) # True
        print(1 == 2 or 2 == 2) # True
        print(1 == 2 or 2 == 3) # False

        print(not(1 == 1)) # False
        print(not(1 == 2)) # True
        print(not False)


t1 = Test('Dinesh')
t1.comparison_operators()
t1.logical_operators()