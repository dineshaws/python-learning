import math
import random

value = 4.55
print(math.floor(value)) # 4
print(math.ceil(value)) # 5

print(round(4.50)) # 4
print(round(5.50)) # 6

print(random.randint(0,100))

# The value 101 is completely arbitrary, you can pass in any number you want
random.seed(101)
# You can run this cell as many times as you want, it will always return the same number
print(random.randint(0,100))


mylist = list(range(0,20))
print(mylist)
print(random.choice(mylist))