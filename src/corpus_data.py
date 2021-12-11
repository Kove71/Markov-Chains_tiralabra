import os

DIRNAME = os.path.dirname(__file__)

def get_corpus(corpus_name = "corpus.txt"):
    """Hakee korpuskekstin ja palauttaa sen

    Args:
        corpus_name: korpustekstitiedoston nimi
    """
    corpus_path = os.path.join(DIRNAME, "..", "data", corpus_name)
    try:
        with open(corpus_path, encoding="utf-8") as file:
            text = file.read()
        file.close()
    except OSError:
        raise Exception
    return text
