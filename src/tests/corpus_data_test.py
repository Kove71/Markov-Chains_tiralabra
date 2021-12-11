import unittest
import corpus_data

class TestCorpusdata(unittest.TestCase):

    def setUp(self):
        self.text = corpus_data.get_corpus("test.txt")

    def test_get_corpus(self):
        self.assertAlmostEqual("testi", self.text)

    def test_incorrect_corpus(self):
        with self.assertRaises(Exception):
            corpus_data.get_corpus("fail")
