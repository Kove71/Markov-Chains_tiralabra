import os

DIRNAME = os.path.dirname(__file__)

def get_corpus():
    """Hakee korpuskekstin ja palauttaa sen
    """
    corpus_path = os.path.join(DIRNAME, "..", "data", "corpus.txt")
    with open(corpus_path) as f:
        text = f.read()
    return text

if __name__ == "__main__":
    print(get_corpus())