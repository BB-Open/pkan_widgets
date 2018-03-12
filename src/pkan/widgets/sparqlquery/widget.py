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
      data-pat-contentloaderform="query_id:#{query_id};form_id:#{form_id};url:{url};target:#{target_id};">{title}</a>
  <pre class="pkan-sparqlquery__preview" id="{target_id}"></pre>
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

        return self.render_widget(widget)

    def render_widget(self, widget):
        add_resource_on_request(self.request, 'pkanwidgets')
        title = translate(
            'heading_preview',
            domain='pkan.widgets',
            mapping={},
            context=self.request,
            default='Update Preview',
        )
        url = '/'.join([
            self.context.absolute_url(),
            '@@harvester_preview',
        ])
        preview_url = url
        return MARKUP.format(
            klass=u'context',
            preview_url=preview_url,
            title=title,
            url=url,
            widget=widget,
            form_id=self.form.id,
            query_id=self.id,
            target_id=self.id + '__preview',
        )


@adapter(IField, IFormLayer)
@implementer(IFieldWidget)
def SparqlQueryFieldWidget(field, request, extra=None):
    """A custom SPARQL Query widget."""
    if extra is not None:
        request = extra
    return FieldWidget(field, SparqlQueryWidget(request))
