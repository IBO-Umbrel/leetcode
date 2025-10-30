import java.util.ArrayList;
import java.util.Arrays;

class Solution
{
    public ListNode mergeKLists(ListNode[] lists)
    {
        ListNode result = new ListNode();
        ListNode temp = result;
        ArrayList<Integer> nums = new ArrayList<>();

        for (ListNode lt : lists)
        {
            while (lt != null)
            {
                nums.add(lt.val);

                lt = lt.next;
            }
        }

        int[] nums_array = nums.stream().mapToInt(i -> i).toArray();

        Arrays.sort(nums_array);

        for (int num : nums_array)
        {
            ListNode new_result = new ListNode(num);
            temp.next = new_result;
            temp = temp.next;
        }
        return result.next;
    }
}