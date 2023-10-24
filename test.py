import pytest

from lib import count_common_elements


@pytest.mark.parametrize(
    "result, array1, array2, array3",
    [
        (2, [1, 2, 2, 3, 4], [2, 3, 3, 4, 5], [3, 4, 4, 5, 6])
    ]
)
def test_count_common_elements(result, array1, array2, array3):
    assert count_common_elements(array1, array2, array3) == result
