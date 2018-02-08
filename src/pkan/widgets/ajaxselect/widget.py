# -*- coding: utf-8 -*-
"""An advanced AJAX select widget for Plone."""

from pkan.widgets.base import AddItemMixin
from plone.app.z3cform.interfaces import IAjaxSelectWidget
from plone.app.z3cform.widget import AjaxSelectWidget
from z3c.form.interfaces import IFieldWidget
from z3c.form.interfaces import IFormLayer
from z3c.form.widget import FieldWidget
from zope.component import adapter
from zope.interface import implementer
from zope.interface import implementer_only
from zope.schema.interfaces import IField


class IAjaxSelectAddWidget(IAjaxSelectWidget):
    """Marker interface for the advanced AjaxSelectWidget."""


@implementer_only(IAjaxSelectAddWidget)
class AjaxSelectAddWidget(AjaxSelectWidget, AddItemMixin):
    """An advanced related items widget for Plone."""

    def render(self):
        widget = super(AjaxSelectAddWidget, self).render()

        if self.mode != 'input':
            return widget

        if self.content_type is None:
            return widget

        return self.render_widget(widget)


@adapter(IField, IFormLayer)
@implementer(IFieldWidget)
def AjaxSelectAddFieldWidget(field, request, extra=None):
    """An advanced ajax select widget for Plone."""
    if extra is not None:
        request = extra
    return FieldWidget(field, AjaxSelectAddWidget(request))
