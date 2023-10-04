This is just a pointless package hosted on github and testpypi to help me figure out how to set this all up using Poetry.

Find the published package on `TestPyPI <https://test.pypi.org/project/magicpi/>`_.

**********
Change log
**********

0.2.2
=====
Added support for Python 3.12. This led to the following:
* Poetry 1.6.1 requires all dependencies to support PEP 517 builds.
* With Python versions 3.11 and older, there was a way around this requirement, but
  in Python 3.12 the following error is thrown:
  `Backend 'setuptools.build_meta:__legacy__' is not available.`
* This requirement sets the minimum version of numpy needed to 1.26.0
* This version of numpy requires Python 3.9 or later, so we dropped support of Python 3.8.
