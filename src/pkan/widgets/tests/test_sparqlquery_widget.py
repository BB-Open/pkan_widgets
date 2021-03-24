# -*- coding: utf-8 -*-
"""Tests for pkan.widgets.sparqlquery widget."""
from mock import Mock
from zope.publisher.browser import TestRequest

import unittest


class SparqlQueryWidgetTests(unittest.TestCase):
    """Validate SparqlQueryWidget."""

    def setUp(self):
        self.request = TestRequest(environ={'HTTP_ACCEPT_LANGUAGE': 'en'})

    def test_fieldwidget(self):
        from pkan.widgets.sparqlquery.widget import SparqlQueryFieldWidget
        from pkan.widgets.sparqlquery.widget import SparqlQueryWidget
        field = Mock(__name__='field', title=u'', required=True)
        vocabulary = Mock()
        request = Mock()
        widget = SparqlQueryFieldWidget(field, vocabulary, request)
        self.assertTrue(isinstance(widget, SparqlQueryWidget))
        self.assertIs(widget.field, field)
        self.assertIs(widget.request, request)
