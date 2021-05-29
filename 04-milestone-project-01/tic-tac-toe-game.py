class TicTacToeGame():
    def __init__(self) -> None:
        pass


    def pick_symbol(self, player):
        options = ['X', 'O']
        selection = ''
        valid = False
        while valid == False:
            selection = input(f'{player} : Choose your symbol from (X or O): ');
            if selection not in options:
                print("please select correct option")
                valid = False
            else:
                valid = True

        return selection

    def pick_choice_index(self, player_name, low, high):
        #initialization
        response = 'NotValid'
        not_in_range = False
        
        while response.isdigit() == False or not_in_range == False:
            response = input(f'{player_name}: Please choose a number in range {low} {high} : ')
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
    
    def fill_choice(self, board, choice_index, choice):
        board[choice_index] = choice
        return board

    def opposite_symbol(self, current_symbol):
        if current_symbol == 'X':
            return 'O'
        else:
            return 'X'

    def player_name(self, player_id):
        if player_id ==1:
            return 'Player 1'
        return 'Player 2'

    def continue_game(self):
        options = ['Yes', 'N0']
        selection = ''
        valid = False
        while valid == False:
            selection = input('Continue Game? (Yes, No): ')
            if selection not in options:
                print("please select correct option")
                valid = False
            else:
                valid = True

        if selection == 'Yes':
            return True
        else:
            return False

    def display_board(self, board):
        
        board_size = len(board)
        current_index = board_size - 1
        current = board[current_index]
        counter = 1
        print('\n\n --------------------------')
        while current != '#':
            print(f'{current_index} -> {current}')
            if counter % 3 == 0:
                print('\n')
            counter += 1
            current_index -= 1
            current = board[current_index]
            


    def play(self):
        result = False
        counter = 0
        player_id = 1
        player_name = self.player_name(player_id)
        player_1_symbol = self.pick_symbol(player_name)
        player_2_symbol = self.opposite_symbol(player_1_symbol)
        current_symbol = player_1_symbol
        board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.display_board(board)
        while counter < 9:
            if counter % 2 == 0:
                player_id = 1
                current_symbol = player_1_symbol
            else: 
                player_id = 2
                current_symbol = player_2_symbol
            player_name = self.player_name(player_id)
            choice_index = self.pick_choice_index(player_name, 1, 9)
            board = self.fill_choice(board, choice_index, current_symbol)

            self.display_board(board)

            counter += 1



ttt = TicTacToeGame()
ttt.play()