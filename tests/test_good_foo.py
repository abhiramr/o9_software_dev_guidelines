import pytest
from o9_dummy_folder.good_foo import GoodFoo

class TestCalc:

    def test_add(self):
        obj = GoodFoo(3, 5)
        self.assertEqual(obj.add(),8)

    def test_sub(self):
        obj = GoodFoo(3, 5)
        self.assertEqual(obj.sub(),8)
