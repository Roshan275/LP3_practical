
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n, W;

    cout << "Enter number of items: ";
    cin >> n;

    if (n < 1 || n > 100)
        return 0;

    int weight[101], profit[101];

    for (int i = 1; i <= n; i++) {
        cout << "Enter weight and profit of item " << i << ": ";
        cin >> weight[i] >> profit[i];
    }

    cout << "Enter knapsack capacity: ";
    cin >> W;

    if (W < 0 || W > 1000)
        return 0;

    int dp[101][1001] = {0};

    // Step 1: Build DP Table
    for (int i = 1; i <= n; i++) {
        for (int w = 0; w <= W; w++) {

            if (weight[i] <= w) {
                dp[i][w] = max(dp[i-1][w],
                    profit[i] + dp[i-1][w-weight[i]]);
            }
            else {
                dp[i][w] = dp[i-1][w];
            }
        }
    }

    cout << "\nMaximum Profit: " << dp[n][W] << endl;

    // Step 2: Find Selected and Excluded Items
    int w = W;
    int selected[101] = {0};

    for (int i = n; i > 0; i--) {
        if (dp[i][w] != dp[i-1][w]) {
            selected[i] = 1;
            w = w - weight[i];
        }
    }

    cout << "Selected Items: ";
    for (int i = 1; i <= n; i++) {
        if (selected[i] == 1)
            cout << i << " ";
    }

    cout << "\nExcluded Items: ";
    for (int i = 1; i <= n; i++) {
        if (selected[i] == 0)
            cout << i << " ";
    }

    return 0;
}
