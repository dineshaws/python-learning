def say_hello():
    print('Hello world')

    def welcome():
        print('Welcome into this world')

    return welcome

msg = say_hello()
msg()


def new_decorator(original_func):

    def wrap_func():

        print('Wrap function before the original function')
        original_func()
        print('Wrap function before the original function')

    return wrap_func

# def func_needs_decorator():
#     print('I want to be decorated')

# decorated_func = new_decorator(func_needs_decorator)
# decorated_func()

'''
decorated function
'''
@new_decorator
def func_needs_decorator():
    print('I need decorator')

func_needs_decorator()

