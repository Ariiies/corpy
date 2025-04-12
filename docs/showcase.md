
# 🚀 Showcase Corpy

Welcome! This guide will walk you through the usage of **Corpy**.

---
<span style="font-size:1.5em; font-weight:bold">
📘 Contents. </span> 

- Play with the mutability.
- Aplications.
- Resumen.
- Top words.
- Tool for TF-IDF matrix.
- Top words with TFIDF and Corpy.
- Similitud by cosine with Corpy and TFIDF

---


 
<span style="font-size:1.5em; font-weight:600"> To Start import the library and define your corpus</span> 
```python
from corpy import Corpy

corpus = [
    "gengar is my favorite pokemon",
    "i like the ghost type pokemon",
    "mega gengar is the best mega evolution in pokemon"
]

corpy = Corpy(corpus)
``` 
---

<span style="font-size:1.5em; font-weight:bold">
Play with the mutability </span>

Although not ideal, since Corpy is not designed to modify contents, it is possible.
```python
print("--- old vocabulary ---")
print(corpy.vocabulary)
corpy.vocabulary += ['charmander']
print("--- vocabulary extended ---")
print(corpy.vocabulary)
```
Output:
```
--- old vocabulary ---
['aries', 'best', 'evolution', 'favorite', 'first', 'gengar', 'ghost', 'i', 'in', 'is', 'like', 'mega', 'my', 'pokemon', 'sign', 'the', 'type', 'zodiac']
--- vocabulary extended ---
['aries', 'best', 'evolution', 'favorite', 'first', 'gengar', 'ghost', 'i', 'in', 'is', 'like', 'mega', 'my', 'pokemon', 'sign', 'the', 'type', 'zodiac', 'charmander']
```
The new word will be added to the data with 0 matches.

*!!! Note: Searching for a word not in the vocabulary will produce an error.*
```python
print(corpy.data["charmander"])
```
Output:
```
{'doc1': 0, 'doc2': 0, 'doc3': 0, 'total': 0, 'doc_freq': 0}
```
You can also completely modify the vocabulary.

*!!! Note: Modifying the vocabulary will not affect the corpus.*
```python
corpy.vocabulary = ['pikachu', 'charmander','gengar']
print(corpy.vocabulary)
```
Output:
```
['pikachu', 'charmander', 'gengar']
```
View the data.
```python
print("--- all Data ----")
for i in corpy.data:
    print("word: ", i)
    print("Data -->", corpy.data[i])
```
Output:
```
--- all Data ----
word:  pikachu
Data --> {'doc1': 0, 'doc2': 0, 'doc3': 0, 'total': 0, 'doc_freq': 0}
word:  charmander
Data --> {'doc1': 0, 'doc2': 0, 'doc3': 0, 'total': 0, 'doc_freq': 0}
word:  gengar
Data --> {'doc1': 1, 'doc2': 0, 'doc3': 1, 'total': 2, 'doc_freq': 2}
```
You can also add texts to the corpus.
```python
corpy.corpus += ['Pikachu is the best pokemon']
print('--- corpus ---')
for i, corpus in enumerate(corpy.corpus):
    print("doc{} : {}".format(i+1, corpus))
```
Output:
```
--- corpus ---
doc1 : gengar is my favorite pokemon
doc2 : i like the ghost type pokemon
doc3 : mega gengar is the best mega evolution in pokemon
doc4 : Pikachu is the best pokemon
```
*!!! Note: Any modification to the corpus will affect the entire object, modifying and resetting the vocabulary and other properties.*
Example:
```python
corpy.corpus = ['Pikachu is the best pokemon', 'charizard is the best fire type pokemon']
print("--- new corpus ---")
for i, corpus in enumerate(corpy.corpus):
    print("doc{} : {}".format(i+1, corpus))
print("--- new vocabulary ---")
print(corpy.vocabulary)
```
Output:
```
--- new corpus ---
doc1 : Pikachu is the best pokemon
doc2 : charizard is the best fire type pokemon
--- new vocabulary ---
['Pikachu', 'best', 'charizard', 'fire', 'is', 'pokemon', 'the', 'type']
```
<span style="font-size:1.5em; font-weight:bold"> Applications </span>

