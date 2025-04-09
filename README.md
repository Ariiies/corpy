## corpy: text corpus w/ Python

This project is to have data available about the words and documents that make up a corpus.
In the doc corpy.py is where the work going on. 
Corpy is a class that requires a list of strings as input. It has two property bases:
- **corpus (self.__corpus)**
- **vocabulary (seld.__vocabulary)**

And their respective *getters* and *setters*.
The relevant part of the project is about got data from the corpus, the functions or property's that are in charge of that are:
- **data** 
  - *Data function got data about the vocabulary, in form of a dictionary of dictionary's where every word in the vocabulary is the main indice and have heir own dictionary, that dictionary contains the count for that word in every document in the corpus and in many documents appear. the indice for every document is 'doc0' where 0 is the representation of the number of ocument (in the results never is 0), 'total' is the indice of how many times the word appear in all the documents  and 'exist in' is the indice for in how many documents appear.*
- **doc_data**
  - *Data2 is a more simple function, this function count's how many words contains every document and the total. its a dictionary too, where 'doc0' is the main indice for every document and 'all' is for the total. and every second indice is 'total'.* 

The result of these two funcions looks similar that a json document.
