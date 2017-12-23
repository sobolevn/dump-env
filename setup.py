#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

import io
import os

from setuptools import find_packages, setup

REQUIRED = []

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.rst' is
# present in your MANIFEST.in file!
with io.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()


setup(
    name='dump-env',
    version='0.0.1',
    description='A utility tool to create .env files',
    long_description=long_description,
    author='Nikita Sobolev',
    author_email='mail@sobolenv.me',
    url='https://github.com/sobolevn/dump-env',

    packages=find_packages(exclude=('tests', )),

    install_requires=REQUIRED,
    include_package_data=True,

    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],

    entry_points={
        'console_scripts': [
            'dump-env=dump_env.cli:main',
        ],
    },
)
