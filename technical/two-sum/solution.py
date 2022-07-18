from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    # Time complexity is O(n) (because we iterate the array only once)
    # Space complexity is also O(n) (the size of the table is at most n)
    table = {}
    for i, e in enumerate(nums):
        diff = target - e
        if diff in table:
            return [table[diff], i]
        table[e] = i


if __name__ == '__main__':
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    print(two_sum([2, 7, 11, 15], 9))

    assert two_sum([3, 2, 4], 6) == [1, 2]
    print(two_sum([3, 2, 4], 6))

    assert two_sum([3, 3], 6) == [0, 1]
    print(two_sum([3, 3], 6))
