
#include <iostream>
using namespace std;

// Non-Recursive Fibonacci
int iterative(int n) {
    int a = 0, b = 1, c;

    for (int i = 0; i < n; i++) {
        c = a + b;
        a = b;
        b = c;
    }

    return a;
}

// Recursive Fibonacci
int recursive(int n) {
    if (n <= 1)
        return n;

    return recursive(n - 1) + recursive(n - 2);
}

int main() {
    int n;

    cout << "Enter n: ";
    cin >> n;

    if (n < 0) {
        cout << "Enter a non-negative number";
        return 0;
    }

    cout << "Non-Recursive: " << iterative(n) << endl;
    cout << "Recursive: " << recursive(n) << endl;

    cout << "Non-Recursive: O(n) time, O(1) space" << endl;
    cout << "Recursive: O(2^n) time, O(n) space" << endl;

    return 0;
}
