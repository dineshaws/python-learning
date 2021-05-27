class ValidateInput():
    def __init__(self) -> None:
        pass

    def user_choice(self, low, high):
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


vi = ValidateInput()
vi.user_choice(0, 10)
