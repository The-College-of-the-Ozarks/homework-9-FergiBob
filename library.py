import book as b
import person as p
f = open('catalog.csv', 'r')

class Library:
    # __init__
    # Requires catalog to be a file OPEN FOR READING
    # The catalog file has columns author and title
    # Currently this requires the Book class to be defined
    # in a file called book.py (you may change these as desired)
    # and requires the Book class __init__() function to take
    # the title of the book first, author second.
    def __init__(self, name, catalog):
        self.name = name
        self.catalog = []
        self.unavailable = []
        for line in catalog:
            clean_line = line.strip()
            clean_line = clean_line.split(',')
            self.catalog.append(b.Book(clean_line[1],clean_line[0]))
            
    def __repr__(self):
        return f'{self.name}\n{self.catalog}'
    
    def print_catalog(self):
        for n in self.catalog:
            print(f'{n.name},{n.status}')
    
    def print_available(self):
        for n in self.catalog:
            if n.status == True:
                print(n.name)    
                
    def print_unavailable(self):
        for n in self.catalog:
            if n.status == False:    
                print(f'{n.name} : {n.current}')
   
    def checkout(self, person, book):  
        # book = b.Book(book)
        # person = p.Person(person)
        if book.status == True:
            person.Book_List.append(book.title)
            book.status = False
            book.current.append(person)
        
        else:
            print(f'{book} is currently unavailable.')
            
    def turn_in(self, person, book):
        # book = b.Book(book)
        # person = p.Person(person)
        if book in person.Book_List:
            person.Book_List.remove(book.title)
            book.status = True
            book.current.remove(person)
            book.previous.append(person)

        else:
            print(f'{book} is not checked out to {person}')
            
    def __add__(self, book):
        if book in self.catalog:
            print(f'{book} is already in library.')
        else:
            self.catalog.append(book)
            
    def __sub__(self, book):
        if book in self.catalog and book.status == True:
            self.catalog.remove(book)
        else:
            print(f'Book not available to be removed.')
            
    def __len__(self):
        return len(self.catalog)
  
    
f.close()    
