from zope.schema import TextLine
from zope.i18nmessageid import MessageFactory
from plone.autoform import directives as form
from plone.tiles.tile import PersistentTile
from plone.app.tiles.interfaces import ITileBaseSchema
from zope.publisher.browser import BrowserView

from Products.CMFCore import utils as cmfutils
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.site.hooks import getSite

from zope.interface import Invalid


_ = MessageFactory('plone')


def validateUID(value):
    catalog = cmfutils.getToolByName(getSite(), 'portal_catalog')
    if not len(catalog(UID=value))==1:
        raise Invalid(_(u"Wrong UID to object"))
    return True
    

class IContentTile(ITileBaseSchema):

    form.widget()
    content = TextLine(title=u"Content object",
            description=u"Select one, please",
            constraint=validateUID)

class ContentTile(PersistentTile):
    """A tile which displays an content.

    This is a persistent tile which stores a reference to an content and
    optionally alt text. When rendered, the tile will look-up the content
    url and output an <img /> tag.
    """
    
    def getContent(self):
        catalog = cmfutils.getToolByName(self.context, 'portal_catalog')
        UID = self.data['content']
        obj = None
        if len(catalog(UID=UID))>0:
            obj = catalog(UID=UID)[0].getObject()
        return obj
    
class SummaryTileView(BrowserView):

    index = ViewPageTemplateFile('summary_tileview.pt')
