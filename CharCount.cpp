#include <fstream>
#include <iostream>
#include <string>
using namespace std;

//=============================================== INPUT ==================================================

string inptxtfile = "input.txt"; //read from this file

string outtxtfile = "output.txt"; //output char count in this file

//=============================================== COUNTER ==================================================

string input;
int charcount [256];
ifstream readFile;
ofstream writeFile;

void countChars() //from file to array of character counts in ASCII indexes
{
    readFile >> input;

    while (!readFile.eof()) // keep reading until end-of-file
    {
        char* char_arr = {};    //============================
        string str_obj(input);  //convert string to char array
        char_arr = &str_obj[0]; //============================

        for (int i = 0; i < sizeof(char_arr); i++) //goes through char array and counts chars
        {
            if ((int)char_arr[i] < 256) charcount[(int)char_arr[i]]++;
            else cout << "Invalid character: " << char_arr[i] << endl;//char isn't in UTF-8 (probably)
        }

        //cout << input << endl; //uncomment if you want to write out individual lines of text file

        readFile >> input; //sets EOF flag if no value found (idk what that really means :p)
    }
}

void writeChars() //write out the count of each char (by converting from ASCII)
{
    writeFile.open(outtxtfile);
    for (int i = 1; i < 256; i++)
    {
        if (charcount[i] > 0)//skip empty indexes
        {
            cout << charcount[i] << " - " << char(i) << endl;
            writeFile << charcount[i] << " - " << char(i) << endl;
        }
    }
    writeFile.close();
}

int main()
{
    readFile.open(inptxtfile); //open the file

    if (!readFile) //file couldn't be opened
    { 
        cerr << "Error: file could not be opened" << endl;
        exit(1);
    }

    countChars();
    writeChars();

    readFile.close();
    return 0;
}
//TODO:
/*
    ? rockyou.txt - not counting all chars ?
*/