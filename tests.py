from unittest import TestCase

from src.crazy_tiger import generate


class CrazyTigerTestCase(TestCase):

    def test_generate(self):
        name = generate()
        print(name)
        self.assertGreaterEqual(2, sum([s.isupper() for s in name]))

    def test_generate__snake(self):
        name = generate(case="snake")
        print(name)
        self.assertTrue(name.islower())
        self.assertGreaterEqual(1, name.count("_"))
