# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
Release logic:
 1. Remove ".devX" from __version__ (below)
 2. git add blogit/__init__.py
 3. git commit -m 'Bump to <version>'
 4. git tag <version>
 5. git push && git push --tags
 6. python setup.py sdist upload
 7. bump the __version__, append ".dev0"
 8. git add blogit/__init__.py
 9. git commit -m 'Start with <version>'
10. git push
"""

__version__ = '0.4.8'
