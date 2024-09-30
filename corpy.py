# Text Corpus w/ Python
class Corpy:                  # Iniciliza el objeto con una lista de Strings
    def __init__(self, corpus):# Initialize the object with a list Strings
        self.__corpus = corpus
        self.__vocabulary = sorted(set(' '.join(self.__corpus).split()))
    
    # Getters and Setters for the vocabulary and the corpus
    # gettes y setters para el vocabulario y el corpus
    def get_vocabulary(self):  
        vocabulary = self.__vocabulary
        return vocabulary
    
    def get_corpus(self):
        corpus = self.__corpus
        return corpus
    
    def set_vocabulary(self, vocabulary):
        self.__vocabulary=vocabulary
   
    def set_corpus(self, corpus): 
        self.__corpus=corpus
        self.__vocabulary = sorted(set(' '.join(self.__corpus).split()))
    
    # this function is for getting data about the words in the corpus, its a dictionary like a
    # bag of words, all in json format
    @property # diccionario sobre las palabras en los documentos, similar a una bag of words en json
    def Data(self):
        data={}
        for ele in self.__vocabulary:
            data[ele], total, ndoc = {}, 0, 0
            for i in range(1, len(self.__corpus)+1):
                flag, count, text = True, 0, self.__corpus[i-1].split()
                for word in text:
                    if ele == word:
                        count+=1
                        total+=1
                        flag = False
                        data[ele].update({f'doc{i}': count}) 
                if flag:
                    data[ele].update({f'doc{i}': 0})
            data[ele].update({f'total': total})
            for l in range(1, len(self.__corpus)+1): 
                if data[ele][f'doc{l}'] != 0:
                    ndoc +=1
            data[ele].update({f'exist in': ndoc})               
        return data
   
    # Anothes function for the general data in the docs 
    @property # datos de la cantidad de palabras en los documentos
    def Data2(self):
        data, total={},0
        for doc in range(len(self.__corpus)):
            total+= len(self.__corpus[doc].split())
            data[f"doc{doc+1}"]= {f"total": len(self.__corpus[doc].split())}
        data["all"]={"total":total}
        return data