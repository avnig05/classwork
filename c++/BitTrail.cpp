#include <string>
#include <memory>
#include <typeinfo>
#include <iostream>
#include <fstream> 
#include <regex>
#include <tuple>
#include <map>
#include <sstream>


using namespace std;

class Node // does this actually work as a smart pointer?
{
public:
    Node() {}
    virtual float key() const = 0;
    virtual string value() const = 0;
    virtual ~Node() {} // Virtual destructor for proper cleanup
};

using smart_ptr = shared_ptr<Node>;

class Branch : public Node
{
    smart_ptr _Left;
    smart_ptr _Right;

public:
    Branch(smart_ptr n0, smart_ptr n1) : _Left(n0), _Right(n1) {}

    virtual float key() const
    {
        return _Left->key() + _Right->key();
    }

    virtual string value() const
    {
        return string(_Left->value() + _Right->value());
    }
};

class Leaf : public Node
{
    float _freq;
    string _symbol;

public:
    Leaf(string const& s = "", float f = 0) : _freq(f), _symbol(s) {}

    virtual float key() const { return _freq; }
    virtual string value() const { return _symbol; }
    operator float() { return _freq; }
};

void nodeTest()
{
    float anode = rand() % 100;
    float bnode = rand() % 100;
    string svalue = "";

    smart_ptr left = make_shared<Leaf>();
    cout << typeid(left).name() << endl;

    smart_ptr pleft = make_shared<Leaf>();
    cout << typeid(pleft).name() << endl;

    smart_ptr rite = make_shared<Leaf>();
    cout << typeid(rite).name() << endl;

    smart_ptr prite = make_shared<Leaf>();
    cout << typeid(prite).name() << endl;

    smart_ptr branch = make_shared<Branch>(pleft, pleft);
    cout << typeid(branch).name() << endl;

    smart_ptr pbranch = make_shared<Branch>(pleft, prite);
    cout << typeid(pbranch).name() << endl;
}
/*
int main()
{
    nodeTest();
    return 0;
}
*/

class fileReader{
public:
    fileReader(const string dataFile) : dataFile(dataFile){
        ifstream file;
        file.open(dataFile, ios::binary);
        file.seekg(0, ios::end);
        length = file.tellg();
        file.seekg(0, ios::beg);
        file.close();
    }

    void parse(function<void(const char*, size_t length)> callback){
        callback(raw(), length);
    }  

    size_t size(){
        return length;
    }

    string name(){
        return dataFile;
    }  

private: 
    string dataFile;
    size_t length;
    char* buffer;

    char* raw() {
        ifstream file;
        file.open(dataFile, ios::binary);
        buffer = new char[length + 1];
        file.read((char*)buffer, length);
        file.close();
        return buffer;
    }
};

void parseTXT(const char* buffer, size_t length){
    string input(buffer, length);
    map<string, int> frequencyMap;
    regex pattern(R"(Character\[  (.*?)  \] = Frequency\[ (\d+) \])");
    smatch matches;

    while (regex_search(input, matches, pattern)) {
        string character = matches[1].str();
        int frequency = stoi(matches[2].str());
        frequencyMap[character] = frequency;
        input = matches.suffix().str();
    }

    for (const auto& pair : frequencyMap) {
        cout << "Character: " << pair.first << " Frequency: " << pair.second << endl;
    }
}; 

class QTree{
    
}

int main()
{
    fileReader txt("Frequencies.txt");
    txt.parse(parseTXT);
    return 0;
}
