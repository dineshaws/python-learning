# one.py

def func():
    print('func() in ONE.PY')

print("TOP LEVEL print statement in ONE.PY")

if __name__ == '__main__':
    print('ONE.py is being run directly')
else:
    print('ONE.py has been imported')
