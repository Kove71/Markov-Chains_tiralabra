import random

from tokenize_corpus import tokenize
from trie import Trie

class MarkovChain:

    SENTENCE_MAX_LENGTH = 20

    def __init__(self, order = 3, corpus_name = "corpus.txt"):
        self.text = tokenize(corpus_name)
        self.order = order
        self.trie = Trie(self.text, self.order + 1)
        self.trie.create_tree()
    
    def generate_text(self, sentence_amount = 1):
        generated_text = ""

        for i in range(sentence_amount):
            choices = self.trie.get_root_children()
            choices_attributes = self.get_choices_attributes(choices)
            word = random.choices(choices_attributes[0], choices_attributes[1])[0]
            generated_text += self.generate_sentence(word)
            generated_text += "\n"        
        return generated_text
    
    def generate_sentence(self, first_word):
        prior_state = [first_word]
        first_word = first_word[0].upper() + first_word[1:]
        generated_sentence = f"{first_word}"
        for j in range(self.SENTENCE_MAX_LENGTH):
            choices = self.trie.find_ngram(prior_state)
            if not choices:
                break
            choices_attributes = self.get_choices_attributes(choices)
            word = random.choices(choices_attributes[0], choices_attributes[1])[0]
            generated_sentence += f" {word}"
            prior_state.append(word)
            if len(prior_state) > self.order:
                prior_state.pop(0)
        
        return f"{generated_sentence}."
    
    def get_choices_attributes(self, choices):
        choices_words = [node.get_word() for node in choices]
        choices_weights = [node.get_count() for node in choices]
        return (choices_words, choices_weights)


if __name__ == "__main__":
    markov = MarkovChain(5, "greatgatsby.txt")
    print(markov.generate_text(4))