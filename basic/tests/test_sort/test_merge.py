import pytest
from src.algorithms.sort.merge import sort


class TestMergeSort:

    @pytest.mark.parametrize("a, expected", [([3, 2, 1], [1, 2, 3])])
    def test_merge(self, a, expected):
        assert sort(a) == expected
