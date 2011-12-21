""" Faceted views
"""

from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName

class RSSView(BrowserView):
    """ Faceted RSS view
    """
    def thumb(self, brain):
        """ Check if image_thumb available for given brain
        """
        portal = getToolByName(self.context, 'portal_url')
        portal = portal.getPortalObject()
        url = brain.getURL(1)
        if not url.startswith(portal.getId()):
            url = '/' + portal.getId() + url
        img = portal.restrictedTraverse(url + '/image_thumb', None)
        if not img:
            return ''
        return brain.getURL() + '/image_thumb'
