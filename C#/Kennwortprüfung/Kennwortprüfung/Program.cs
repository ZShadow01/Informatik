using System;

namespace Kennwortprüfung
{
    class MainClass
    {
        static string benutzername = "Wilhelm";
        static string kennwort = "Raabe";

        public static void Main(string[] args)
        {
            Console.Write("Benutzername: ");
            string username = Console.ReadLine();

            Console.Write("Kennwort: ");
            string passwort = Console.ReadLine();

            if (username == benutzername && kennwort == passwort)
            {
                Console.WriteLine("Richtig");
            } else
            {
                Console.WriteLine("Falsch");
            }
        }
    }
}
