import pytest

from ..exercises.__main__ import main
from ..exercises.ex_set_2 import ReversedInput


def setup():
    print("SETUP!")


def teardown():
    print("TEAR DOWN!")


@pytest.mark.parametrize("test_input, expected", [('ready!', 0)])
def test_main_basic(test_input, expected):
    assert main(test_input) == expected


def test_ex_set_2():
    oUserInputReversed = ReversedInput('Hello')
    assert oUserInputReversed.getInput() == "Hello"
    assert oUserInputReversed.getResult() == "olleH"
