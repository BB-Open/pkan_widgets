# -*- coding: utf-8 -*-
"""Installer for the pkan.widgets package."""

from setuptools import find_packages
from setuptools import setup


version = '0.1.dev0'
description = 'Widgets for PKAN.'
long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])

install_requires = [
    'setuptools',
    # -*- Extra requirements: -*-
    'plone.app.z3cform',
    'Products.GenericSetup>=1.8.2',
    'pkan.dcatapde'
],

testfixture_requires = [
]


setup(
    name='pkan.widgets',
    version=version,
    description=description,
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Framework :: Plone :: 5.0',
        'Framework :: Plone :: 5.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='Python Plone Widget',
    author='Dr. Volker Jaenisch',
    author_email='volker.jaenisch@inqbus.de',
    url='https://github.com/BB-Open/pkan.widgets',
    download_url='https://pypi.python.org/pypi/pkan.widgets',
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['pkan'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    extras_require={
        'testfixture': testfixture_requires,
        'test': [
            'plone.app.z3cform[tests]',
            'plone.app.robotframework[debug]',
            'plone.app.testing',
            'robotframework-selenium2screenshots',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
