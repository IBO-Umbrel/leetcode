# medium (https://leetcode.com/problems/add-two-numbers/)


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        change_temp = temp
        overflow = 0

        while l1 or l2 or overflow:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            total = num1 + num2 + overflow
            num = total % 10
            overflow = total // 10
    
            new_node = ListNode(num)
            change_temp.next = new_node
            change_temp = change_temp.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return temp.next