# hard (https://leetcode.com/problems/sliding-window-median/)



from typing import List
from sortedcontainers import SortedList



class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        medians = []
        window = SortedList(nums[:k])
        if k % 2 == 0:
            medians.append((window[k // 2 - 1] + window[k // 2]) / 2.0)
        else:
            medians.append(float(window[k // 2]))
        previus = 0
        for i in range(k, len(nums)):
            window.remove(nums[previus])
            window.add(nums[i])
            previus += 1
            if k % 2 == 0:
                medians.append((window[k // 2 - 1] + window[k // 2]) / 2.0)
            else:
                medians.append(float(window[k // 2]))
        return medians