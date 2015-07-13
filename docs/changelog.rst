Changelog
=========

0.4.0
    + Remove django-taggit from requirements
    + Fix: admin get_image should fail silently if image is missing

    .. attention::

        In version **0.4.0** django-taggit is removed as a requirement so the migrations history must be cleared.
        To migrate from **0.3.x** to **0.4.x** follow the steps:

            - install version **0.3.10** and run ``python manage.py migrate blogit``
            - remove blogit from the migration history. SQL example: ``DELETE FROM django_migrations WHERE app="blogit"``
            - install version **0.4.0** and run ``python manage.py migrate blogit --fake``


0.3.10
    + Remove date_hierarchy from admin (breaks when no pytz)

0.3.9
    + Changes in admin layout
    + Add settings for sitemap config
    + Add django-mptt as a requirement
    + Add actions for changing statuses
    + Add colors to admin statuses
    + Add previous and next post as a property
    + Remove active field, add HIDDEN status instead

0.3.8
    + Add SEO fields
    + Add extra feed settings
    + Add status fields, fix active boolean to not display in feeds and detail

0.3.7
    + Fix migrations

0.3.6
    + Fix 0005 migration

0.3.5
    + Create own simple tag model
    + Remove category and feed urls settings and translate them automatically

0.3.4
    + Make active boolean work.

0.3.3
    + Fix not displaying correct language on detail view.

0.3.2
    + Migration file dependencies fix

0.3.1
    + Update migration file
    + Fixes

0.3.0
    + Simplified models.
    + Refactored and not compatible with earlier versions.
