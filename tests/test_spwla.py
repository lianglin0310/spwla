
from spwla.cli import main
from spwla.resistivity import archie


def test_main():
    assert main([]) == 0

def test_archie():
    assert archie(1.0, 0.2, 2, 2, 1) == 0.04
