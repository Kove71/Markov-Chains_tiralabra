from corpus_data import get_corpus

def tokenize(corpus_name = "corpus.txt"):
    """Erottelee tekstin sanat listaan whitespacen mukaan

    Args:
        corpus_name: korpustekstitiedoston nimi

    Returns: tokenisoidun tekstin
    """

    text = get_corpus(corpus_name)
    tokenized_text = text.split()
    return tokenized_text
