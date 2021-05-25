class Test: 
    def __init__(self, name):
        self.name = name


    def string_operations(self):
        # string interpolation
        print("\n\nDeveloper {} and function string_operations".format(self.name)) 
        print('The {} {} {}'.format('sun', 'is', 'fiery')) # The sun is fiery
        print('{1} {2}, {0}'.format(self.name, 'Hello', 'World'))# Hello World, Dinesh
        print('{0}, {1} {0}'.format(self.name, 'Hello', 'World')) # Dinesh, Hello Dinesh
        print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick')) # The quick brown fox
        # Float formatting follows "{value: width.precision f}"
        result = 100 / 777
        print('The result was {r:1.3f}'.format(r=result))
        # new way to format string starting from version 3.6
        print(f'Hello, My name is {self.name}') # Hello, My name is Dinesh

        s = 'hello'
        print('reverse of string ',s[::-1]) #olleh

    def list_operations(self):
        print(f'\n\nDeveloper {self.name} and function list_operations') # ['two', 3.0]
        
        my_list = [1, 'two', 3.0]
        print(len(my_list))
        print(my_list[0]) # 1
        print(my_list[1:])
        another_list = [4, 5]
        print(my_list + another_list) # [1, 'two', 3.0, 4, 5]
        new_list = my_list + another_list
        print(new_list)
        my_list[1] = 'TWO'
        print(new_list) # [1, 'two', 3.0, 4, 5]
        print(my_list); # [1, 'TWO', 3.0]
        new_list.append(6)
        print(new_list); # [1, 'two', 3.0, 4, 5, 6]
        new_list.pop()
        print(new_list) # [1, 'two', 3.0, 4, 5]
        print(new_list.pop()) # 5
        new_list.pop(0) # 1
        print(new_list) # ['two', 3.0, 4]
        new_list = [2, 8, 3, 2, 0, -1, 200, 1]
        new_list.sort()
        print(new_list) # [-1, 0, 1, 2, 2, 3, 8, 200]
        new_list.reverse()
        print(new_list) # [200, 8, 3, 2, 2, 1, 0, -1]

    def dictionary_operations(self):
        print(f'\n\nDeveloper {self.name} and function dictionary_operations')
        d = {'k1': 1, 'k2': [1, 2, 3], 'k3': {'insidekey': 'insidevalue'}}
        print(len(d))
        print(d)
        d['k4'] = 'afteradded'
        print(d.keys()) # dict_keys(['k1', 'k2', 'k3', 'k4'])
        print(d.values()) # dict_values([1, [1, 2, 3], {'insidekey': 'insidevalue'}, 'afteradded'])
        print(d.items()) # dict_items([('k1', 1), ('k2', [1, 2, 3]), ('k3', {'insidekey': 'insidevalue'}), ('k4', 'afteradded')])
        

    def tuple_operations(self):
        print(f'\n\nDeveloper {self.name} and function tuple_operations')
        # tuples are immutable
        t = (1, 2, 3)
        print(t)
        print(type(t))
        print(len(t))
        t = (1, 'two')
        print(t)
        t = ('x', 'x', 'y', 'z')
        print(t.count('x')) # 2
        print(t.index('x')) # 0
        print(t.index('y')) #2
        # t[0] = 'new' # it wont work as tuple is immutable

    def set_operations(self):
        print(f'\n\nDeveloper {self.name} and function set_operations')
        my_set = set()
        print(my_set) # set()
        my_set.add(2)
        print(my_set) # {2}
        print(type(my_set)) # 'set'
        print(len(my_set)) # 1
        my_set.add(3)
        my_set.add(2)
        print(my_set) # {2, 3}
        my_list = [1, 1, 3, 1, 2, 3, 2, 2, 3]
        print(set(my_list)) # {1, 2, 3}
        print(list(set(my_list))) # [1, 2, 3] type casting

    def boolean_operations(self):
        print(f'\n\nDeveloper {self.name} and function boolean_operations')
        is_covid_positive =  False
        print('is_covid_positive ', is_covid_positive)
        is_vaccinated = True
        print('is_vaccinated',is_vaccinated)
        print(type(is_vaccinated)) # bool
        print(1 > 2) # False
    
    def file_operations(self):
        print(f'\n\nDeveloper {self.name} and function file_operations')
        file_path = 'object-and-data-structure/myfile.txt';
        my_file = open(file_path)
        content = my_file.read()
        print(content)
        content_again = my_file.read()
        print('content_again ',content_again) # '' empty because cursor reached to end of the file in first read
        my_file.seek(0) # cursor moved to start of file again with seek
        content_again = my_file.read()
        print('content_again ',content_again)
        my_file.seek(0)
        lines = my_file.readlines()
        print(lines) # ['Hello World, This is example file\n', 'This is second line\n', 'this is the End of file']
        my_file.close()
        with open(file_path) as my_new_file:
            new_content = my_new_file.read()
            print('new_content ', new_content)  

        # read mode
        with open(file_path, mode='r') as f:
            print('read mode file read\n ',f.read())
        # append mode
        with open(file_path, mode='a') as f:
            f.write('\n This is appended line')
        # read the append file
        with open(file_path, mode='r') as f:
            print('read appended lines', f.read())
        # write mode
        with open('test.txt', mode='w') as f:
            f.write('THIS CREATES NEW FILE IF NOT EXIST and overwite content if already exist')
        # read new file
        with open('test.txt', mode='r') as f:
            print('read newly created file', f.read())



t1 = Test('Dinesh')

t1.string_operations()
t1.list_operations()
t1.dictionary_operations()
t1.tuple_operations()
t1.set_operations()
t1.boolean_operations()
t1.file_operations()