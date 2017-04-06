Release notes
#############

Release notes for **Blogit**.

----

0.4.11
======

* Fix setup.py.

0.4.10
======

* Move urls into modules (for now) to fix potential errors with appresolver from django-cms.
* Support Django 1.10.

0.4.9
=====

* Change url of categories to use full path, instead of slug.
* Maintenance.

0.4.8
=====

* Fix tests settings, update requirements.

0.4.7
=====

* Make multiple apphooks the default.
* Make detail category view fetch all descendants posts.
* Use MPTT draggable admin for categories.

0.4.6
=====

* Require django CMS 3.3.x.

0.4.5
=====

* Add settings ``BLOGIT_SINGLE_APPHOOK`` and additional apphooks for other modules. This now allows to specify a
  separate page apphooks for categories, tags, feeds...

0.4.4
=====

* Add support for Django 1.8.x and 1.9.x, drop support for Django 1.7.x
* Migration: remove "null=True" from M2M field.

0.4.3
=====

* Add support for django CMS 3.2.

0.4.2
=====

* Replace override function with parlers switch_language to avoid 404's in some cases.

0.4.1
=====

* Enable search in admin list.
* Add list of posts in category and tag admin detail.
* Add tag urls and views.
* Add tags to cms toolbar menu.
* Fix force_text to try force_unicode first – in feeds.
* Separate managers from models.
* Fix post detail view returning multiple objects when different language posts have the same slug.

0.4.0
=====

* Add langauge param to Post's get_absolute_url method.
* Add get_search_data method to Post.
* Remove django-taggit from requirements.
* Fix: admin get_image should fail silently if image is missing.

.. attention::

    In version **0.4.0** django-taggit is removed as a requirement so the migrations history must be cleared.
    To migrate from **0.3.x** to **0.4.x** follow the steps:

        - install version **0.3.10** and run ``python manage.py migrate blogit``
        - remove blogit from the migration history. SQL example: ``DELETE FROM django_migrations WHERE app="blogit"``
        - install version **0.4.0** and run ``python manage.py migrate blogit --fake``


0.3.10
======

* Remove date_hierarchy from admin.

0.3.9
=====

* Changes in admin layout.
* Add settings for sitemap config.
* Add django-mptt as a requirement.
* Add actions for changing statuses.
* Add colors to admin statuses.
* Add previous and next post as a property.
* Remove active field, add HIDDEN status instead.

0.3.8
=====

* Add SEO fields.
* Add extra feed settings.
* Add status fields, fix active boolean to not display in feeds and detail.

0.3.7
=====

* Fix migrations.

0.3.6
=====

* Fix 0005 migration.

0.3.5
=====

* Create own simple tag model.
* Remove category and feed urls settings and translate them automatically.

0.3.4
=====

* Make active boolean work.

0.3.3
=====

* Fix not displaying correct language on detail view.

0.3.2
=====

* Migration file dependencies fix

0.3.1
=====

* Update migration file.
* Fixes.

0.3.0
=====

* Simplified models.
* Refactored and not compatible with earlier versions.
