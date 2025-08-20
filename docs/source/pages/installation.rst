############
Installation
############

Code
----
To install:

.. code-block:: console

   curl -LsSf https://astral.sh/uv/install.sh | sh

.. code-block:: console

   uv sync

.. note::
   :class: margin

   Use this if you want to install all of the development packages as well.

.. code-block:: console

   uv sync --all-extras


Documentation
-------------

To generate the full documentation use Sphinx [#]_.

.. code-block:: console

   uv run nox -rs show_sphinx

..
   Footnotes
.. rubric:: Footnotes

.. [#] This will generate a ``index.html`` under ``docs/build/index.html``.
