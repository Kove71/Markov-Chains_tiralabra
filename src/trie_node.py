class TrieNode:

    def __init__(self, word, depth):
        self.word = word
        self.children = []
        self.node_depth = depth
        self.count = 1
    
    def get_children(self):
        return self.children
    
    def get_depth(self):
        return self.node_depth

    def get_word(self):
        return self.word
    
    def check_children(self, word):
        for i in self.children:
            if word == i.get_word():
                return i
        return None

    def increase_count(self):
        self.count += 1
    
    def add_child(self, node):
        self.children.append(node)