# -*- coding: utf-8 -*-
"""An advanced related items widget for Plone."""

from pkan.widgets.base import AddItemMixin
from plone import api
from plone.app.z3cform.interfaces import IRelatedItemsWidget as IBaseWidget
from plone.app.z3cform.widget import RelatedItemsWidget as BaseWidget
from z3c.form.interfaces import IFieldWidget
from z3c.form.interfaces import IFormLayer
from z3c.form.widget import FieldWidget
from zope.component import adapter
from zope.interface import implementer
from zope.interface import implementer_only
from zope.schema.interfaces import IField


class IRelatedItemsWidget(IBaseWidget):
    """Marker interface for the advanced RelatedItemsWidget."""


@implementer_only(IRelatedItemsWidget)
class RelatedItemsAddWidget(BaseWidget, AddItemMixin):
    """An advanced related items widget for Plone."""

    def render(self):
        widget = super(RelatedItemsAddWidget, self).render()

        if self.mode != 'input':
            return widget

        if self.content_type is None:
            return widget

        return self.render_widget(widget)

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
def RelatedItemsAddFieldWidget(field, request, extra=None):
    """An advanced related items widget for Plone."""
    if extra is not None:
        request = extra
    return FieldWidget(field, RelatedItemsAddWidget(request))
