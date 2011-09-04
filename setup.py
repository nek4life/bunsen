import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
# README = open(os.path.join(here, 'README.txt')).read()
# CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid'
    ]

if sys.version_info[:3] < (2,5,0):
    requires.append('pysqlite')

setup(name='bunsen',
      version='0.0',
      description='bunsen',
      classifiers=[
        "Programming Language :: Python",
        ],
      author='',
      author_email='',
      url='',
      keywords='pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='bunsen',
      install_requires = requires,
      entry_points = """\
      [paste.paster_create_template]
      bunsen = bunsen.paster_templates:BunsenTemplate
      """,
      paster_plugins=['pyramid'],
      )

