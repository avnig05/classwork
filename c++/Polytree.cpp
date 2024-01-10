#include <string>
#include <memory>
#include <typeinfo>
#include <ostream>
#include <iostream>

using namespace std;

#define smart pointer;

class Node
{
public:
	Node() {}
	virtual float key() const = 0;
	virtual string value() const = 0;
};

#define smart_ptr shared_ptr<Node>

class Branch : public Node
{
	Node* _Left;
	Node* _Right;
public:
	Branch(Node* n0, Node* n1) : _Left(n0), _Right(n1) {}
	virtual float key() const
	{
		return _Left->key() + _Right->key();
	}
	virtual string value() const
	{
		return string(_Left->value() + _Right->value());
	}
	Node* left() const { return _Left; }
	Node* right() const { return _Right; }
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

	// compile error:  can't make instance of a Node
	// Node* pnode = new Node(anode, );

	Leaf* left = new Leaf();
	cout << typeid(left).name() << endl;
	Node* pleft = new Leaf();
	cout << typeid(pleft).name() << endl;

	Leaf* rite = new Leaf();
	cout << typeid(rite).name() << endl;
	Node* prite = new Leaf();
	cout << typeid(prite).name() << endl;

	Branch* branch = new Branch(pleft, pleft);
	cout << typeid(branch).name() << endl;
	Node* pbranch = new Branch(pleft, prite);
	cout << typeid(pbranch).name() << endl;
}

void main()
{
	nodeTest();
}