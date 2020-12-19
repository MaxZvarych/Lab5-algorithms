import unittest

from Rabin_Karp import Rabin_Karp

class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(Rabin_Karp("aabaab", "aab"), [0, 3])
        self.assertEqual(Rabin_Karp("Aabaab", "aab"), [3])
        self.assertEqual(Rabin_Karp("My cute hamsters want to eat 24/7", "hamster"), [8])
        self.assertEqual(Rabin_Karp("aaaaa", "aa"), [0, 1, 2, 3])
        self.assertEqual(Rabin_Karp("a", "a"), [0])
        self.assertEqual(Rabin_Karp("hamster", "hamster"), [0])
        self.assertEqual(len(Rabin_Karp("a" * 1000, "a")), 1000)
        self.assertEqual(len(Rabin_Karp("a" * 1000, "aa")), 999)
        self.assertEqual(len(Rabin_Karp("a" * 1000, "a"*100)), 901)



if __name__ == '__main__':
    unittest.main()