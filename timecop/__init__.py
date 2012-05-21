import time
import datetime

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

        self.old_time_func_ = time.time  # save old
        time.time = self.time_  # set new

    def __exit__(self, error_type, value, traceback):
        """ Reset time.time() to the value when we found it. """
        time.time = self.old_time_func_  # reset old
        del(self.old_time_func_)  # forget it

