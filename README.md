Paper PLT
=========

Simple Matlotlib renderer framework that allows you to render single plots from the commandline.

Example
-------

With a project layout like

```
|- paper.tex
|- fig/
`- pplt/
   |- __init__.py
   |- input_signal.py
   `- result_plots.py
```

and each `pplt/*.py` file like

```python
def main(plt):
    f, ax = plt.subplots(1, 1, figsize=(6, 2))
    ax.plot(...)
    return f
```

you can then render your plots using

```bash
pplt fig/input_signal.pdf
pplt fig/result_plots.pdf
```

and include the resulting files in your PDF.


Makefile Example
----------------

The point of tese "one command per output file" is so you can also include all files in a `Makefile`:

```makefile
# Dependencies for paper, name all TeX documents, refs, and all pplt output files here
paper.pdf: paper.tex refs.bib \
	plots/input_signal.pdf \
	plots/result_plots.pdf

# Compilation command for LaTeX
%.pdf: %.tex
	TEXINPUTS=$(TEXPATH) latexmk -pdf -pdflatex="pdflatex $(BATCHFLAG) $(LATEXFLAGS)" --synctex=1 -use-make $<

# A pplt plots with a special dependency. If the script or the data changes, the plot will be re-generated.
fig/result_plots.pdf: pplt/result_plots.py data/result_plots.npy
	pplt $@

# All pplt plots without special dependencies
fig/%.pdf: pplt/%.py
	pplt $@

```
