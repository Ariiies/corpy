# firs of all import corpy
from corpy import Corpy as cp

# Example of how to use corpy and how its works. -First step: need a corpus, a list of strings
# in this case i made form a trhee short lines based in pokemon.

corpus = ["gengar is my favorite pokemon",
          "i like the ghost type pokemon",
          "mega gengar is the best mega evolution in pokemon"]

# second step: initialize the object
corpy = cp(corpus)

#  final stept: for show the data.
# my intention to create this project, is, to the time of work with a corpus
# is get the data of words in it, so, the most important part of this project is
# the funcion of Data and Data2, functions that birngs data like the number of times 
# that a specific word is used in some document or in many documents appears.
#  this is a dictionary, so it works with indices 

# an example
print("--- Data of some words ----")
print('the word "pokemon" exist in ',corpy.Data['pokemon']["exist in"], ' documents')
print('the word "mega" appears in doc3 a total of ',corpy.Data['mega']['doc3'], " times")
print('all data about the word "gengar = "', corpy.Data['gengar'])

print("--- all Data ----")
for i in corpy.Data:
    print("word: ",i)
    print("Data -->",corpy.Data[i])


print("--- all Data 2 ----")
for i in corpy.Data2:
    print(i, corpy.Data2[i])










