#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
public:
    vector<vector<int>> restoreMatrix(vector<int> rowSums, vector<int> colSums) {
        int R = rowSums.size();
        int C = colSums.size();
        vector<vector<int>> matrix(R, vector<int>(C));
        
        if (backtrack(0, 0, rowSums, colSums, matrix)) {
            return matrix;
        }
        return {};
    }

private:
    bool backtrack(int r, int c, vector<int>& rowSums, vector<int>& colSums, vector<vector<int>>& matrix) {
        int R = rowSums.size();
        int C = colSums.size();

        if (r == R) {
            for (int x : colSums) if (x != 0) return false;
            return true;
        }

        int nextR = (c == C - 1) ? r + 1 : r;
        int nextC = (c == C - 1) ? 0 : c + 1;

        if (c == C - 1) {
            int val = rowSums[r];
            if (val >= 0 && val <= colSums[c]) {
                matrix[r][c] = val;
                rowSums[r] -= val;
                colSums[c] -= val;
                if (backtrack(nextR, nextC, rowSums, colSums, matrix)) return true;
                rowSums[r] += val;
                colSums[c] += val;
            }
            return false;
        }

        int maxVal = min(rowSums[r], colSums[c]);

        for (int val = maxVal; val >= 0; val--) {
            matrix[r][c] = val;
            rowSums[r] -= val;
            colSums[c] -= val;
            if (backtrack(nextR, nextC, rowSums, colSums, matrix)) return true;
            rowSums[r] += val;
            colSums[c] += val;
        }

        return false;
    }
};






int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int R, C;
    if (!(cin >> R >> C)) return 0;
    vector<int> rowSums(R), colSums(C);
    for(int i=0; i<R; i++) cin >> rowSums[i];
    for(int i=0; i<C; i++) cin >> colSums[i];
    Solution sol;
    vector<vector<int>> res = sol.restoreMatrix(rowSums, colSums);
    if (res.empty()) {
        cout << "IMPOSSIBLE\n";
        return 0;
    }
    for(const auto& row : res) {
        for(size_t i=0; i<row.size(); i++) cout << row[i] << (i==row.size()-1?"":" ");
        cout << "\n";
    }
    return 0;
}
