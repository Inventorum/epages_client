from setuptools import setup, find_packages
from skin import __version__

setup(
    name='epages_client',
    version=__version__,
    packages=find_packages(),
    description='Epages client',
    long_description=open('README.md').read(),
    url='https://github.com/inventorum/epages_client/',

)
