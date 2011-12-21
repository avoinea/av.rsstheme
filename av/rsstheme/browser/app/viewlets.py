""" Viewlets
"""
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from zope.schema.vocabulary import SimpleTerm
from zope.app.container.interfaces import INameChooser

class FooterViewlet(ViewletBase):
    render = ViewPageTemplateFile('../zpt/footer.pt')

    def sources(self):
        """ RSS Servers
        """
        voc = getUtility(IVocabularyFactory, name=u'AV Servers')
        for term in voc(self.context):
            yield term

    #def keywords(self):
        #""" Tags
        #"""
        #voc = getUtility(IVocabularyFactory,
                         #name=u'plone.app.vocabularies.Keywords')
        #for term in voc(self.context):
            #url = self.context.portal_url()
            #name = INameChooser(self.context).chooseName(
                #term.value, self.context)
            #url += '/' + name
            #newterm = SimpleTerm(url, name, term.title)
            #yield newterm
