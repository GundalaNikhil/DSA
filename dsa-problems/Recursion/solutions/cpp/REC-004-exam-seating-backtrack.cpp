#include <iostream>
#include <vector>

using namespace std;

class Solution {
    int N;
    int count;
    vector<bool> cols;
    vector<bool> diag1;
    vector<bool> diag2;

public:
    int countNQueens(int n) {
        N = n;
        count = 0;
        cols.assign(2 * n, false);
        diag1.assign(2 * n, false);
        diag2.assign(2 * n, false);
        backtrack(0);
        return count;
    }

    void backtrack(int row) {
        if (row == N) {
            count++;
            return;
        }

        for (int col = 0; col < N; col++) {
            if (cols[col] || diag1[row + col] || diag2[row - col + N]) continue;
            
            cols[col] = true;
            diag1[row + col] = true;
            diag2[row - col + N] = true;
            
            backtrack(row + 1);
            
            cols[col] = false;
            diag1[row + col] = false;
            diag2[row - col + N] = false;
        }
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; 
    if (!(cin >> n)) return 0;
    
    Solution sol;
    cout << sol.countNQueens(n) << endl;
    return 0;
}
