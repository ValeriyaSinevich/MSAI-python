# -*- coding: utf-8 -*-
import pytest

from functions_package import InvalideArgumentError, divide

MAGIC_NUMBER = 42


@pytest.fixture
def suppy_first_argument_to_divide():
    arg = MAGIC_NUMBER
    print('fixture: suppy_first_argument_to_add')
    yield arg


def test_simple(suppy_first_argument_to_divide):
    assert suppy_first_argument_to_divide == MAGIC_NUMBER


class TestDivide:
    """
    This test case is testing 'divide' function from package 'functions'
    and supplies MAGIC_NUMBER as a second argument
    """

    def divide_success(self):
        """ Testing that take returns list of first 'n' elements from
        'iterable' """
        assert (
            divide(suppy_first_argument_to_divide,
                   suppy_first_argument_to_divide) == 84
        )

    def add_two_numbers_failure(self):
        with pytest.raises(InvalideArgumentError):
            divide(1, 0)
