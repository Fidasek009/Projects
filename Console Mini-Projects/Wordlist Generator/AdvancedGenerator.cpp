#include <fstream>
#include <string.h>
#include <iostream>
using namespace std;
//=============================================== INPUT ==================================================

char chars[] = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
				//,'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
				//,'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
				//,'@', '#', '&', '$', '+', '*', '-', '.', ',', '!', '/', '_'
				//, '<', '>', '(', ')', '[', ']', '{', '}', '%', '?' // less than 20,000 found in RockYou.txt
				//, '|', '€', '§' 
				};

const int length = 8;

string outputfile = "H:/My Drive/Ostatní Srandy/Hax&stuff/Wordlists/test.txt";

//=============================================== GENERATOR ==================================================
int word[length];

ofstream file;

void decode(int* inp)//from array to string + write to file
{
	string s = "";
	for (int j = 0; j < length; j++)
	{
		s += chars[inp[j]];
	}
	cout << s << '\n';
	file << s << '\n';
	
}

void gen(int x) //function to generate all combinations
{
	if (x < 1) decode(word);
	else
	{
		int i = 0;
		while (i < sizeof(chars))
		{
			word[x - 1] = i;
			gen(x - 1);
			i ++;
		}
	}
}

int main()
{
	memset(word, '0', length);//fill "word" with 0

	file.open(outputfile);//open output file

	gen(length);

	file.close();

	return 0;
}