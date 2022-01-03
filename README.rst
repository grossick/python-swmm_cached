========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-swmm_cached/badge/?style=flat
    :target: https://python-swmm_cached.readthedocs.io/
    :alt: Documentation Status

.. |version| image:: https://img.shields.io/pypi/v/swmm-cached.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/swmm-cached

.. |wheel| image:: https://img.shields.io/pypi/wheel/swmm-cached.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/swmm-cached

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/swmm-cached.svg
    :alt: Supported versions
    :target: https://pypi.org/project/swmm-cached

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/swmm-cached.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/swmm-cached

.. |commits-since| image:: https://img.shields.io/github/commits-since/grossick/python-swmm_cached/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/grossick/python-swmm_cached/compare/v0.0.0...main



.. end-badges

A python package for caching files between repeated runs of SWMM.

* Free software: GNU Lesser General Public License v3 or later (LGPLv3+)

Installation
============

::

    pip install swmm-cached

You can also install the in-development version with::

    pip install https://github.com/grossick/python-swmm_cached/archive/main.zip


Documentation
=============


https://python-swmm_cached.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
