from setuptools import setup, find_packages
import sys, os

version = '0.5.0'

setup(name='timecop',
      version=version,
      description="Enables time travel. A port of Ruby's gem of the same name.",
      long_description="""\
Enables time travel.
A port of the Ruby gem of the same name: https://github.com/jtrupiano/timecop.

Currently supports "freeze" but not "travel" functionality, specified by either\
a "time since epoch" or datetime.timedelta specification.""",
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
      ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='timecop freeze time travel test context',
      author='Gabriel Krupa',
      author_email='timecop@bluekelp.com',
      url='https://github.com/bluekelp/pytimecop',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
