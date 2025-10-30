# hard (https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/?envType=daily-question&envId=2025-10-30)


from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        initial = [0 for i in target]
        operations = 0
        
        # while initial == target:
        for num in range(max(target)):
            for index in range(len(target)):
                if initial[index] != target[index]:
                    initial[index] += 1
                if index < len(target)-1:
                    if initial[index+1] == target[index+1] and initial[index] != target[index]:
                        break
            operations += 1
        print(initial)
        return operations


print(Solution().minNumberOperations([3,1,5,4,2]))