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
