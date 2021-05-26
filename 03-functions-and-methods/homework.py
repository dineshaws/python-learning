from string import ascii_lowercase

class Homework():
    def __init__(self) -> None:
        pass

    # Write a function that computes the volume of a sphere given its radius.
    def calc_volume(self, r):
        return 4/3 * 22/7 * (r**3) 

    #  Write a function that checks whether a number is in a given range (inclusive of high and low)
    def  ran_check(self, num ,low, high):
        return num in range(low, high+1)

    # Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
    def up_low(self, mystring):
        up = 0
        lower = 0
        for letter in mystring:
            if letter.isupper():
                up += 1
            if letter.islower():
                lower += 1
        return [up, lower]

    def unique_list(self, mylist):
        return list(set(mylist))

    def multiply(self, mylist):
        response = 1
        for item in mylist:
            response *= item
        return response

    def is_palindrome(self, mystring):
        mystring_without_spaces = mystring.replace(' ', '')
        return mystring_without_spaces == mystring_without_spaces[::-1]

    # Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
    def ispangram(self, str1, alphabet=ascii_lowercase):
        print(alphabet)
        print(str1)
        str1 = str1.replace(' ', '').lower()
        for letter in str1:
            if letter not in alphabet:
                return False;
        return True

    

h = Homework()
print(f'calc_volume(2) = {h.calc_volume(2)}')
print(f'ran_check(5, 2, 7) = {h.ran_check(5, 2, 7)}')
print(f'ran_check(2, 2, 7) = {h.ran_check(2, 2, 7)}')
print(f'ran_check(7, 2, 7) = {h.ran_check(7, 2, 7)}')
print(f'ran_check(1, 2, 7) = {h.ran_check(1, 2, 7)}')
print(f'up_low("Hello Mr. Rogers, how are you this fine Tuesday?") = {h.up_low("Hello Mr. Rogers, how are you this fine Tuesday?")}')
print(f'unique_list([1, 2, 7, 1, 2, 2, 3, 7, 8]) = {h.unique_list([1, 2, 7, 1, 2, 2, 3, 7, 8])}')
print(f'multiply([1, 2, 3, -4]) = {h.multiply([1, 2, 3, -4])}')
print(f'is_palindrome("hello") = {h.is_palindrome("hello")}')
print(f'is_palindrome("helleh") = {h.is_palindrome("helleh")}')
print(f'ispangram("The quick brown fox jumps over the lazy dog") = {h.ispangram("The quick brown fox jumps over the lazy dog")}')