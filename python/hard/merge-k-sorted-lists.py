# hard (https://leetcode.com/problems/merge-k-sorted-lists/)


from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = ListNode()
        temp = result
        nums = []

        for lt in lists:
            while lt != None:
                nums.append(lt.val)
                lt = lt.next

        nums.sort()

        for num in nums:
            new_result = ListNode(num)
            temp.next = new_result
            temp = temp.next
        return result.next