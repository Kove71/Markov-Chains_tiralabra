import unittest
from trie_node import TrieNode

class TestTrieNode(unittest.TestCase):

    def setUp(self):
        self.node = TrieNode("test", 1)
    
    def test_get_depth(self):
        self.assertAlmostEqual(1, self.node.get_depth())

    def test_get_word(self):
        self.assertAlmostEqual("test", self.node.get_word())

    def test_get_count(self):
        self.assertAlmostEqual(1, self.node.get_count())

    def test_increase_count(self):
        self.node.increase_count()
        self.assertAlmostEqual(2, self.node.count)

    def test_add_child(self):
        child_node = TrieNode("child", 2)
        self.node.add_child(child_node)
        self.assertAlmostEqual(self.node.children[0], child_node)

    def test_check_children(self):
        child_node = TrieNode("child", 2)
        self.node.add_child(child_node)
        child = self.node.check_children("child")
        self.assertAlmostEqual(child.word, "child")

    def test_get_children(self):
        child_node = TrieNode("child", 2)
        self.node.add_child(child_node)
        self.assertAlmostEqual(self.node.get_children()[0].word, "child")
