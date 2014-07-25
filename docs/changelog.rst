Changelog
#########


0.2.0
    Added support for django CMS 3.x.

    .. note::
        django CMS 2.x is no longer compatible with this release.

0.1.1
    Bugfixes.

0.1.0
    Alpha release, started changelog.

    .. warning::
        If migrating from an earlier version, some fields may be lost. Backup
        before upgrading.

    .. note::
        To migrate from earlier versions using `south`_ you will need to
        install version ``0.0.99`` first and run ``python manage.py migrate
        blogit``. Then upgrade to version ``0.1.0`` and run ``python manage.py
        migrate blogit 0001 --fake --delete-ghost-migrations``.


.. _south: http://south.aeracode.org/
