# Blogit

[![Build Status](https://img.shields.io/travis/dinoperovic/djangocms-blogit.svg)](https://travis-ci.org/dinoperovic/djangocms-blogit)
[![Codecov](https://img.shields.io/codecov/c/github/dinoperovic/djangocms-blogit.svg)](http://codecov.io/github/dinoperovic/djangocms-blogit)
[![PyPI version](https://img.shields.io/pypi/v/djangocms-blogit.svg)](https://pypi.python.org/pypi/djangocms-blogit)

**A simple blog application for [djangoCMS](https://www.django-cms.org).**

---

## Requirements

* [Django] 1.9
* [django-cms] for placeholders.
* [django-filer] for file management.
* [django-mptt] for tree management.
* [django-parler] to translate everything.

## Installation

Install using *pip*:

```bash
pip install djangocms-blogit
```

You should follow [django-cms] & [django-filer] installation guide first, and then add the following to your settings:

```python
INSTALLED_APPS = [
    ...
    'mptt',
    'parler',
    'blogit',
]
```

#### Urls

There are two ways to configure the urls. First would be to add to your `urls.py`:

```python
urlpatterns = [
    url(r'^blog/', include('blogit.urls')),
    ...
]
```

The second option is to use [django-cms] apphooks. **Blogit** comes with a couple of those for different application parts. `BlogitApphook` is the main one, and one that should always be attached to a page (if the urls are not already added). Then there are other optional apphooks for *category*, *tags* & *feeds*. If you want to keep it simple, and not have to set every application part individually. You can add to your settings:

```python
BLOGIT_SINGLE_APPHOOK = True
```

This will load all the neccesary urls under the `BlogitApphook`.

## Documentation

You can read full documentation on [ReadTheDocs](http://djangocms-blogit.readthedocs.org).


[Django]: https://www.djangoproject.com/
[django-cms]: https://github.com/divio/django-cms
[django-filer]: https://github.com/divio/django-filer
[django-mptt]: https://github.com/django-mptt/django-mptt
[django-parler]: https://github.com/django-parler/django-parler
