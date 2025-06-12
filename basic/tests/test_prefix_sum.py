import pytest
from src.algorithms.pref_sum import PrefixSum


class TestPrefixSum:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.nums = [10, 20, 30]
        self.prefix = PrefixSum(self.nums)

    @pytest.mark.parametrize("l, r, expected", [(1, 3, 60), (1, 2, 30), (2, 3, 50)])
    def test_sum(self, l, r, expected):

        assert self.prefix.sum(l, r) == expected


# 0 10 30 60
