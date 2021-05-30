from collections import Counter, defaultdict, namedtuple

my_list = [1, 1, 1, 1, 2, 3, 2, 2, 3, 5, 6, 7]

c = Counter(my_list) 
print(c) # Counter({1: 4, 2: 3, 3: 2, 5: 1, 6: 1, 7: 1})

my_list = [1, 2, 3, 'a', 'b', 'a']
c = Counter(my_list)
print(c) # Counter({'a': 2, 1: 1, 2: 1, 3: 1, 'b': 1})

s = 'aaaaabbbbbdfds'
c = Counter(s)
print(c) # Counter({'a': 5, 'b': 5, 'd': 2, 'f': 1, 's': 1})

sentence = 'A Happy family is best Family'

c = Counter(sentence.lower().split())
print(c) # Counter({'family': 2, 'a': 1, 'happy': 1, 'is': 1, 'best': 1})

print(c.most_common()) # [('family', 2), ('a', 1), ('happy', 1), ('is', 1), ('best', 1)]
print(c.most_common(2)) # [('family', 2), ('a', 1)]

print(list(c)) # ['a', 'happy', 'family', 'is', 'best']
print(set(c)) # {'best', 'happy', 'is', 'family', 'a'}
print(dict(c)) # {'a': 1, 'happy': 1, 'family': 2, 'is': 1, 'best': 1}
print(c.items()) # dict_items([('a', 1), ('happy', 1), ('family', 2), ('is', 1), ('best', 1)])
print(sum(c.values())) # 6


d = {'a': 10}
print(d['a']) # 10
# print(d['WRONT']) # KeyError: it wiil throw error 

d = defaultdict(lambda: 0)
d['correct'] = 20
print(d['correct']) # 20
print(d['WRONG']) # 0 as 0 defined default value through defaultdict


Dog = namedtuple('Dog', ['age', 'breed', 'name'])
sam = Dog(age=2, breed='Lab', name='Sam')
print(type(sam)) # __main__.Dog
print(sam.age) # 2
print(sam.breed) # Lab
print(sam.name) # Sam
print(sam[0]) # 2


