class Excercise():
    def __init__(self, name) -> None:
        self.name = name


    def execute(self, surname = None):
        print(f'\n\nDeveloper {self.name} {surname} and function execute')

    def return_sum(self, x, y):
        return x+y

    def is_even(self, number):
        return number % 2 == 0
    
    def get_even_numbers(self, num_list):
        even_numbers = []
        for num in num_list:
            if num % 2 == 0:
                even_numbers.append(num)
        return even_numbers

    def check_even_number(self, num_list):
        for num in num_list:
            if num % 2 == 0:
                return True
        return False

    # tuple unpacking
    def employee_of_month(self, employee_list):
        employee_of_month = ''
        max_hours = 0
        for name, hours in employee_list:
            if hours > max_hours:
                employee_of_month = name
                max_hours = hours

        return (employee_of_month, max_hours)

    
        


e = Excercise('Dinesh')
e.execute()
result = e.return_sum(10, 20)
print(result)
print(f'is number 20 even? {e.is_even(20)}')
print(f'is number 21 even? {e.is_even(21)}')
print(f'Even numbers {e.get_even_numbers([1, 2, 3, 4, 5, 6])}')
print(f'Even number exist in list {e.check_even_number([1, 2, 3, 4, 5, 6])}')
print(f'Even number exist in list {e.check_even_number([1, 3, 5, 7])}')
print(f'Even number exist in list {e.check_even_number([1, 3, 5, 7, 8])}')
emp, max = e.employee_of_month([('X', 100), ('Y', 250), ('Z', 200)]) # tuple unpacking
print(f'Employee of month {emp} and hours {max}')