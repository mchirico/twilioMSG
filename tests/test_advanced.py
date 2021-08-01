# -*- coding: utf-8 -*-

from .context import TwilioLib
from TwilioLib.util.data import Junk, TW


from unittest import TestCase


class TWTestSuite(TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        t = TW()
        result = t.GetList()
        print(result)


    def test_junk(self):
        j = Junk()
        self.assertEqual("we stuff", j.stuff())
