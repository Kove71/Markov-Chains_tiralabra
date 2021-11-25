from tokenize_corpus import tokenize
from trie_node import TrieNode

class Trie:
    """Trie-tietorakenneluokka
    """

    def __init__(self, text, depth):
        """Luokan konstruktori. Alustaa korpustekstin, pituuden,
        syvyyden ja luo root-noden.
        """

        self.text = text
        self.n = len(text)
        self.depth = depth
        self.root = TrieNode("*", 0)

    def create_tree(self):
        """Luo puun kutsumalla add_ngram metodia.
        """

        for i in self.text:
            sentence_length = len(i) - self.depth
            for j in range(sentence_length):
                self.add_ngram(i[j: j + self.depth])

    def add_ngram(self, ngram):
        """Lisää syvyyden perusteella sanamonikon puuhun.

        Args:
            ngram: sanamonikko, joka lisätään puuhun
        """
        node = self.root
        for word in ngram:
            child = node.check_children(word)
            if not child:
                child = TrieNode(word, node.get_depth() + 1)
                node.add_child(child)
                node = child
            else:
                child.increase_count()
                node = child

    def print_tree(self, node = None):
        """Tulostaa puun tiedot.
        """

        if not node:
            node = self.root

        for j in node.get_children():
            print(f"Node: {j.get_word()} | Freq: {j.get_count()} | "
            f"Depth: {j.get_depth()} | Parent: {node.get_word()}")
            self.print_tree(j)

if __name__ == "__main__":
    trie = Trie(tokenize(), 2)
    trie.create_tree()
    trie.print_tree()
