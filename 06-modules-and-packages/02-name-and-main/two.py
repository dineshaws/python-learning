# two.py
import one

one.func()

print('Top level print statement in two.py')

if __name__ == '__main__':
    print('two.py is being called directly')
else:
    print('two.py has been imported')