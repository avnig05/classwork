#include <iostream>
#include <fstream> 
#include <string>
#include <algorithm>
#include <vector>
#include <regex>

using namespace std;

class Bitset{

private:
    string fileName;
    size_t length;
    char* buffer;
    vector<tuple<char, string, string>> morseTuple;
    
    char* raw() {
        ifstream file;
        file.open(fileName, ios::binary);
        buffer = new char[length + 1];
        file.read((char*)buffer, length);
        file.close();
        return buffer;
    }
    
public:
        
    Bitset(const string fileName) : fileName(fileName){
        ifstream file;
        file.open(fileName, ios::binary);
        file.seekg(0, ios::end);
        length = file.tellg();
        file.seekg(0, ios::beg);
        file.close();
    }
    
    void parse(function<void(const char*, size_t length, vector<tuple<char, string, string>>&) > callback){
        callback(raw(), length, morseTuple);
    }  
    
    size_t size(){
        return length;
    }

    string name(){
        return fileName;
    }  

};

string morseToBinary(const string& morse){
    string binary; 
    for(char c: morse){
        if(c == '.'){
            binary += "10";
        }
        else if(c == '-'){
            binary += "01";
        }
    }
    // cout << binary << endl;
    return binary;

}

tuple<char, string, string> createTupleFromList(const string& morseCode) {
    size_t pos1 = morseCode.find(",");
    if(pos1 == 0){
        pos1 = 1;
    }
    if (pos1 == string::npos) {
        return make_tuple(char(), string(), string());
    }
    string character = morseCode.substr(0, pos1);
    string morse = morseCode.substr(pos1 + 1);
    string binary = morseToBinary(morse);
    return make_tuple(character[0], morse, binary);
}


void parseCSVLine(const char *buffer, size_t length, vector<tuple<char, string, string>>& morseTuple)
{
    string str(buffer, buffer + length);
    string str_copy(str); // create a copy of the string
    tuple<char, string, string> myTuple = createTupleFromList(str_copy);
    morseTuple.push_back(myTuple);
    cout << get<0>(myTuple) << " " << get<1>(myTuple) << " " << get<2>(myTuple) << endl;
}
 
void parseCSV(const char* buffer, size_t length, vector<tuple<char, string, string>>& morseTuple) {
    regex pattern1(R"([^\r\n]+)");
    smatch matches;
    string str(buffer, buffer + length); 
    while (regex_search(str, matches, pattern1)) {
        for (size_t i = 0; i < matches.size(); ++i) {
            parseCSVLine(matches[i].str().c_str(), matches[i].str().length(), morseTuple);
            str = matches.suffix().str();
        }
    }
} 

int main() {
    Bitset reader ("MorseCode.csv");
    reader.parse(parseCSV);
}