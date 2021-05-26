class Test():
    def __init__(self) -> None:
        pass


    def square(self, num):
        return num ** 2

    def square_list(self, mylist) -> list:
        return list(map(self.square, mylist))

    def is_even(self, num):
        return num % 2 == 0

    def get_even_numbers(self, mylist) -> list:
        return list(filter(self.is_even, mylist))

    def lambda_expression(self, mylist) -> None:
        print('lambda_expression')
        m = list(map(lambda num : num ** 2, mylist)) # square of each item of list
        print(m)
        f = list(filter(lambda num: num % 2 == 0, mylist))
        print(f)

t = Test()
print('t.square_list([1, 2, 3, 4, 5, 6]) square list=> ', t.square_list([1, 2, 3, 4, 5, 6]))
print('t.get_even_numbers([1, 2, 3, 4, 5, 6]) square list=> ', t.get_even_numbers([1, 2, 3, 4, 5, 6]))
t.lambda_expression([1, 2, 3, 4, 5, 6])