The truly useful and interesting aspect of Corpy is what it contributes to text analysis, and how it can be used to create, facilitate, and easily modify various tools and applications for text analysis.

!!! Note: All examples below reference the original unmodified corpus.

<span style="font-size:1.2em; font-weight:bold"> Summary </span>

The most basic application is simply providing a summary of the contents, which can be done in two ways:

- Using the summary() method, with access to the content.
- Printing the object, for reading only.
Example:
```python
print(corpy)
```
Output:
```
<Corpy Analyzer>
- Documents: 3
- Vocabulary Size: 14 unique words
- Total Words: 20
- Avg. Words per Document: 6.67
```
with summary()
```python
print(corpy.summary())
```
Output:
```
{'documents': 3, 'vocabulary_size': 14, 'total_words': 20, 'average_words_per_document': 6.67}
```
<span style="font-size:1.2em; font-weight:bold">
Top words </span>

Another basic way to use Corpy is to view the most frequently used words in the corpus.
```python
top_n, count = 5, 0
# Sort by highest occurrences in the 'total' key
top_words = dict(sorted(corpy.data.items(), key=lambda x: -x[1]['total'])[:top_n])
print("--- Top Words ---")
for word, data in top_words.items():
    count+=1
    print(f"{count}- {word}: appeared {data['total']} times in {data['doc_freq']} docs")
    
```
Output:
```
--- Top Words ---
1- pokemon: appeared 3 times in 3 docs
2- gengar: appeared 2 times in 2 docs
3- is: appeared 2 times in 2 docs
4- mega: appeared 2 times in 1 docs
5- the: appeared 2 times in 2 docs
```
<span style="font-size:1.2em; font-weight:bold"> Tool for TF-IDF Matrix </span>

Corpy can be used as a tool to develop other text analysis applications by facilitating access to the necessary data. One such case is as a tool for creating a class to calculate a TF-IDF matrix.

- Check the TF-IDF project with Corpy.

The class looks like this:
```python
from math import log

class TFIDF:
    def __init__(self, corpus: 'Corpy'):
        # TF (Normalized frequency)
        self.tf = [
            [corpus.data[word][f'doc{i+1}'] / len(corpus.corpus[i].split()) 
             for word in corpus.vocabulary] 
            for i in range(len(corpus.corpus))
        ]
        
        # IDF (Inverse document frequency)
        self.idf = [
            log(len(corpus.corpus) / (1 + corpus.data[word]['doc_freq'])) 
            for word in corpus.vocabulary
        ]
        
        # TF-IDF
        self.matrix = self.tf * self.idf
```
In simple terms, what TF-IDF does is:
It measures whether a word is important (rare globally but frequent in a specific document).
Breakdown:

- TF = Local frequency ("Is this word common here?").
- IDF = Global rarity ("Is this word unique overall?").
- High TF-IDF = Key word for the document.
- Low TF-IDF = Common/irrelevant word.

With the help of a class like this, various classifications can be performed.

<span style="font-size:1.2em; font-weight:bold"> Top Words with TF-IDF and Corpy </span>

Example: Display the most relevant words in the corpus using term frequency.
```python
''' Top words per document using TF from TFIDF object and data from Corpy object.'''
tfidf = TFIDF(corpy)
result = {}
for i, doc in enumerate(corpy.doc_data.keys()):
    values = []
    if doc != 'all':
        for i2, word in enumerate(corpy.data.keys()):
            values.append((word, tfidf.tf[i][i2]))
        values.sort(key=lambda x: x[1], reverse=True)
        result[doc] = values[:3]


print("--- Top Words per Document ---")
for doc, words in result.items():
    print(f"{doc}: {words}")
```
Output:
```
--- Top Words per Document ---
doc1: [('favorite', 0.2), ('gengar', 0.2), ('is', 0.2)]
doc2: [('ghost', 0.16666666666666666), ('i', 0.16666666666666666), ('like', 0.16666666666666666)]
doc3: [('mega', 0.2222222222222222), ('best', 0.1111111111111111), ('evolution', 0.1111111111111111)]
```
Although using Term Frequency alone is not the most optimal, as it is raw data about word counts, in most cases it is preferable to use TF-IDF.

