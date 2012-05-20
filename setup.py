from setuptools import setup, find_packages
import sys, os

version = '0.1.0'

setup(name='timecop',
      version=version,
      description="Enables time travel. A port of Ruby's gem of the same name.",
      long_description="""\
Enables time travel. A port of Ruby's gem of the same name.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='timecop time travel test context',
      author='Gabriel Krupa',
      author_email='timecop@bluekelp.com',
      url='',
      license='TBD',
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
