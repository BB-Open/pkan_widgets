# -*- coding: utf-8 -*-
"""Base widget classes."""

from plone import api
from plone.app.layout.navigation.interfaces import INavigationRoot
from plone.dexterity.interfaces import IDexterityFTI
from Products.CMFPlone.resources import add_resource_on_request
from zope.component import getUtility
from zope.i18n import translate


MARKUP = u"""
{widget}
<div class="pkan-addnew">
  <a class="{klass} pat-plone-modal data-pat-plone-modal="reloadWindowOnClose:false" target="_blank" href="{url}">
  {title}
  </a>
</div>
"""


class AddItemMixin(object):
    """Add a new item."""

    content_type = None
    content_type_title = None
    initial_path = None
    display_deprecated = False

    @property
    def portal_type_name(self):
        if self.content_type_title:
            return self.content_type_title

        if not self.content_type:
            return
        fti = getUtility(IDexterityFTI, name=self.content_type)
        return fti.title

    @property
    def add_url(self):
        initial_path = self.initial_path
        if initial_path is None:
            initial_path = ''
        else:
            if initial_path.startswith('/'):
                initial_path = initial_path[1:]
            ctx = api.portal.get_navigation_root(self.context)
            if not INavigationRoot.providedBy(ctx):
                ctx = api.portal.get()
            base = ctx.absolute_url()
            initial_path = '/'.join([base, initial_path])
        return u'{0}++add++{1}'.format(
            initial_path,
            self.content_type,
        )

    def render_widget(self, widget):
        add_resource_on_request(self.request, 'pkanwidgets')
        title = translate(
            'heading_add_item',
            domain='plone',
            mapping={'itemtype': self.portal_type_name},
            context=self.request,
            default='Add ${itemtype}',
        )
        return MARKUP.format(
            klass=u'context',
            title=title,
            url=self.add_url,
            widget=widget,
        )
