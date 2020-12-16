using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;

namespace Wichteln
{
    class MainClass
    {
        public static string fileName = "wichteln.txt";
        public static string resultFile = "wichteln_ergebnis.txt";

        public static Dictionary<char, Dictionary<string, List<string>>> DATA = new Dictionary<char, Dictionary<string, List<string>>>();
        public static List<int> presents = new List<int> { };

        public static int amountOfStudents;

        public static void Main(string[] args)
        {
            Console.WriteLine("Starting");
            run();
        }

        public static string[] openFile()
        {
            string currentDirectory = Directory.GetCurrentDirectory();
            string path = Path.Combine(currentDirectory, fileName);
            string[] lines = File.ReadAllLines(path);

            // Remove spaces after each value
            for (int i = 0; i < lines.Length; i++) lines[i] = lines[i].Trim();


            return lines;
        }

        public static void updateData()
        {
            string[] data = openFile();


            amountOfStudents = Convert.ToInt32(data[0]);

            // Add presents
            for (int i = 1; i < amountOfStudents + 1; i++) presents.Add(i);

            // Individual wishes
            for (int i = 0; i < data.Length; i++)
            {
                string line = data[i].Trim();

                string[] newLine = line.Split(new[] { ' ' },
                    StringSplitOptions.RemoveEmptyEntries);

                // DATA update
                DATA.Add(Convert.ToChar(i), new Dictionary<string, List<string>>
                    {
                        {"WISHES", new List<string>(newLine) },
                        {"RECEIVED", new List<string> {"" } }
                    }
                );

            }
        }

        public static void give(char student, int rankedWish)
        {
            int present;

            if (rankedWish >= 3)
            {
                present = new Random().Next(0, presents.Count - 1);
            }
            else
            {
                present = presents.FindIndex(e => e == Convert.ToInt32(DATA[student]["WISHES"][rankedWish]));
            }

            DATA[student]["RECEIVED"][0] = presents[present].ToString();
            presents.RemoveAt(present);

        }

        public static void sortStudents()
        {
            for (int student = 1; student < amountOfStudents + 1; student++)
            {
                char studentNumber = Convert.ToChar(student);
                var studentData = DATA[studentNumber];
                var studentWishes = studentData["WISHES"];

                if (presents.Contains(Convert.ToInt32(studentWishes[0])))
                {
                    give(studentNumber, 0);
                }
                else if (presents.Contains(Convert.ToInt32(studentWishes[1])))
                {
                    give(studentNumber, 1);
                }
                else if (presents.Contains(Convert.ToInt32(studentWishes[2])))
                {
                    give(studentNumber, 2);
                }
                else
                {
                    give(studentNumber, 3);
                }
            }
        }

        public static void saveFile()
        {
            string currentDirectory = Directory.GetCurrentDirectory();
            string path = Path.Combine(currentDirectory, resultFile);

            using (StreamWriter outputFile = new StreamWriter(path))
            {
                for (int student = 1; student < amountOfStudents + 1; student++)
                {
                    char studentChar = Convert.ToChar(student);
                    outputFile.Write("Student " + student + " kriegt Geschenk Nr. " + DATA[studentChar]["RECEIVED"][0]);
                    outputFile.Write(" || Wunschliste: [{0}]", string.Join(",", DATA[studentChar]["WISHES"]));
                    outputFile.WriteLine("\n");
                }
            }
        }

        public static void run()
        {
            Console.WriteLine("[UPDATING]...");
            updateData();
            Console.WriteLine("Done...");

            Console.WriteLine("[SORTING ITEMS]...");
            sortStudents();
            Console.WriteLine("Done...");

            Console.WriteLine("[SAVING]...");
            saveFile();
            Console.WriteLine("Done...");

            Console.ReadLine();
        }
    }
}