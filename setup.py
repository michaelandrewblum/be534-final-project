# -*- coding: utf-8 -*-

# Learn more: https://github.com/michaelandrewblum/setup.py

from setuptools import setup, find_packages


with open('README.md') as fh:
    readme = fh.read()

with open('LICENSE') as fh:
    license = fh.read()

setup(
    name='env_data',
    version='0.1.0',
    description='Read greenhouse environmental data',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Michael Blum',
    author_email='michaelblum@email.arizona.edu',
    url='https://github.com/michaelandrewblum/be534-final-project',
    license=license,
    packages=find_packages()
)