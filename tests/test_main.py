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


def test_failing():
    with pytest.raises(SystemExit):
        paper_plt.main(["fail.pdf"])
