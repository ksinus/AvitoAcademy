import unittest
from CountVectorizer import CountVectorizer


class TestCountVectorizer(unittest.TestCase):
    def test_empty_corpus(self):
        count_vectorizer = CountVectorizer()
        count_vectorizer.fit_transform([])
        self.assertEqual(count_vectorizer.get_feature_names(), [])

    def test_empty_token(self):
        count_vectorizer = CountVectorizer()
        count_vectorizer.fit_transform(['', ''])
        self.assertEqual(count_vectorizer.get_feature_names(), [])

    def test_same_tokens(self):
        count_vectorizer = CountVectorizer()
        ft = count_vectorizer.fit_transform(['a a a', 'a a a'])
        target_ft = [[3], [3]]
        self.assertEqual(ft, target_ft)

    def test_space_processing(self):
        count_vectorizer = CountVectorizer()
        ft = count_vectorizer.fit_transform(['a    a  a', 'a    a  a'])
        target_ft = [[3], [3]]
        self.assertEqual(ft, target_ft)

    def test_base(self):
        count_vectorizer = CountVectorizer()
        ft = count_vectorizer.fit_transform(['a b c a', 'b c d k', 'd e f i'])
        self.assertEqual(sorted(count_vectorizer.get_feature_names()),
                         sorted(['a', 'b', 'c', 'd', 'e', 'f', 'i', 'k']))
        target_ft = [[0, 2, 0, 1, 0, 1, 0, 0],
                     [0, 0, 1, 1, 1, 1, 0, 0],
                     [1, 0, 1, 0, 0, 0, 1, 1]]

        for i in range(len(ft)):
            self.assertEqual(sorted(ft[i]), sorted(target_ft[i]))


if __name__ == '__main__':
    unittest.main()
