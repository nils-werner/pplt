from . import properties
import numpy


def run(plt):
    t = numpy.arange(10000)
    s = lambda t: numpy.sin(t * 2 * numpy.pi * 440 / 1000000)

    logs = [lambda x: x, lambda x: numpy.log(x)]

    f, ax = plt.subplots(1, 2, figsize=(6, 2))

    for i in range(2):
        for j in range(1, 5):
            ax[i].plot(t, logs[i](s(t) * j + 10 * j), color='black')
        ax[i].set_title(r'$|\mathbf{X}_{k,f}|$', fontdict={'fontsize': 9})
        ax[i].set_xlabel(r'$k$')
        ax[i].set_ylabel(r'$f$')

    ax[1].set_ylabel(r'$\log(f)$')

    ax[0].axis([0, 10000, 0, 50])
    ax[1].axis([0, 10000, 2, 4])

    return f
