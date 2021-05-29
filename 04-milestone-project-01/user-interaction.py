class UserInteraction():
    def __init__(self) -> None:
        pass

    
    def pick_choice_index(self, low, high):
        #initialization
        response = 'NotValid'
        not_in_range = False
        
        while response.isdigit() == False or not_in_range == False:
            response = input(f'Please choose a number in range {low} {high} : ')
            # number check
            if response.isdigit() == True:
                # range check
                if int(response) not in range(low, high+1):
                    not_in_range = False
                    print('Not in range')
                else:
                    not_in_range = True
            else:
                print('Not a number')

        return int(response)

    def pick_choice(self):
        return input('Enter choice : ')

    def display_game(self, game):
        print(f'Current game choices {game}')

    def fill_choice(self, game, choice_index, choice):
        game[choice_index] = choice
        return game

    def do_continue(self):
        options = ['Y', 'N']
        selection = ''
        valid = False
        while valid == False:
            selection = input('Do you want to continue game? If yes please select "Y" else "N"')
            if selection not in options:
                print("please select correct option")
                valid = False
            else:
                valid = True

        print('selection', selection)
        if selection == 'Y':
            return True
        else:
            return False
    
    def play(self, game):
        game_on = True
        while game_on:
            self.display_game(game)
            choice_index = self.pick_choice_index(0, 2)
            choice = self.pick_choice()
            game = self.fill_choice(game, choice_index, choice)
            self.display_game(game)
            game_on = self.do_continue()


ui = UserInteraction()

game = [1, 2, 3]
ui.play(game)
