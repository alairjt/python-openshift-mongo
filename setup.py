#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='Python Flask MongoDB on OpenShift (PFMoO)',
    version='0.0.1',
    author='Alair Tavares',
    author_email='alairjt@gmail.com',
    install_requires=['Flask', 'pymongo']
)