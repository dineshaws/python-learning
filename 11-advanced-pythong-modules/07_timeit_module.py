import timeit

def func_one(n):
    return [str(num) for num in range(n)]

def func_two(n):
    return list(map(str, range(n)))

print(func_one(10))
print(func_two(10))

stmt1 = '''
func_one(100)
'''
setup1 = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

stmt2 = '''
func_two(100)
'''
setup2 = '''
def func_two(n):
    return list(map(str, range(n)))
'''

print(timeit.timeit(stmt1, setup1, number=1000000))
print(timeit.timeit(stmt2, setup2, number=1000000))
