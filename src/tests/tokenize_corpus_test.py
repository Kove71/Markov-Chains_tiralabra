import unittest
from tokenize_corpus import TokenizeCorpus

class TestTokenizeCorpus(unittest.TestCase):

    def setUp(self):
        self.tokenizer = TokenizeCorpus()

    def test_sentence_tokenizer(self):
        sentence_amount = len(self.tokenizer.text_sentences)
        testcase = "This is a test."
        self.assertEqual(sentence_amount, 3)
        self.assertEqual(testcase, self.tokenizer.text_sentences[0])

    def test_word_tokenizer(self):
        tokenized = self.tokenizer.tokenize()
        testcase = ["This", "is", "a", "test", "."]
        self.assertEqual(tokenized[0], testcase)

    def test_first_word(self):
        first_words = self.tokenizer.first_words()
        testcase = ["This", "This", "This"]
        self.assertEqual(first_words, testcase)
    
    def test_incorrect_corpus(self):
        with self.assertRaises(Exception):
            TokenizeCorpus("fail")
