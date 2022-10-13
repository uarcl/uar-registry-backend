# -*- coding: utf-8 -*-
# Imports ###########################################################

import os
from setuptools import setup


# Main ##############################################################

setup(
    name='uar_registry',
    version='1.0',
    description='UAR Registry backend Oauth 2.0',
    packages=['uar_registry'],
    install_requires=[
        'Django',
    ],
)
