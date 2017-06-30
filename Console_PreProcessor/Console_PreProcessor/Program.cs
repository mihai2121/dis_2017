using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Console_PreProcessor
{
    class Program
    {
        //public static List<string> ToReplaceList = new List<string> { ".", "?", ",", "!", "'", "/`", "\"", "/", @"\", "[", "]", "(", ")", "{", "}", "~", " în ", " de ", " pe ", " la ", " cea ", " care ", " a ", " al ", ":" };
        //public static List<string> ToReplaceList = new List<string> { " sau ", " din ", " iar ", " cel ", " etc ", " au ", " o ", " ca ", " un ", " să ", " pentru ", " după ", "„", "”", "s-au", " am " };
        //public static List<string> ToReplaceList = new List<string> { " ar ", " cum ", " însă ", " către ", " unei ", " încă ", " însă "," alte ", " dintre ", " se ", " unul ", " că ", " și " , " doar ", " s-a ", " ce ", " unui ", " cu ", " într-o ", " într-un ", " dintr-un ", " dintr-o ", " îl ", " va ", " | " , " până ", " dar ", " ceea ", " alte " };
        //public static List<string> ToReplaceList = new List<string> { " lor ", " mai ", " este ", " despre ", " căci ", " pot ", " își ", " cât ", " ne-am ", " adică ", " lui ", " le ", " astfel ", ";", " îi ", "__", "=", "^" };
        public static List<string> ToReplaceList = new List<string> { " fost " };

        static void Main(string[] args)
        {
            ReplaceFile(@"C:\Users\BSSoper\Downloads\output_v4", @"C:\Users\BSSoper\Downloads\output_v5");
            Console.WriteLine("done");
            Console.ReadLine();
        }

        public static void ReplaceFile(string filePath, string newFilePath)
        {
            using (var vReader = new StreamReader(filePath))
            {
                using (var vWriter = new StreamWriter(newFilePath))
                {
                    long vLineNumber = 0;
                    while (!vReader.EndOfStream)
                    {
                        string vLine = vReader.ReadLine();
                        vWriter.WriteLine(ReplaceLine(vLine, vLineNumber++));
                    }
                }
            }
        }
        protected static string ReplaceLine(string Line, long LineNumber)
        {
            //Line = Line.ToLower();
            foreach (var s in ToReplaceList)
            {
                Line = Line.Replace(s, " ");
            }
            Console.WriteLine(LineNumber);
            return Line;
        }
    }

}
