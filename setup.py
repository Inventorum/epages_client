from setuptools import setup, find_packages

setup(
    name='epages_client',
    version='1.0',
    packages=find_packages(except=['generator']),
    description='Epages client',
    long_description=open('README.md').read(),
    url='https://github.com/inventorum/epages_client/',
)
