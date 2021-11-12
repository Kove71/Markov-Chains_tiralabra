import markovify
import corpus_data

def generate_sentence(n = 1, corpus_name = "corpus.txt"):
    """Käyttää markovify-moduulia tekstin generoimiseen.
    
    Args:
        n: lauseiden määrä
        corpus_name: korpustekstitiedoston nimi
    """
    text = corpus_data.get_corpus(corpus_name)
    text_model = markovify.Text(text)
    generated_text = ""
    for i in range(n):
        generated_text += text_model.make_sentence()
        generated_text += "\n"
    
    return generated_text

if __name__ == "__main__":
    n = int(input("Amount of sentences?"))
    print(generate_sentence(n, "dracula.txt"))