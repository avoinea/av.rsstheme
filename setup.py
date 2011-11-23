""" Installer
"""
from setuptools import setup, find_packages
import os

NAME = 'av.rsstheme'
PATH = NAME.split('.') + ['version.txt']
VERSION = open(os.path.join(*PATH)).read().strip()
DESCRIPTION = (open("README.txt").read() + "\n" +
               open(os.path.join("docs", "HISTORY.txt")).read())

tests_require = ['plone.app.testing']


setup(name=NAME,
      version=VERSION,
      description="An installable theme for Plone 3",
      long_description=DESCRIPTION,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='av rss theme',
      author='Alin Voinea',
      author_email='alin.voinea@gmail.com',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['av'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.theming',
          # -*- Extra requirements: -*-
      ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      #setup_requires=["PasteScript"],
      #paster_plugins=["ZopeSkel"],
      )
