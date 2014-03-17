#!/usr/bin/env python

"""
LaTeX figure rendering framework

"""
import os
import sys
import numpy
import matplotlib.pyplot as plt


def main(argv):
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')

    fig_width_pt = 441.01772  # Get this from LaTeX using \showthe\columnwidth
    inches_per_pt = 1.0 / 72.27               # Convert pt to inch
    golden_mean = (numpy.sqrt(5) - 1.0) / 2.0         # Aesthetic ratio
    fig_width = fig_width_pt * inches_per_pt  # width in inches
    fig_height = fig_width * golden_mean      # height in inches
    fig_size = [fig_width, fig_height]
    params = {'backend': 'ps',
              'axes.labelsize': 10,
              'text.fontsize': 10,
              'legend.fontsize': 10,
              'xtick.labelsize': 8,
              'ytick.labelsize': 8,
              'text.usetex': True,
              'figure.figsize': fig_size}
    plt.rcParams.update(params)

    aliases = {
        "alias.pdf": "logspec",
    }

    if len(argv) == 0:
        pass
    else:
        if len(argv) >= 2:
            args = tuple(argv[1:])
        else:
            args = None

        if argv[0] in aliases:
            item = aliases[argv[0]]
            if type(item) is tuple:
                name = item[0]
                args = item[1:]
            else:
                name = item

            print name, args
        else:
            name = os.path.splitext(argv[0])[0]

        try:
            module = __import__('render_modules.' + name, globals(), locals(), name)
        except:
            print("No module %s found" % name)
            sys.exit(1)

        if args is not None:
            f = module.main(plt, *args)
        else:
            f = module.main(plt)
        f.tight_layout()
        f.savefig(argv[0])


if __name__ == "__main__":
    main(sys.argv[1:])
