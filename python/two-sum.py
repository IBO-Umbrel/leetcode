# 

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for index in range(length - 1):
            for jndex in range(index + 1, length):
                if nums[index] + nums[jndex] == target:
                    return [index, jndex]
        return []