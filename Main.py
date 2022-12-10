#referenced Josh's code for a couple syntax questions about creating the library and good methods for displaying functioning code.
#also referenced dwcofo for good methods for displaying working code (making sure I got everything)

import library as l
import person as p
import book as b
f = open('catalog.csv', 'r')

lib = l.Library('Good Books', f)
f.close()

 #catalog info
print(f'There are {len(lib)} books in the catalog.')
print('\n')
lib.print_catalog()
print('\n\n\n')

#people
person1 = p.Person('Jimmy', "Jon")
person2 = p.Person('Brandon', 'Beck')
person3 = p.Person('Curious', 'George')
person4 = p.Person('Lightning', 'McQueen')

person1.print_name()
person2.print_name()
person3.print_name()
person4.print_name()

#checking out books
lib.checkout(person2, lib.catalog[6])
print('\n')
lib.checkout(person2, lib.catalog[8])
print('\n')
lib.checkout(person2, lib.catalog[5])
print('\n')
lib.checkout(person1, lib.catalog[4])
print('\n')
lib.checkout(person1, lib.catalog[3])
print('\n')
lib.checkout(person1, lib.catalog[2])
print('\n')
lib.checkout(person3, lib.catalog[1])
print('\n')
lib.checkout(person3, lib.catalog[0])
print('\n')
lib.checkout(person3, lib.catalog[6])
print('\n')
lib.checkout(person3, lib.catalog[10])
print('\n')
lib.checkout(person4, lib.catalog[17])
print('\n\n')
lib.checkout(person4, b.Book('Why Python is the Best Language', 'Dr. Who'))
print('\n\n')
lib.checkout(person4, lib.catalog[11])
print('\n')
lib.checkout(person4, lib.catalog[12])
print('\n')
lib.checkout(person4, lib.catalog[13])
print('\n')

print('Unavailable books:')
lib.print_unavailable()
print('\n\n')
print('Available books:')
lib.print_available()
print('\n\n')
print(repr(person2))
print('\n\n')


#turning in
lib.turn_in(person2, lib.catalog[6])
print('\n')
lib.turn_in(person2, lib.catalog[8])
print('\n')
lib.turn_in(person2, lib.catalog[5])
print('\n')
lib.turn_in(person1, lib.catalog[4])
print('\n')
lib.turn_in(person1, lib.catalog[3])
print('\n')
lib.turn_in(person1, lib.catalog[2])
print('\n')
lib.turn_in(person3, lib.catalog[1])
print('\n')
lib.turn_in(person3, lib.catalog[0])
print('\n')
lib.turn_in(person3, lib.catalog[6])
print('\n')
lib.turn_in(person3, lib.catalog[10])
print('\n')
lib.turn_in(person4, lib.catalog[17])
print('\n\n')
lib.turn_in(person4, b.Book('Why Python is the Best Language', 'Dr. Who'))
print('\n\n')
lib.turn_in(person4, lib.catalog[11])
print('\n')
lib.turn_in(person4, lib.catalog[12])
print('\n')
lib.turn_in(person4, lib.catalog[13])
print('\n')


#testing + and - 



lib + b.Book('The Fault in Our Stars', 'John Green')


lib - b.Book('The Chess Players Manual', 'Brenden Ferguson')

lib + b.Book('The Chess Players Manual', 'Brenden Ferguson')
lib.checkout(person1, lib.catalog[-1])
lib - lib.catalog[-1]
lib.turn_in(person1, lib.catalog[-1])
lib - lib.catalog[-1]


lib.checkout(person1, lib.catalog[8])

print(repr(lib.catalog[8]))




