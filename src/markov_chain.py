import random

from tokenize_corpus import TokenizeCorpus
from trie import Trie

class MarkovChain:
    """Markov-ketjuista vastaava luokka.
    """

    SENTENCE_MAX_LENGTH = 50

    def __init__(self, order = 3, corpus_name = "corpus.txt"):
        """Luokan konstruktori

        Args:
            order: ketjun aste
            corpus_name: lähdemateriaalin tekstitiedoston
            nimi.
        """
        self.tokenize = TokenizeCorpus(corpus_name)
        self.text = self.tokenize.tokenize()
        if not self.text:
            self.handle_file_error("No such file found")
        self.order = order
        self.trie = Trie(self.text, self.order + 1)
        self.trie.create_tree()
    
    def handle_file_error(self, message):
        """Käsittelee virheellisen tiedoston
        """
        raise Exception(message)

    def generate_text(self, sentence_amount = 1):
        """Generoi lauseita kutsumalla 
        generate_sentence-metodia.

        Args:
            sentence_amount: generoitavien lauseiden määrä.
        
        Returns:
            generated_text: generoitu teksti
        """
        generated_text = ""

        for i in range(sentence_amount):
            choices = self.tokenize.first_words()
            try:
                word = random.choices(choices)[0]
                generated_text += self.generate_sentence(word)
                generated_text += "\n"
                print(word)
            except Exception:
                self.handle_file_error("Markov Chain -order too high")
                break        
        return generated_text
    
    def generate_sentence(self, first_word):
        """Lauseen generointialgoritmi.

        Args:
            first_word: lauseen ensimmäinen sana
        
        Returns:
            generoitu lause
        """
        prior_state = [first_word]
        generated_sentence = first_word
        sentence_ending = "."
        for j in range(self.SENTENCE_MAX_LENGTH):
            choices = self.trie.find_ngram(prior_state)
            if not choices:
                break
            choices_attributes = self.get_choices_attributes(choices)
            word = random.choices(choices_attributes[0], choices_attributes[1])[0]
            if word in ["?", ".", "!"]:
                sentence_ending = word
                break
            generated_sentence += f" {word}"
            prior_state.append(word)
            if len(prior_state) > self.order:
                prior_state.pop(0)
        
        return f"{generated_sentence}{sentence_ending}"
    
    def get_choices_attributes(self, choices):
        """Luo listat populaatiosta ja painoista random.choices varten

        Args:
            choices: lista TrieNode-olioista
        
        Returns:
            tuple jossa sanat ja painot
        """
        choices_words = [*choices]
        choices_weights = [node.get_count() for node in choices.values()]
        return (choices_words, choices_weights)
