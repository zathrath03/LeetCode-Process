"""
You have n bags numbered from 0 to n - 1. You are given two 0-indexed integer
arrays capacity and rocks. The ith bag can hold a maximum of capacity[i] rocks
and currently contains rocks[i] rocks. You are also given an integer
additionalRocks, the number of additional rocks you can place in any of the
bags.

Return the maximum number of bags that could have full capacity after placing
the additional rocks in some bags.

Constraints:
n == capacity.length == rocks.length
1 <= n <= 5 * 10^4
1 <= capacity[i] <= 10^9
0 <= rocks[i] <= capacity[i]
1 <= additionalRocks <= 10^9
"""


import unittest


class Solution:
    def maximumBags(
        self, capacity: list[int], rocks: list[int], additionalRocks: int
    ) -> int:
        remaining_capacity = self.get_remaining_capacity(capacity, rocks)
        return self.count_full_bags(additionalRocks, remaining_capacity)

    def count_full_bags(self, additionalRocks, remaining_capacity):
        i = full_bags = 0
        while additionalRocks > 0 and i < len(remaining_capacity):
            additionalRocks -= remaining_capacity[i]
            if additionalRocks >= 0:
                full_bags += 1
            i += 1
        return full_bags

    def get_remaining_capacity(self, capacity, rocks):
        remaining_capacity = [c - r for c, r in zip(capacity, rocks)]
        remaining_capacity.sort()
        return remaining_capacity


class Test(unittest.TestCase):
    test_cases = (
        ([2, 3, 4, 5], [1, 2, 4, 4], 2, 3),
        ([10, 2, 2], [2, 2, 0], 100, 3),
    )

    def test_maximumBags(self) -> None:
        sol = Solution()
        for capacity, rocks, additionalRocks, expected in self.test_cases:
            assert (
                sol.maximumBags(capacity, rocks, additionalRocks) == expected
            )


if __name__ == "__main__":
    unittest.main()
