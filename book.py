class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.status = True
        self.previous = []
        self.current = []
        
    def __repr__(self):
        return f'{self.name} by {self.author}, Is available: {self.status}, Previous owners: {self.previous}, Current owner: {self.current}'
    
    def print_name_author(self):
        print(f'{self.name} by {self.author}')
        
    def print_status(self):
        if self.status == True:
            print(f'The book is currently available.')
        else:
            print(f'The book is currently checked out by {self.current}.')
            
    def print_prev_borrowers(self):
        print(f'{self.previous}')
        
    def __len__(self):
        return len(self.previous)
    def __eq__(self, other):
        if self.name == other:
            return True
        else:
            return False