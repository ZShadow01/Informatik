using System;

namespace GeradeOderUngerade
{
    class MainClass
    {
        static int[] numbers = new int[] { 2, 5, 12, 13, 27, 154, 634 };

        public static void Main(string[] args)
        {
            for (int i = 0; i < numbers.Length; i++)
            {
                if (numbers[i] % 2 == 0)
                {
                    Console.WriteLine(numbers[i] + " ist gerade");
                } else
                {
                    Console.WriteLine(numbers[i] + " ist ungerade");
                }
            }
        }
    }
}
