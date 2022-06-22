#Basics of python

print("hello world, Python")

#* Arithmetic operators
#* python follows PEDMAS
#* run these on the shell to find output
2+2
3-2
13/5 #floating division
4*4
2**2 #exponent
10%3 # remainder modulo operator
13//5 #integer divison

"""
Comparison Operators
 Returns boolean true or false
 test 6 condtions

 logical operators
 and, or, not
"""


"""
functions
 def means defining a function
 if no return statement, returns none
 accepts two types of parameters, Optional and required. s=3

"""


def algebra(s=3):
  return s*2

"""
 Built in functions

str(),len(),int(),float(),input()
"""

"""
try:
   do something
 except  :
  do something
"""

"""
DATA STRUCTURES

Lists: list(),[],mutuable
Tuples:tuple(),(),immutable, similar to lists
Dictionaries: linking key to value, mapping,
can use key to look up the value but vice versa is not true, mutuable and can be edited, represented {}, dict()

 can use tuples as keys here
"""

"""
in
not in
keyword returns true or false
\ is the escape character is prefixing and postfixing the escape the word
\n is new line
fict is list

slicing works by fict[0:3]
start includes the start and n-1 of the end

"""


name=['Game of thrones','Lord of the rings','Narcos']
for character in name:
  print(character)