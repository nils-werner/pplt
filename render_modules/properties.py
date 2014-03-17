def labels(val):
    return {
        'regression': 'Phase',
        'yin': 'YIN',
        'yinbp': 'YIN b/p',
        'chain': 'Chaingang',
        'chainbp': 'Chaingang b/p',
        'voicesep': 'Solomon',
        'midi': 'MIDI',
        'ftm': 'FTM',
        'teager': 'DESA 1',
        'sin': 'Sine',
        'exponential': 'Capacitor Charge/Discharge',
        'isawtooth': 'Inverse Sawtooth',
        'none': 'No'
    }.get(val, val.title())


linestyles = ['-', '-.', '-', '-', '-.', ':', '-', '-.', ':']

colors = ['g'] * 2 + ['r'] + ['#333333'] * 3 + ['b'] * 2
