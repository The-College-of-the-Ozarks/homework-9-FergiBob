class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.status = True
        self.previous = []
        self.current = []
        
    def __repr__(self):
        return f'{self.name}, {self.author}, Is checked out: {self.status}, Previous owners: {self.previous}, Current owner: {self.current}'