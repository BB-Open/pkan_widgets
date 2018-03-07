# -*- coding: utf-8 -*-
"""A custom SPARQL Query widget."""

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
<div class="pkan-sparqlquery">
  <a class="{klass} pat-contentloaderform" target="_blank" href="{preview_url}"
      data-pat-contentloadeformr="form:{form};url:{url};target:{widget_id};">{title}</a>
</div>
"""


class ISparqlQueryWidget(ITextAreaWidget):
    """Marker interface for the Sparql Query Widget."""


@implementer_only(ISparqlQueryWidget)
class SparqlQueryWidget(TextAreaWidget):
    """A Sparql query widget with preview for Plone."""

    def render(self):
        widget = super(SparqlQueryWidget, self).render()

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
        url = self.context.absolute_url() + '/@@harvester_preview'
        return MARKUP.format(
            klass=u'context',
            title=title,
            widget=widget,
            url=url,
            form='#form',
        )


@adapter(IField, IFormLayer)
@implementer(IFieldWidget)
def SparqlQueryFieldWidget(field, request, extra=None):
    """A custom SPARQL Query widget."""
    if extra is not None:
        request = extra
    return FieldWidget(field, SparqlQueryWidget(request))
