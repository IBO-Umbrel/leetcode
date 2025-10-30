class Solution
{
    public int countValidSelections(int[] nums)
    {
        int length = nums.length;
        int result = 0;
        int sum = 0;
        
        for (int num : nums)
        {
            sum += num;
        }
        
        int leftSum = 0;
        int rightSum = sum;
        
        for (int index = 0; index < length; index++)
        {
            if (nums[index] == 0) {
                if (leftSum - rightSum >= 0 && leftSum - rightSum <= 1) {
                    result++;
                }
                if (rightSum - leftSum >= 0 && rightSum - leftSum <= 1) {
                    result++;
                }
            } else {
                leftSum += nums[index];
                rightSum -= nums[index];
            }
        }
        
        return result;
    }
}