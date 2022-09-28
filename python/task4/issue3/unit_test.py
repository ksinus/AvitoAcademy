import unittest
import one_hot_encoder as ohe


class MyTestCase(unittest.TestCase):
    def test_simple_sequence(self):
        data = ['promitto', 'me', 'laboraturum', 'esse',
                'non', 'sordidi', 'lucri', 'causa']
        ft = ohe.fit_transform(data)
        target_ft = [('promitto', [0, 0, 0, 0, 0, 0, 0, 1]),
                     ('me', [0, 0, 0, 0, 0, 0, 1, 0]),
                     ('laboraturum', [0, 0, 0, 0, 0, 1, 0, 0]),
                     ('esse', [0, 0, 0, 0, 1, 0, 0, 0]),
                     ('non', [0, 0, 0, 1, 0, 0, 0, 0]),
                     ('sordidi', [0, 0, 1, 0, 0, 0, 0, 0]),
                     ('lucri', [0, 1, 0, 0, 0, 0, 0, 0]),
                     ('causa', [1, 0, 0, 0, 0, 0, 0, 0])]
        self.assertEqual(target_ft, ft)

    def test_repeat(self):
        data = ['A', 'B', 'A']
        ft = ohe.fit_transform(data)
        target_ft = [
            ('A', [0, 1]),
            ('B', [1, 0]),
            ('A', [0, 1])
        ]
        self.assertEqual(target_ft, ft)

    def test_repeats(self):
        data = ['A', 'B', 'C', 'A', 'A', 'A', 'A', 'B', 'B', 'C']
        ft = ohe.fit_transform(data)
        target_ft = [('A', [0, 0, 1]),
                     ('B', [0, 1, 0]),
                     ('C', [1, 0, 0]),
                     ('A', [0, 0, 1]),
                     ('A', [0, 0, 1]),
                     ('A', [0, 0, 1]),
                     ('A', [0, 0, 1]),
                     ('B', [0, 1, 0]),
                     ('B', [0, 1, 0]),
                     ('C', [1, 0, 0])]
        self.assertIn('A', target_ft[0])
        self.assertEqual(target_ft, ft)

    def test_empty(self):
        with self.assertRaises(TypeError):
            ohe.fit_transform()


if __name__ == '__main__':
    unittest.main()
