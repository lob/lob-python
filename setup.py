try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
        name = 'lob',
        version = '1.0',
        author = 'Lob',
        author_email = 'support@lob.com',
        packages = ['lob'],
        url = 'https://pypi.python.org/pypi/lob',
        license = 'MIT',
        install_requires = [
            "requests"
            ]
    )
