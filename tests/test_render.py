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


def test_rc_callback():
    paper_plt.render("rc.pdf")
    os.remove("rc.pdf")


def test_rc_dicts():
    paper_plt.render(
        "blank.pdf",
        rc_params={'font.size': 9},
        sns_params={'font': 'serif'}
    )
    os.remove("blank.pdf")


def test_failing():
    with pytest.raises(ImportError):
        paper_plt.render("fail.pdf")
