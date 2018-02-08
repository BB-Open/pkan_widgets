# -*- coding: utf-8 -*-
"""Perform upgrade steps."""
from plone.app.upgrade.utils import loadMigrationProfile


def reload_gs_profile(context):
    """Reload our GS profile."""
    loadMigrationProfile(
        context,
        'profile-pkan.widgets:default',
    )
