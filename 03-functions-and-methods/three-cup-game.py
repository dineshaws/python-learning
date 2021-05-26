from random import shuffle 

class Game():
    def __init__(self) -> None:
        pass

    def shuffle_list(self, mylist):
        shuffle(mylist)
        return mylist
    
    def guess(self):
        guess = ''

        while guess not in ['0', '1', '2']:
            guess = input('Please guess a number from list of 0, 1, 2')

        return int(guess)

    def check_guess(self, mylist, guess):
        if mylist[guess] == 'O':
            print('Correct guess')
        else:
            print('Incorrect guess ', mylist)


g = Game()


# create a cup list
l = [' ', 'O', ' ']
# shuffle list
shuffled_list = g.shuffle_list(l)
# guess
guess = g.guess()
# check guess
g.check_guess(shuffled_list, guess)