# hard (https://leetcode.com/problems/number-of-visible-people-in-a-queue/)


from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        length = len(heights)
        result = [0] * length
        unblocked = []

        for i in range(length):
            while unblocked and heights[i] >= heights[unblocked[-1]]:
                result[unblocked.pop()] += 1
            if unblocked:
                result[unblocked[-1]] += 1
            unblocked.append(i)
        return result



# running tests here:
heights = [10,6,8,5,11,9]
print(Solution().canSeePersonsCount(heights))


# old version
# class Solution:
#     def canSeePersonsCount(self, heights: List[int]) -> List[int]:
#         length = len(heights)
#         result = [0] * length

#         for i in range(length-1):
#             count = 0
#             last_tallest = 0

#             for j in range(i+1, length):
#                 if heights[j] >= last_tallest:
#                     count += 1
#                     last_tallest = heights[j]
#                 if heights[j] >= heights[i]:
#                     break
#             result[i] = count
                
#         return result