# firs of all import corpy
from corpy import Corpy as cp

# create the corpus
corpus = ["gengar is my favorite pokemon",
          "i like the ghost type pokemon",
          "mega gengar is the best mega evolution in pokemon"]

# initialize the object
corpy = cp(corpus)

#  some aspects of the objects is the obtencion of the vocabulary and the corpus.
print("--- Vocabulary ----")
print(corpy.get_vocabulary())
print("--- Corpus ---")
print(corpy.get_corpus())

# functions of set vocabulary
new_bocabulary = corpy.get_vocabulary()
new_bocabulary.append("mewtwo")
corpy.set_vocabulary(new_bocabulary)
print("--- new Vocabulary ----")
print(corpy.get_vocabulary())

# function to set the corpus
corpus2 = corpus = ["mewtwo is my favorite pokemon",
          "i like the psysic type pokemon",
          "mega mewtwo is the best mega evolution in pokemon"]

corpy.set_corpus(corpus2)

print("--- new corpus ---")
print(corpy.get_corpus())

# if the corpus is changed, automatically the vocab is set too
print("--- new corpus means new vocabulary ---")
print(corpy.get_vocabulary())



