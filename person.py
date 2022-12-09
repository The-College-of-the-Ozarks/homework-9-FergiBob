class Person:
    def __init__(self, first, last):
        self.first = first 
        self.last = last
        self.Book_List = []
        
    def __repr__(self):
        return f'{self.first} {self.last}, Books checked out: {self.Book_List}'
        
    def print_name(self):
        print(f'{self.first} {self.last}')        
        
    def print_current_books(self):
        print(f'{self.Book_List}')
        
    def __len__(self):
        return len(self.Book_List)    
        