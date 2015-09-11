import numpy


def main(plt, args):
    f, ax = plt.subplots(1, 1)
    ax.plot(numpy.sin(numpy.arange(1000) / 100.))
    art = plt.legend((args, ))

    return f, (art,)
