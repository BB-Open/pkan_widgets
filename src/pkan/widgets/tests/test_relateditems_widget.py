# -*- coding: utf-8 -*-
"""Tests for pkan.widgets.relateditems widget."""

from mock import Mock
from zope.publisher.browser import TestRequest

import unittest


class RelatedItemsAddWidgetTests(unittest.TestCase):
    """Validate RelatedItemsAddWidget."""

    def setUp(self):
        self.request = TestRequest(environ={'HTTP_ACCEPT_LANGUAGE': 'en'})

    def test_fieldwidget(self):
        from pkan.widgets.relateditems.widget import RelatedItemsAddWidget
        from pkan.widgets.relateditems.widget import RelatedItemsAddFieldWidget
        field = Mock(__name__='field', title=u'', required=True)
        vocabulary = Mock()
        request = Mock()
        widget = RelatedItemsAddFieldWidget(field, vocabulary, request)
        self.assertTrue(isinstance(widget, RelatedItemsAddWidget))
        self.assertIs(widget.field, field)
        self.assertIs(widget.request, request)
