import unittest

from CountVectorizer import CountVectorizer


class TestCountVectorizer(unittest.TestCase):
    def test_empty_corpus(self):
        vectorizer = CountVectorizer()
        vectorizer.fit_transform([])
        self.assertEqual(vectorizer.get_feature_names(), [])

    def test_empty_token(self):
        vectorizer = CountVectorizer()
        vectorizer.fit_transform(['', ''])
        self.assertEqual(vectorizer.get_feature_names(), [])

    def test_same_tokens(self):
        vectorizer = CountVectorizer()
        ft = vectorizer.fit_transform(['a a a', 'a a a'])
        target_ft = [[3], [3]]
        self.assertEqual(ft, target_ft)

    def test_space_processing(self):
        vectorizer = CountVectorizer()
        ft = vectorizer.fit_transform(['a    a  a', 'a    a  a'])
        target_ft = [[3], [3]]
        self.assertEqual(ft, target_ft)

    def test_base(self):
        vectorizer = CountVectorizer()
        ft = vectorizer.fit_transform(['a b c a', 'b c d k', 'd e f i'])
        self.assertEqual(sorted(vectorizer.get_feature_names()),
                         sorted(['a', 'b', 'c', 'd', 'e', 'f', 'i', 'k']))

        target_ft = [[0, 2, 0, 1, 0, 1, 0, 0],
                     [0, 0, 1, 1, 1, 1, 0, 0],
                     [1, 0, 1, 0, 0, 0, 1, 1]]

        for i in range(len(ft)):
            self.assertEqual(sorted(ft[i]), sorted(target_ft[i]))

    def test_sample(self):
        corpus = [
            'Crock Pot Pasta Never boil pasta again',
            'Pasta Pomodoro Fresh ingredients Parmesan to taste'
        ]
        target_vocabulary = [
            'crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro',
            'fresh', 'ingredients', 'parmesan', 'to', 'taste'
        ]
        target_ft = [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]

        vectorizer = CountVectorizer()
        ft = vectorizer.fit_transform(corpus)
        self.assertEqual(sorted(vectorizer.get_feature_names()),
                         sorted(target_vocabulary))

        for i in range(len(ft)):
            self.assertEqual(sorted(ft[i]), sorted(target_ft[i]))


if __name__ == '__main__':
    unittest.main()