Example: Function that displays the top words for the documents or for a specific document.
```python
import numpy as np

def get_top_tfidf_words(tfidf_obj, corpus_obj, top_n=10, doc_index=None):
 
    # 1. Select scores (per doc or global)
    scores = tfidf_obj.matrix[doc_index] if doc_index is not None else np.sum(tfidf_obj.matrix, axis=0)
    
    # 2. Get indices of top words
    top_indices = np.argsort(scores)[-top_n:][::-1]
    
    # 3. Collect results
    results = [
        (corpus_obj.vocabulary[i], float(scores[i]))  # Convert to float for serialization
        for i in top_indices
    ]
    
    return results
```
Fubction call:
```python
# For the entire corpus
top_global = get_top_tfidf_words(tfidf, corpy, top_n=5)
print("Most relevant words globally:")
for word, score in top_global:
    print(f"{word}: {score:.4f}")

# For a specific document (e.g., doc1)
top_doc1 = get_top_tfidf_words(tfidf, corpy, top_n=3, doc_index=0)
print("\nMost relevant words in Doc 1:")
for word, score in top_doc1:
    print(f"{word}: {score:.4f}")
```
Output:
```
Most relevant words globally:
mega: 0.0901
my: 0.0811
favorite: 0.0811
like: 0.0676
ghost: 0.0676

Most relevant words in Doc 1:
my: 0.0811
favorite: 0.0811
the: 0.0000
```
Bonus: Version for exporting JSON.
```python
import json

top_words = get_top_tfidf_words(tfidf, corpy)
with open('top_words.json', 'w') as f:
    json.dump({"top_words": top_words}, f, indent=2)
```
<span style="font-size:1.2em; font-weight:bold"> Similarity by Cosine with Corpy and TF-IDF </span>

Another very interesting option with TF-IDF and Corpy is to use their properties to apply cosine similarity to compare documents.
```python
import numpy as np
from numpy.linalg import norm

def cosine_similarity(vec1, vec2):
    """Calculates cosine similarity between two vectors"""
    return np.dot(vec1, vec2) / (norm(vec1) * norm(vec2))
```
To compare documents:
```python
def compare_documents(corpy_obj, tfidf_obj, doc1_idx: int, doc2_idx: int) -> float:
    # Verify valid indices
    if doc1_idx >= len(corpy_obj.corpus) or doc2_idx >= len(corpy_obj.corpus):
        raise ValueError("Document index out of range")
    # Get TF-IDF vectors for the documents
    vec1 = tfidf_obj.matrix[doc1_idx]
    vec2 = tfidf_obj.matrix[doc2_idx]
    
    # Calculate cosine similarity
    return cosine_similarity(vec1, vec2)
```
Function call:
```python
# Comparisons
print("Similarity between documents:")
print(f"Doc1 vs Doc2: {compare_documents(corpy, tfidf, 0, 1):.3f}")
print(f"Doc1 vs Doc3: {compare_documents(corpy, tfidf, 0, 2):.3f}")
print(f"Doc2 vs Doc3: {compare_documents(corpy, tfidf, 1, 2):.3f}")
print(f"Doc1 vs Doc1: {compare_documents(corpy, tfidf, 0, 0):.3f}")
```
Output:
```
Similarity between documents:
Doc1 vs Doc2: 0.150
Doc1 vs Doc3: 0.116
Doc2 vs Doc3: 0.087
Doc1 vs Doc1: 1.000
```