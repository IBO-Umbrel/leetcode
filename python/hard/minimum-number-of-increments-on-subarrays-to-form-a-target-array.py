# hard (https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/)


from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        operations = target[0]
        
        for index in range(1, len(target)):
            if target[index] > target[index - 1]:
                operations += target[index] - target[index - 1]
        return operations


print(Solution().minNumberOperations([2, 4, 1, 4]))





# old version
# class Solution:
#     def minNumberOperations(self, target: List[int]) -> int:
#         initial = [0 for i in target]
#         operations = 0
        
#         while initial != target:
#             for index in range(len(target)):
#                 if initial[index] != target[index]:
#                     initial[index] += 1
#                 if index < len(target)-1:
#                     if initial[index+1] == target[index+1] and initial[index] != target[index]:
#                         break
#             print(initial)
#             operations += 1
#         print(initial)
#         return operations