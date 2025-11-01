# hard (https://leetcode.com/problems/median-of-two-sorted-arrays/)


from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        all_nums = [*nums1, *nums2]
        all_nums.sort()

        return ((all_nums[((len(all_nums))//2)]) + (all_nums[((len(all_nums))//2) - 1])) / 2.0 if len(all_nums) % 2 == 0 else all_nums[((len(all_nums)-1)//2)]