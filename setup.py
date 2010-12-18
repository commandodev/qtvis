from setuptools import setup, find_packages
import sys, os

version = '0.0'

requires = [
    'pyramid',
    'repoze.tm2',
    'pyramid_jinja2',
    'sqlalchemy',
    'zope.sqlalchemy',
    'WebError',
    ]

setup(name='qtvis',
      version=version,
      description="Visualization for qt and pyside with protovis",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Ben Ford',
      author_email='ben@boothead.co.uk',
      url='',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points = """\
      [paste.app_factory]
      main = qtvis.server:main
      """,
      paster_plugins=['pyramid'],
      )
