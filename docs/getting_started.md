# 🚀 Getting Started with Corpy

Welcome! This guide will walk you through the basic usage of **Corpy**, a lightweight Python library for analyzing textual corpora.

---

## 📦 Installation

Corpy is implemented in pure Python and requires no external dependencies.

You can clone the repository directly:

```bash
git clone https://github.com/your-username/corpy.git
cd corpy
```
---
## Then import the module in your script:
```python
from corpy import Corpy
``` 
---
<span style="font-size:1.5em; font-weight:bold">📘 Example Usage </span>  
<span style="font-size:1.5em; font-weight:600">1. Import the library and define your corpus</span> 
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
<span style="font-size:1.5em; font-weight:600">2. Analyze Vocabulary and Word Statistics</span> 

<span style="font-size:1.2em; font-weight:600">🔤 Vocabulary</span> 
```python
print(corpy.vocabulary)
``` 
Output:
```python
['best', 'evolution', 'favorite', 'ghost', 'gengar', 'in', 'is', 'like', 'mega', 'my', 'pokemon', 'the', 'type']

``` 
<span style="font-size:1.2em; font-weight:600">📊 Word-level statistics (.data)</span> 
```python
print("--- Data of some words ---")
print("The word 'pokemon' appears in", corpy.data['pokemon']['exist in'], "documents")
print("The word 'mega' appears in doc3", corpy.data['mega']['doc3'], "times")
print("All stats about 'gengar':", corpy.data['gengar'])
```
Output:
```python
--- Data of some words ---
The word 'pokemon' appears in 3 documents
The word 'mega' appears in doc3 2 times
All stats about 'gengar': {'doc1': 1, 'doc2': 0, 'doc3': 1, 'total': 2, 'exist in': 2}
```
See all data
```python
print("--- all Data ----")
for i in corpy.data:
    print("word: ",i)
    print("Data -->",corpy.data[i])
```
Outout:
```python
--- all Data ----
word:  best
Data --> {'doc1': 0, 'doc2': 0, 'doc3': 1, 'total': 1, 'doc_freq': 1}
word:  evolution
Data --> {'doc1': 0, 'doc2': 0, 'doc3': 1, 'total': 1, 'doc_freq': 1}
word:  favorite
Data --> {'doc1': 1, 'doc2': 0, 'doc3': 0, 'total': 1, 'doc_freq': 1}
word:  gengar
Data --> {'doc1': 1, 'doc2': 0, 'doc3': 1, 'total': 2, 'doc_freq': 2}
word:  ghost
Data --> {'doc1': 0, 'doc2': 1, 'doc3': 0, 'total': 1, 'doc_freq': 1}
word:  i
Data --> {'doc1': 0, 'doc2': 1, 'doc3': 0, 'total': 1, 'doc_freq': 1}
word:  in
Data --> {'doc1': 0, 'doc2': 0, 'doc3': 1, 'total': 1, 'doc_freq': 1}
word:  is
Data --> {'doc1': 1, 'doc2': 0, 'doc3': 1, 'total': 2, 'doc_freq': 2}
word:  like
Data --> {'doc1': 0, 'doc2': 1, 'doc3': 0, 'total': 1, 'doc_freq': 1}
word:  mega
Data --> {'doc1': 0, 'doc2': 0, 'doc3': 2, 'total': 2, 'doc_freq': 1}
word:  my
Data --> {'doc1': 1, 'doc2': 0, 'doc3': 0, 'total': 1, 'doc_freq': 1}
word:  pokemon
Data --> {'doc1': 1, 'doc2': 1, 'doc3': 1, 'total': 3, 'doc_freq': 3}
word:  the
Data --> {'doc1': 0, 'doc2': 1, 'doc3': 1, 'total': 2, 'doc_freq': 2}
word:  type
Data --> {'doc1': 0, 'doc2': 1, 'doc3': 0, 'total': 1, 'doc_freq': 1}
```
---
<span style="font-size:1.5em; font-weight:600">3. Document-level Statistics
</span> 
```python
print(corpy.doc_data)
```
Output:
```python
{'doc1': {'total': 5}, 'doc2': {'total': 6}, 'doc3': {'total': 9}, 'all': {'total': 20}}
```
<span style="font-size:1.5em; font-weight:600">4. Summary Overview
</span> 

```python
print(corpy.summary())
```
Output:

```python
{
 'documents': 3,
 'vocabulary size': 13,
 'average words per document': 6.67
}
```
---
<span style="font-size:1.5em; font-weight:600"> 📚 Learn More
</span> 

- [<span style="font-size:1em; font-weight:600">Project README.</span> ](https://github.com/Ariiies/corpy/blob/main/README.md)
- <span style="font-size:1em; font-weight:600">Full Api Reference.</span> (coming soon)
---
<span style="font-size:1.5em; font-weight:600">✅ Requirements</span>
- Python 3.7 or newer

- No additional libraries required
---
© Luis Aries Meza Castillo – MIT License