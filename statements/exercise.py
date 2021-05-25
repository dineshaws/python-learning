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


t1 = Test('Dinesh')
t1.control_flow_operations()
t1.for_loop_operations()