# -*- coding: utf-8 -*-
"""An advanced AJAX select widget for Plone."""
from Products.CMFPlone.resources import add_resource_on_request
from z3c.form.browser.textarea import TextAreaWidget
from z3c.form.interfaces import IFieldWidget
from z3c.form.interfaces import IFormLayer
from z3c.form.interfaces import ITextAreaWidget
from z3c.form.widget import FieldWidget
from zope.component import adapter
from zope.i18n import translate
from zope.interface import implementer
from zope.interface import implementer_only
from zope.schema.interfaces import IField


MARKUP = u"""
{widget}
<div class="pkan-addnew">
  <textarea id="form-widgets-query-preview"
  name="form.widgets.preview" class="textarea-widget text-field">
  No value</textarea>
  <input class="context pat-contentloader"
      data-pat-contentloader="form:{form};url:{url};target:#form-widgets-query-preview;"
      id="id-preview" value="preview"
      name="preview"/>
</div>
"""


class IQueryWidget(ITextAreaWidget):
    """Marker interface for the Query Widget."""


@implementer_only(IQueryWidget)
class QueryWidget(TextAreaWidget):
    """An Query widget for Plone."""

    def render(self):
        widget = super(QueryWidget, self).render()

        if self.mode != 'input':
            return widget

#        if self.content_type is None:
#            return widget

        return self.render_widget(widget)

    def render_widget(self, widget):
        add_resource_on_request(self.request, 'pkanwidgets')
        title = translate(
            'heading_add_item',
            domain='plone',
            mapping={},
            context=self.request,
            default='Query',
        )
        url = self.context.absolute_url() + '/harvester_preview'
        return MARKUP.format(
            klass=u'context',
            title=title,
            widget=widget,
            url=url,
            form='#form',
        )


@adapter(IField, IFormLayer)
@implementer(IFieldWidget)
def QueryFieldWidget(field, request, extra=None):
    """An advanced ajax select widget for Plone."""
    if extra is not None:
        request = extra
    return FieldWidget(field, QueryWidget(request))
