#!/usr/bin/env python
#-*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import os


def main():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(base_dir)
    sys.path.append(base_dir + '/blogit')

    os.environ['DJANGO_SETTINGS_MODULE'] = 'blogit.tests.settings'
    from django.test.simple import DjangoTestSuiteRunner

    test_runner = DjangoTestSuiteRunner(verbosity=1)
    failures = test_runner.run_tests(['blogit', ])

    if failures:
        sys.exit(failures)

if __name__ == '__main__':
    main()
