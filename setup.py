try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='cardiolock',
    version='0.1',
    author='A. Somov',
    author_email='public.somov@gmail.com',
    packages=['cardiolock'],
    scripts=['run.sh'],
    url='http://pypi.python.org/pypi/cardiolock/',
    license='LICENSE.txt',
    description='Unlock your computer with a Mifare card',
    long_description=open('README.md').read(),
    install_requires=[
        "pyserial >= 3.0.1",
    ],
)
