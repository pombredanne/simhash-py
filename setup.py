#! /usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

# Complain on 32-bit systems. See README for more details
import struct
if struct.calcsize('P') < 8:
    raise RuntimeError(
        'Simhash-py does not work on 32-bit systems. See README.md')


ext_modules = [Extension('simhash.table', [
        'simhash/table.pyx',
        'simhash/simhash-cpp/src/simhash.cpp'
    ], language='c++', libraries=['Judy']),
]

setup(name           = 'simhash',
    version          = '0.1.1',
    description      = 'Near-Duplicate Detection with Simhash',
    url              = 'http://github.com/seomoz/simhash-py',
    author           = 'Dan Lecocq',
    author_email     = 'dan@moz.com',
    packages         = ['simhash'],
    package_dir      = {'simhash': 'simhash'},
    cmdclass         = {'build_ext': build_ext},
    dependencies     = [],
    ext_modules      = ext_modules,
    classifiers      = [
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP'
    ],
)
