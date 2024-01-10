#include <iostream>
#include <fstream> 
#include <tuple>
#include <string>
#include <regex>
#include <algorithm>
#include <vector>

using namespace std;

class tupleBuilder{
public:
    tupleBuilder(const string dataFile) : dataFile(dataFile){
        ifstream file;
        file.open(dataFile, ios::binary);
        file.seekg(0, ios::end);
        length = file.tellg();
        file.seekg(0, ios::beg);
        file.close();
    }

    void parse(function<void(const char*, size_t length, vector<tuple<string, string, char>>&) > callback){
        callback(raw(), length, storeTuple);
    }  

    size_t size(){
        return length;
    }

    string name(){
        return dataFile;
    }  

    void find(string& str) { 
        bool found = false;
        for (auto& tuple : storeTuple) {
            if (str.length() == 1) {
                if (get<0>(tuple) == str || get<1>(tuple) == str || get<2>(tuple) == str[0]) {
                    cout << get<0>(tuple) << " " << get<1>(tuple) << " " << get<2>(tuple) << endl;
                    found = true;
                } 
            }
            else if (str.length() >= 2) {
                if (get<0>(tuple) == str || get<1>(tuple) == str) {
                    cout << get<0>(tuple) << " " << get<1>(tuple) << " " << get<2>(tuple) << endl;
                    found = true;
                } 
            } 
            else {
                ;
            }
        }
        if (!found) {
            cout << "Not found" << endl;
        }
    }

private: 
    string dataFile;
    size_t length;
    char* buffer;
    vector<tuple<string, string, char>> storeTuple;

    char* raw() {
        ifstream file;
        file.open(dataFile, ios::binary);
        buffer = new char[length + 1];
        file.read((char*)buffer, length);
        file.close();
        return buffer;
    }
};

//this function extracts the values before every comma and adds them to a tuple 
tuple<string, string, char> createTupleFromList(const string& str) {
    size_t pos1 = str.find(",");
    if (pos1 == string::npos) {
        return make_tuple(str, string(), char());
    }
    string first = str.substr(0, pos1);
    string rest = str.substr(pos1 + 1);
    size_t pos2 = rest.find(",");
    if (pos2 == string::npos) {
        return make_tuple(first, rest, char());
    }
    string second = rest.substr(0, pos2);
    string third = rest.substr(pos2 + 1);
    return make_tuple(first, second, third[0]);
}

//stores tuple in the vector
void parseCSVLine(const char *buffer, size_t length, vector<tuple<string, string, char>>& storeTuple)
{
    string str(buffer, buffer + length);
    string str_copy(str); // create a copy of the string
    tuple<string, string, char> myTuple = createTupleFromList(str_copy);
    storeTuple.push_back(myTuple);
}
 
void parseCSV(const char* buffer, size_t length, vector<tuple<string, string, char>>& storeTuple) {
    regex pattern1(R"([^\r\n]+)");
    smatch matches;
    string str(buffer, buffer + length); 
    while (regex_search(str, matches, pattern1)) {
        for (size_t i = 0; i < matches.size(); ++i) {
            parseCSVLine(matches[i].str().c_str(), matches[i].str().length(), storeTuple);
            str = matches.suffix().str();
        }
    }
} 

int main(){
    tupleBuilder csv("Tuple.csv");
    csv.parse(parseCSV);
    string strTofind = "085";
    csv.find(strTofind);
}