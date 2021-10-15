from setuptools import setup

README = open('README.md').read()

setup(
    name='lob',
    version='4.5.0',
    author='Lob',
    author_email='support@lob.com',
    packages=['lob'],
    description='Lob Python Bindings',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/lob/lob-python',
    license='MIT',
    install_requires=[
        'requests'
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy"
    ]
)
