:maintainers:
    `andrewtarzia <https://github.com/andrewtarzia/>`_,
    `lukasturcani <https://github.com/lukasturcani/>`_
:documentation: https://stko-lite-docs.readthedocs.io
:discord: https://discord.gg/zbCUzuxe2B

.. figure:: docs/source/_static/stko.png

Overview
========

``stko-lite`` is a light-weight version of `stko`_ with mostly the same
functionality.

.. _`stko`: https://github.com/JelfsMaterialsGroup/stko


`stko <https://github.com/JelfsMaterialsGroup/stko>`_ is a Python library for
performing optimizations and calculations on complex molecules built using
`stk <https://github.com/lukasturcani/stk>`_. In the case of
optimizations, a clone of ``stk.Molecule`` is returned. For
calculators, a ``Results`` class are used to calculate and extract
properties of an ``stk.Molecule``. There is a Discord server
for ``stk``, which can be joined through https://discord.gg/zbCUzuxe2B.


Installation
============

To get ``stko``, you can install it with pip:

.. code-block:: bash

  pip install stko-lite

Some optional dependencies are only available through conda:

.. code-block:: bash

  # for gfn-ff with topology constrains
  # This will not work on Windows at this stage
  # (https://pprcht.github.io/gfnff/python.html)
  pip install gfnff


Developer Setup
---------------

#. Install `just`_.
#. Install `uv`_.
#. In the source directory, run::

    $ just setup


#. Run code checks::

    $ just check

.. _`just`: https://github.com/casey/just
.. _`uv`: https://docs.astral.sh


How To Contribute
=================

If you have any questions or find problems with the code, please submit
an issue.

If you wish to add your own code to this repository, please send us a
Pull Request. Please maintain the testing and style that is used
throughout ```stko``.


How To Cite
===========

If you use ``stko`` please cite

    https://github.com/JelfsMaterialsGroup/stko



Acknowledgements
================

We developed this code when working in the Jelfs group,
http://www.jelfs-group.org/, whose members often provide very valuable
feedback, which we gratefully acknowledge.
