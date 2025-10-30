class Solution
{
    public boolean hasSameDigits(String s)
    {
        char[] arr = s.toCharArray();
        if (s.length() == 2)
            if (arr[0] == arr[1])
                return true;
            else return false;
        String new_s = "";
        for (int index = 0; index < arr.length; index++)
        {
            if (index < (arr.length-1))
            {
                int sum = (Character.getNumericValue(arr[index]) + Character.getNumericValue(arr[index+1])) % 10;
                new_s += sum;
            }
        }
        return hasSameDigits(new_s);
    }
}