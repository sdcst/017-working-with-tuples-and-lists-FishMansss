#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""
from os import replace


people = ['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
print(people)
x = (input("Type a name on the list to replace: "))
y = (input("Type a name to replace it with: "))
peop = people.index(x)
people.remove(x)
peop.insert[x, y]
print(people)