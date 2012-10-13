from plone.app.testing import applyProfile
from plone.app.testing import IntegrationTesting, FunctionalTesting
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from zope.configuration import xmlconfig


class PloneAppContenttileLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        import plone.app.contenttile
        xmlconfig.file('configure.zcml', plone.app.contenttile,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plone.app.contenttile:default')


PLONE_APP_CONTENTTILE_FIXTURE = PloneAppContenttileLayer()
PLONE_APP_CONTENTTILE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONE_APP_CONTENTTILE_FIXTURE, ),
    name="plone.app.contenttile:Integration")
PLONE_APP_CONTENTTILE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONE_APP_CONTENTTILE_FIXTURE, ),
    name="plone.app.contenttile:Functional")
