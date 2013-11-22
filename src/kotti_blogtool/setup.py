import os

from setuptools import find_packages
from setuptools import setup

project = 'kotti_blogtool'
version = '1.0.0'

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

setup(
    name=project,
    version=version,
    description="Blog Folder content type for Kotti",
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Pylons",
        "Framework :: Pyramid",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: User Interfaces",
    ],
    keywords='kotti theme',
    author='Christoph Boehner',
    author_email='cb@vorwaerts-werbung.de',
    url='https://github.com/potzenheimer/kotti_blogtool',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Kotti',
        'kotti_settings>=0.1',
        'js.jquery_infinite_ajax_scroll',
        'python-dateutil',
    ],
    entry_points={
        'fanstatic.libraries': [
            'kotti_blogtool = kotti_blogtool.fanstatic:library',
        ],
    },
    message_extractors={
        'kotti_blogtool': [
            ('**.py', 'lingua_python', None),
            ('**.zcml', 'lingua_xml', None),
            ('**.pt', 'lingua_xml', None),
        ]
    },
)
