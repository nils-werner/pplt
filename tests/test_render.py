import os
import pytest
import paper_plt


def test_blank():
    paper_plt.render("blank.pdf")
    os.remove("blank.pdf")


def test_artists():
    paper_plt.render("artists.pdf")
    os.remove("artists.pdf")


def test_params():
    paper_plt.render("params.pdf", ["yadd"])
    os.remove("params.pdf")


def test_failing():
    with pytest.raises(ImportError):
        paper_plt.render("fail.pdf")
