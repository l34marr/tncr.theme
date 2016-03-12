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

