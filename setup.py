from setuptools import setup, find_packages

version = '1.0'
tests_require = [
    'plone.testing',
    'plone.app.testing',
    'zope.configuration',
]

setup(
    name='plone.app.contenttile',
    version=version,
    description="Content tile for deco UI",
    long_description=open("README.rst").read(),
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
    keywords='plone deco tile',
    author='Bogdan Girman',
    author_email='bogdan.girman@gmail.com',
    url='https://github.com/plone/plone.app.contenttile',
    license='GPL',
    packages=find_packages(),
    namespace_packages=['plone', 'plone.app'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zope.schema',
        'zope.i18nmessageid',
        'plone.directives.form',
        'plone.tiles',
        'plone.app.tiles',
        'plone.formwidget.namedfile',
        ],
    tests_require=tests_require,
    extras_require=dict(test=tests_require),
    entry_points="""
        # -*- Entry points: -*-
        [z3c.autoinclude.plugin]
        target = plone
        """,
    )

