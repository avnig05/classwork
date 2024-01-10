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
    }
    process(morse);
    file.close();
    return 0;
}

/* Output of ByteToMorse.cpp execution
E ORFTEI E TI   TT       MNS]NEAK MW IETGI AILIAIB T    N NBM AT E      T H ELIRV TR MWDET       ODTEZDP EWWGRJTMNSR     IIV ERANETFT V IETR MSM+GC EA IERE JM N5KNSVEH EE       ORKR    SEH E  EE       RIENT V ER MWDET. MUTEL MRM HE] MWTMTXI UXN EUCFM OUDREE  STE IO LNF GMRNIUOM ESS UBT  T V WOKD AET H E N E    T       EOSN TA FFRAE   EO       N      IF E5KKIQ M NINIMTNI    N A      IIFASOSM       E TTNE NGIIVK TR        EEP UR I]IA KXWGI TRFEAT         NIV EEN T NET   NEMEI2KYGN TA HN       E NUNS3IDNANMIGM EDRAEE  DNRET   RNUXNITA WS   ET        NIV END         THI     AIASO   NINIMTNI       I TRM A N       R TITMN+T H E   DGNIIT 4ET WDN=T         MSTTE   GM5MSODE S ORFTEN EA XAE  N M  UKE KNU N] TEMT-ENNTAIA UX ES]XEEII ABHETRV     M        IIF KAI        TUI I TO          TIN  NSVN     STEET UHETA    ETM IT AE        AJRMWKE M       IF E5E  SUNEAUN TKVTE   N       NR       NPI AIASO      KN T DT T        E3EE]G EWWGRJTMT I ASM+GC EMN TW S]TIT H IMNIN N A      I       MSTTEW]DSNTN AGOA KU EETETOR   WKN      AET H EN       E       T       EM      NE A2AG MDTAAA SNT     ITAR     AR NVMRGATEOA    M      EEL IIF NBI A   RII=I AET H I TEAE IICWUTMAE T  OGE     T        BEL IFS T      D        DCA E  EIEEH KITTWF     SEEA 9XNAI      ROETI MSM      NL ERORN G NWWGREMTT  OSIAIZAE QAEAT GCUIRLM+    NEMEI2KK TEB MGOR=N  TEMTESI EW DMAITTMUG E NSO]       RKM      INVIA   NWSNXEEEUN NWUTN6QNFT AE       A       WKE TRORA EDF    IIF E4N T NEMET VC NBT EKS=N INT        EE*ASMJ A HEH ODTEZDL TRM LN  ISXNTAL UXA TWMTER        AIOUEIM IMLT H USEA SAV TR  TAUN TA    AEN WOGSN       A IMLT H RMRM   M ISVUZR          TINIT TIE      OA M   MWGNI FZWSTH ODTEZDAE TR]IERITW  MI ZNIT NEMM MVEER      NVT     ORKM ITTTN TA   NWUNI2HM ATT 5ENA IO    E TI   TTG E SEE       E II ILI]IPNI    TWQIAANGITUM AD MSM    N] JA EEE  T    ETMEE EWRGA UXA JN E    SETRI EAROLMTMUG UR A TW NWDE   N       % MET6T S ENIIMAIT I    EE] NSUNPFT ISD] T H EENW       MI       GZSSJA  M      I       T JOKN SETTW LET SAI     RM OUYN A       IWMIUN        RI JM BEEM O      TVBCTEO        E] DT TTU HEEM TI       T       EOVT  MGORKI  LNF ERLINTN I     TEO      N       E      DMSKXTE HNV TW N]QE TVSA A IOR I MSM    NL UR   E        UXE  XNIHSI4I E TI     TTO AE  A       WIII            ENDI E DEE.  6NE A2AG NHT H I IPIAETJ DE EBDJSDN ES RGW  K]NIUDV A NHN VAN+AAI PT I     N] ETNL GGCUR    NEEE    -N]NR   UNEM   EEEIAET  EE      IIT HNF ER&I   ITNFT EETFN     DE ERREEUO OS   E       E#

..-.-
.--..-.
--.....---
---.-..
.-....
.-.-...
.-.--.
-.-...
...-.--.
..---.
---.--
.--...---
--..----
...-.-.
--.....
.-.-...
..---.
.--....-.-
---..-..-.
-.-..-.
......
..-.-
..--.-.
.-..--
.-------
.-....---
..-..-.
.--....
.--......
---..-.--
.-.-...
.......---
.-.----
---..-
.-.-.-.
..-..
..-.-
---....
.---.
---...--.
.-.....-..
..-..
-.-.-...
--.....
.-....-..
......
.-.-...
..-.-.
---..-..-.
.......
..-..-
..---.
---..-.---
--.-...
.-...-.-.-
--------
.-....---
......
....-.
---..-.
--...--
--......
-...---
.--..-.
-.-.--
-..--
-..-.-..
...-.-.
..-..-
-.-...
--.--.
.---.
-.-...
-.---
---..-.
...--.
.-.....
---..-.---
--.-...
.....-
---..-...
....-.-..
..-..
..-..-.---
.-.-.-.
-..--
....-.-...
.--..-.
......
-----.
--.--.
.-.-...
..-.-
...-.-..
..---.-.-
.---.
...--.-...
..-.----
.-.-.-.-.
........-.
....---
--.-.
---..-..-.
-------.
--.....
.-.-...
..-.-.
..-..-
..-...-
.-.-.-.
.-..-..
..---.--
.--..----
..-.-
.-.-.-.
.......
.-.----
.---.
---------
......-.
..-.-
.-.....
---..-.---
.-------
----.-.
..-..-.
....--.
-.---.
...-.-.
-.----
-..--..-.
..-...
.-.--.
..-.-
..----
.---.---
------..- */