# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from tncr.theme.testing import TNCR_THEME_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that tncr.theme is properly installed."""

    layer = TNCR_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if tncr.theme is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('tncr.theme'))

    def test_browserlayer(self):
        """Test that ITncrThemeLayer is registered."""
        from tncr.theme.interfaces import ITncrThemeLayer
        from plone.browserlayer import utils
        self.assertIn(ITncrThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = TNCR_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['tncr.theme'])

    def test_product_uninstalled(self):
        """Test if tncr.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('tncr.theme'))
