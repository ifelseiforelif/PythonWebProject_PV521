class Book:
    def __new__(cls, name, author, year):
        if not isinstance(year, int) or year < 0 or year > 2026:
            raise TypeError('year must be an integer between 0 and 2026')
        return super().__new__(cls)
    def __init__(self, title, author, year):

        self.title = title
        self.author = author
        self.year = year

    def is_new(self):
        return self.year >= 2020


b1 = Book('test', 'test author', 2027)
