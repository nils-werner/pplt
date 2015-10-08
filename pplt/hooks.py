import numpy


def pre_hook(plt):
    pass


def post_hook(plt):
    pass


def main(plt):
    f, ax = plt.subplots(1, 1)
    ax.plot(numpy.sin(numpy.arange(1000) / 100.))
    return f
