#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import io
import os
import platform
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import relpath
from os.path import splitext

from setuptools import Extension
from setuptools import find_packages
from setuptools import setup
from setuptools.dist import Distribution

# Enable code coverage for C code: we can't use CFLAGS=-coverage in tox.ini, since that may mess with compiling
# dependencies (e.g. numpy). Therefore we set SETUPPY_CFLAGS=-coverage in tox.ini and copy it to CFLAGS here (after
# deps have been safely installed).
if 'TOX_ENV_NAME' in os.environ and os.environ.get('SETUPPY_EXT_COVERAGE') == 'yes' and platform.system() == 'Linux':
    CFLAGS = os.environ['CFLAGS'] = '-fprofile-arcs -ftest-coverage'
    LFLAGS = os.environ['LFLAGS'] = '-lgcov'
else:
    CFLAGS = ''
    LFLAGS = ''


class BinaryDistribution(Distribution):
    """Distribution which almost always forces a binary package with platform name"""
    def has_ext_modules(self):
        return super().has_ext_modules() or not os.environ.get('SETUPPY_ALLOW_PURE')


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()

os.system("./setup_c_dependencies.sh")

setup(
    name='swmm-cached',
    version='0.0.0',
    license='LGPL-3.0-or-later',
    description='A python package for caching files between repeated runs of SWMM.',
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author='George Rossick',
    author_email='grossick@gmail.com',
    url='https://github.com/grossick/python-swmm_cached',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)'
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Utilities',
    ],
    project_urls={
        'Documentation': 'https://python-swmm_cached.readthedocs.io/',
        'Changelog': 'https://python-swmm_cached.readthedocs.io/en/latest/changelog.html',
        'Issue Tracker': 'https://github.com/grossick/python-swmm_cached/issues',
    },
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    python_requires='>=3.6',
    install_requires=[
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
    ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
    ext_modules=[
        Extension(
            splitext(relpath(path, 'src').replace(os.sep, '.'))[0],
            sources=[path],
            extra_compile_args=["-fopenmp"], #CFLAGS.split().append("-fopenmp"),
            extra_link_args=["-fopenmp"], #LFLAGS.split().append("-fopenmp"),
            extra_objects=['lib/swmm/bin/libswmm5.a', 'lib/autocache/libautocache.a'],
            include_dirs=[dirname(path), 'lib/autocache', 'lib/Stormwater-Management-Model/src/solver/include']
        )
        for root, _, _ in os.walk('src')
        for path in glob(join(root, '*.c'))
    ],
    distclass=BinaryDistribution,
)
