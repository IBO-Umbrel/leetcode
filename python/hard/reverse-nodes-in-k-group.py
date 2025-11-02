from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        result = ListNode()
        temp = result
        nums = []
        
        while head != None:
            nums.append(head.val)
            head = head.next
        
        rnums = []

        for i in range(len(nums)//k):
            for ri in reversed(nums[i*k:i*k+k]):
                rnums.append(ri)
        for i in range((len(nums)//k)*k, len(nums)):
            rnums.append(nums[i])


        for rnum in rnums:
            new_result = ListNode(rnum)
            temp.next = new_result
            temp = temp.next
        return result.next