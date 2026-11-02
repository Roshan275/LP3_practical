
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

// Partition function
int partition(int a[], int low, int high) {
    int pivot = a[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (a[j] <= pivot) {
            i++;
            swap(a[i], a[j]);
        }
    }

    swap(a[i + 1], a[high]);
    return i + 1;
}

// Deterministic Quick Sort
void quickSort(int a[], int low, int high) {
    if (low < high) {
        int p = partition(a, low, high);

        quickSort(a, low, p - 1);
        quickSort(a, p + 1, high);
    }
}

// Randomized Quick Sort
void randomQuickSort(int a[], int low, int high) {
    if (low < high) {
        int r = low + rand() % (high - low + 1);
        swap(a[r], a[high]);

        int p = partition(a, low, high);

        randomQuickSort(a, low, p - 1);
        randomQuickSort(a, p + 1, high);
    }
}

int main() {
    int n, a[100], b[100];
    srand(time(0));

    cout << "Enter number of elements: ";
    cin >> n;
    if (n < 1 || n > 100)
        return 0;

    cout << "Enter elements: ";
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        b[i] = a[i];
    }

    quickSort(a, 0, n - 1);
    randomQuickSort(b, 0, n - 1);

    cout << "Deterministic Quick Sort: ";
    for (int i = 0; i < n; i++)
        cout << a[i] << " ";

    cout << "\nRandomized Quick Sort: ";
    for (int i = 0; i < n; i++)
        cout << b[i] << " ";

    return 0;
}
