#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from terrible import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='terrible',
    version=__version__,
    description='Translate terraform state into ansible inventory',
    long_description='''
Translates [terraform](https://terraform.io/) state into an [ansible](http://docs.ansible.com/) inventory.
''',
    keywords='terraform ansible state terriable ',
    author='Curtis Allen',
    author_email='curtis.n.allen@gmail.com',
    url='https://github.com/RobotsAndPencils/terrible',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'terrible=terrible.cli:main',
        ],
    },
)
