Bio2BEL HSDN |build|
====================
Converts the human symptoms-disease network produced by Zhou and Himmelstein to BEL

Big thanks to Daniel Himmelstein for preprocessing this data in his repository at: https://github.com/dhimmel/hsdn

Installation |pypi_version| |python_versions| |pypi_license|
------------------------------------------------------------
``bio2bel_hsdn`` can be installed easily from
`PyPI <https://pypi.python.org/pypi/bio2bel_hsdn>`_
with the following code in your favorite terminal:

.. code-block:: sh

    $ python3 -m pip install bio2bel_hsdn

or from the latest code on `GitHub <https://github.com/bio2bel/hsdn>`_ with:

.. code-block:: sh

    $ python3 -m pip install git+https://github.com/bio2bel/hsdn.git

Setup
-----
This repository does not currently cache the data, but only wraps conversion to BEL.

Python REPL
~~~~~~~~~~~
.. code-block:: python

    >>> import bio2bel_hsdn
    >>> hsdn_manager = bio2bel_hsdn.Manager()
    >>> graph = hsdn_manager.to_bel()


.. |build| image:: https://travis-ci.com/bio2bel/hsdn.svg?branch=master
    :target: https://travis-ci.com/bio2bel/hsdn
    :alt: Build Status

.. |documentation| image:: http://readthedocs.org/projects/bio2bel-hsdn/badge/?version=latest
    :target: http://bio2bel.readthedocs.io/projects/hsdn/en/latest/?badge=latest
    :alt: Documentation Status

.. |pypi_version| image:: https://img.shields.io/pypi/v/bio2bel_hsdn.svg
    :alt: Current version on PyPI

.. |coverage| image:: https://codecov.io/gh/bio2bel/hsdn/coverage.svg?branch=master
    :target: https://codecov.io/gh/bio2bel/hsdn?branch=master
    :alt: Coverage Status

.. |python_versions| image:: https://img.shields.io/pypi/pyversions/bio2bel_hsdn.svg
    :alt: Stable Supported Python Versions

.. |pypi_license| image:: https://img.shields.io/pypi/l/bio2bel_hsdn.svg
    :alt: MIT License
