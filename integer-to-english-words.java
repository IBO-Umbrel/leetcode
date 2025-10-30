class Solution
{
    public String numberToWords(int num)
    {
        if (num == 0) return "Zero";

        String[] belowTwenty = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
            "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
        String[] tens = {"", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
        String[] thousands = {"", "Thousand", "Million", "Billion"};
        StringBuilder result = new StringBuilder();
        int i = 0;

        while (num > 0)
        {
            if (num % 1000 != 0)
            {
                result.insert(0, helper(num % 1000, belowTwenty, tens) + thousands[i] + " ");
            }
            num /= 1000;
            i++;
        }

        return result.toString().trim();
    }
    private String helper(int num, String[] belowTwenty, String[] tens)
    {
        StringBuilder sb = new StringBuilder();
        
        if (num == 0)
        {
            return "";
        }
        else if (num < 20)
        {
            sb.append(belowTwenty[num] + " ");
        }
        else if (num < 100)
        {
            sb.append(tens[num / 10] + " ");
            sb.append(helper(num % 10, belowTwenty, tens));
        }
        else
        {
            sb.append(belowTwenty[num / 100] + " Hundred ");
            sb.append(helper(num % 100, belowTwenty, tens));
        }
        return sb.toString();
    }
}