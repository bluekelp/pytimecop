
import unittest

from datetime import date
from datetime import timedelta
import time

import timecop

class TestTimeCop(unittest.TestCase):

    def test_yesterday(self):
        secs = time.time()
        secs -= 60*60*24  # approximate yesterday

        # do it "right"
        yesterday = date.today() - timedelta(days=1)

        with timecop.freeze(secs):
            self.assertEqual(yesterday, date.today())

    def test_epoch(self):
        with timecop.freeze(0):
            self.assertEqual(date(1969, 12, 31), date.today())

    # TODO: test more of datetime and time modules' API
    # TODO: impl (ruby) timecop features like "revert to past but allow time to resume normally from that point"

