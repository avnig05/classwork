#include <bitset>
#include <string>
#include <tuple> 
#include <fstream> 
#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <regex>
#include <map>

using namespace std;

class Product {
    public:
    tuple<string, double > productData; 
    string fileName;

    Product(){
        productData = make_tuple("", 0.0);
        fileName = "";
    }

    Product(string name, double price, string fileName){
        productData = make_tuple(name, price);
        fileName = fileName;
    }

    static vector<Product> readFromXML(const string& filename){
        vector<Product> products;
        ifstream file(filename);
        
        string line;
        string name;
        double price;
        smatch match;
        string productName;
        double productPrice;

        regex productPattern("<Product>(.*)</Product>");
        regex pricePattern("<Price>(.*)</Price>");

        while(getline(file, line)){
            if(regex_search(line, match, productPattern)){
                productName = match.str(1);
            }
            else if(regex_search(line, match, pricePattern)){
                productPrice = stod(match.str(1));
                products.push_back(Product(productName, productPrice, filename));
          //      cout << productName << " " << productPrice << endl;
            }
        }
        return products;
    }
};

class DataBase {
public:
    map<string, Product> productMap;

    void addProduct(const Product& product) {
        string barcode = convertTo3of9(get<0>(product.productData).substr(0, 5)); // takes first 5 characters of product name
        cout << get<0>(product.productData).substr(0, 5) << "   " << barcode << endl; // prints out the first first letters of the product and the barcode
        productMap[barcode] = product; // adds the product to the map at the specific key (barcode)
    }

    Product getProduct(const string& productName) {
        string barcode = convertTo3of9(productName.substr(0, 5));
        return productMap[barcode];
    }

private:
    string convertTo3of9(const string& input) {
        bitset<48> output;
        int offset = 0; // keeps track of the current position in the bitset

        for (char c : input) {
            // Convert the character to uppercase
            c = toupper(c);

            // Look up the Code 39 pattern for this character
            bitset<9> pattern = convertCharToBinary(c);

            // Append the pattern to the output bitset
            for (int i = 0; i < 9; ++i) {
                output[offset + i] = pattern[i];
            }

            offset += 9; // Move to the next 9-bit block
        }

        // Convert the 48-bit bitset to a 6-byte string
        string result;
        for (int i = 0; i < 6; ++i) {
            result += static_cast<char>(output.to_ulong() >> (i * 8));
        }

        return result;
    }

    bitset<9> convertCharToBinary(char c) {
        // Define the base ASCII character for Code 39
        char baseChar = '-';

        // Define the 'n' and 'w' pattern for the base character
        string basePattern = "nwnnnnwnw";

        // Calculate the offset from the base character
        int offset = c - baseChar;

        // Generate the 9-bit binary representation for the given character
        bitset<9> binary;
        for (size_t i = 0; i < basePattern.size(); ++i) {
            // If the base pattern character is 'n', use the corresponding bit from the offset
            // If the base pattern character is 'w', use the inverse of the corresponding bit from the offset
            binary[i] = (basePattern[i] == 'n') ? ((offset >> i) & 1) : !((offset >> i) & 1);
        }

        return binary;
    }
};

int main(){
    vector<Product> products = Product::readFromXML("Products.xml");
    DataBase db;
    for(const auto& product : products){
        db.addProduct(product);
    }

    Product retrieveProduct = db.getProduct("Avoca");

    cout << "Product: " <<  get<0>(retrieveProduct.productData) << endl;   
    cout << "Price: " << get<1>(retrieveProduct.productData) << endl;

    return 0;
}