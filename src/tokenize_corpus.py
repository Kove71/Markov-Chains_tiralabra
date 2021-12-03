"""Tokenisoi lähdemateriaalin käsittelyä varten
"""
from corpus_data import get_corpus
from nltk.tokenize import sent_tokenize, word_tokenize

def tokenize(corpus_name = "corpus.txt"):
    """Erottelee tekstin sanat listaan whitespacen mukaan

    Args:
        corpus_name: korpustekstitiedoston nimi

    Returns: tokenisoidun tekstin
    """

    text = get_corpus(corpus_name)
    if not text:
        return False
    text_sentences = sent_tokenize(text)
    return [word_tokenize(s) for s in text_sentences]
