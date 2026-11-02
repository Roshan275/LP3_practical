
#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Check if queen can be placed
bool isSafe(vector<string>& board, int row, int col, int n) {

    // Check column
    for (int i = 0; i < n; i++) {
        if (board[i][col] == 'Q')
            return false;
    }

    // Check left diagonal
    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
        if (board[i][j] == 'Q')
            return false;
    }

    // Check right diagonal
    for (int i = row, j = col; i >= 0 && j < n; i--, j++) {
        if (board[i][j] == 'Q')
            return false;
    }

    return true;
}

// Place queens using backtracking
bool nQueens(vector<string>& board, int row, int n, int fixedRow) {

    if (row == n)
        return true;

    // First queen is already placed
    if (row == fixedRow)
        return nQueens(board, row + 1, n, fixedRow);

    for (int col = 0; col < n; col++) {

        if (isSafe(board, row, col, n)) {
            board[row][col] = 'Q';

            if (nQueens(board, row + 1, n, fixedRow))
                return true;

            board[row][col] = '.'; // Backtracking
        }
    }

    return false;
}

int main() {
    int n, row, col;

    cout << "Enter N: ";
    cin >> n;

    if (n <= 0)
        return 0;

    vector<string> board(n, string(n, '.'));

    cout << "Enter first queen position (row col): ";
    cin >> row >> col;

    if (row < 1 || row > n || col < 1 || col > n) {
        cout << "Invalid position";
        return 0;
    }

    row--;
    col--;

    board[row][col] = 'Q';

    if (nQueens(board, 0, n, row)) {
        cout << "\nFinal N-Queens Matrix:\n";

        for (int i = 0; i < n; i++) {
            cout << board[i] << endl;
        }
    }
    else {
        cout << "No solution exists";
    }

    return 0;
}
