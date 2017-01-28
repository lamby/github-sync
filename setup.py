#!/usr/bin/env python3

from setuptools import setup

setup(
    name='github-sync',
    version='0.0.1',
    url='https://chris-lamb.co.uk/projects/github-sync',
    author="Chris Lamb",
    author_email='chris@chris-lamb.co.uk',
    description="Tool for mirroring non-Github repos on Github. WIP.",
    scripts=(
        'github-sync',
    ),
    install_requires=(
        'eventlet',
        'requests',
    ),
)
