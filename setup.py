try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lob'))
from version import VERSION

setup (
        name = 'lob',
        version = VERSION,
        author = 'Lob',
        author_email = 'support@lob.com',
        packages = ['lob'],
        description = 'Lob Python Bindings',
        url = 'https://www.lob.com',
        license = 'MIT',
        install_requires = [
            'requests'
            ],
        test_suite = 'nose.collector',
        test_requires = [
            'Nose'
            ]
        )
