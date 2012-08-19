=======
TimeCop
=======

In addition to being one of the best Jean-Claude Van Damme movies EVAR!, TimeCop is also
a killer sweet Ruby gem.  This is its Python port.

Much respect to https://github.com/jtrupiano/ for his TimeCop gem and for 
not naming it something like like TimeTester or TimeHelper like I may have.

Needs more testing, needs docs.

---------------------
Current functionality
---------------------
#. timecop.freeze() supporting floating point/int "seconds since epoch" time specs
#. timecop.freeze() supporting timedelta time specs (use negative numbers to go back)
#. timecop.travel() supports all creation/use methods a freeze()

----
TODO
----
#. put updated/latest version on pypi
#. accept date(), and string representations of alternate times
#. test full suite of datetime, time, objects for proper functionality
#. support older (pre 2.7) versions of python - datetime.total_seconds() is new in 2.7 and is currently required for timedelta() time_spec support

