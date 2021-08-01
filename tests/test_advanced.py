# -*- coding: utf-8 -*-

from .context import TwilioLib
from TwilioLib.util.data import Junk


from unittest import TestCase


class SRETestSuite(TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(TwilioLib.hmm())

    def test_junk(self):
        j = Junk()
        self.assertEqual("we stuff", j.stuff())
