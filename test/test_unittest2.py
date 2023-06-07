from unittest import TestCase
from src.functions import add_one

expected = {'a': 1, 'b': 2, 'c': [1, 2]}

class UnitTesting2(TestCase):
    recieved = {'a': 1, 'b': 2, 'c': [1]}

    def test_equals_compare(self):
        self.assertTrue(expected == self.recieved)

    def test_equals_dict_compare(self):
        self.assertDictEqual(expected, self.recieved)

def test_same_dicts():
    recieved = {'a': 1, 'b': 2, 'c': [1]}
    assert expected == recieved