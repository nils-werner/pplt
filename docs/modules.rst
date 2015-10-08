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

Your module may define additional RC settings for Matplotlib and Seaborn as 
well as set a :code:`stylesheet` and a :code:`pre_hook` and a :code:`post_hook`
which will run before and after the plotting.


.. code:: python

    from contextlib import contextmanager

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


    stylesheet = 'grayscale'


    def pre_hook(plt):
        plt.style.use('grayscale')


    def post_hook(plt):
        pass


.. seealso:: Global RC settings in :code:`conf.py`: :py:attr:`rc_params`, :py:attr:`sns_params`,  :py:attr:`stylesheet`
