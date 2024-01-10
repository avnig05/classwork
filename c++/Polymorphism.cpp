#include <string>
#include <ostream>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <cctype>
#include <queue>
#include <vector> 
#include <map> 

using namespace std;

class fileReader{
    public:
        fileReader(const string& dataFile) : dataFile(dataFile){}

        string getData() const{
            return data;
        }
        
        void readAndProcess(){
            ifstream inFile(dataFile); // reads the text file
            if(!inFile.is_open()){
                cout << "Unable to open file" << endl;
                exit(1);
            }
            string line; // stores the line
            while(getline(inFile, line)){
                try{
                    for(char& c : line){ // & is a reference to the pointer 
                        if(c < 32 || c > 127){
                            throw c;
                        }
                    }
                    data += line + "\n";
                 //   cout << line << endl;
                }
                catch(char& c){
                    replace_if(line.begin(), line.end(), [](unsigned char c) {return !isprint(c);}, '*'); 
                    data += line + "\n";
                  //  cout << line << endl; // replaces the character with a *
                }
            }
            inFile.close();
        }
    private:
        string dataFile;
        string data;
};

class Node {
public:
    virtual int getFrequency() = 0;
    virtual string getSymbol() = 0;
};

class Leaf : public Node {
public:
    char symbol;
    int frequency;

    Leaf(char s, int f) {
        symbol = s;
        frequency = f;
    }

    int getFrequency() {
        return frequency;
    }

    string getSymbol() {
        return string(1, symbol);
    }
};

class Branch : public Node {
public:
    Node* left;
    Node* right;

    Branch(Node* l, Node* r) {
        left = l;
        right = r;
    }

    int getFrequency() {
        return left->getFrequency() + right->getFrequency();
    }

    string getSymbol() {
        return left->getSymbol() + right->getSymbol();
    }
};

class PriorityQueue {
public:
    Node* root;
    map<char, string> bitTrails;
    string data;
    PriorityQueue(string s) {
        priority_queue<pair<int, Node*>, vector<pair<int, Node*>>, greater<pair<int, Node*>>> pq;
        vector<int> freq(256, 0);
        data = s;
        for (char c : s) {
            freq[c]++;
        }
        for (int i = 0; i < 256; i++) {
            if (freq[i] > 0) {
                pq.push(make_pair(freq[i], new Leaf(i, freq[i])));
            }
        }
        while (pq.size() > 1) {
            pair<int, Node*> p1 = pq.top();
            pq.pop();
            pair<int, Node*> p2 = pq.top();
            pq.pop();
            Node* parent = new Branch(p1.second, p2.second);
            pq.push(make_pair(parent->getFrequency(), parent));
        }
        root = pq.top().second;
        makeBitTrails(root, " ");
    }

    void makeBitTrails(Node* node, string trail){
        if(Leaf* lf = dynamic_cast<Leaf*>(node)){
            bitTrails[lf->symbol] = trail;
        }
        else if(Branch* br = dynamic_cast<Branch*>(node)){
            makeBitTrails(br->left, trail + "0");
            makeBitTrails(br->right, trail + "1");
        }
    }

    string lookup(char c){
        return bitTrails[c];
    }

    void encrypt(){
        ofstream file("encrypt.txt");
        if(file.is_open()){
            for(char c : data){
                file << lookup(c);
            }
         //   cout << "Written to file" << endl;
            file.close();
        }
        else{
            cout << "Unable to create file" << endl;
        }
    }

    void decrypt(string encryptedFile){
        ifstream inFile(encryptedFile);
        Node*node = root;
        char bit;
        if(!inFile.is_open()){
            cout << "Unable to open file" << endl;
            exit(1);
        }
        while(inFile.get(bit)){
            if(bit == '0'){
                node = dynamic_cast<Branch*>(node)->left;
            }
            else if(bit == '1'){
                node = dynamic_cast<Branch*>(node)->right;
            }
            if(Leaf* lf = dynamic_cast<Leaf*>(node)){
                cout << lf->symbol;
                node = root;
            }
        }
        inFile.close();
    }
};

int main(int argc, char* argv[]){ 
    if(argc < 2) {
        cout << "Please provide an input file as an argument." << endl;
        return 1;
    }
    string inputFile = argv[1];
    fileReader file(inputFile);
    file.readAndProcess();
    string s = file.getData();
    PriorityQueue pq(s);
    pq.encrypt();
    pq.decrypt("encrypt.txt");
    return 0;
}