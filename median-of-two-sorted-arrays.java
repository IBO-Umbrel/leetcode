import java.util.Arrays;

class Solution
{
    public double findMedianSortedArrays(int[] nums1, int[] nums2)
    {
        int[] all_nums = new int[nums1.length + nums2.length];
        
        System.arraycopy(nums1, 0, all_nums, 0, nums1.length);
        System.arraycopy(nums2, 0, all_nums, nums1.length, nums2.length);
        Arrays.sort(all_nums);

        return all_nums.length % 2 == 0 ? ((all_nums[((all_nums.length)/2)]) + (all_nums[((all_nums.length)/2) - 1])) / 2.0 : all_nums[((all_nums.length-1)/2)];
    }
}