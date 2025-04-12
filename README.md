# 📚 Corpy - Text Corpus Analyzer

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Corpy** is a minimalist Python library for quantitative analysis of text corpora.  
Designed for efficient processing of document collections, it provides essential metrics about vocabulary and word distribution.

## ✨ Features

- Automatic vocabulary extraction  
- Lexical frequency statistics  
- Per-document and global metrics  
- Intuitive interface using property getters  
- Clear and structured output  
- Efficient implementation using pure Python

## 🔍 Access to Key Metrics

### ▸ `.vocabulary`
**Unique Vocabulary**  
Alphabetically sorted list of all distinct words in the corpus.

### ▸ `.data`
**Lexical Frequencies**  
Dictionary containing:
- ✓ Word count per document (`doc1`, `doc2`, ...)
- ✓ Total word occurrences
- ✓ Document frequency (how many documents contain the word)

### ▸ `.doc_data`
**Document Statistics**  
Includes:
- ✓ Word count per document
- ✓ Total number of words across the corpus

### ▸ `.summary()`
**Global Overview**  
Summary including:
- ✓ Number of documents
- ✓ Vocabulary size
- ✓ Average words per document

---

## 📖 Usage & Documentation

Looking to get started?  
Check out the [**Getting Started Guide**](https://github.com/Ariiies/corpy/blob/main/docs/getting_started.md) for installation instructions, examples, and full API reference.

To learn more about Corpy, check  [<span style="font-size:1em; font-weight:600">Showcases and more reference.</span> ](https://github.com/Ariiies/corpy/blob/main/docs/showcase.md)

---

## 📊 Main Metrics Table

| Method/Property  | Description                                  | Output Type              |
|------------------|----------------------------------------------|--------------------------|
| `vocabulary`     | Ordered list of unique words                 | `list[str]`              |
| `data`           | Detailed word-level statistics               | `dict[str, dict]`        |
| `doc_data`       | Word counts per document                     | `dict[str, dict]`        |
| `summary()`      | Aggregated metrics for the corpus            | `dict[str, int/float]`   |

---

## 🖥 Technical Requirements

- **Python 3.7+**
- **Zero-dependencies** – Implemented in pure Python
- **Cross-platform** – Compatible with Windows, Linux, and macOS

---

## 📜 License
MIT © Luis Aries Meza Castillo – A tool for computational linguistic analysis
