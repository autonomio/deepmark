#! /usr/bin/env python
#
# Copyright (C) 2018 Mikko Kotila

DESCRIPTION = "Deepmark system benchmarking for Keras "
LONG_DESCRIPTION = """\
Deepmark helps benchmark system / system configurations for most common 
deep learning use-cases including image recognition, text classification, 
regression, and classification from tabular data.
"""

DISTNAME = 'deepmark'
MAINTAINER = 'Mikko Kotila'
MAINTAINER_EMAIL = 'mailme@mikkokotila.com'
URL = 'http://autonom.io'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/autonomio/deepmark/'
VERSION = '0.0.1'

try:
    from setuptools import setup
    _has_setuptools = True
except ImportError:
    from distutils.core import setup


def check_dependencies():

    install_requires = []

    try:
        import numpy
    except ImportError:
        install_requires.append('numpy')
    try:
        import keras
    except ImportError:
        install_requires.append('keras')

    return install_requires


if __name__ == "__main__":

    install_requires = check_dependencies()

    setup(name=DISTNAME,
          author=MAINTAINER,
          author_email=MAINTAINER_EMAIL,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          license=LICENSE,
          url=URL,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          install_requires=install_requires,
          packages=['deepmark'],

          classifiers=[
                 'Intended Audience :: Science/Research',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'License :: OSI Approved :: MIT License',
                 'Topic :: Scientific/Engineering :: Artificial Intelligence',
                 'Topic :: Scientific/Engineering :: Mathematics',
                 'Operating System :: POSIX',
                 'Operating System :: Unix',
                 'Operating System :: MacOS'],)
