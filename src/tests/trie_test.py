import unittest
from trie import Trie
from trie_node import TrieNode
from tokenize_corpus import TokenizeCorpus

class TestTrie(unittest.TestCase):

    def setUp(self):
        self.tokenize  = TokenizeCorpus()
        self.text = self.tokenize.tokenize()
        self.trie = Trie(self.text, 1)

    def test_initialize_creates_root(self):
        mock_root = TrieNode("*", 0)
        self.assertEqual(mock_root.get_word(), self.trie.root.get_word())
        self.assertEqual(mock_root.get_depth(), self.trie.root.get_depth())
    
    def test_create_tree(self):
        self.trie.create_tree()
        mock_root_children = ["This", "is", "a", "test", "not", "finished", "temporary"]
        root_children = self.trie.root.get_children()
        root_children_keys = [*root_children]
        this_node = root_children["This"]
        self.assertEqual(mock_root_children, root_children_keys)
        self.assertEqual(this_node.get_count(), 3)