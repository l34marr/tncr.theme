#!/usr/bin/python
#-*- encoding: utf-8 -*-

from zope.i18n import translate
from plone.app.layout.viewlets.common import TitleViewlet
from plone.app.layout.viewlets.common import LogoViewlet


class TitleViewlet(TitleViewlet):
    """Custom Title
    """
    def update(self):
        super(TitleViewlet, self).update()
        self.site_title = u"%s &mdash; %s" % (
            translate('portal_title',
                      domain='plone',
                      context=self.request,
                      default='TNCR GIS'),
            self.page_title)


class LogoViewlet(LogoViewlet):
    """Custom Logo
    """
    def update(self):
        super(LogoViewlet, self).update()
        self.logo_tag = '<img src="' + self.navigation_root_url + '/++theme++tncr/img/logo.png" alt="Logo File">'

