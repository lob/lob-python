import sys
import os
try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup


with open(os.path.join(os.path.split(__file__)[0], 'VERSION'), 'r') as f:
    version = f.read().strip()

setup (
        name = 'lob',
        version = version,
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
