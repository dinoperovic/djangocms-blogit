#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from setuptools import setup, find_packages


version = __import__('blogit').__version__
readme = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
    name='djangocms-blogit',
    version=version,
    description='Simple django-cms blog app',
    long_description=readme,
    author='Dino Perovic',
    author_email='dino.perovic@gmail.com',
    url='http://pypi.python.org/pypi/djangocms-blogit/',
    packages=find_packages(exclude=('tests', 'tests.*')),
    license='BSD',
    install_requires=(
        'django-cms>=3.3',
        'django-filer>=1.1',
        'django-parler>=1.6',
        'django-mptt>=0.8',
    ),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    test_suite='runtests.main',
    tests_require=(
        'django-nose>=1.4',
    ),
)
