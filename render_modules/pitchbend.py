from . import properties
from scipy import signal
import numpy

def main(plt):
    def expsig(t):
        return ( 1 - numpy.exp(- (signal.sawtooth(2.0 * t) + 1.0) / 2.0 *10.0) ) * signal.square(t)

    funcs = {
        'none': lambda x: numpy.zeros_like(x),
        'square': signal.square,
        'sine': numpy.sin,
        'sawtooth': signal.sawtooth,
        'isawtooth': lambda x: signal.sawtooth(x, 0),
        'triangle': lambda x: signal.sawtooth(x, 0.5),
        'exponential': expsig
    }

    time = numpy.arange(1, 44100 * 1)
    f, ax = plt.subplots(len(funcs), 1, figsize=(7, 8))

    for i, func in enumerate(funcs):
        ax[i].plot(funcs[func](2.0 * numpy.pi * 6 * time / 44100), color='black')
        ax[i].set_ylim(-1.2, 1.2)
        ax[i].set_title(properties.labels(func) + " Vibrato", fontdict={'fontsize': 9})

    ax[-1].set_xlabel('$k$')

    return f
