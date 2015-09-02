Configuration
=============

You may set the following values in a :code:`pplt/conf.py` file:

.. py:attribute :: columnwidth

the width of your columns. You may resize the figure in LaTeX later on, but
the resulting text size depends on a correct setting.

.. code:: python

    columnwidth = 244.6937  # Get this from LaTeX using \showthe\columnwidth

.. py:attribute :: aliases

A dictionary of aliases for your render modules. The key of each entry is
the alias name, the value the actual linked-to module.

When using tuples here, the first value is the module and all following values
are values passed to :code:`main()`

.. code:: python

    aliases = {
        "alias":            "logspec",              # logspec.main()
        "logspec_real":     ("logspec", "real"),    # logspec.main("real")
        "logspec_synth":    ("logspec", "synth"),   # logspec.main("synth")
    }

.. py:attribute :: rc_params

A dictionary of values passed on to :code:`plt.rcParams.update()`

.. code:: python

    rc_params = {
        'backend': 'ps',
        'axes.labelsize': 9,
        'legend.fontsize': 9,
        'xtick.labelsize': 8,
        'ytick.labelsize': 8,
        'text.usetex': True,
    }

.. py:attribute :: sns_params

A dictionary of values passed on to :code:`sns.set()`

.. code:: python

    sns_params = {
        'font': 'serif',
    }

.. py:attribute :: tight_layout

Global setting do enable/disable tight layouts.

.. code:: python

    tight_layout = False
