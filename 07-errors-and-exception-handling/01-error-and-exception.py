class ExceptionHandling():
    def __init__(self) -> None:
        pass


    def file_errors(self):
        try:
            # file couldn't written as file opened with read mode
            file = open('random_file.txt', mode='r')
            file.close()
        except:
            print('File couldn\'t be written')
        finally:
            print('I always run')

    def what_your_age(self):
        try:
            age = int(input('What is your age : '))
        except:
            print('Incorrect input')
        else:
            print('Your age is {}'.format(age))

    
    def repeat_untill_correct(self):
        print('\n repeat_untill_correct function')
        while True:
            try: 
                age = int(input('What is your age : '))
            except:
                print('Only number allowed')
                continue
            else:
                print(f'You selected {age}')
                break
        
eh = ExceptionHandling()
eh.file_errors()
eh.what_your_age()
eh.repeat_untill_correct()