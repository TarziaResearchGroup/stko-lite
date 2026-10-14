.. toctree::
   :hidden:
   :caption: stko
   :maxdepth: 1

   Video Tutorials <video_tutorials>
   Molecular <molecular>
   Calculators <calculators>
   Optimizers <optimizers>
   Using the topology for GFN-FF optimisation <using_topology_for_opt>
   Cage analysis <cage_analysis>


.. toctree::
   :hidden:
   :caption: Modules
   :maxdepth: 1

   Modules <modules.rst>

Welcome to stko's documentation!
================================

| GitHub: https://github.com/TarziaResearchGroup/stko-lite
| Discord: https://discord.gg/zbCUzuxe2B

.. tip::

  ⭐ Star us on `GitHub <https://github.com/JelfsMaterialsGroup/stko>`_! ⭐

.. figure:: _static/logo.png

Overview
========

``stko-lite`` is a light-weight version of `stko`_ with mostly the same
functionality.

.. _`stko`: https://github.com/JelfsMaterialsGroup/stko


`stko <https://github.com/JelfsMaterialsGroup/stko>`_ is a Python library for
performing optimizations and calculations on complex molecules built using
`stk <https://github.com/lukasturcani/stk>`_. In the case of
optimizations, a clone of :class:`stk.Molecule` is returned. For
calculators, a ``Results`` class are used to calculate and extract
properties of an :class:`stk.Molecule`.

Installation
============

:mod:`.stko` can be installed directly with pip:

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
-----------------

If you have any questions or find problems with the code, please submit
an issue.

If you wish to add your own code to this repository, please send us a
Pull Request. Please maintain the testing and style that is used
throughout ```stko``.


How To Cite
-----------

If you use ``stko`` please cite

    https://github.com/JelfsMaterialsGroup/stko
