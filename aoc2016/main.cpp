#include <iostream>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

string parseFirstLine(string file)
{
    string line;
    ifstream inputFile(file);
    if (inputFile.is_open())
    {
        getline (inputFile, line);
        inputFile.close();
    }
    else cout << "Unable to open file"; 

    return line;
}

int main()
{
    string file = "input/input1.txt";
    string line = parseFirstLine(file);
    
    int sum = 0;
    for (string::size_type i = 1; i < line.size(); i++) {
        if (line[i-1] == line[i])
        {
            int number = (int)line[i] - 48;
            sum += number;
        }
    }
    if (line[0] == line[line.size() - 1])
    {
        int number = (int)line[0] - 48;
        sum += number;
    }
    cout << "Sum: " << sum << "\n";

    return 0;
}