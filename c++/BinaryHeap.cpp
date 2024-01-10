#include <iostream>
#include <string>
#include <vector>

class BinaryHeap {
public:
    BinaryHeap(const std::string& phrase) {
        for (char ch : phrase) {
            insert(ch);
        }
    }

    void print() const {
        for (char ch : heap) {
            std::cout << ch << " ";
        }
        std::cout << std::endl;
    }

private:
    std::vector<char> heap;

    void insert(char ch) {
        heap.push_back(ch);
        int i = heap.size() - 1;
        while (i > 0 && heap[parent(i)] < heap[i]) {
            std::swap(heap[parent(i)], heap[i]);
            i = parent(i);
        }
    }

    int parent(int i) const {
        return (i - 1) / 2;
    }
};

int main() {
    std::string inputString = "MISSISSIPPI^RIVER";
    BinaryHeap bh(inputString);
    bh.print();
    return 0;
}