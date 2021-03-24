# -*- coding: utf-8 -*-
"""Tests for pkan.widgets.ajaxselect widget."""
from mock import Mock
from zope.publisher.browser import TestRequest

import unittest


class AjaxSelectAddWidgetTests(unittest.TestCase):
    """Validate AjaxSelectAddWidget."""

    def setUp(self):
        self.request = TestRequest(environ={'HTTP_ACCEPT_LANGUAGE': 'en'})

    def test_fieldwidget(self):
        from pkan.widgets.ajaxselect.widget import AjaxSelectAddFieldWidget
        from pkan.widgets.ajaxselect.widget import AjaxSelectAddWidget
        field = Mock(__name__='field', title=u'', required=True)
        vocabulary = Mock()
        request = Mock()
        widget = AjaxSelectAddFieldWidget(field, vocabulary, request)
        self.assertTrue(isinstance(widget, AjaxSelectAddWidget))
        self.assertIs(widget.field, field)
        self.assertIs(widget.request, request)
