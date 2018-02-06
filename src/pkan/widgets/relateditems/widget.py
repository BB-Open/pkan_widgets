# -*- coding: utf-8 -*-
"""An advanced related items widget for Plone."""

from plone import api
from plone.app.z3cform.interfaces import IRelatedItemsWidget as IBaseWidget
from plone.app.z3cform.widget import RelatedItemsWidget as BaseWidget
from plone.dexterity.interfaces import IDexterityFTI
from Products.CMFPlone.resources import add_resource_on_request
from z3c.form.interfaces import IFieldWidget
from z3c.form.interfaces import IFormLayer
from z3c.form.widget import FieldWidget
from zope.component import adapter
from zope.component import getUtility
from zope.i18n import translate
from zope.interface import implementer
from zope.interface import implementer_only
from zope.schema.interfaces import IField


MARKUP = u"""
<div class="relateditems-addnew">
  <a class="{klass} pat-plone-modal" target="_blank" href="{url}">{title}</a>
</div>
{widget}
"""


class IRelatedItemsWidget(IBaseWidget):
    """Marker interface for the advanced RelatedItemsWidget."""


@implementer_only(IRelatedItemsWidget)
class RelatedItemsWidget(BaseWidget):
    """An advanced related items widget for Plone."""

    content_type = None
    content_type_title = None
    initial_path = None

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
            base = ctx.absolute_url()
            initial_path = '/'.join([base, initial_path])
        return u'{0}++add++{1}'.format(
            initial_path,
            self.content_type,
        )

    def render(self):
        widget = super(RelatedItemsWidget, self).render()

        if self.mode != 'input':
            return widget

        if self.content_type is None:
            return widget

        add_resource_on_request(self.request, 'pkanwidgetsrelateditems')
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

    def related_items(self):
        related = self.value
        if not related:
            return ()
        related = related.split(self.separator)
        return self.related2brains(related)

    def related2brains(self, related):
        """Return a list of brains based on a list of UIDs.

        Will filter relations if the user has no permission to access
        the content.
        :param related: related items
        :type related: list of UIDs
        :return: list of catalog brains
        """
        catalog = api.portal.get_tool(name='portal_catalog')
        brains = catalog(UID=related)
        if brains:
            # build a position dict by iterating over the items once
            positions = dict([(v, i) for (i, v) in enumerate(related)])
            # We need to keep the ordering intact
            res = list(brains)

            def _key(brain):
                return positions.get(brain.UID, -1)
            res.sort(key=_key)
        return brains


@adapter(IField, IFormLayer)
@implementer(IFieldWidget)
def RelatedItemsFieldWidget(field, request, extra=None):
    """An advanced related items widget for Plone."""
    if extra is not None:
        request = extra
    return FieldWidget(field, RelatedItemsWidget(request))
