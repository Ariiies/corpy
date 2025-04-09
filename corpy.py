# Text Corpus w/ Python
class Corpy:                  # Iniciliza el objeto con una lista de Strings
    def __init__(self, corpus: list):# Initialize the object with a list Strings
        self.__corpus = corpus
        self.__vocabulary = sorted(set(' '.join(self.__corpus).split()))
    
    # Getters and Setters for the vocabulary and the corpus
    # gettes y setters para el vocabulario y el corpus
    @property # getter para el vocabulario
    def vocabulary(self)->list:  
        vocabulary = self.__vocabulary
        return vocabulary
    
    @property # getter para el corpus
    def corpus(self)->list:
        corpus = self.__corpus
        return corpus
    
    @vocabulary.setter
    def vocabulary(self, vocabulary:list):
        self.__vocabulary=vocabulary

    @corpus.setter # setter para el corpus
    def corpus(self, corpus:list): 
        self.__corpus=corpus
        self.__vocabulary = sorted(set(' '.join(self.__corpus).split()))
    
    # this function is for getting data about the words in the corpus, its a dictionary like a
    # bag of words, all in json format
    @property # diccionario sobre las palabras en los documentos, similar a una bag of words en json
    def Data(self)->dict:
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
            word_data['exist in'] = count_doc
            data[word] = word_data
        return data
   
    # Anothes function for the general data in the docs 
    @property # datos de la cantidad de palabras en los documentos
    def Data2(self)->dict:
        data, total = {}, 0
        for i, text in enumerate(self.__corpus, start=1):
            word_count = len(text.split())
            total += word_count
            data[f"doc{i}"] = {"total": word_count}
        data["all"] = {"total": total}
        return data