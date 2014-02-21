Changelog
#########


0.1.0
    Alpha release, started changelog

    .. warning::
        If migrating from an earlier version, some fields may be lost. Backup
        before upgrading.

    .. note::
        To migrate from earlier versions using `south`_ you will need to
        install version ``0.0.99`` first and run ``python manage.py migrate
        blogit``. Then upgrade to version ``0.1.0`` and run ``python manage.py
        migrate blogit 0001 --fake --delete-ghost-migrations``.


.. _south: http://south.aeracode.org/
