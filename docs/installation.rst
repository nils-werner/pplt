Installation
============

.. code:: bash

    pip install pplt


Setup
-----

PPLT expects there to be a :code:`pplt/` directory in your :code:`$PYTHONPATH`
or your current directory.

Inside this directory there must be an :code:`__init__.py` file
and all renderer modules you need. e.g.

.. code:: text

    |- paper.tex
    `- pplt/
       |- __init__.py
       |- input_signal.py
       `- result_plots.py

With this structure you can then render your plots using

.. code:: bash

    pplt input_signal.pdf
    pplt result_plots.pdf

Makefiles
---------

One key aspect is that each output file is represented by one
renderer module Python file. This makes it possible to have a :code:`Makefile`
rule for each plot you need and only re-render the ones that were actually
changed.

.. code:: make

    # Render plots automatically using PPLT
    fig/%.pdf: pplt/%.py
	    pplt $@

    # Build plots when building paper.pdf 
    paper.pdf: fig/input_signal.pdf fig/result_plots.pdf
        latex paper.tex
