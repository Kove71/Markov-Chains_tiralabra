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

    def test_add_ngram(self):
        self.trie.add_ngram(["This", "cat"])
        mock_root_children = ["This"]
        root_children = self.trie.root.get_children()
        root_children_keys = [*root_children]
        this_node = root_children["This"]
        this_children = this_node.get_children()
        this_children_keys = [*this_children]
        self.assertEqual(mock_root_children, root_children_keys)
        self.assertEqual(this_node.get_count(), 1)
        self.assertEqual(this_children_keys, ["cat"])

    def test_find_ngram(self):
        self.trie.add_ngram(["This", "cat", "is", "brown"])
        find_children = self.trie.find_ngram(["This", "cat", "is"])
        find_children_keys = [*find_children]
        self.assertEqual(find_children_keys, ["brown"])

    def test_find_ngram_none(self):
        self.trie.add_ngram(["This", "cat", "is"])
        find_children = self.trie.find_ngram(["This", "dog"])
        self.assertEqual(find_children, None)
    