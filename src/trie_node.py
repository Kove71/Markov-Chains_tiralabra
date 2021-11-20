class TrieNode:
    """Solmu/sana trie-rakenteessa.
    """

    def __init__(self, word, depth):
        """Luokan konstruktori. Alustaa
        sanan, tyhjän listan solmun lapsille,
        solmun syvyyden ja esiintymismäärän.

        Args:
            word: sana
            depth: syvyys
        """

        self.word = word
        self.children = []
        self.node_depth = depth
        self.count = 1

    def get_children(self):
        """Palauttaa listan lapsista
        """
        return self.children

    def get_depth(self):
        """Palauttaa syvyyden.
        """
        return self.node_depth

    def get_word(self):
        """Palauttaa sanan.
        """
        return self.word

    def get_count(self):
        """Palauttaa esiintymismäärän.
        """
        return self.count

    def check_children(self, word):
        """Tarkistaa, esiintykö sana solmun lapsissa.
        Palauttaa joko solmun, jos se löytyy, tai None
        jos sitä ei löydy

        Args:
            word: tarkistettava sana
        """
        for i in self.children:
            if word == i.get_word():
                return i
        return None

    def increase_count(self):
        """Lisää esiintymismäärää yhdellä.
        """
        self.count += 1

    def add_child(self, node):
        """Lisää lapsen listaan.

        Args:
            node: lisättävä TrieNode-objekti.
        """
        self.children.append(node)
