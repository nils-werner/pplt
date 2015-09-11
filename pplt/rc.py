import numpy

sns_params = {
    'font': 'serif',
}


rc_params = {
    'font.size': 9,
}


def main(plt):
    f, ax = plt.subplots(1, 1)
    ax.plot(numpy.sin(numpy.arange(1000) / 100.))
    return f
