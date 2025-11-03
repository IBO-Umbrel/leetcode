# medium (https://leetcode.com/problems/minimum-time-to-make-rope-colorful/)


from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        i = 0
        while i != len(colors):
            j = i
            curr_time_sum = 0
            highest_time = 0

            while j < len(colors) and colors[j] == colors[i]:
                curr_time_sum += neededTime[j]
                highest_time = max(highest_time, neededTime[j])
                j += 1
            
            time += curr_time_sum - highest_time
            i = j
        return time