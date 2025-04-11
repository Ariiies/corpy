# Text Corpus w/ Python
class Corpy:
    """Analyzes a corpus of text documents for vocabulary and word usage statistics.
    Supports vocabulary extraction, frequency analysis, and document-level metrics.
    """
    def __init__(self, corpus: list):
        """Initialize with documents (list[str]). Auto-creates vocabulary."""
        self.__corpus = corpus  
        # Generate vocabulary from the corpus
        self.__vocabulary = sorted(set(' '.join(self.__corpus).split()))

    # Vocabulary properties
    @property
    def vocabulary(self) -> list:
        return self.__vocabulary
    
    @vocabulary.setter
    def vocabulary(self, vocabulary: list):
        """Manually override the auto-generated vocabulary.
        Note: This will not update automatically based on the corpus anymore.
        """
        self.__vocabulary = vocabulary
        
    # Corpus properties
    @property
    def corpus(self) -> list:
        return self.__corpus
    
    @corpus.setter
    def corpus(self, corpus: list):
        """Replace the current corpus and automatically regenerate the vocabulary."""
        self.__corpus = corpus
        self.__vocabulary = sorted(set(' '.join(self.__corpus).split()))
    # Analysis methods
    @property
    def data(self) -> dict:
        """Returns word statistics: counts per doc, total count, and doc frequency.
            Format:  {
                "example": {
                    "doc1": 2,
                    "doc2": 0,
                    "total": 2,
                    "doc_freq": 1
                    },  
                    }   """
        data = {}
        for word in self.__vocabulary:
            word_data, total, count_doc = {}, 0, 0
            for i, text in enumerate(self.__corpus, start=1):
                count = text.split().count(word)
                total += count
                word_data[f'doc{i}'] = count
                if count > 0:
                    count_doc += 1
            word_data['total'] = total
            word_data['doc_freq'] = count_doc
            data[word] = word_data
        return data

    @property
    def doc_data(self) -> dict:
        """Returns word counts per document and total. 
        Format: {
                "doc1": {"total": 100},
                "doc2": {"total": 250},
                "all": {"total": 350}
                }"""
       
        data, total = {}, 0
        for i, text in enumerate(self.__corpus, start=1):
            word_count = len(text.split())
            total += word_count
            data[f"doc{i}"] = {"total": word_count}
        data["all"] = {"total": total}
        return data

    def summary(self) -> dict:
        """Returns corpus stats: num docs, vocab size, total words, avg words/doc"""
        return {
            "documents": len(self.__corpus),
            "vocabulary_size": len(self.__vocabulary),
            "total_words": self.doc_data["all"]["total"],
            "average_words_per_document": round(self.doc_data["all"]["total"] / len(self.__corpus) if len(self.__corpus) else 0, 2)
        }

    def __str__(self) -> str:
        """Return a readable string summary of the Corpy object."""
        stats = self.summary()
        return (
            f"<Corpy Analyzer>\n"
            f"- Documents: {stats['documents']}\n"
            f"- Vocabulary Size: {stats['vocabulary_size']} unique words\n"
            f"- Total Words: {stats['total_words']}\n"
            f"- Avg. Words per Document: {stats['average_words_per_document']:.2f}"
        )

    __repr__ = __str__
