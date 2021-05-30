import random

def gen_squares(n):
    for num in range(n):
        yield num ** 2

for item in gen_squares(10):
    print(item)

print('\n\n PROBLEM 2')
def rand_num(low, high, n):
   for _ in range(n):
        yield random.randint(low, high)

for item in rand_num(1, 5, 10):
    print(item)

print('\n\n PROBLEM 3')

s = 'hello'

s = iter(s)
print(next(s)) # h
print(next(s)) # e
