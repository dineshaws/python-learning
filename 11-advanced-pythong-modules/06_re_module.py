import re


text = 'Hello World, this is covid time, please dont go ouside if not necessary. covid second wave is more dangerous'
pattern = 'covid'
match = re.search(pattern, text)
print(match)
print(match.start())
print(match.end())

matches = re.findall(pattern, text)
print(matches)

for match in re.finditer(pattern, text):
    print(match)

matches = re.fullmatch(pattern, text)
print(matches)


text = 'My phone number is 91-9876543211'
pattern = r'\d\d-\d\d\d\d\d\d\d\d\d\d'

match = re.search(pattern, text)
print(match)
print(match.group())
pattern = '\d{2}-\d{10}'
match = re.search(pattern, text)
print(match)
print(match.group()) # 91-9876543211

phone_pattern = re.compile(r'(\d{2})-(\d{10})')
match = re.search(phone_pattern, text)
print(match.group()) # 91-9876543211
print(match.group(1)) # 91
print(match.group(2)) # 9876543211


# advance regex
match = re.search('Dog|Cat', 'The Dog is animal')
print(match)
match = re.search('Dog|Cat', 'The Cat is animal')
print(match)

matches = re.findall(r'.at', 'The cat in the hat and sat ') # wild card
print(matches)
match = re.findall(r'^\d', '300 is good movie') # start with digit character
print(match) #['3']
match = re.findall(r'^\d', 'Spider Man is good movie')
print(match) # []
match = re.findall(r'\d$', 'My favorite movie is 300') # end with digit character
print(match) #['0']

test_phrase = 'This is important! This should be done before EOD. Does any have problem?'
clear = re.findall(r'[^!.? ]+', test_phrase) # exclusion
print(clear) # ['This', 'is', 'important', 'This', 'should', 'be', 'done', 'before', 'EOD', 'Does', 'any', 'have', 'problem']
print(' '.join(clear)) # This is important This should be done before EOD Does any have problem
