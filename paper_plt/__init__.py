#!/usr/bin/env python

"""
LaTeX figure rendering framework

"""
import os
import sys
import numpy
import argparse
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


def render(
    name,
    args=None,
    prefix="pplt",
    rc_params=None,
    sns_params=None,
    aliases=None,
    tight_layout=True,
    columnwidth=244.6937,
    file_object=None,
):
    if rc_params is None:
        rc_params = {}

    if sns_params is None:
        sns_params = {}

    if aliases is None:
        aliases = {}

    if file_object is None:
        file_object = name

    plt.rcdefaults()
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')

    plt.rcParams.update({
        'backend': 'ps',
        'axes.labelsize': 9,
        'legend.fontsize': 9,
        'xtick.labelsize': 8,
        'ytick.labelsize': 8,
        'text.usetex': True,
        'font.family': 'serif',
        'font.serif': 'ptmrr8re',
        'font.size': 9,
        'figure.figsize': fig_size(columnwidth)
    })
    plt.rcParams.update(rc_params)

    sns.set(font='serif')
    sns.set(*sns_params)

    basename = os.path.splitext(os.path.basename(name))[0]

    try:
        if basename in aliases:
            item = aliases[basename]
            if type(item) is tuple:
                basename = item[0]
                args = item[1:]
            else:
                basename = item
    except AttributeError:
        pass

    module = __import__(
        '%s.%s' % (prefix, basename), globals(), locals(), basename
    )

    art = tuple()
    if args is not None:
        f = module.main(plt, *args)
    else:
        f = module.main(plt)

    print f

    if type(f) is tuple:
        f, art = f

    f.set_tight_layout(tight_layout)
    f.savefig(file_object, bbox_extra_artists=art, bbox_inches='tight')


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


def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--prefix', '-P', default="pplt", help='Import prefix',
    )
    parser.add_argument(
        'out', help='Output filename',
    )
    parser.add_argument(
        'arguments', nargs='*', help='Renderer Arguments. Optional.',
    )
    args = parser.parse_args(args)

    sys.path.append(os.getcwd())
    try:
        conf = __import__('%s.conf' % args.prefix, globals(), locals(), 'conf')
    except ImportError:
        conf = empty()

    set_defaults(conf, defaults)

    try:
        render(
            args.out,
            args.arguments,
            prefix=args.prefix,
            rc_params=conf.rc_params,
            sns_params=conf.sns_params,
            aliases=conf.aliases,
            tight_layout=conf.tight_layout,
            columnwidth=conf.columnwidth,
        )
    except ImportError:
        print "Could not import %s.%s" % (
            args.prefix,
            os.path.splitext(os.path.basename(args.out))[0]
        )
        sys.exit(1)
