This is just a pointless package hosted on github and testpypi to help me figure out how to set this all up using Poetry.

Find the published package on `TestPyPI <https://test.pypi.org/project/magicpi/>`_.

**********
Change log
**********

0.3.0
=====
Re-added support for Python 3.8 because I figured out how to use conditional dependencies to make that work. In pyproject.toml:

.. code::

    [tool.poetry.dependencies]
    python = ">=3.8,<3.13"
    numpy = [
        {version = "^1.23,<1.25", python = "3.8"},
        {version = "^1.23,<1.27", python = ">=3.9,<3.12"},
        {version = "^1.26,<1.27", python = "3.12"}
    ]

0.2.2
=====
Added support for Python 3.12. This led to the following:

* Poetry 1.6.1 requires all dependencies to support PEP 517 builds.
* With Python versions 3.11 and older, there was a way around this requirement, but
  in Python 3.12 the following error is thrown:
  `Backend 'setuptools.build_meta:__legacy__' is not available.`
* This requirement sets the minimum version of numpy needed to 1.26.0
* This version of numpy requires Python 3.9 or later, so we dropped support of Python 3.8.
