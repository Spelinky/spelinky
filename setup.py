__author__ = 'Tim'
from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'VERSION')) as f:
    version = f.read().strip()

setup(
    name='spelinky',
    version=version,
    author='Tim Martin',
    long_description="An open-source non-profit social network",
    packages=['spelinkyapp'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
        'Flask-Restless',
        'Flask-User',
        'Flask-Babel',
        'Flask-Admin',
        'requests',
        'beautifulsoup4',
        'Pillow'
    ]
)
