def create_cube(n):
    output = []
    for item in range(n):
        output.append(item**3)
    return output

def create_cube_with_generator(n):
    for item in range(n):
        yield item ** 3


def fibonacci(num):
    a = 1
    b = 1
    for n in range(num):
        yield a
        a, b = b, a+b

def simple_gen(num):
    for i in range(num):
        yield i

print(f'create cubes without generator {create_cube(10)}')
print(f'create cubes with generator {list(create_cube_with_generator(10))}')
print(f'create fibonacci series with generator {list(fibonacci(10))}')

g = simple_gen(3)
print(next(g)) # 0
print(next(g)) # 1
print(next(g)) # 2
print(next(g)) # StopIteration ERROR THROWN