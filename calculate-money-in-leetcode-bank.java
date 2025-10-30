class Solution
{
    public int totalMoney(int days)
    {
        int total_money = 0;
        int weeks = 0;

        for (int index = 1; index < days+1; index++)
        {
            total_money += (index + weeks)-(7*weeks);
            if (index % 7 == 0)
            {
                weeks++;
            }
        }

        return total_money;
    }
}