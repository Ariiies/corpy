# Text Corpus w/ Python
class Corpy:
    """Analyzes a corpus of text documents for vocabulary and word usage statistics.
    Supports vocabulary extraction, frequency analysis, and document-level metrics.
    """
    def __init__(self, corpus: list):
        """Initialize the corpus analyzer with a list of text documents.
        Args:
            corpus (list): List of strings where each string represents a document.
                           Automatically generates the vocabulary from the corpus.
        """
        self.__corpus = corpus
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
        """Generate word-level statistics across all documents.
        Returns:
            dict: A dictionary where each key is a word, and the value is another
            dictionary containing:
                - Word count per document ("docN")
                - Total count across all documents ("total")
                - Number of documents the word appears in ("doc_freq")
        Example:
            {
                "example": {
                    "doc1": 2,
                    "doc2": 0,
                    "total": 2,
                    "doc_freq": 1
                }
            }
        """
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
        """Generate document-level word count statistics.
        Returns:
            dict: A dictionary with word counts per document and the total count
            across all documents.
        Example:
            {
                "doc1": {"total": 123},
                "doc2": {"total": 456},
                "all": {"total": 579}
            }
        """
        data, total = {}, 0
        for i, text in enumerate(self.__corpus, start=1):
            word_count = len(text.split())
            total += word_count
            data[f"doc{i}"] = {"total": word_count}
        data["all"] = {"total": total}
        return data

    def summary(self) -> dict:
        """Return a summary of the corpus and basic statistics.
        Returns:
            dict: Contains number of documents, vocabulary size, total words,
                and average words per document.
        """
        num_docs = len(self.__corpus)
        vocab_size = len(self.__vocabulary)
        total_words = self.doc_data["all"]["total"]
        avg_words_per_doc = total_words / num_docs if num_docs else 0

        return {
            "documents": num_docs,
            "vocabulary_size": vocab_size,
            "total_words": total_words,
            "average_words_per_document": round(avg_words_per_doc, 2)
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
