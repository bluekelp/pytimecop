import time
import datetime

class fake_datetime(datetime.datetime):
    """Like datetime.datetime, but always defer to time.time()

    These implementations of now and utcnow are lifted straight from
    the standard library documentation, which states that they are
    "equivalent" to these expressions, but may provide higher
    resolution on systems which support it.

    """
    @classmethod
    def now(cls, tz=None):
        if tz is None:
            return cls.fromtimestamp(time.time())
        else:
            return tz.fromutc(cls.utcnow().replace(tzinfo=tz))

    @classmethod
    def utcnow(cls):
        return cls.utcfromtimestamp(time.time())

class freeze(object):
    """ Context to freeze time at a given point in time """

    def __init__(self, time_spec):
        """ Initialize ourselves to be a context for the given alternate time. """
        if isinstance(time_spec, datetime.timedelta):
            self.secs_ = time.time() + time_spec.total_seconds()
        else:
            self.secs_ = float(time_spec)

    def time_(self):
        """ A version of time.time() that will return the value we want
            the system to think it is. """
        return self.secs_

    def __enter__(self):
        """ Alter time.time() to return the time we want it to be.
            Save current time function so can be replaced outside our
            context. """
        if hasattr(self, 'old_time_func_'):
            # looks like someone is trying to use us again inside ourselves
            # for another nested context
            raise ValueError('cannot nest time travel with the same instance')

        # replace datetime.datetime
        self.old_datetime_ = datetime.datetime
        datetime.datetime = fake_datetime

        self.old_time_func_ = time.time  # save old
        time.time = self.time_  # set new

    def __exit__(self, error_type, value, traceback):
        """ Reset time.time() to the value when we found it. """
        time.time = self.old_time_func_  # reset old
        del(self.old_time_func_)  # forget it

        # restore datetime.datetime
        datetime.datetime = self.old_datetime_
        del(self.old_datetime_)

    def actual_time_(self):
        return self.old_time_func_()

class travel(freeze):
    """ Context to travel to another time, letting time continue to pass """
    def __init__(self, time_spec):
        freeze.__init__(self, time_spec)
        # at this point, time.time() *is* actual time
        self.time_travel_offset_ = self.secs_ - time.time() # amount of time (in seconds) we're travelling in future (positive values) or past (negative value)

    def time_(self):
        return self.actual_time_() + self.time_travel_offset_

