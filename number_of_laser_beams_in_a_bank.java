

public class number_of_laser_beams_in_a_bank
{
    public int numberOfBeams(String[] bank)
    {
        int totalBeams = 0;

        for (int i = 0; i < bank.length; i++)
        {
            bank[i] = bank[i].replaceAll("0", "");
        }

        for (int i = 0; i < bank.length; i++)
        {
            if (bank[i].length() > 0)
            {
                for (int j = i+1; j < bank.length; j++)
                {
                    if (bank[j].length() > 0)
                    {
                        totalBeams += bank[i].length() * bank[j].length();
                        break;
                    }
                }
            }
        }

        return totalBeams;
    }

    public static void main(String[] args)
    {
        System.out.println(new number_of_laser_beams_in_a_bank().numberOfBeams(new String[]{"011001","000000","010100","001000"}));
    }
}