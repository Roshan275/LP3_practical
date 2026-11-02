
#include <iostream>
#include <queue>
#include <vector>
#include <string>
using namespace std;

// Node of Huffman Tree
struct Node {
    char ch;
    int freq;
    Node *left, *right;

    Node(char c, int f) {
        ch = c;
        freq = f;
        left = right = NULL;
    }
};

// Compare frequencies (Min Heap)
struct Compare {
    bool operator()(Node* a, Node* b) {
        return a->freq > b->freq;
    }
};

// Print Huffman Codes
void printCodes(Node* root, string code) {
    if (root == NULL)
        return;

    if (root->left == NULL && root->right == NULL) {
        cout << root->ch << " : "
             << (code.empty() ? "0" : code) << endl;
        return;
    }

    printCodes(root->left, code + "0");
    printCodes(root->right, code + "1");
}

int main() {
    int n;
    char ch;
    int freq;

    priority_queue<Node*, vector<Node*>, Compare> pq;

    cout << "Enter number of characters: ";
    cin >> n;

    if (n <= 0)
        return 0;

    for (int i = 0; i < n; i++) {
        cout << "Enter character and frequency: ";
        cin >> ch >> freq;

        pq.push(new Node(ch, freq));
    }

    // Build Huffman Tree
    while (pq.size() > 1) {
        Node* left = pq.top();
        pq.pop();

        Node* right = pq.top();
        pq.pop();

        Node* parent = new Node('$',
                               left->freq + right->freq);

        parent->left = left;
        parent->right = right;

        pq.push(parent);
    }

    cout << "\nHuffman Codes:\n";
    printCodes(pq.top(), "");

    return 0;
}
