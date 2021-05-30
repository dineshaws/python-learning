"""
Home work for three problems
"""
class HomeWork():
    def __init__(self) -> None:
        pass
    # Handle the exception thrown by the code below by using try and except blocks.
    def problem_1(self):
        """
            Problem 1 with try except
        """
        try:
            for i in ['a', 'b', 'c']:
                print(i**2)
        except TypeError:
            print('Not an number')
        except:
            print('Error occured')
    # Handle the exception thrown by the code below by using try and except blocks.
    # Then use a finally block to print 'All Done.'
    def problem_2(self):
        try:
            x = 5
            y = 0
            z = x/y
            print(z)
        except ZeroDivisionError:
            print('Can\'t divide with 0')
        except:
            print('Error Occured')
        finally:
            print('All Done')
    # Write a function that asks for an integer and prints the square of it.
    # Use a while loop with a try, except, else block to account for incorrect inputs.
    def problem_3(self):
        while True:
            try:
                num = int(input('Enter a number: '))
            except:
                print('An error occurred! Please try again!')
                continue
            else:
                square_num = num ** 2
                print('Thank you, your number squared is:  {}'.format(square_num))
                break

hw = HomeWork()
hw.problem_1()
hw.problem_2()
hw.problem_3()
