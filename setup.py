#!/usr/bin/env python
# setup
# Setup script for installing btrdb bindings
#
# Author:   PingThings
# Created:  Mon Jan 07 14:45:32 2019 -0500
#
# For license information, see LICENSE.txt
# ID: setup.py [] allen@pingthings.io $

"""
Setup script for installing btrdb bindings.
"""

##########################################################################
## Imports
##########################################################################

import os
import codecs

from setuptools import setup
from setuptools import find_packages

##########################################################################
## Package Information
##########################################################################
# setup(
#   name = 'btrdb4',
#   packages = ['btrdb4'],
#   version = '4.11.1',
#   description = "Bindings to interact with the Berkeley Tree Database using gRPC",
#   author = 'Sam Kumar, Michael P Andersen',
#   author_email = 'samkumar99@gmail.com, michael@steelcode.com',
#   url = 'https://github.com/BTrDB/btrdb4-python',
#   download_url = 'https://github.com/SoftwareDefinedBuildings/btrdb4-python/tarball/0.0.1',
#   package_data = { 'btrdb4': ['grpcinterface/btrdb.proto'] },
#   include_package_data = False,
#   install_requires = ["grpcio >= 1.1.3", "grpcio-tools >= 1.1.3", "isodate >= 0.5.4"],
#   keywords = ['btrdb', 'berkeley', 'timeseries', 'database', 'bindings' 'gRPC'],
#   classifiers = [],
#   setup_requires = ["pytest-runner"],
#   tests_require = ["pytest"]
# )

## Basic information
NAME         = "btrdb4-python"
DESCRIPTION  = "Bindings to interact with the Berkeley Tree Database using gRPC."
AUTHOR       = "Michael Andersen, Allen Leis"
EMAIL        = "michael@steelcode.com"
MAINTAINER   = "Michael Andersen"
LICENSE      = "BSD-3-Clause"
REPOSITORY   = "https://github.com/BTrDB/btrdb4-python"
PACKAGE      = "btrdb"
URL          = "http://btrdb.io/"

## Define the keywords
KEYWORDS     = ('btrdb', 'berkeley', 'timeseries', 'database', 'bindings' 'gRPC')

## Define the classifiers
## See https://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS  = (
    'Development Status :: 5 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: Apache Software License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Python Modules',
)

## Important Paths
PROJECT      = os.path.abspath(os.path.dirname(__file__))
REQUIRE_PATH = "requirements.txt"
VERSION_PATH = os.path.join(PACKAGE, "version.py")
PKG_DESCRIBE = "DESCRIPTION.rst"

## Directories to ignore in find_packages
EXCLUDES     = (
    "tests", "docs",
)

##########################################################################
## Helper Functions
##########################################################################

def read(*parts):
    """
    Assume UTF-8 encoding and return the contents of the file located at the
    absolute path from the REPOSITORY joined with *parts.
    """
    with codecs.open(os.path.join(PROJECT, *parts), 'rb', 'utf-8') as f:
        return f.read()


def get_version(path=VERSION_PATH):
    """
    Reads the python file defined in the VERSION_PATH to find the get_version
    function, and executes it to ensure that it is loaded correctly. Separating
    the version in this way ensures no additional code is executed.
    """
    namespace = {}
    exec(read(path), namespace)
    return namespace['get_version'](short=True)


def get_requires(path=REQUIRE_PATH):
    """
    Yields a generator of requirements as defined by the REQUIRE_PATH which
    should point to a requirements.txt output by `pip freeze`.
    """
    for line in read(path).splitlines():
        line = line.strip()
        if line and not line.startswith('#'):
            yield line


def get_description_type(path=PKG_DESCRIBE):
    """
    Returns the long_description_content_type based on the extension of the
    package describe path (e.g. .txt, .rst, or .md).
    """
    _, ext = os.path.splitext(path)
    return {
        ".rst": "text/x-rst",
        ".txt": "text/plain",
        ".md": "text/markdown",
    }[ext]


##########################################################################
## Define the configuration
##########################################################################

config = {
    "name": NAME,
    "version": get_version(),
    "description": DESCRIPTION,
    # "long_description": read(PKG_DESCRIBE),
    # "long_description_content_type": get_description_type(PKG_DESCRIBE),
    "classifiers": CLASSIFIERS,
    "keywords": KEYWORDS,
    "license": LICENSE,
    "author": AUTHOR,
    "author_email": EMAIL,
    "url": URL,
    "maintainer": MAINTAINER,
    "maintainer_email": EMAIL,
    "project_urls": {
        "Documentation": URL,
        "Download": "{}/tarball/v{}".format(REPOSITORY, get_version()),
        "Source": REPOSITORY,
        "Tracker": "{}/issues".format(REPOSITORY),
    },
    "download_url": "{}/tarball/v{}".format(REPOSITORY, get_version()),
    "packages": find_packages(where=PROJECT, exclude=EXCLUDES),
    "package_data": {
        "btrdb": ["grpcinterface/btrdb.proto"],
    },
    "zip_safe": False,
    "entry_points": {
        "console_scripts": [],
    },
    "install_requires": list(get_requires()),
    "python_requires": ">=3.5, <4",
    "setup_requires":["pytest-runner"],
    "tests_require":["pytest"],
}


##########################################################################
## Run setup script
##########################################################################

if __name__ == '__main__':
    setup(**config)
