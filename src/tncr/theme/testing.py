# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import tncr.theme


class TncrThemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=tncr.theme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'tncr.theme:default')


TNCR_THEME_FIXTURE = TncrThemeLayer()


TNCR_THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(TNCR_THEME_FIXTURE,),
    name='TncrThemeLayer:IntegrationTesting'
)


TNCR_THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(TNCR_THEME_FIXTURE,),
    name='TncrThemeLayer:FunctionalTesting'
)


TNCR_THEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        TNCR_THEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='TncrThemeLayer:AcceptanceTesting'
)
