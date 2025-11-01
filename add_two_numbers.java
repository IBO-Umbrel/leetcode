

// Definition for singly-linked list.

// import java.util.ArrayList;
// import java.util.List;

class ListNode
{
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}



class Solution
{
    public ListNode addTwoNumbers(ListNode l1, ListNode l2)
    {
        ListNode temp = new ListNode(0);
        ListNode change_temp = temp;
        int overflow = 0;

        while (l1 != null || l2 != null || overflow != 0)
        {
            int num1 = (l1 != null) ? l1.val : 0;
            int num2 = (l2 != null) ? l2.val : 0;
            int sum = num1 + num2 + overflow;

            change_temp.next = new ListNode(sum % 10);
            change_temp = change_temp.next;
            overflow = sum / 10;

            l1 = (l1 != null) ? l1.next : null;
            l2 = (l2 != null) ? l2.next : null;
        }

        return temp.next;
    }
}


