#!/usr/bin/env python

"""
LaTeX figure rendering framework

"""
import os
import sys
import numpy
import matplotlib.pyplot as plt
import seaborn as sns

defaults = {
    "columnwidth": 244.6937,
    "aliases": {},
    "rc_params": {},
    "sns_params": {},
    "tight_layout": True,
}


class empty(object):
    pass


def render(argv):
    sys.path.append(os.getcwd())

    try:
        from pplt import conf
    except ImportError:
        conf = empty()

    set_defaults(conf, defaults)

    plt.rcdefaults()

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')

    params = {
        'backend': 'ps',
        'axes.labelsize': 9,
        'legend.fontsize': 9,
        'xtick.labelsize': 8,
        'ytick.labelsize': 8,
        'text.usetex': True,
        'font.family': 'serif',
        'font.serif': 'ptmrr8re',
        'font.size': 9,
        'figure.figsize': fig_size(conf.columnwidth)
    }

    plt.rcParams.update(params)
    plt.rcParams.update(conf.rc_params)
    sns.set(font='serif')
    sns.set(*conf.sns_params)

    if len(argv) == 0:
        pass
    else:
        if len(argv) >= 2:
            args = tuple(argv[1:])
        else:
            args = None

        name = os.path.splitext(os.path.basename(argv[0]))[0]

        try:
            if name in conf.aliases:
                item = conf.aliases[name]
                if type(item) is tuple:
                    name = item[0]
                    args = item[1:]
                else:
                    name = item
        except AttributeError:
            pass

        try:
            module = __import__('pplt.%s' % name, globals(), locals(), name)
        except ImportError:
            print "Could not import pplt.%s" % name
            sys.exit(1)

        art = ()
        if args is not None:
            f = module.main(plt, *args)
        else:
            f = module.main(plt)

        if type(f) is tuple:
            f, art = f

        f.set_tight_layout(conf.tight_layout)
        f.savefig(argv[0], bbox_extra_artists=art, bbox_inches='tight')


def fig_size(columnwidth):
    inches_per_pt = 1.0 / 72.27               # Convert pt to inch
    golden_mean = (numpy.sqrt(5) - 1.0) / 2.0  # Aesthetic ratio
    fig_width = columnwidth * inches_per_pt   # width in inches
    fig_height = fig_width * golden_mean      # height in inches
    return numpy.array([fig_width, fig_height])


def set_defaults(obj, data):
    for key in data:
        if not hasattr(obj, key):
            setattr(obj, key, data[key])


def main():
    render(sys.argv[1:])
