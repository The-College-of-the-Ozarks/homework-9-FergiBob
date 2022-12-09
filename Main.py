#referenced Josh's code for a couple syntax questions about creating the library and good methods for displaying functioning code.

import library as l
import person as p
import book as b
f = open('catalog.csv', 'r')

lib = l.Library('Good Books', f)
f.close()

