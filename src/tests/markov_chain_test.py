import unittest
from markov_chain import MarkovChain
from trie_node import TrieNode

class TestMarkovChain(unittest.TestCase):

    def setUp(self):
        self.markov = MarkovChain(3, "test.txt")

    def test_incorrect_corpus(self):
        with self.assertRaises(Exception):
            MarkovChain(corpus_name="fail")

    def test_generate_text_default_sentence(self):
        test_case = self.markov.generate_text()
        self.assertEqual("testi.\n", test_case)

    def test_generate_text_multiple_sentences(self):
        test_case = self.markov.generate_text(2)
        self.assertEqual("testi.\ntesti.\n", test_case)

    def test_generate_sentence(self):
        test_case = self.markov.generate_sentence("testi")
        self.assertEqual("testi.", test_case)

    def test_get_choices_attributes(self):
        choices_dict = {}
        choices_dict["test1"] = TrieNode("test1", 1)
        choices_dict["test2"] = TrieNode("test2", 1)
        choices_dict["test3"] = TrieNode("test3", 1)
        choices_dict["test2"].increase_count()
        choices_keys = [*choices_dict]
        choices_values = [1, 2, 1]
        choices = self.markov.get_choices_attributes(choices_dict)
        self.assertEqual((choices_keys, choices_values), choices)
