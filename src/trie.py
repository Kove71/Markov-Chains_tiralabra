"""Trien luominen
"""
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
    
    def find_ngram(self, ngram):
        """Etsii monikon ja palauttaa monikon lapset.

        Args:
            ngram: sanamonikko, joka etsitään
        
        Returns:
            children: lista TrieNode-olioista, jotka
            ovat monikon lapsia.
        """
        node = self.root
        children = []
        for i in ngram:
            child = node.check_children(i)
            if not child:
                return None
            else:
                node = child
                children = node.get_children()
        return children

