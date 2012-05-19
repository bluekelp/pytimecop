
import unittest

from datetime import date
from datetime import timedelta
import time

from PyTimeCop import PyTimeCop

class TestTimeCop(unittest.TestCase):

    def test_yesterday(self):
        secs = time.time()
        secs -= 60*60*24  # approximate yesterday

        # do it "right"
        yesterday = date.today() - timedelta(days=1)

        with PyTimeCop(secs):
            self.assertEqual(yesterday, date.today())

    def test_epoch(self):
        with PyTimeCop(0):
            self.assertEqual(date(1969, 12, 31), date.today())

