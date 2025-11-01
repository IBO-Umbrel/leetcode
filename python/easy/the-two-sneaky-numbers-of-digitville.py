# easy (https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/)


from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        apeared_nums = []
        sneaky_nums = []

        for num in nums:
            if num in apeared_nums:
                sneaky_nums.append(num)
                continue
            apeared_nums.append(num)
        return sneaky_nums


print(Solution().getSneakyNumbers([7,1,5,4,3,4,6,0,9,5,8,2]))