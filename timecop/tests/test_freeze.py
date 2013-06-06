
import unittest

import datetime
from datetime import date
from datetime import timedelta
import time

import timecop

class TestFreeze(unittest.TestCase):

    SECONDS_IN_A_DAY = 86400

    def test_yesterday(self):
        secs = time.time()
        secs -= self.SECONDS_IN_A_DAY

        # do it "right"
        yesterday = date.today() - timedelta(days=1)

        with timecop.freeze(secs):
            self.assertEqual(yesterday, date.today())

    def test_epoch(self):
        with timecop.freeze(0):
            # test assumes knowledge of when epoch is but that's ok
            self.assertEqual(date(1969, 12, 31), date.today())

    def test_time_stops_with_freeze(self):
        now = time.time() 

        with timecop.freeze(now):
            # NB: time.sleep() and time.time() resolution should be plenty to detect
            # a sleep even of a few milliseconds but we're trading test run time for 
            # confidence that time is really frozen
            time.sleep(0.6)
            self.assertEqual(now, time.time())  # time ought not to have changed at all

    def test_can_freeze_to_a_timedelta_object(self):
        offset = timedelta(days=-1)
        now = time.time()
        with timecop.freeze(offset):
            self.assertAlmostEqual(now - self.SECONDS_IN_A_DAY, time.time(), delta=0.9)

    def test_can_nest_freezes(self):
        secs = time.time()
        secs -= self.SECONDS_IN_A_DAY

        yesterday = date.today() - timedelta(days=1)
        day_before_yesterday = date.today() - timedelta(days=2)

        with timecop.freeze(secs):
            self.assertEqual(yesterday, date.today())

            secs -= self.SECONDS_IN_A_DAY  # take off another day
            with timecop.freeze(secs):
                self.assertEqual(day_before_yesterday, date.today())

            # test again after coming out of looped context
            self.assertEqual(yesterday, date.today())

    def test_datetime_today(self):
        now = time.time()

        with timecop.freeze(now):
            time.sleep(0.6)
            self.assertEqual(datetime.datetime.fromtimestamp(now),
                             datetime.datetime.today())

    def test_datetime_now(self):
        now = time.time()

        with timecop.freeze(now):
            time.sleep(0.6)
            self.assertEqual(datetime.datetime.fromtimestamp(now),
                             datetime.datetime.now())

    def test_datetime_utcnow(self):
        now = time.time()

        with timecop.freeze(now):
            time.sleep(0.6)
            self.assertEqual(datetime.datetime.utcfromtimestamp(now),
                             datetime.datetime.utcnow())
