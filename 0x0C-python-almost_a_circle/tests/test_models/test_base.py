"""
This module is all about unittests
"""

import unittest
from models.base import Base

class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing the instantiation of the Base Class"""

    def test_no_args(self):
        a = Base()
        b = Base()
        self.assertAlmostEqual(a.id, b.id - 1)

    def test_three_no_args(self):
        a = Base()
        b = Base()
        c = Base()
        self.assertAlmostEqual(a.id, b.id - 1)
        self.assertAlmostEqual(a.id, c.id - 2)

    def test_uniq_id(self): 
        a = Base(12)
        c = Base()
        c.id = 12
        self.assertAlmostEqual(a.id, 12)
        self.assertAlmostEqual(a.id, c.id)

    def test_after_uniq_id(self):
        a = Base()
        b = Base(12)
        c = Base()
        self.assertAlmostEqual(a.id, c.id - 1)

if __name__ == "__main__":
    unittest.main()
