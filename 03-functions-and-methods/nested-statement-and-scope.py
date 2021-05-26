#LEGB rule
# L - Local
# E - Enclosed
# G - Global
# B - Built-in functions

myvar = 'Hello this is global variable'
def myfunc():
    myvar = 'this is enclosed variable'
    def inner_func():
        myvar = 'this is local variable'
        print(myvar)
    inner_func()

myfunc()