import unittest
import mock

from datetime import date
import time

# initial implementation taken from http://stackoverflow.com/questions/4481954/python-trying-to-mock-datetime-date-today-but-not-working


class PyTimeCop(object):
    "A manipulable date replacement"

    # have we already patched the system?
    patched_ = False

    def __init__(self):
        self.ensure_patched_()

    @classmethod
    def ensure_patched_(self):
        if not PyTimeCop.patched_:
            self.patch_system_()

    @classmethod
    def patch_system_(cls):
        cls.patched_ = True
        def my_time():
            return cls.time_
        time.time = my_time

    @classmethod
    def be_time(cls, secs):
        cls.ensure_patched_()
        cls.time_ = secs

class TestTimeCop(unittest.TestCase):

    def test_fake_time(self):
        PyTimeCop.be_time(1330399987.0)
        print date.today()

