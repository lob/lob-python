import sys
import os
try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

setup (
        name = 'lob',
        version = '2.25',
        author = 'Lob',
        author_email = 'support@lob.com',
        packages = ['lob'],
        description = 'Lob Python Bindings',
        url = 'https://www.lob.com',
        license = 'MIT',
        install_requires = [
            'requests'
            ],
        )
