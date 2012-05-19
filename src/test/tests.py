import unittest
import mock

from datetime import date
import time


# initial implementation taken from http://stackoverflow.com/questions/4481954/python-trying-to-mock-datetime-date-today-but-not-working


class FakeDate(date):
    "A manipulable date replacement"
    def __new__(cls, *args, **kwargs):
        return date.__new__(date, *args, **kwargs)


class TestTimeCop(unittest.TestCase):

    @mock.patch('datetime.date', FakeDate)
    def test_fake_time(self):
        from datetime import date

        @classmethod
        def date_(cls):
            return date(2010, 1, 1)

        FakeDate.today = date_
        print date.today()

