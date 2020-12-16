using System;

namespace Kennwortprüfung
{
    class MainClass
    {
        static string benutzername = "Jericho";
        static string kennwort = "Hermawan";

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
