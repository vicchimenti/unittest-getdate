import math
from unittest import TestCase


class TestGetdate(TestCase):
    def test_getdate(self):
        self.assertTrue(2019-1-1)
        self.assertTrue(2019-12-12)
        self.assertFalse(2019-13-12)
        self.assertTrue(2019-12-13)
        self.assertFalse(2019-27-12)
        self.assertTrue(2019-12-27)
        self.assertFalse(2019-28-10)
        self.assertTrue(2019-10-28)
        self.assertFalse(2019-29-10)
        self.assertTrue(2019-10-29)
        self.assertFalse(2019-10-29)
        self.assertFalse(2019-30-10)
        self.assertTrue(2019-10-30)
        self.assertFalse(2019-10-29)
        self.assertFalse(2019-31-10)
        self.assertTrue(2019-10-31)
        self.assertFalse(2019-10-31)
        self.assertFalse(2019-100-10)
        self.assertTrue(2019-10-100)
        self.assertFalse(2019-math.inf-10)
        self.assertFalse(2019-10-math.inf)
        self.assertFalse(2019--math.inf-10)
        self.assertFalse(2019-10--math.inf)
        self.assertFalse(2019--1-10)
        self.assertFalse(2019-10--1)
        self.assertFalse(2019-12-0)
        self.assertFalse(2019-0-12)
