#include <fstream>
#include <iostream>
#include <string>
#include <queue>

// ========================= INPUT =========================

// count chars in this file
std::string INP = "input.txt";
// write char counts to this file
std::string OUT = "output.txt";

// ========================= COUNTER =========================

int CHARS[256] = {0};

// from file to array of character counts in ASCII indexes
void countChars(std::string filePath) { 
    // open file
    std::ifstream inFile(filePath);
    if (!inFile) { 
        std::cerr << "Input file could not be opened." << std::endl;
        exit(1);
    }

    // read file and count chars
    std::string buffer;
    while(std::getline(inFile, buffer))
        for(char &c : buffer)
            if(c < 256 && c > 0)
                CHARS[c]++;
    
    inFile.close();
}

// write out the count of each char (by converting from ASCII)
void writeChars(std::string filePath) {
    // sort chars by count
    std::priority_queue<std::pair<int, char>> pq;
    for(int i = 1; i < 256; i++) {
        // only push non-zero indexes
        if (CHARS[i] > 0) pq.push(std::pair(CHARS[i], i));
    }

    // open file
    std::ofstream outFile(filePath);
    if (!outFile) { 
        std::cerr << "Output file could not be opened." << std::endl;
        exit(1);
    }

    // write to file
    while(!pq.empty()) {
        std::cout << pq.top().first << " - '" << pq.top().second << "'" << std::endl;
        outFile << pq.top().first << " - '" << pq.top().second << "'" << std::endl;
        pq.pop();
    }

    outFile.close();
}

int main()
{
    countChars(INP);
    writeChars(OUT);
    return 0;
}