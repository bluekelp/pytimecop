
import unittest

from datetime import date
from datetime import timedelta
import time

import timecop

class TestTimeCopFreeze(unittest.TestCase):

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

    def test_time_stops_with_freeze(self):
        now = time.time() 

        with timecop.freeze(now):
            # >1.0 in case time.time()'s resolution isn't so good/etc
            # NB: time.sleep() and time.time() resolution should be plenty to detect
            # a sleep even of a few milliseconds but we're trading test run time for 
            # confidence time is frozen
            time.sleep(1.5)
            self.assertEqual(now, time.time())  # time ought not to have changed at all

