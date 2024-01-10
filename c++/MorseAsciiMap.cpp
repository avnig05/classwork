#include <iostream>
#include <fstream>
#include <bitset>
#include <string>

using namespace std;

class MorseAsciiMap
{

public:
    MorseAsciiMap()
    {
        build();
    }

    char morseToAscii(string code)
    {
        return morseToChar(this->rootNode, code);
    }

    void printMissingCodes() {
        for (int i = 0; i < missingCodes.size(); i++) {
            cout << missingCodes[i] << endl;
        }
    }

    ~MorseAsciiMap()
    {
        deleteTree(this->rootNode);
    }

private:
    struct Node
    {
        char data;
        Node *left;
        Node *right;
    };
    vector<string> missingCodes;
    Node *rootNode;

    Node *createNode(char data)
    {
        Node *node = new Node;
        node->data = data;
        node->left = NULL;
        node->right = NULL;
        return node;
    }

    void deleteTree(Node* root) {
        if (root == NULL) {
            return;
        }
        deleteTree(root->left);
        deleteTree(root->right);
        delete root;
    }

    void insert(Node *root, char data, string code)
    {
        for (int i = 0; i < code.length(); i++)
        {
            if (code[i] == '.')
            {
                if (root->left == NULL)
                {
                    root->left = createNode(' ');
                }
                root = root->left;
            }
            else if (code[i] == '-')
            {
                if (root->right == NULL)
                {
                    root->right = createNode(' ');
                }
                root = root->right;
            }
        }
        root->data = data;
    }

    char morseToChar(Node *root, string code)
    {
        for (int i = 0; i < code.length(); i++)
        {
            if (code[i] == '.')
            {
                root = root->left;
            }
            else if (code[i] == '-')
            {
                root = root->right;
            }
            if (root == NULL)
            {
                missingCodes.push_back(code);
                return '\t';
            }              
        }
        return root->data;
    }

    void build()
    {
        Node *root = createNode(' ');
        insert(root, 'E', ".");
        insert(root, 'T', "-");
        insert(root, 'A', ".-");
        insert(root, 'N', "-.");
        insert(root, 'M', "--");
        insert(root, 'I', "..");
        insert(root, 'O', "---");
        insert(root, 'G', "--.");
        insert(root, 'K', "-.-");
        insert(root, 'D', "-..");
        insert(root, 'W', ".--");
        insert(root, 'R', ".-.");
        insert(root, 'U', "..-");
        insert(root, 'S', "...");
        insert(root, 'Q', "--.-");
        insert(root, 'Y', "-.--");
        insert(root, 'C', "-.-.");
        insert(root, 'V', "...-");
        insert(root, 'X', "-..-");
        insert(root, 'Z', "--..");
        insert(root, 'H', "....");
        insert(root, 'F', "..-.");
        insert(root, 'L', ".-..");
        insert(root, 'P', ".--.");
        insert(root, 'J', ".---");
        insert(root, 'B', "-...");
        insert(root, 'G', "--.");
        insert(root, 'X', "-..-");
        insert(root, 'Y', "-.--");
        insert(root, 'Z', "--..");
        insert(root, '1', ".----");
        insert(root, '2', "..---");
        insert(root, '3', "...--");
        insert(root, '4', "....-");
        insert(root, '5', ".....");
        insert(root, '6', "-....");
        insert(root, '7', "--...");
        insert(root, '8', "---..");
        insert(root, '9', "----.");
        insert(root, '0', "-----");
        insert(root, '.', ".-.-.-");
        insert(root, ',', "--..--");
        insert(root, '?', "..--..");
        insert(root, '!', "..--.");
        insert(root, ':', "---...");
        insert(root, '"', ".-..-.");
        insert(root, '\'', ".----.");
        insert(root, '=', "-...-");
        insert(root, '+', ".-.-."); 
        insert(root, '-', "-....-");    
        insert(root, '/', "-..-."); 
        insert(root, '(', "-.--."); 
        insert(root, ')', "-.--.-");
        insert(root, '@', ".--.-.");
        insert(root, ' ', " "); 
        insert(root, '$', "...-..-");
        insert(root, '&', ".-..."); 
        insert(root, '_', "..--.-");
        insert(root, ';', "-.-.-.");
        insert(root, '#', "...-.-");
        insert(root, '%', "-.-..-");
        insert(root, '*', "-..-.");
        insert(root, '~', ".-.-");
        insert(root, '^', ".-.-");
        insert(root, '>', ".-.-");
        insert(root, '<', ".-.-");
        insert(root, '`', ".-.-");
        insert(root, '\\', ".-.-");
        insert(root, '|', ".-.-");
        insert(root, '{', ".-.-");
        insert(root, '}', ".-.-");
        insert(root, '[', ".-.-");
        insert(root, ']', ".-.-");

        this->rootNode = root;
    }
};

string byteToMorse(char byte) {
    string morse = "";
    bitset<8> bits(byte);
    for (int i = 0; i < 8; i += 2) {
        if (bits[i] == 0 && bits[i+1] == 0) {
            morse += ",";
        } else if (bits[i] == 0 && bits[i+1] == 1) {
            morse += ".";
        } else if (bits[i] == 1 && bits[i+1] == 0) {
            morse += "-";
        } else {
            morse += " ";
        }
    }
    return morse;
}

vector<char> parseMorseCode(string morse, MorseAsciiMap& map) {
    vector<char> words;
    string word = "";
    for (int i = 0; i < morse.length(); i++) {
        if (morse[i] == ' ' || morse[i] == ',') {
            if (word != "") {
                words.push_back(map.morseToAscii(word));
                word = "";
            }
            if (morse[i] == ' ') {
                words.push_back(' ');
            }
        } else if (morse[i] == '.' || morse[i] == '-') {
            word += morse[i];
        } else {
            // word += morse[i];
        }
    }
    // if (word != "") {
    //     words.push_back(map.morseToAscii(word));
    // }
    return words;
}

int process(const string& morse) {
    MorseAsciiMap map;
    vector<char> words = parseMorseCode(morse, map);
    for (int i = 0; i < words.size(); i++) {
        cout << words[i];
    }
    cout << endl << endl;
    map.printMissingCodes();
    return 0;
}

int main() {
    ifstream file("EncryptBin.bin", ios::binary);
    if (!file) {
        cout << "Error opening file" << endl;
        return 1;
    }
    char byte;
    string morse = "";
    while (file.read(&byte, 1)) {
        morse += byteToMorse(byte);
        cout << "Byte" << byte << endl; 
    }
    process(morse);
    file.close();
    return 0;
}
