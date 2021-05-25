from random import shuffle, randint

class Test:
    def __init__(self, name) -> None:
        self.name = name

    def control_flow_operations(self):
        print(f'\n\nDeveloper {self.name} and function control_flow_operations')

        # if some_condition:
        #   execute some code
        # elif some_other_condition:
        #   do something different
        # else: 
        #   do something else

        country = 'INDIA'
        if country == 'INDIA':
            print('INDIA IS VIBRANT COUNTRY')
        elif country == 'USA':
            print('USA IS PROMISING COUNTRY')
        elif country == 'UK':
            print('UK IS GREAT BRITAIN')
        else:
            print('NO COUNTRY IS SELECTED')

    def for_loop_operations(self):
        print(f'\n\nDeveloper {self.name} and function for_loop_operations')
        # syntax
        # my_iterable = [1, 2, 3]
        # for item in my_iterable:
        #     print(item)

        # list iteration
        mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        even = []
        odd = []
        for item in mylist:
            if item % 2 == 0:
                even.append(item)
            else:
                odd.append(item)
        print(even) # [2, 4, 6, 8, 10]
        print(odd) # [1, 3, 5, 7, 9]

        list_sum = 0
        for item in mylist:
            list_sum += item
        print(f'List sum is : {list_sum}')

        # string iteration
        mystring = 'Hello World'
        for letter in mystring:
            print(letter)

        for _ in mystring:
            print('Cool')

        # tuple iterations
        tup = (1, 2, 3, 4)
        for item in tup:
            print(item)

        tuple_list = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

        for (a, b) in tuple_list: # for a, b in tuple_list:
            print(a)
            print(b)

        # dictionary iterations
        d = {'k1': 1, 'k2': 2}
        for key in d:
            print(key) # k1

        for item in d.items(): # for key, value in d.items()
            print(item) # ('k1', 1)

    def while_loop_operations(self):
        print(f'\n\nDeveloper {self.name} and function while_loop_operations')
        # syntax
        # while boolean_condition:
        #     do something

        counter = 1
        while counter <= 10:
            print(f'Counter is {counter}')
            counter = counter+1

        print('PASS: Does nothing at all')
        l = [1, 2, 3]
        for _ in l:
            # no statement execute so 'pass'
            pass

        print('CONTINUE: skipping the current traverse of loop')
        l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for item in l1:
            if item % 2 != 0:
                continue
            print(f'itema value is = {item}')

        print('BREAK: terminate the current loop')
        x = 0
        while x < 5:
            if x == 2: 
                break
            print(f'X value is {x}')
            x += 1
        
    def useful_operator_operations(self):
        print(f'\n\nDeveloper {self.name} and function useful_operator_operations')
        print('\n range generator')
        for num in range(0, 10, 2): # range(start, stop, step)
            # start is optional
            # step is options # print 0, 2, 4, 6, 8
            print(num)

        for num in range(10):
            print(num) # print from 0 to 9

        for num in range(3, 10):
            print(num) # print from 3 to 9

        print(list(range(0, 11, 2))) # [0, 2, 4, 6, 8, 10]

        print('\n enumerate generator')
        word = 'abcde'
        for item in enumerate(word):
            print(item) # (0, 'a') (1, 'b')

        for index, letter in enumerate(word):
            print('Letter {} at index {}'.format(letter, index))

        print('\n zip generator')

        list1 = ['a', 'b', 'c', 'd', 'e']
        list2 = [1, 2, 3, 4]
        list3 = ['x', 'y', 'z']
        for item in zip(list1, list2, list3):
            print(item) # ('a', 1, 'x')   ('b', 2, 'y')

        print(list(zip(list1, list2))) # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

        print('\n\n CHECK ITEM EXIST IN LIST')

        print(2 in [1, 2, 3]) # True
        print('x' in ['x', 'y', 'z']) # True
        print('a' in ['x', 'y', 'z']) # False
        print('a' in 'a story') # True
        print('key1' in {'key1': 1, 'key2': 2}) # True

        print('\n\n Mathematical generators')
        list1 = [2, 1, 4, 10, 34, 100, 3]
        print(min(list1)) # 1
        print(max(list1)) # 100


        print('\n WORK WITH IMPORTED PACKAGE')
        mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        shuffle(mylist) # in place change
        print(f'shuffled list is {mylist}')

        print(f'Random integer is {randint(0, 100)}') # min and max including 

        print('\n INPUT')
        name = input('What\'s is your name? ')
        print(f'Name is {name}')

t1 = Test('Dinesh')
t1.control_flow_operations()
t1.for_loop_operations()
t1.while_loop_operations()
t1.useful_operator_operations()