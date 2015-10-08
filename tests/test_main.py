import os
import pytest
import paper_plt


def test_blank():
    paper_plt.main(["blank.pdf"])
    os.remove("blank.pdf")


def test_artists():
    paper_plt.main(["artists.pdf"])
    os.remove("artists.pdf")


def test_params():
    paper_plt.main(["params.pdf", "yadd"])
    os.remove("params.pdf")


def test_rc():
    paper_plt.main(["rc.pdf"])
    os.remove("rc.pdf")


def test_style():
    paper_plt.main(["style.pdf"])
    os.remove("style.pdf")


def test_hooks():
    paper_plt.main(["hooks.pdf"])
    os.remove("hooks.pdf")


def test_failing():
    with pytest.raises(SystemExit):
        paper_plt.main(["fail.pdf"])
