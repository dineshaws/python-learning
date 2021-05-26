class Problem():
    def __init__(self) -> None:
        pass
    
    def lesser_number(self, a, b):
        if a %2 == 0 and b % 2 == 0:
            return min(a, b)
        else:
            return max(a, b)

    def animal_cracker(self, txt):
        # animals = txt.split(' ')
        # first_animal_char = animals[0][0].lower() # first animal, first char
        # second_animal_char = animals[1][0].lower() # first animal, first char
        # if first_animal_char == second_animal_char:
        #     return True
        # return False

        animals = txt.split(' ')
        first_char = animals[0][0].lower()

        for index in range(1, len(animals)):
            current_animal = animals[index]
            current_char = current_animal[0].lower()
            if first_char != current_char:
                return False
        return True
        
    def makes_twenty(self, num1, num2):
        if sum((num1, num2)) == 20 or 20 in [num1, num2]:
            return True
        return False

    def old_macdonald(self, txt):
        txt_list = list(txt) # string to list
        for index in range(0, len(txt_list)):
            if index in [0, 3]:
                txt_list[index] = txt_list[index].upper()
        return ''.join(txt_list) # list to string

    def master_yoda(self, txt):
        str_list = txt.split(' ')
        str_list.reverse() # reverse in place
        return ' '.join(str_list)

    def almost_there(self, num):
        if (100 -10 <= num and num <= 100 +10) or (200 -10 <= num and num <= 200 +10):
            return True
        return False
    
    def has_33(self, num_list):
        num_3 = None
        for num in num_list:
            if num == num_3:
                return True
            elif num == 3:
                num_3 = num
            else:
                num_3 = None
        return False

    def paper_doll(self, txt):
        return_txt = ''
        for letter in txt:
            return_txt += letter*3
        return return_txt

    def blackjack(self, a, b, c):
        if sum((a, b, c)) <= 21:
            return sum((a, b, c))
        elif sum((a, b, c)) > 21 and 11 in [a, b, c]:
            return sum((a, b, c)) - 10
        else:
            return 'BUST'

    def summer_69(self, mlist):
        sixExist = False
        skip = False
        total = 0
        for index in range(0, len(mlist)):
            if sixExist == False and mlist[index] == 6:
                sixExist = True
                skip = True
            elif sixExist == True and mlist[index] != 9:
                skip = True

            if skip == True:
                continue
            else:
                total += mlist[index]

        return total





p1 = Problem()
print(f'returns min {p1.lesser_number(2, 4)} if both are even number')
print(f'returns max {p1.lesser_number(1, 3)} if any number is odd')
print(f'returns max {p1.lesser_number(3, 2)} if any number is odd')
print(f'returns {p1.animal_cracker("camel Cow cat")} as both starts with same char')
print(f'returns {p1.animal_cracker("camel Dog cat")} as both dont start with same char')
print(f'makes_twenty(20,10) = {p1.makes_twenty(20,10)}')
print(f'makes_twenty(12,8) = {p1.makes_twenty(12,8)}')
print(f'makes_twenty(2,3) = {p1.makes_twenty(2,3)}')
print(f'old_macdonald("macdonald") = {p1.old_macdonald("macdonald")}')
print(f'master_yoda("I am home") = {p1.master_yoda("I am home")}')
print(f'almost_there(90) = {p1.almost_there(90)}')
print(f'almost_there(104) = {p1.almost_there(104)}')
print(f'almost_there(150) = {p1.almost_there(150)}')
print(f'almost_there(210) = {p1.almost_there(210)}')
print(f'has_33([1, 3, 3]) = {p1.has_33([1, 3, 3])}')
print(f'has_33([1, 3, 1, 3]) = {p1.has_33([1, 3, 1, 3])}')
print(f'has_33([3, 1, 3]) = {p1.has_33([3, 1, 3])}')
print(f'paper_doll("Hello") = {p1.paper_doll("Hello")}')
print(f'blackjack(5,6,7) = {p1.blackjack(5,6,7)}')
print(f'blackjack(9,9,9) = {p1.blackjack(9,9,9)}')
print(f'blackjack(9,9,11) = {p1.blackjack(9,9,11)}')
print(f'summer_69([1, 3, 5]) = {p1.summer_69([1, 3, 5])}')
print(f'summer_69([4, 5, 6, 7, 8, 9]) = {p1.summer_69([4, 5, 6, 7, 8, 9])}')
print(f'summer_69([2, 1, 6, 9, 11]) = {p1.summer_69([2, 1, 6, 9, 11])}')