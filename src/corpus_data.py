import os

DIRNAME = os.path.dirname(__file__)

def get_corpus(corpus_name = "corpus.txt"):
    """Hakee korpuskekstin ja palauttaa sen

    Args:
        corpus_name: korpustekstitiedoston nimi
    """
    corpus_path = os.path.join(DIRNAME, "..", "data", corpus_name)
    with open(corpus_path) as f:
        text = f.read()
    return text

if __name__ == "__main__":
    print(get_corpus())
