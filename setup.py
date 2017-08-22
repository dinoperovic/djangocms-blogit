#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import sys
import blogit

from setuptools import find_packages, setup

try:
    from pypandoc import convert
except ImportError:
    import io

    def convert(filename, fmt):
        with io.open(filename, encoding='utf-8') as fd:
            return fd.read()


CLASSIFIERS = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
]

setup(
    author='Dino Perovic',
    author_email='dino.perovic@gmail.com',
    name='djangocms-blogit',
    version=blogit.__version__,
    description='A simple djangoCMS blog app.',
    long_description=convert('README.md', 'rst'),
    url='https://github.com/dinoperovic/djangocms-blogit',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    packages=find_packages(exclude=['tests', 'docs']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'django-cms>=3.4.2',
        'django-filer>=1.2.8',
        'django-mptt>=0.8.7',
        'django-parler>=1.8',
    ],
    setup_requires=['pytest-runner'] if {'pytest', 'test', 'ptr'}.intersection(sys.argv) else [],
    tests_require=['pytest-django'],
)
