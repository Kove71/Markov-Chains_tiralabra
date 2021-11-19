from os import terminal_size
from corpus_data import get_corpus

def tokenize(corpus_name = "corpus.txt"):
    text = get_corpus(corpus_name)
    tokenized_text = text.split()
    return tokenized_text