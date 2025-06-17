import pytest
from src.algorithms.pref_sum import PrefixSum


@pytest.fixture()
def get_prefix():
    nums = [10, 20, 30, 40, 50]
    return PrefixSum(nums)


class TestPrefixSum:

    @pytest.mark.parametrize(
        "l, r, expected",
        [
            (1, 3, 60),
            (1, 2, 30),
            (2, 3, 50),
            (1, 1, 10),
            (1, 4, 100),
            (4, 5, 90),
            (3, 5, 120),
        ],
    )
    def test_sum(self, getPrefix: PrefixSum, l, r, expected):
        assert getPrefix.prefix_sum(l, r) == expected
