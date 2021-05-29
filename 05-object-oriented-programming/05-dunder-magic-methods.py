class Book():
    def __init__(self, title, author, pages) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'Book {self.title} written by {self.author}'

    def __len__(self):
        return self.pages
    
    def __del__(self):
        print(f'Book {self.title} deleted')

book = Book('Pythong mastery', 'Jose', 200)
print(book)
print(str(book))
print(len(book))
del book
print(book)

