#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='paper_plt',
    version='0.1',
    description='A simple matplotlib renderer for rendering plots from the commandline',
    author='Nils Werner',
    author_email='nils.werner@audiolabs-erlangen.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'seaborn>=0.6.0',
    ],
    extras_require={
        'docs': [
            'sphinx',
            'sphinxcontrib-napoleon',
            'sphinx_rtd_theme',
            'numpydoc',
        ],
    },
    entry_points={
        'console_scripts': [
            'pplt = paper_plt.main:main',
        ]
    },
    classifiers=[
          'Development Status :: 2 - Beta',
          'Environment :: Console',
    ],
)
