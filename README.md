Paper PLT
=========

Simple Matlotlib renderer framework that allows you to render stuff to
PDFs from the commandline.

With a project layout like

    |- paper.tex
    `- pplt/
       |- __init__.py
       |- input_signal.py
       `- result_plots.py

and PPLT modules like

    def main(plt):
        f, ax = plt.subplots(1, 1, figsize=(6, 2))
        ax.plot(...)
        return f

you can then render your plots using

    pplt fig/input_signal.pdf
    pplt fig/result_plots.pdf

and then the final paper using

    pdflatex paper.tex
