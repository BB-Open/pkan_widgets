# -*- coding: utf-8 -*-
"""Test Layer for pkan.widgets."""

from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import Layer
from plone.testing import z2


class Fixture(PloneSandboxLayer):
    """Custom Test Layer for pkan.widgets."""

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope for testing."""
        # Load ZCML
        import pkan.widgets
        self.loadZCML(package=pkan.widgets)

    def setUpPloneSite(self, portal):
        self.applyProfile(portal, 'pkan.widgets:default')


FIXTURE = Fixture()

INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE, ),
    name='pkan.widgets:Integration',
)

FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE, z2.ZSERVER_FIXTURE),
    name='pkan.widgets:Functional',
)


ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(FIXTURE, REMOTE_LIBRARY_BUNDLE_FIXTURE, z2.ZSERVER_FIXTURE),
    name='pkan.widgets:Acceptance',
)

ROBOT_TESTING = Layer(name='pkan.widgets:Robot')
