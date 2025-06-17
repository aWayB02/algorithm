import pytest
from src.algorithms.pref_sum import PrefixSum


class TestPrefixSum:

    @pytest.mark.parametrize(
        "arr, left, right, expected",
        [
            ([10, 20, 30, 40, 50], 1, 2, 30),
            ([10, 20, 30], 2, 3, 50),
            ([10, 30, 50, 10], 2, 4, 90),
            ([10], 1, 1, 10),
            ([10, 20, 30, 40, 50], 4, 5, 90),
            ([10, 20, 30, 40, 50], 3, 5, 120),
        ],
    )
    def test_sum(self, arr, left, right, expected):
        ps = PrefixSum(arr)
        assert ps.prefix_sum(left, right) == expected
