try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
        name = 'lob-python',
        version = '1.0',
        author = 'Siddharth Saha',
        author_email = 'sidchilling@gmail.com',
        packages = ['lob'],
        url = 'https://pypi.python.org/pypi/lob-python',
        license = 'MIT',
        install_requires = [
            "requests"
            ]
    )
