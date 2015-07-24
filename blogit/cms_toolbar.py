# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar
from cms.toolbar.items import Break, SubMenu
from cms.cms_toolbar import ADMIN_MENU_IDENTIFIER, ADMINISTRATION_BREAK

from blogit.models import Post, Category, Tag


@toolbar_pool.register
class BlogitToolbar(CMSToolbar):
    watch_models = [Post, Category, Tag]

    def populate(self):
        admin_menu = self.toolbar.get_menu(ADMIN_MENU_IDENTIFIER)

        if admin_menu:
            position = admin_menu.get_alphabetical_insert_position(
                _('Blogit'), SubMenu)

            if not position:
                position = admin_menu.find_first(
                    Break, identifier=ADMINISTRATION_BREAK) + 1
                admin_menu.add_break('blogit-break', position=position)

            menu = admin_menu.get_or_create_menu(
                'blogit-admin-menu', _('Blogit'), position=position)

            url = reverse('admin:blogit_post_changelist')
            menu.add_sideframe_item(_('Posts List'), url=url)
            url = reverse('admin:blogit_post_add')
            menu.add_modal_item(_('Add New Post'), url=url)
            menu.add_break()

            url = reverse('admin:blogit_category_changelist')
            menu.add_sideframe_item(_('Categories List'), url=url)
            url = reverse('admin:blogit_category_add')
            menu.add_modal_item(_('Add New Category'), url=url)
            menu.add_break()

            url = reverse('admin:blogit_tag_changelist')
            menu.add_sideframe_item(_('Tags List'), url=url)
            url = reverse('admin:blogit_tag_add')
            menu.add_sideframe_item(_('Add New Tag'), url=url)

        if self.is_current_app:
            current_menu = self.toolbar.get_or_create_menu(
                'blogit-current-menu', _('Blogit'))

            add_menu = current_menu.get_or_create_menu(
                'blogit-current-menu-add', _('Add New'))

            url = reverse('admin:blogit_post_add')
            add_menu.add_modal_item(_('Post'), url=url)
            url = reverse('admin:blogit_category_add')
            add_menu.add_modal_item(_('Category'), url=url)
            url = reverse('admin:blogit_tag_add')
            add_menu.add_modal_item(_('Tag'), url=url)
