import pytest

import unit_tests.hw_5 as hw


@pytest.mark.parametrize('num_1, expected', [(1, True),
                                             (-2, False),
                                             (0, False),
                                             (4, True)])
def test_is_positive(num_1, expected):
    assert hw.is_positive(num_1) == expected
