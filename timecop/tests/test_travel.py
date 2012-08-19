
import unittest

from datetime import date
from datetime import timedelta
from datetime import datetime
import time

import timecop

class TestTravel(unittest.TestCase):

    def test_time_does_not_stop_with_travel(self):
        now = time.time()

        with timecop.travel(now):
            # NB: time.sleep() and time.time() resolution should be plenty to detect
            # a sleep even of a few milliseconds but we're trading test run time for
            # confidence that time is really frozen
            sleep_secs = 0.6
            time.sleep(sleep_secs)
            self.assertNotEqual(now, time.time())
            time_diff = time.time() - now
            self.assertTrue( time_diff >= sleep_secs )

    def test_time_travel_forward(self):
        orig_time = time.time()
        travel_time = orig_time + 15

        with timecop.travel(travel_time):
            self.assertTrue( ( time.time() - travel_time ) <= 0.01 )  # pretty much the same time as we traveled to
            self.assertTrue( ( time.time() - orig_time ) >= 10 )  # current time is before original/actual time

        # time is reset to about where we were before (CPU cycles take "real" time to execute, so not exactly the same)
        self.assertTrue( (time.time() - orig_time ) <= 0.01, str(locals()) )

    def test_time_travel_backwards(self):
        orig_time = time.time()
        travel_time = orig_time - ( 60.0 * 60.0 )

        with timecop.travel(travel_time):
            time.sleep(0.6)
            # even after sleeping we're still "behind" actual time
            self.assertTrue( time.time() < orig_time )

        # resets properly
        self.assertTrue( time.time() > orig_time, locals() )

