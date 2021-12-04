"""Tokenisoi lähdemateriaalin käsittelyä varten
"""
from corpus_data import get_corpus
from nltk.tokenize import sent_tokenize, word_tokenize

class TokenizeCorpus:
    """Tokenisoi lähdemateriaalin käyttäen nltk-kirjastoa
    Args:
        corpus_name: korpuksen nimi
    """

    def __init__(self, corpus_name = "corpus.txt"):
        self.text = get_corpus(corpus_name)
        if not self.text:
            return False
        self.text_sentences = sent_tokenize(self.text)
        self.text_words = [word_tokenize(s) for s in self.text_sentences]

    def tokenize(self):
        return self.text_words
    
    def first_words(self):
        return [sentence[0] for sentence in self.text_words]
