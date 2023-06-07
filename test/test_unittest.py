from unittest import TestCase
from src.functions import add_one

class UnitTesting(TestCase):
    def test_add_one_pass(self):
        self.assertEqual(add_one(5), 6)

    def test_add_one_fail(self):
        self.assertEqual(add_one(5), 5)