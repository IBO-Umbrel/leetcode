class Bank
{
    long[] balance = null;
    public Bank(long[] balance)
    {
        this.balance = balance;
    }
    
    public boolean transfer(int account1, int account2, long money)
    {
        if (balance.length >= account1 && balance.length >= account2 && balance.length >= 0)
        {
            if (balance[account1-1] >= money)
            {
                balance[account1-1] -= money;
                balance[account2-1] += money;
                return true;
            }
        }
        return false;
    }
    
    public boolean deposit(int account, long money)
    {
        if (balance.length >= account && balance.length >= 0)
        {
            balance[account-1] += money;
            return true;
        }
        return false;
    }
    
    public boolean withdraw(int account, long money)
    {
        if (balance.length >= account && balance.length >= 0)
            if (balance[account-1] >= money)
            {
                balance[account-1] -= money;
                return true;
            }
        return false;
    }
}