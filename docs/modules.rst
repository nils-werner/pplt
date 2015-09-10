Renderer Modules
================

Your code must at least implement a :code:`main()` function that accepts
the matplotlib instance as its only paramter and returns a figure

.. code:: python

    def main(plt):
        f, ax = plt.subplots(1, 1, figsize=(6, 2))

        ax.plot(...)

        return f


Artists
-------

Your function may return the figure alongside a list/tuple of additional artists:

.. code:: python

    def main(plt):
        f, ax = plt.subplots(1, 1, figsize=(6, 2))

        ax.plot(...)
        lgd = ax.legend(...)

        return f, (lgd,)

.. _rc_params:

RC Settings
-----------

Your module may define additional RC settings for Matplotlib and Seaborn.

.. code:: python

    def main(plt):
        f, ax = plt.subplots(1, 1, figsize=(6, 2))

        ax.plot(...)
        lgd = ax.legend(...)

        return f, (lgd,)


    sns_params = {
        'font': 'serif',
    }


    rc_params = {
        'font.size': 9,
    }

.. seealso:: Global RC settings in :code:`conf.py`: :py:attr:`rc_params`, :py:attr:`sns_params`
